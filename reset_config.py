from genie import testbed
from concurrent.futures import ThreadPoolExecutor,as_completed
import logging
from pyats.log import ScreenHandler
import os
import subprocess

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

filepath = os.path.dirname(os.path.realpath(__file__))
CONFIG_PATH = f"{filepath}/xrd/configs/"

def reset_config(device):
    logger.info(f"{device.name}: Connecting")
    device.connect(via = 'cli', log_stdout=False, connection_timeout=15)
    logger.info(f"{device.name}: Clear configuration inconsistency")
    device.execute("clear configuration inconsistency")
    logger.info(f"{device.name}: Copying initial config to router")
    filename = f"{device.name}_startup.cfg"
    subprocess.run(f"docker cp {CONFIG_PATH}{filename} {device.name}:/harddisk:/",shell=True)
    logger.info(f"{device.name}:Commit replace initial config")
    device.configure([f"load /harddisk:/{filename}",
                      "commit replace"])
    logger.info(f"{device.name}: Clear configuration inconsistency")
    device.execute("clear configuration inconsistency")

if __name__ == "__main__":
    logger.addHandler(ScreenHandler())
    testbed = testbed.load('testbed.yaml')
    with ThreadPoolExecutor(max_workers=10) as executor:
        threads = []
        for device in testbed:
            threads.append(executor.submit(reset_config,device))
        for thread in as_completed(threads):
             thread.result()
