from genie.testbed import load
import logging
from unicon.core.errors import ConnectionError
from pyats.log import ScreenHandler

logger = logging.getLogger(__name__)
logger.addHandler(ScreenHandler())
logger.setLevel(logging.INFO)

testbed = load('testbed.yaml')

for device in testbed:
    try:
        device.connect(log_stdout=False, connection_timeout=10)
    except ConnectionError as e:
        logger.warning(f'Failed to connect to {device.name}.')
        continue

    # Step 0 - Parse a `show version` command to each device and save it to a variable

    # Step 1 - print only the value of 'software_version' key of the output dictionary

## Disconnecting from all devices in the testbed
for device in testbed:
    if device.connected:
        device.disconnect()
