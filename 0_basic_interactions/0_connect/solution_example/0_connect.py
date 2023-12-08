from genie.testbed import load
import logging
from unicon.core.errors import ConnectionError
from pyats.log import ScreenHandler



logger = logging.getLogger(__name__)
logger.addHandler(ScreenHandler())
logger.setLevel(logging.INFO)

# Step 0 - Load the testbed
testbed = load('testbed.yaml')

# Step 1 - Connect to all devices in the testbed
fail_connect = False
for device in testbed:
    logger.info(f'Trying to connect to {device.name}.')
    try:
        device.connect(log_stdout=False, connection_timeout=10)
        logger.info(f'Connected to {device.name}.')
    except ConnectionError as e:
        logger.warning(f'Failed to connect to {device.name}.')
        fail_connect = True

# Step 2 - Use Python logic to confirm we are successfully connected to all devices
if fail_connect == False:
    logger.info('We have been able to connect to all devices!')
else:
    logger.warning('We have not been able to connect to all devices!')

# Step 3 - Disconnect from all devices in the testbed
for device in testbed:
    if device.connected:
        logger.info(f'Trying to disconnect from {device.name}.')
        device.disconnect()
        logger.info(f'Disconnected from {device.name}.')
    else:
        logger.info(f'Not connected to {device.name}.')
