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
expected_conf = Config(expected_conf_str)
expected_conf.tree()

testbed = load('testbed.yaml')
xrd1 = testbed.devices['xrd-1']

try:
    xrd1.connect(log_stdout=False, connection_timeout=10)
except ConnectionError as e:
    logger.warning(f'Failed to connect to {xrd1.name}.')
    exit(1)

# Step 0 - Collect the `show running router bgp` and save it to a variable
output = xrd1.execute('show running router bgp')
# Remove the first line of the output as it contains the timestamp
output = output[output.index('\n'):]
# Step 1 - Convert the BGP config output to a `Config` object
config = Config(output)
config.tree()

# Step 2 - Use the `Diff` module to find the differences between the two configurations
diff = Diff(expected_conf, config)
diff.findDiff()

# Step 3 - Print the differences between the two configurations
logger.info(diff)

## Disconnecting from the device
if xrd1.connected:
    xrd1.disconnect()
