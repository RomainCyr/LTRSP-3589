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

def netconf_configure_with_lock(device: Device,target: str,config: str):
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
    device.netconf.lock(target=target)
    device.netconf.edit_config(
            target=target,
            config=config,
        )
    device.netconf.commit()
    last_commit_id = device.netconf.get(("subtree", string_from_file("netconf/filter_last_commit_id.xml")))
    last_commit_id = xmltodict.parse(last_commit_id.xml)
    last_commit_id = last_commit_id["rpc-reply"]["data"]["config-manager"]["global"]["config-commit"]["last-commit-id"]["#text"]
    device.netconf.unlock(target=target)
    return last_commit_id


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
    traceroute = device.netconf.request(
            string_from_file("netconf/traceroute.xml").format(destination=destination,source=source)
        )
    traceroute = xmltodict.parse(traceroute)
    traceroute = traceroute.get("rpc-reply",{}).get("traceroute-response",{}).get("ipv4",{}).get("hops",{}).get("hop",{})
    hops = []

    for hop in traceroute:
        if "hop-address" in hop:
            hops.append(hop["hop-address"])
        else:
            for probe in hop["probes"]["probe"]:
                if "hop-address" in probe:
                    hops.append(probe["hop-address"])
                    break
            else:
                hops.append("*")

    if hops != expected:
        logger.warning(f"Found difference in traceroute:\nExpected:{str(expected)}\nGot:{str(hops)}\n")
        return False
    return True

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect(self, testbed):
        # Step 0 - Connect to devices using the testbed.connect() method
        # The device should be connected using NETCONF
        logger.info(f"Connecting to devices")
        testbed.connect(
            testbed.devices["xrd-1"],
            testbed.devices["xrd-2"],
            testbed.devices["xrd-source"],
            testbed.devices["xrd-dest"],
            vias={
                "xrd-1": "netconf",
                "xrd-2": "netconf",
                "xrd-source": "netconf",
                "xrd-dest": "netconf",
            },
            log_stdout=False,
            connection_timeout=10,
        )


class ODNSRPolicyValidation(aetest.Testcase):

    # Step 1 - Verify no SR policy is configured and forwarding path is as expected
    # This section must pass for the rest of the script to continue.
    # Step 1.0.0 - Check that no SR policy is configured on the device
    # This test section should be executed for both xrd-1 and xrd-2
    @aetest.test
    @aetest.loop(device_name=["xrd-1", "xrd-2"])
    def check_no_policy(self, testbed, device_name):
        # Step 1.0.1 - Retrieve the model Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policy-summary using Netconf
        # Verify that the total-policy-count is 0
        device = testbed.devices[device_name]
        policy_summary = device.netconf.get(
            (
                "subtree",
                string_from_file("netconf/filter_policy_summary.xml"),
            )
        )
        policy_summary = xmltodict.parse(policy_summary.xml)
        policy_summary = policy_summary["rpc-reply"]["data"]["xtc"]["policy-summary"]
        if int(policy_summary["total-policy-count"]) != 0:
            self.failed(f"Existing policy found on device {device.name}",goto=["cleanup"])

    # Step 1.1.0 Loop the test section to have it executed for each pair of source and destination prefixes
    # on both xrd-source and xrd-dest
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
        # Step 1.1.1 - Execute 'traceroute' using the Cisco-IOS-XR-traceroute-act model
        # and compare the path to the expected one
        device = testbed.devices[device_name]
        if not _verify_traceroute(device,source,destination,expected):
            self.failed(f"Unexpected traceroute from {source} source {destination} on {device.name}",goto=["cleanup"])

    # Step 2 Configure the SR policy
    # Step 2.0.0 - Loop the test section to have it executed on xrd-1 and xrd-2
    @aetest.test
    @aetest.loop(device_name=["xrd-1", "xrd-2"])
    def configure_sr_policy(self,testbed,device_name):
        # Step 2.0.1 - Push the configuration of the SR policy using Netconf
        # The configuration in XML format is provided in the file configure_sr_policy.xml
        device = testbed.devices[device_name]
        logger.info("Configuring SR Policy")
        device.last_commit_id = netconf_configure_with_lock(
            device=device,
            target="candidate",
            config=string_from_file("netconf/configure_sr_policy.xml"),
        )

    # Step 2.1.0 - Wait for the SR policy to be installed
    @aetest.test
    def wait_sr_policy_installed(self):
        logger.info("Waiting 10 seconds for the SR policy to be installed")
        sleep(10)

    # Step 2.2.0 - Loop the test section to have it executed on xrd-1 and xrd-2
    # providing the expected policy name
    @aetest.test
    @aetest.loop(device_name=["xrd-1", "xrd-2"],
                 policy_name=["srte_c_10_ep_10.10.10.2", "srte_c_10_ep_10.10.10.1"])
    def verify_odn_policy(self,testbed,device_name,policy_name):
        # Step 2.2.1 - Verify that the policy status is up using the model Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policies
        device = testbed.devices[device_name]
        odn_policy = device.netconf.get(
            (
                "subtree",
                string_from_file("netconf/filter_odn_policy.xml").format(policy_name=policy_name),
            )
        )
        odn_policy = xmltodict.parse(odn_policy.xml)
        odn_policy = odn_policy.get("rpc-reply",{}).get("data",{})
        if not odn_policy:
            self.failed("ODN policy not found",goto=["cleanup"])
        else:
            status = odn_policy.get("xtc",{}).get("policies",{}).get("policy",{}).get("operational-up",None)
            if status != "1":
                self.failed("ODN policy not operational",goto=["cleanup"])
            else:
                self.passed(f"ODN policy {policy_name} is operational")

    # Step 3 - Verify the forwarding after the SR policy is installed
    # Step 3.0 - Loop the test section to have it executed
    # for both destination prefixes 192.168.20.1 and 172.16.20.1 on xrd-source
    # and for both destination prefixes 192.168.10.1 and 172.16.10.1 on xrd-dest
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
        # Step 3.1 - Execute 'traceroute' using the Cisco-IOS-XR-traceroute-act model
        # and compare the path to the expected one
        device = testbed.devices[device_name]
        if not _verify_traceroute(device,source,destination,expected):
            self.failed(f"Unexpected traceroute from {source} source {destination} on {device.name}")

    # Step 4 - Clean configuration
    # Step 4.0.0 - Loop the test section to have it executed on xrd-1 and xrd-2
    @aetest.cleanup
    @aetest.loop(device_name=["xrd-1", "xrd-2"])
    def rollback_configuration(self, testbed,device_name):
        # Step 4.0.1 - Rollback the configuration if the configuration was applied before and using the last commit id
        # The model Cisco-IOS-XR-cfgmgr-rollback-act can be used to rollback the configuration
        # Skip this test section otherwise
        device = testbed.devices[device_name]
        if not getattr(device,"last_commit_id",None):
            self.skipped("No configuration to rollback")
        logger.info(f"Rolling back configuration")
        device.netconf.request(string_from_file("netconf/rollback.xml").format(commit_id=device.last_commit_id))

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect(self, testbed):
        # Step 4.1 - Disconnect from devices using the testbed.disconnect() method
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
