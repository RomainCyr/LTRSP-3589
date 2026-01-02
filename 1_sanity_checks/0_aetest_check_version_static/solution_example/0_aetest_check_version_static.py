from pyats import aetest
import logging
from pyats.log.utils import title

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

    @aetest.test
    def check_current_version(self, testbed):

        test_failed = False
        for device in testbed:
            # Step 0 - Verify the version only if the device is connected
            if device.connected:
            # Step 1 - Parse `show version` output for the device and save it to a variable
                output = device.parse('show version')
                device.version = output['software_version']
            # Step 2 - Print only the value of 'software_version' key of the output dictionary
                logger.info(title(device.name))
                logger.info(f"software_version = {device.version}")
            # Step 3 - Verify the device is running IOS XR 24.4.2, print a warning if it is not the case
                if device.version != '24.4.2':
                    logger.warning(f'{device.name} is not running XR 24.4.2')
            # Step 4 - Update test_failed variable if device is running the wrong version
                    test_failed = True

        if test_failed:
            self.failed(f'Some devices are running the wrong version')


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