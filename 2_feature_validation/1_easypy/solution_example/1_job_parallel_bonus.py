from pyats.easypy import Task,run
import logging

logger = logging.getLogger(__name__)

def main(runtime):
    tasks = []
    for device in runtime.testbed:
        sanity_task = Task("1_sanity_checks.py",taskid=f"Sanity {device.name}", device=device)
        tasks.append(sanity_task)
        sanity_task.start()

    sanity_failed = False
    for sanity_task in tasks:
        sanity_task.wait()
        if not sanity_task.result:
            logger.error(f"Sanity check for task {sanity_task.taskid} failed")
            sanity_failed = True

    if sanity_failed:
        logger.error("Sanity check failed, aborting")
        return

    run("1_sr_policy.py",taskid="SR Policy Test")

