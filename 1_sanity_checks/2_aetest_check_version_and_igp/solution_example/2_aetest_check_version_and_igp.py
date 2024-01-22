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
        # Step 0 - Set the devices to loop over for IGP verification
        to_check = []
        for device in testbed:
            if device.role in ["PE","P"]:
                to_check.append(device)

        # Step 1 - Mark the check_igp_config test section to loop over the list of device to be checked
        aetest.loop.mark(self.check_igp_config,device=to_check)

    @aetest.test
    def check_igp_config(self,device):
        # Step 2 - Collect the 'show running-config router isis' from the device and save it to a variable
        isis_config = device.execute("show running-config router isis")
        #Remove the first line of the output as it contains the timestamp
        isis_config = isis_config[isis_config.index('\n'):]
        # Step 3 - Convert the ISIS configuration to a Genie Config object
        isis_config = Config(isis_config)
        isis_config.tree()


        # Step 4 - Generate the expected ISIS configuration and convert it to a Genie Config object
        # The expected configuration is different if the device is a PE or a P router.
        # The files isis_pe_expected_config.txt and isis_p_expected_config.txt are provided to help you with this task
        # the ISIS NET address can be derived from the Loopback0 address using the provided isis_net_from_ip function
        net = isis_net_from_ip("0",device.interfaces.Loopback0.ipv4.ip.compressed)
        if getattr(device, "role",None) == "PE":
            with open("igp_expected_config_pe.txt") as f:
                expected_config = Config(f.read().format(net=net))
        elif getattr(device, "role",None) == "P":
            with open("igp_expected_config_p.txt") as f:
                expected_config = Config(f.read().format(net=net))
        expected_config.tree()

        # Step 5 - Compare the expected configuration with the actual configuration using the Genie Diff utility
        # The interface sections must be ignored using the 'exclude' keyword
        diff = Diff(isis_config, expected_config, exclude=["(^interface.*)"])
        diff.findDiff()

        # Step 6 - If the configuration are identical, pass the test, otherwise fail the test and print the diff
        if len(diff.diffs) != 0:
             logger.warning(f"Found difference in ISIS config:\n{diff}")
             self.failed("Unexpected ISIS configuration found on device.")

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