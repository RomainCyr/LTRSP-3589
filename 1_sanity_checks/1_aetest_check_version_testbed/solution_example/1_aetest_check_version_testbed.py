# import the aetest module
from pyats import aetest
from unicon.core.errors import ConnectionError
import logging

logger = logging.getLogger(__name__)

class CommonSetup(aetest.CommonSetup):

    # Step 0.1 - Set the devices to loop over for connection
    @aetest.subsection
    @aetest.loop(device_name=["xrd-1","xrd-2","xrd-3","xrd-4","xrd-source","xrd-dest"])
    def connect(self, device_name):
        # Step 0.2 - Connect to the device
        device = testbed.devices[device_name]
        try:
            device.connect(log_stdout=False, connection_timeout=10)
            logger.info(f'{ device.name} - connected')
        except ConnectionError:
            self.failed(f'Failed to connect to {device.name}')

class CheckVersion(aetest.Testcase):

    # Step 1.1 - Set the devices to loop over for version check
    @aetest.test
    @aetest.loop(device_name=["xrd-1","xrd-2","xrd-3","xrd-4","xrd-source","xrd-dest"])
    def check_version(self,device_name):
        # Step 1.2 - Parse `show version` output for the device being tested
        device = testbed.devices[device_name]
        parsed_version = device.parse("show version")
        # Step 1.3 - Verify that the device is running the correct version
        # The expected device version is store in the custom 'version' attribute: device.custom.version
        # use the aetest self.passed() and self.failed() methods to pass or fail the test
        if not parsed_version['software_version'] == device.custom.version:
            self.failed(f"{device.name} is not running {device.custom.version}, but {parsed_version['software_version']}",)
        else :
            self.passed(f"{device.name} is running the correct version: {parsed_version['software_version']}")

class CommonCleanup(aetest.CommonCleanup):

    # Step 2.1 - Set the devices to loop over for disconnecting
    @aetest.subsection
    @aetest.loop(device_name=["xrd-1","xrd-2","xrd-3","xrd-4","xrd-source","xrd-dest"])
    def disconnect(self, device_name):
        # Step 2.2 - Disconnect from the device
        device = testbed.devices[device_name]
        if device.connected:
            device.disconnect()

if __name__ == '__main__':

    from genie.testbed import load

    logger.setLevel(logging.INFO)
    testbed = load(f'testbed.yaml')
    aetest.main(testbed = testbed)