# import the aetest module
from pyats import aetest
from unicon.core.errors import ConnectionError
import logging

logger = logging.getLogger(__name__)

class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def connect_to_devices(self, testbed):
        for device in testbed:
            try:
                device.connect(log_stdout=False, connection_timeout=10)
                logger.info(f'{ device.name} - connected')
            except ConnectionError:
                logger.error(f'{ device.name} - connection failed')
                continue

class CheckVersion(aetest.Testcase):

    # Step 0 - Set the devices to loop over for the test section
    @aetest.test
    def check_version(self,testbed,device_name):
        device = testbed.devices[device_name]
        if device.connected:
            parsed_version = device.parse("show version")
            # Step 1 - Verify if the device is running its expected version

            # Step 2 - Failed the testcase if the device is running the wrong version

            # Step 3 - Pass the testcase if the device is running the correct version

        else:
            self.failed(f"{device.name} is not connected")

class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        for device in testbed:
            if device.connected:
                device.disconnect()

if __name__ == '__main__':

    from genie.testbed import load

    logger.setLevel(logging.INFO)
    testbed = load(f'testbed.yaml')
    aetest.main(testbed = testbed)