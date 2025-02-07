from pyats import aetest
from genie.testbed import load
from genie.conf.base import Device
import logging
import xmltodict
from time import sleep
from typing import List

logger = logging.getLogger(__name__)
def string_from_file(filename: str):
    '''
    Read the content of a file and return it as a string
    Args:
        filename: str - The path to the file
    Returns:
        The content of the file - str
    '''
    with open(filename) as f:
        return f.read()

def netconf_configure(device: Device, target: str, config: str):
    '''
    Configure a device using NETCONF and return the associated commit ID. The configuration is locked and then unlocked
    to ensure that the operation is atomic and that the commit ID is the one associated with the configuration change.
    Args:
        device: genie.conf.base.Device - The device object
        target: str - The NETCONF target configuration store
        config: str - The NETCONF configuration to apply in XML format
    Returns:
        The commit ID associated with the configuration change - str
    '''
    pass
    # Step 4 - Define a Lock context for the target configuration to ensure that the requests are atomic and that
    # the commit ID associated with the configuration change is properly retrieved

    # Step 5 - Apply the configuration using the edit_config() method

    # Step 6 - Commit the configuration

    # Step 7 - Retrieve the last commit ID using the get() method

    # Step 8 - Return the commit ID


def _verify_traceroute(device: Device,source: str,destination: str,expected: List[str]):
    '''
    Execute a traceroute on a XR device using Netconf and compare it to an expected path in a json format
    Args:
        device: genie.conf.base.Device - The device object
        source: str - The source IP address
        destination: str - The destination IP address
        expected: List[str] - A list of IP addresses that corresponds to the expected path
    Returns:
         Assert that the traceroute output is equal to the expected path
    '''
    output = device.netconf.request(
            string_from_file("netconf/traceroute.xml").format(destination=destination,source=source)
        )
    traceroute = xmltodict.parse(output,xml_attribs=False)
    traceroute_hops = traceroute.get("rpc-reply",{}).get("traceroute-response",{}).get("ipv4",{}).get("hops",{}).get("hop",{})
    hops = []
    try:
        for hop in traceroute_hops:
            if "hop-address" in hop:
                hops.append(hop["hop-address"])
            else:
                for probe in hop["probes"]["probe"]:
                    if "hop-address" in probe:
                        hops.append(probe["hop-address"])
                        break
                else:
                    hops.append("*")
    except Exception:
        logger.warning(f"Unexpected traceroute format")
        return False

    if hops != expected:
        logger.warning(f"Found difference in traceroute:\nExpected:{str(expected)}\nGot:{str(hops)}\n")
        return False
    return True

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect(self, testbed):
        # Step 0 - Connect to devices using the testbed.connect() method
        # The device should be connected using NETCONF
        pass


class ODNSRPolicyValidation(aetest.Testcase):

    @aetest.test
    @aetest.loop(device_name=["xrd-1", "xrd-2"])
    def check_no_policy(self, testbed, device_name):
        pass
        # Step 1 - Retrieve the model Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policy-summary using Netconf

        # Step 2 - Retrieve the total-policy-count from the retrieved data

        # Step 3 - Fail the test if the total-policy-count is not 0


    @aetest.test
    @aetest.loop(
        device_name=["xrd-source", "xrd-source", "xrd-dest", "xrd-dest"],
        destination=["192.168.20.1", "172.16.20.1", "192.168.10.1", "172.16.10.1"],
        source=["192.168.10.1", "172.16.10.1", "192.168.20.1", "172.16.20.1"],
        expected=[["10.0.1.0", "10.0.14.1", "10.0.34.0", "10.0.23.0", "10.0.2.1"],
                  ["10.0.1.0", "10.0.14.1", "10.0.34.0", "10.0.23.0", "10.0.2.1"],
                  ["10.0.2.0", "10.0.23.1", "10.0.34.1", "10.0.14.0", "10.0.1.1"],
                  ["10.0.2.0", "10.0.23.1", "10.0.34.1", "10.0.14.0", "10.0.1.1"]
                  ]
    )
    def verify_traceroute_before(self, testbed, device_name, destination, source,expected):
        device = testbed.devices[device_name]
        if not _verify_traceroute(device,source,destination,expected):
            self.failed(f"Unexpected traceroute from {source} source {destination} on {device.name}",goto=["next_tc"])

    @aetest.test
    @aetest.loop(device_name=["xrd-1", "xrd-2"])
    def configure_sr_policy(self,testbed,device_name):
        device = testbed.devices[device_name]
        logger.info("Configuring SR Policy")
        device.last_commit_id = netconf_configure(
            device=device,
            target="candidate",
            config=string_from_file("netconf/configure_sr_policy.xml"),
        )

    @aetest.test
    def wait_sr_policy_installed(self):
        logger.info("Waiting 10 seconds for the SR policy to be installed")
        sleep(10)


    @aetest.test
    @aetest.loop(device_name=["xrd-1", "xrd-2"],
                 policy_name=["srte_c_10_ep_10.10.10.2", "srte_c_10_ep_10.10.10.1"])
    def verify_odn_policy(self,testbed,device_name,policy_name):
        device = testbed.devices[device_name]
        output = device.netconf.get(
            (
                "subtree",
                string_from_file("netconf/filter_odn_policy.xml").format(policy_name=policy_name),
            )
        )
        odn_policy = xmltodict.parse(output.xml,xml_attribs=False).get("rpc-reply",{}).get("data",{})
        if not odn_policy:
            self.failed(f"ODN policy {policy_name} not found",goto=["cleanup"])
        else:
            status = odn_policy.get("xtc",{}).get("policies",{}).get("policy",{}).get("operational-up",None)
            if status != "1":
                self.failed(f"ODN policy {policy_name} not operational",goto=["cleanup"])
            else:
                self.passed(f"ODN policy {policy_name} is operational")

    @aetest.test
    @aetest.loop(
        device_name=["xrd-source", "xrd-source", "xrd-dest", "xrd-dest"],
        destination=["192.168.20.1", "172.16.20.1", "192.168.10.1", "172.16.10.1"],
        source=["192.168.10.1", "172.16.10.1", "192.168.20.1", "172.16.20.1"],
        expected=[
            ["10.0.1.0", "10.0.14.1", "10.0.34.0", "10.0.23.0", "10.0.2.1"],
            ["10.0.1.0", "10.0.12.1", "10.0.2.1"],
            ["10.0.2.0", "10.0.23.1", "10.0.34.1", "10.0.14.0", "10.0.1.1"],
            ["10.0.2.0","10.0.12.0","10.0.1.1"]
        ],
    )
    def verify_traceroute_after(self, testbed, device_name, destination, source,expected):
        device = testbed.devices[device_name]
        if not _verify_traceroute(device,source,destination,expected):
            self.failed(f"Unexpected traceroute from {source} source {destination} on {device.name}")

    @aetest.cleanup
    @aetest.loop(device_name=["xrd-1", "xrd-2"])
    def rollback_configuration(self, testbed,device_name):
        device = testbed.devices[device_name]
        if not getattr(device,"last_commit_id",None):
            self.skipped("No configuration to rollback")
        logger.info(f"Rolling back configuration with commit ID {device.last_commit_id}")
        device.netconf.request(string_from_file("netconf/rollback.xml").format(commit_id=device.last_commit_id))

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect(self, testbed):
        logger.info(f"Disconnecting from devices")
        testbed.disconnect(
            testbed.devices["xrd-1"],
            testbed.devices["xrd-2"],
            testbed.devices["xrd-source"],
            testbed.devices["xrd-dest"]
        )


if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    logging.getLogger('ncclient.transport.ssh').setLevel(logging.WARNING)
    testbed = load("testbed.yaml")
    aetest.main(testbed=testbed)
