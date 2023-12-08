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
        try:
            device.connect(log_stdout=False, connection_timeout=10)
        except ConnectionError as e:
            logger.warning(f'Failed to connect to {device.name}.')
            continue

        # Step 2 - Send a `show version` command to each device and print it
        output = device.execute('show version')
        logger.info(title(device.name))
        logger.info(output.splitlines()[2])

# Step 3 - Disconnect from all devices in the testbed
for device in testbed:
    if device.connected:
        device.disconnect()
