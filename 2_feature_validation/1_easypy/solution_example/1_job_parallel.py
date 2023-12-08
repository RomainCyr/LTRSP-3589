from pyats.easypy import Task,run
import logging

logger = logging.getLogger(__name__)

def main(runtime):
    # Step 2.0 - Create a sanity check task for each device and start them
    tasks = []
    for device in runtime.testbed:
        sanity_task = Task("1_sanity_checks.py",taskid=f"Sanity {device.name}", device=device)
        tasks.append(sanity_task)
        sanity_task.start()

    # Step 2.1 - Wait for all tasks to finish
    sanity_failed = False
    for sanity_task in tasks:
        sanity_task.wait()
        if not sanity_task.result:
            logger.error(f"Sanity check for task {sanity_task.taskid} failed")
            sanity_failed = True

    if sanity_failed:
        logger.error("Sanity check failed, aborting")
        return

    # Step  2.2 Run the SR Policy validation test script
    run("1_sr_policy.py",taskid="SR Policy Test")

