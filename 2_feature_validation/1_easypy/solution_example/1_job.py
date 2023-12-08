from pyats.easypy import run
import logging

logger = logging.getLogger(__name__)

def main(runtime):
    # Step 1.0 - Run the sanity check test script on all devices
    for device in runtime.testbed:
        sanity_task = run("1_sanity_checks.py",taskid=f"Sanity {device.name}", device=device)
        # Step 1.1 - Exit the job if any of the sanity check failed
        if not sanity_task:
            logger.error(f"Sanity check for {device.name} failed, aborting")
            return

    # Step 1.2 - Run the SR Policy validation test script
    run("1_sr_policy.py",taskid="SR Policy Test")

