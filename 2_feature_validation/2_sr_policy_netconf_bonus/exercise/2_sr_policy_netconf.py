from pyats import aetest
from genie.testbed import load
import logging

logger = logging.getLogger(__name__)

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect(self, testbed):
        # Step 0 - Connect to devices using the testbed.connect() method
        # The device should be connected using NETCONF
        pass

# Step 1 - Verify no SR policy is configured and forwarding path is as expected
# This section must pass for the rest of the script to continue.
class InitialVerify(aetest.Testcase):

    must_pass = True

    # Step 1.0.0 - Check that no SR policy is configured on the device
    # This test section should be executed for both xrd-1 and xrd-2
    @aetest.test
    def check_no_policy(self, testbed, device_name):
        # Step 1.0.1 - Retrieve the model Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policy-summary using Netconf
        # Verify that the total-policy-count is 0
        pass

    # Step 1.1.0 Loop the test section to have it executed for each pair of source and destination prefixes
    # on both xrd-source and xrd-dest
    @aetest.test
    def verify_traceroute(self, testbed, device_name, destination, source,expected):
        # Step 1.1.1 - Execute 'traceroute' using the Cisco-IOS-XR-traceroute-act model
        # and compare the path to the expected one
        pass

# Step 2 Configure the SR policy
class ConfigureSRPolicy(aetest.Testcase):

    must_pass = True

    # Step 2.0.0 - Loop the test section to have it executed on xrd-1 and xrd-2
    @aetest.test
    def configure_sr_policy(self,testbed,device_name):
        # Step 2.0.1 - Push the configuration of the SR policy using Netconf
        # The configuration in XML format is provided in the file configure_sr_policy.xml
        pass

    # Step 2.1.0 - Wait for the SR policy to be installed
    @aetest.test
    def wait_sr_policy_installed(self):
        pass

    # Step 2.2.0 - Loop the test section to have it executed on xrd-1 and xrd-2
    # providing the expected policy name
    @aetest.test
    def verify_odn_policy(self,testbed,device_name,policy_name):
        # Step 2.2.1 - Verify that the policy status is up using the model Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policies
        pass

# Step 3 - Verify the forwarding after the SR policy is installed
class VerifyForwarding(aetest.Testcase):

    # Step 3.0 - Loop the test section to have it executed
    # for both destination prefixes 192.168.20.1 and 172.16.20.1 on xrd-source
    # and for both destination prefixes 192.168.10.1 and 172.16.10.1 on xrd-dest
    @aetest.test
    def verify_traceroute(self, testbed, device_name, destination, source,expected):
        # Step 3.1 - Execute 'traceroute' using the Cisco-IOS-XR-traceroute-act model
        # and compare the path to the expected one
        pass


class CommonCleanup(aetest.CommonCleanup):

    # Step 4.0.0 - Loop the test section to have it executed on xrd-1 and xrd-2
    @aetest.subsection
    def rollback_configuration(self, testbed,device_name):
        # Step 4.0.1 - Rollback the configuration if the configuration was applied before and using the last commit id
        # The model Cisco-IOS-XR-cfgmgr-rollback-act can be used to rollback the configuration
        # Skip this test section otherwise
        pass


    @aetest.subsection
    def disconnect(self, testbed):
        # Step 4.1 - Disconnect from devices using the testbed.disconnect() method
        pass


if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    logging.getLogger('ncclient.transport.ssh').setLevel(logging.WARNING)
    testbed = load("testbed.yaml")
    aetest.main(testbed=testbed)
