import logging
from pyats.log import ScreenHandler



logger = logging.getLogger(__name__)
logger.addHandler(ScreenHandler())
logger.setLevel(logging.INFO)

# Step 0 - Load the testbed

# Step 1 - Connect to all devices in the testbed

# Step 2 - Send a `show version` command to each device and print it

# Step 3 - Disconnect from all devices in the testbed
