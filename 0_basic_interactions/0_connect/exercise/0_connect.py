import logging
from pyats.log import ScreenHandler
from genie.testbed import load

logger = logging.getLogger(__name__)
logger.addHandler(ScreenHandler())
logger.setLevel(logging.INFO)

# Step 0 - Load the testbed

# Step 1 - Connect to all devices in the testbed with a for loop 
# and print a message once done

## Disconnecting from all devices in the testbed
for device in testbed:
    if device.connected:
        logger.info(f'Trying to disconnect from {device.name}.')
        device.disconnect()
        logger.info(f'Disconnected from {device.name}.')
    else:
        logger.info(f'Not connected to {device.name}.')
