from pyats import aetest
import logging
logger = logging.getLogger(__name__)

def isis_net_from_ip(area: str,ip: str) -> str:
    '''
    Convert an IP address to an ISIS NET address
    The area and the ip address are padded to 4 and 12 digits respectively.
    Each part of the IP address is padded with 0 and then rearrange in block of 4 digits
    Example: 192.168.1.1 becomes 1921.6800.1001
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
        # Step 0.1 - Set the devices to loop over for connection
        # Mark the 'connect' subsection with the aetest.loop.mark function
        pass

    @aetest.subsection
    def connect(self, device):
        # Step 0.2 - Connect to the device
        pass

class CheckVersion(aetest.Testcase):

    @aetest.setup
    def setup(self,testbed):
        # Step 1.0 - Mark the check_version test section to loop over a list of device with aeest.loop.mark function
        pass

    @aetest.test
    def check_version(self,device):
        # Step 1.1 - Parse `show version` output for the device being tested

        # Step 1.2 - Verify that the device is running the correct version
        # use the aetest self.passed() and self.failed() methods to pass or fail the test
        pass


class CheckIGP(aetest.Testcase):

    @aetest.setup
    def setup(self,testbed):
        # Step 2.0 - Set the devices to loop over for IGP verification
        # Only the device that are PE or P should be tested, the role of the device can be access with device.role
        pass

    @aetest.test
    def check_igp_config(self,device):
        # Step 2.1 Collect the IGP configuration from the device, save it to a variable and convert it to a Genie Config object

        # Step 2.2 - Generate the expected ISIS configuration and convert it to a Genie Config object
        # The expected configuration is different if the device is a PE or a P router.
        # The files isis_pe_expected_config.txt and isis_p_expected_config.txt are provided to help you with this task
        # the ISIS NET address can be derived from the Loopback0 address using the provided isis_net_from_ip function

        # Step 2.3 - Compare the expected configuration with the actual configuration using the Genie Diff utility
        # The interface sections must be ignored using the 'exclude' keyword

        # Step 2.5 - If the configuration are identical, pass the test, otherwise fail the test
        pass

class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def setup(self,testbed):
        # Step 3.0 - Set the devices to loop over for disconnecting
        pass


    @aetest.subsection
    def disconnect(self, device):
        # Step 3.1 - Disconnect from the device
        pass

if __name__ == '__main__':

    from genie.testbed import load

    logger.setLevel(logging.INFO)
    testbed = load(f'testbed.yaml')
    aetest.main(testbed = testbed)