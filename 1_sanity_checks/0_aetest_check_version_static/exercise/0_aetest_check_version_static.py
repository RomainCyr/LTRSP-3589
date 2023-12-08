# import the aetest module
from pyats import aetest
import logging

logger = logging.getLogger(__name__)

class CommonSetup(aetest.CommonSetup):

    # Step 0 - Connect to each device in the testbed
    @aetest.subsection
    def connect_to_devices(self, testbed):
        pass

class CheckVersion(aetest.Testcase):

    # Step 1 - Verify parsed output of 'show version' and verify the device is running IOS XR 7.9.2
    @aetest.test
    def check_current_version(self, testbed):

        # Step 1 - Verify parsed output of 'show version' and verify the device is running IOS XR 7.9.2

        # Step 1.0 - Loop on all devices that are connected.
        # Use the Genie library to parse the `show version` output from each device

        # Step 1.1 - Verify the device is running IOS XR 7.9.2
        
        # Step 1.2 - Fail the test section if the device is running the wrong version.

        # Step 1.3 - Bonus - Test all devices then fail the test if any device is running the wrong OS version.
        pass


class CommonCleanup(aetest.CommonCleanup):

    # Step 2 - Disconnect from each connected device
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        pass

if __name__ == '__main__':

    from genie.testbed import load
    logger.setLevel(logging.INFO)
    testbed = load('testbed.yaml')
    aetest.main(testbed = testbed)