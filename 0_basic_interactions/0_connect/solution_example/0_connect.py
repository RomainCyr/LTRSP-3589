from genie.testbed import load
import logging
from unicon.core.errors import ConnectionError
from pyats.log import ScreenHandler

logger = logging.getLogger(__name__)
logger.addHandler(ScreenHandler())
logger.setLevel(logging.INFO)

# Step 0 - Load the testbed
testbed = load('testbed.yaml')

# Step 1 - Connect to all devices in the testbed with a for loop and print a message once done
for device in testbed:
    logger.info(f'Trying to connect to {device.name}.')
    try:
        device.connect(log_stdout=False, connection_timeout=10)
        logger.info(f'Connected to {device.name}.')
    except ConnectionError as e:
        logger.warning(f'Failed to connect to {device.name}.')

for device in testbed:
    if device.connected:
        logger.info(f'Trying to disconnect from {device.name}.')
        device.disconnect()
        logger.info(f'Disconnected from {device.name}.')
    else:
        logger.info(f'Not connected to {device.name}.')
