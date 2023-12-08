# import the aetest module
from pyats import aetest
import logging

logger = logging.getLogger(__name__)

class CommonSetup(aetest.CommonSetup):

    # Step 0.1 - Set the devices to loop over for connection
    @aetest.subsection
    def connect_to_devices(self, device):
        # Step 0.2 - Connect to the device
        pass

class CheckVersion(aetest.Testcase):

    # Step 1.1 - Set the devices to loop over for version check
    @aetest.test
    def check_current_version(self, device):

        # Step 1.2 - Parse `show version` output for the device being tested

        # Step 1.3 - Verify that the device is running the correct version
        # The expected device version is store in the custom 'version' attribute: device.custom.version
        # use the aetest self.passed() and self.failed() methods to pass or fail the test
        pass


class CommonCleanup(aetest.CommonCleanup):

    # Step 2.1 - Set the devices to loop over for disconnecting
    @aetest.subsection
    def disconnect(self, device):
        # Step 2.2 - Disconnect from the device
        pass

if __name__ == '__main__':

    from genie.testbed import load

    logger.setLevel(logging.INFO)
    testbed = load('testbed.yaml')
    aetest.main(testbed = testbed)