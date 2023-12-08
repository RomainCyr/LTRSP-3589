from genie.testbed import load
import logging
from unicon.core.errors import ConnectionError
from genie.utils.diff import Diff
from genie.utils.config import Config
from pyats.log import ScreenHandler


logger = logging.getLogger(__name__)
logger.addHandler(ScreenHandler())
logger.setLevel(logging.INFO)

expected_conf_str = '''
router bgp 65000
 bgp router-id 10.10.10.2
 address-family vpnv4 unicast
 !
 neighbor 10.10.10.4
  remote-as 65000
  update-source Loopback0
  address-family vpnv4 unicast
  !
 !
 vrf A
  address-family ipv4 unicast
   redistribute ospf A route-policy IMPORT_B
'''

# Step 0 - Convert the expected_conf_str to a Config object
expected_conf = Config(expected_conf_str)
expected_conf.tree()

# Step 1 - Load the testbed and connect to xrd-1
testbed = load('testbed.yaml')
xrd1 = testbed.devices['xrd-1']

try:
    xrd1.connect(log_stdout=False, connection_timeout=10)
except ConnectionError as e:
    logger.warning(f'Failed to connect to {xrd1.name}.')
    exit(1)

# Step 2 - Get the `show running config router bgp` output and convert it to a `Config` object
output = xrd1.execute('show running router bgp')
#Remove the first line of the output as it contains the timestamp
output = output[output.index('\n'):]
config = Config(output)
config.tree()

# Step 3 - Use the `Diff` module to print the differences between the two configurations
diff = Diff(expected_conf.config, config.config)
diff.findDiff()

logger.info(diff)

# Step 4 - Disconnect from xrd-1
if xrd1.connected:
    xrd1.disconnect()
