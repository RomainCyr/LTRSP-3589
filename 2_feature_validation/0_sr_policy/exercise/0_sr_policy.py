from pyats import aetest
from genie.testbed import load

import logging
import re
from typing import List

logger = logging.getLogger(__name__)

def parse_traceroute(output: str) -> List[str]:
    """
    Parses the output of a traceroute command and extracts the IP addresses of each hop.

    Args:
        output: The output of the traceroute command.

    Returns:
        A list of IP addresses representing each hop - List[str]

    Example:
        RP/0/RP0/CPU0:xrd-1#traceroute 10.10.10.2 source 10.10.10.1
         1  10.0.14.1 [MPLS: Label 16002 Exp 0] 19 msec  11 msec  12 msec
         2  10.0.34.0 [MPLS: Label 16002 Exp 0] 9 msec  10 msec  10 msec
         3  10.0.23.0 14 msec  *  8 msec
        RP/0/RP0/CPU0:xrd-1#

        Returns ["10.0.14.0","10.0.34.0","10.0.23.0"]
    """

    hops = []
    for line in output.splitlines():
        if re.match(r"^\s*\d+\s+", line):
            hops.append(line.split()[1])
    return hops


class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect(self, testbed):
        # Step 0 - Connect to devices using the testbed.connect() method
        pass

# Step 1 - Verify no SR policy is configured and forwarding path is as expected
# This section must pass for the rest of the script to continue.
class InitialVerify(aetest.Testcase):
    must_pass = True

    # Step 1.0.0 - Check that no SR policy is configured on the device
    # This test section should be executed for both xrd-1 and xrd-2
    @aetest.test
    def check_no_policy(self, testbed, device_name):
        # Step 1.0.1 - Execute 'show segment-routing traffic-eng policy summary'
        # Verify that the total number of policies is 0
        pass

    # Step 1.1.0 Loop the test section to have it executed
    # for both destination prefixes 192.168.20.1 and 172.16.20.1
    @aetest.test
    def verify_traceroute(self, testbed, source, destination):
        # Step 1.1.1 - Execute 'traceroute' from xrd-source, parse it
        # and compare the path to the expected one
        pass

# Step 2 Configure the SR policy
class ConfigureSRPolicy(aetest.Testcase):
    must_pass = True

    # Step 2.0.0 - Loop the test section to have it executed on xrd-1 and xrd-2
    @aetest.test
    def configure_sr_policy(self, testbed, device_name):
        # Step 2.0.1 - Execute the configuration commands to configure the SR policy
        # The configuration is provided in the file sr_policy_config.txt
        pass

    @aetest.test
    def wait_sr_policy_installed(self):
        # Step 2.1.0 - Wait for the SR policy to be installed
        pass

    # Step 2.2.0 - Loop the test section to have it executed on xrd-1 and xrd-2
    # providing the expected policy name
    @aetest.test
    def verify_odn_policy(self, testbed, device_name, policy_name):
        # Step 2.2.1 - Verify that the policy status is up
        pass


# Step 3 - Verify the forwarding after the SR policy is installed
class VerifyForwarding(aetest.Testcase):

    # Step 3.0 - Loop the test section to have it executed for both destination prefixes
    @aetest.test
    def verify_traceroute(self, testbed, source, destination, expected):
        # Step 3.1 - Execute 'traceroute' from xrd-source, parse it
        # and compare the path to the expected one
        pass

# Step 4 - Clean configuration and disconnect
class CommonCleanup(aetest.CommonCleanup):

    # Step 4.0.0 - Loop the test section to have it executed on xrd-1 and xrd-2
    @aetest.subsection
    def rollback_configuration(self, testbed, device_name):
        # Step 4.0.1 - Rollback the configuration if configuration was applied before
        # Skip this test section otherwise
        pass

    @aetest.subsection
    def disconnect(self, testbed):
        # Step 4.1 - Disconnect from devices using the testbed.disconnect() method
        pass


if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    testbed = load("testbed.yaml")
    aetest.main(testbed=testbed)
