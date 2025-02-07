from pyats import aetest
from genie.testbed import load
from genie.conf.base import Device
import logging
import re
from time import sleep
from typing import List

logger = logging.getLogger(__name__)

def parse_traceroute(output: str) -> List[str]:
    '''
    Parses the output of a traceroute command and extracts the IP addresses of each hop.

    Args:
        output: str - The output of the traceroute command.

    Returns:
        A list of IP addresses representing each hop - List[str]

    Example:
        RP/0/RP0/CPU0:xrd-1#traceroute 10.10.10.2 source 10.10.10.1
         1  10.0.14.1 [MPLS: Label 16002 Exp 0] 19 msec  11 msec  12 msec
         2  10.0.34.0 [MPLS: Label 16002 Exp 0] 9 msec  10 msec  10 msec
         3  10.0.23.0 14 msec  *  8 msec
        RP/0/RP0/CPU0:xrd-1#

        Returns ["10.0.14.0","10.0.34.0","10.0.23.0"]
    '''

    hops = []
    for line in output.splitlines():
        if re.match(r"^\s*\d+\s+", line):
            hops.append(line.split()[1])
    return hops

def _verify_traceroute(device: Device,source: str,destination: str,expected: List[str]):
    '''
    Execute a traceroute on a device and compare it to an expected path (list of IP addresses that corresponds
    to the hops)
    Args:
        device: Device - The device object
        source: str - The source IP address
        destination: str - The destination IP address
        expected: List[str] - A list of IP addresses that corresponds to the expected path
    Returns:
        True if the traceroute output is equal to the expected path, False otherwise - bool
    '''
    output = device.execute(f"traceroute {destination} source {source}")
    parsed = parse_traceroute(output)
    if parsed != expected:
        logger.warning(f"Found difference in traceroute:\nExpected:{str(expected)}\nGot:{str(parsed)}\n")
        return False
    return True


class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect(self, testbed):
        # Step 0 - Connect to devices under test using the testbed.connect() method
        logger.info(f"Connecting to devices")
        testbed.connect(
            testbed.devices["xrd-1"],
            testbed.devices["xrd-2"],
            testbed.devices["xrd-source"],
            testbed.devices["xrd-dest"],
            vias={
                "xrd-1": "cli",
                "xrd-2": "cli",
                "xrd-source": "cli",
                "xrd-dest": "cli",
            },
            log_stdout=False,
            connection_timeout=10,
        )


class ODNSRPolicyValidation(aetest.Testcase):

    @aetest.test
    @aetest.loop(device_name=["xrd-1", "xrd-2"])
    def check_no_policy(self, testbed, device_name):
        device = testbed.devices[device_name]
        policy_summary = device.execute(
            "show segment-routing traffic-eng policy summary"
        )
        if not "Total policies: 0" in policy_summary:
            self.failed(f"Existing policy found on device {device.name}",goto=["next_tc"])

    @aetest.test
    @aetest.loop(
        source=["192.168.10.1", "172.16.10.1"],
        destination=["192.168.20.1", "172.16.20.1"],
    )
    def verify_traceroute_before(self, testbed, source, destination):
        expected=["10.0.1.0", "10.0.14.1", "10.0.34.0", "10.0.23.0", "10.0.2.1"]
        device = testbed.devices["xrd-source"]
        if not _verify_traceroute(device,source,destination,expected):
            self.failed(f"Unexpected traceroute from {source} source {destination} on {device.name}",goto=["next_tc"])

    @aetest.test
    @aetest.loop(device_name=["xrd-1", "xrd-2"])
    def configure_sr_policy(self, testbed, device_name):
        # Step 1 - Open the SR policy configuration file and save it to a variable
        with open("sr_policy_config.txt") as f:
            config = f.read()
        logger.info("Configuring SR Policy")
        # Step 2 - Configure the SR policy on the device
        device = testbed.devices[device_name]
        device.configure(config)
        # Step 3 - Mark the device for rollback
        device.rollback = True

    @aetest.test
    def wait_sr_policy_installed(self):
        logger.info("Waiting 10 seconds for the SR policy to be installed")
        sleep(10)

    # Step 4 - Set the loop parameters for the verify_odn_policy test section
    @aetest.test
    @aetest.loop(
        device_name=["xrd-1", "xrd-2"],
        policy_name=["srte_c_10_ep_10.10.10.2", "srte_c_10_ep_10.10.10.1"],
    )
    def verify_odn_policy(self, testbed, device_name, policy_name):
        # Step 5 - Execute the 'show segment-routing traffic-eng policy name <policy_name>' command
        device = testbed.devices[device_name]
        output = device.execute(
            f"show segment-routing traffic-eng policy name {policy_name}"
        )
        # Step 6 - Fail the testcase if the policy is not up and operational
        if not "Admin: up  Operational: up" in output:
            self.failed(f"ODN policy {policy_name} not up on {device.name}",goto=["cleanup"])

    @aetest.test
    @aetest.loop(
        source=["192.168.10.1", "172.16.10.1"],
        destination=["192.168.20.1", "172.16.20.1"],
        expected=[
            ["10.0.1.0", "10.0.14.1", "10.0.34.0", "10.0.23.0", "10.0.2.1"],
            ["10.0.1.0", "10.0.12.1", "10.0.2.1"],
        ],
    )
    def verify_traceroute_after(self, testbed, source, destination, expected):
        device = testbed.devices["xrd-source"]
        if not _verify_traceroute(device,source,destination,expected):
            self.failed(f"Unexpected traceroute from {source} source {destination} on {device.name}")

    @aetest.cleanup
    @aetest.loop(device_name=["xrd-1", "xrd-2"])
    def rollback_configuration(self, testbed, device_name):
        device = testbed.devices[device_name]
        if not getattr(device,"rollback",None):
            self.skipped("No configuration to rollback")
        logger.info(f"Rolling back configuration")
        device.execute("rollback configuration last 1")

class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect(self, testbed):
        logger.info(f"Disconnecting from devices")
        testbed.disconnect(
            testbed.devices["xrd-1"],
            testbed.devices["xrd-2"],
            testbed.devices["xrd-source"],
            testbed.devices["xrd-dest"],
        )


if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    testbed = load("testbed.yaml")
    result = aetest.main(testbed=testbed)
    aetest.exit_cli_code(result)
