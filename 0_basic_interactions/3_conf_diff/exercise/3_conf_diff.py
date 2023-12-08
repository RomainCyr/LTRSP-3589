import logging
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

# Step 1 - Load the testbed and connect to xrd-1

# Step 2 - Get the `show running config router bgp` output and convert it to a `Config` object

# Step 3 - Use the `Diff` module to print the differences between the two configurations

# Step 4 - Disconnect from xrd-1
