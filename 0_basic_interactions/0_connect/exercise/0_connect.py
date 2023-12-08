import logging
from pyats.log import ScreenHandler


logger = logging.getLogger(__name__)
logger.addHandler(ScreenHandler())
logger.setLevel(logging.INFO)

# Step 0 - Load the testbed

# Step 1 - Connect to all devices in the testbed

# Step 2 - Use Python logic to confirm we are successfully connected to all devices
    
# if ...:
    logger.info('We have been able to connect to all devices!')

# Step 3 - Disconnect from all devices in the testbed
