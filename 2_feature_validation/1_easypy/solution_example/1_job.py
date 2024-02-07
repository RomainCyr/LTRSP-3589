from pyats.easypy import run
import logging

logger = logging.getLogger(__name__)

def main(runtime):
    # Step 0 - Use a for loop to iterate over all devices of the testbed
    for device in runtime.testbed:
    # Step 1 - Run the AETest script on each device using the easypy run() method
        sanity_task = run("1_sanity_checks.py",taskid=f"Sanity {device.name}", device=device)
    # Step 2 - Exit the job if any of the sanity check failed
        if not sanity_task:
            logger.error(f"Sanity check for {device.name} failed, aborting")
            return

    # Step 3 - Run the AETest SR Policy validation test script using the easypy run() method
    run("1_sr_policy.py",taskid="SR Policy Test")

