from genie import testbed
from concurrent.futures import ThreadPoolExecutor,as_completed
import logging
from pyats.log import ScreenHandler
from unicon.eal.dialogs import Statement, Dialog

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



CONFIG_PATH = "xrd-tools/cl_lab/configs/"
HOST_PASSWORD = "cisco123"

def reset_config(device):
    logger.info(f"{device.name}: Connecting")
    device.connect(via = 'cli', log_stdout=False, connection_timeout=15)
    logger.info(f"{device.name}: Clear configuration inconsistency")
    device.execute("clear configuration inconsistency")
    logger.info(f"{device.name}: Copying initial config to router")
    password_dialog = Dialog(
        [
            Statement(
                pattern=r"Password:",
                action=lambda spawn: spawn.sendline(HOST_PASSWORD),
                loop_continue=True,
                continue_timer=False
            )
        ]
    )
    device.execute(f"scp cisco@172.40.0.1:{CONFIG_PATH}{device.name}_startup.cfg vrf MGMT /harddisk:/{device.name}_startup.cfg",reply= password_dialog)
    logger.info(f"{device.name}:Commit replace initial config")
    device.configure([f"load /harddisk:/{device.name}_startup.cfg",
                      "commit replace"])
    logger.info(f"{device.name}: Clear configuration inconsistency")
    device.execute("clear configuration inconsistency")

if __name__ == '__main__':
    logger.addHandler(ScreenHandler())
    testbed = testbed.load('testbed.yaml')

    with ThreadPoolExecutor(max_workers=10) as executor:
        threads = []
        for device in testbed:
            threads.append(executor.submit(reset_config,device))
        for thread in as_completed(threads):
             thread.result()
