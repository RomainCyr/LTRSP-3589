from pyats import aetest
import logging
from genie.utils.config import Config
from genie.utils.diff import Diff

logger = logging.getLogger(__name__)

def isis_net_from_ip(area: str,ip: str) -> str:
    '''
    Convert an IP address to an ISIS NET address
    The area and the ip address are padded to 4 and 12 digits respectively.
    Each part of the IP address is padded with 0 and then rearrange in block of 4 digits
    Example: 192.168.1.1 becomes 192.168.001.001 and then becomes 1921.6800.1001 (3 blocks of 4 digits)
    Input:
        area: str - the area number
        ip: str - the ip address
    Return the ISIS NET address - str
    '''
    system_id = ip.split('.')
    for index in range(len(system_id)):
        system_id[index] = str(system_id[index]).rjust(3,'0')
    system_id = ''.join(system_id)
    system_id = f"{system_id[:4]}.{system_id[4:8]}.{system_id[8:]}"
    area = str(area).rjust(4,'0')
    return f"49.{area}.{system_id}.00"


class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def setup(self,testbed):
        aetest.loop.mark(self.connect,device=[device for device in testbed])

    @aetest.subsection
    def connect(self, device):
        try:
            device.connect(log_stdout=False, connection_timeout=10)
            self.passed(f'{ device.name} - connected')
        except ConnectionError:
            self.failed(f'Failed to connect to {device.name}.')

class CheckVersion(aetest.Testcase):

    @aetest.setup
    def setup(self,testbed):
        aetest.loop.mark(self.check_version, device=[device for device in testbed])

    @aetest.test
    def check_version(self,device):
        parsed_version = device.parse("show version")
        if not parsed_version['software_version'] == device.custom.version:
            self.failed(f"{device.name} is not running {device.custom.version}, but {parsed_version['software_version']}",)
        else :
            self.passed(f"{device.name} is running the correct version: {parsed_version['software_version']}")


class CheckIGP(aetest.Testcase):

    @aetest.setup
    def setup(self,testbed):
        pass
        # Step 0 - Set the devices to loop over for IGP verification

        # Step 1 - Mark the check_igp_config test section to loop over the list of device to be checked

    @aetest.test
    def check_igp_config(self,device):
        pass
        # Step 2 - Collect the IGP configuration from the device and save it to a variable

        # Step 3 - Convert the IGP configuration to a Genie Config object


        # Step 4 - Generate the expected ISIS configuration and convert it to a Genie Config object
        # The expected configuration is different if the device is a PE or a P router.
        # The files isis_pe_expected_config.txt and isis_p_expected_config.txt are provided to help you with this task
        # the ISIS NET address can be derived from the Loopback0 address using the provided isis_net_from_ip function

        # Step 5 - Compare the expected configuration with the actual configuration using the Genie Diff utility
        # The interface sections must be ignored using the 'exclude' keyword

        # Step 6 - If the configuration are identical, pass the test, otherwise fail the test and print the diff

class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def setup(self,testbed):
        aetest.loop.mark(self.disconnect,device=[device for device in testbed])


    @aetest.subsection
    def disconnect(self, device):
        if device.connected:
            device.disconnect()

if __name__ == '__main__':

    from genie.testbed import load

    logger.setLevel(logging.INFO)
    testbed = load(f'testbed.yaml')
    aetest.main(testbed = testbed)