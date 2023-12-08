from genie.testbed import load
import logging
from unicon.core.errors import ConnectionError
from pyats.log import ScreenHandler
from pyats.log.utils import title

logger = logging.getLogger(__name__)
logger.addHandler(ScreenHandler())
logger.setLevel(logging.INFO)

# Step 0 - Load the testbed
testbed = load('testbed.yaml')

# Step 1 - Connect to all devices in the testbed
for device in testbed:
    if device.name != 'jumphost':
        try:
            device.connect(log_stdout=False, connection_timeout=10)
        except ConnectionError as e:
            logger.warning(f'Failed to connect to {device.name}.')
            continue

        # Step 2 - Use the pyATS genie library to parse the output of the 'show version' command
        output = device.parse('show version')
        logger.info(title(device.name))
        logger.info(f"software_version = {output['software_version']}")

# Step 3 - Disconnect from all devices in the testbed
for device in testbed:
    if device.connected:
        device.disconnect()
