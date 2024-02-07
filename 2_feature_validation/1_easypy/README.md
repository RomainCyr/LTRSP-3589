# 1. Easypy: Automated Easy Testing

This exercise aims to show how Easypy can be used to scale AEtest scripts.
Easypy is a framework that simplifies the execution of AEtest scripts and provides standardized runtime environment for
test script execution.
It provides additional features and functionality such as **built-in logging**, **result reporting**, and
**error handling capabilities**. Easypy also offers the ability to easily **run tasks in parallel**.

This exercise focuses on the Easypy job file and is composed of 4 steps that needs to be completed:

0. Use a loop to execute the **Sanity Checks** script on all devices of the testbed.
1. Run the AETest script on each device.
2. Exit the Easypy job if any of the sanity check fails.
3. Run the **SR Policy Validation** script.

## Output example

Output has been truncated for brevity. Only the Easypy report is shown below.

```plaintext
2024-01-21T12:56:06: %EASYPY-INFO: +------------------------------------------------------------------------------+
2024-01-21T12:56:06: %EASYPY-INFO: |                             Task Result Summary                              |
2024-01-21T12:56:06: %EASYPY-INFO: +------------------------------------------------------------------------------+
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-1: 1_sanity_checks.common_setup                                PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-1: 1_sanity_checks.CheckVersion                                PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-1: 1_sanity_checks.CheckIGP                                    PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-1: 1_sanity_checks.common_cleanup                              PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-2: 1_sanity_checks.common_setup                                PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-2: 1_sanity_checks.CheckVersion                                PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-2: 1_sanity_checks.CheckIGP                                    PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-2: 1_sanity_checks.common_cleanup                              PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-3: 1_sanity_checks.common_setup                                PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-3: 1_sanity_checks.CheckVersion                                PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-3: 1_sanity_checks.CheckIGP                                    PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-3: 1_sanity_checks.common_cleanup                              PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-4: 1_sanity_checks.common_setup                                PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-4: 1_sanity_checks.CheckVersion                                PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-4: 1_sanity_checks.CheckIGP                                    PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-4: 1_sanity_checks.common_cleanup                              PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-source: 1_sanity_checks.common_setup                           PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-source: 1_sanity_checks.CheckVersion                           PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-source: 1_sanity_checks.CheckIGP                              SKIPPED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-source: 1_sanity_checks.common_cleanup                         PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-dest: 1_sanity_checks.common_setup                             PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-dest: 1_sanity_checks.CheckVersion                             PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-dest: 1_sanity_checks.CheckIGP                                SKIPPED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-dest: 1_sanity_checks.common_cleanup                           PASSED
2024-01-21T12:56:06: %EASYPY-INFO: SR Policy Test: 1_sr_policy.common_setup                                  PASSED
2024-01-21T12:56:06: %EASYPY-INFO: SR Policy Test: 1_sr_policy.ODNSRPolicyValidation                         PASSED
2024-01-21T12:56:06: %EASYPY-INFO: SR Policy Test: 1_sr_policy.common_cleanup                                PASSED
2024-01-21T12:56:06: %EASYPY-INFO: 
2024-01-21T12:56:06: %EASYPY-INFO: +------------------------------------------------------------------------------+
2024-01-21T12:56:06: %EASYPY-INFO: |                             Task Result Details                              |
2024-01-21T12:56:06: %EASYPY-INFO: +------------------------------------------------------------------------------+
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-1: 1_sanity_checks
2024-01-21T12:56:06: %EASYPY-INFO: |-- common_setup                                                          PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- connect                                                           PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |-- CheckVersion                                                          PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- check_version                                                     PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |-- CheckIGP                                                              PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- check_igp_config                                                  PASSED
2024-01-21T12:56:06: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
2024-01-21T12:56:06: %EASYPY-INFO:     `-- disconnect                                                        PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-2: 1_sanity_checks
2024-01-21T12:56:06: %EASYPY-INFO: |-- common_setup                                                          PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- connect                                                           PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |-- CheckVersion                                                          PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- check_version                                                     PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |-- CheckIGP                                                              PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- check_igp_config                                                  PASSED
2024-01-21T12:56:06: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
2024-01-21T12:56:06: %EASYPY-INFO:     `-- disconnect                                                        PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-3: 1_sanity_checks
2024-01-21T12:56:06: %EASYPY-INFO: |-- common_setup                                                          PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- connect                                                           PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |-- CheckVersion                                                          PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- check_version                                                     PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |-- CheckIGP                                                              PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- check_igp_config                                                  PASSED
2024-01-21T12:56:06: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
2024-01-21T12:56:06: %EASYPY-INFO:     `-- disconnect                                                        PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-4: 1_sanity_checks
2024-01-21T12:56:06: %EASYPY-INFO: |-- common_setup                                                          PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- connect                                                           PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |-- CheckVersion                                                          PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- check_version                                                     PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |-- CheckIGP                                                              PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- check_igp_config                                                  PASSED
2024-01-21T12:56:06: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
2024-01-21T12:56:06: %EASYPY-INFO:     `-- disconnect                                                        PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-source: 1_sanity_checks
2024-01-21T12:56:06: %EASYPY-INFO: |-- common_setup                                                          PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- connect                                                           PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |-- CheckVersion                                                          PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- check_version                                                     PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |-- CheckIGP                                                             SKIPPED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- check_igp_config                                                 SKIPPED
2024-01-21T12:56:06: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
2024-01-21T12:56:06: %EASYPY-INFO:     `-- disconnect                                                        PASSED
2024-01-21T12:56:06: %EASYPY-INFO: Sanity xrd-dest: 1_sanity_checks
2024-01-21T12:56:06: %EASYPY-INFO: |-- common_setup                                                          PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- connect                                                           PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |-- CheckVersion                                                          PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- check_version                                                     PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |-- CheckIGP                                                             SKIPPED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- check_igp_config                                                 SKIPPED
2024-01-21T12:56:06: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
2024-01-21T12:56:06: %EASYPY-INFO:     `-- disconnect                                                        PASSED
2024-01-21T12:56:06: %EASYPY-INFO: SR Policy Test: 1_sr_policy
2024-01-21T12:56:06: %EASYPY-INFO: |-- common_setup                                                          PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- connect                                                           PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |-- ODNSRPolicyValidation                                                 PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   |-- check_no_policy[device_name=xrd-1]                                PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   |-- check_no_policy[device_name=xrd-2]                                PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   |-- verify_traceroute_before[destination=192.168.20.1,source=19...    PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   |-- verify_traceroute_before[destination=172.16.20.1,source=172...    PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   |-- configure_sr_policy[device_name=xrd-1]                            PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   |-- configure_sr_policy[device_name=xrd-2]                            PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   |-- wait_sr_policy_installed                                          PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   |-- verify_odn_policy[device_name=xrd-1,policy_name=srte_c_10_e...    PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   |-- verify_odn_policy[device_name=xrd-2,policy_name=srte_c_10_e...    PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   |-- verify_traceroute_after[destination=192.168.20.1,expected=[...    PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   |-- verify_traceroute_after[destination=172.16.20.1,expected=['...    PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   |-- rollback_configuration[device_name=xrd-1]                         PASSED
2024-01-21T12:56:06: %EASYPY-INFO: |   `-- rollback_configuration[device_name=xrd-2]                         PASSED
2024-01-21T12:56:06: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
2024-01-21T12:56:06: %EASYPY-INFO:     `-- disconnect                                                        PASSED                                                     PASSED
```

## Folders

The files with the exercise are in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## Easypy Job File

A job file allows the aggregation of multiple test scripts together and executed within the same runtime environment.
It can be used to run multiple test scripts in a row, or to run the same testscript multiple times with different parameters.

In this exercise, a job file will be used to chain the execution of the **Sanity Check** script on all device and then the **SR Policy Validation** script.

A job file is run using the pyats command line. The job file is passed as an argument to the `pyats run job` command.
For example, to run the job file `1_job.py` with the testbed `testbed.yaml`, the following command is used `pyats run job 1_job.py --testbed testbed.yaml`.

There are many other arguments available and even custom one can be created. Refer to the documentation below for more information.

> https://pubhub.devnetcloud.com/media/pyats/docs/easypy/usages.html

A job file must satisfy the following requirements:

- A `main()` function must be defined, it is the main entry point of the job file run.
- A `runtime` argument is passed to the `main(runtime)` function. It will be automatically passed and is used to provide the runtime environment.

The runtime provides multiple information about the current job and environment. For example the testbed is accessible from the runtime with `runtime.testbed`, the job name can be accessed with `runtime.job.name` and modified.

Refer to the documentation below for more information.

> https://pubhub.devnetcloud.com/media/pyats/docs/easypy/jobfile.html#run-api

## Sanity Checks script modification

The `1_job.py` is used to launch the `1_sanity_checks.py` test script for each device. Therefore, the `1_sanity_checks.py` should not handle a list of device but only one.
This is done because the `1_sanity_checks.py` script is only doing verification that are device specific. It concerns only one device at a time and does not need to look at multiples devices.

When executing the test script standalone, the `testbed` argument was passed to the `aetest.main()` function, and it was available to all test sections as an argument. Running the test script with a job file, there will be no more `testbed` argument passed, but only a `device` argument.

The `sanity_checks.py` script from previous exercises is reused but slightly modified to ensure that each test section
is made for handling only one device. The modified `1_sanity_checks.py` file is already provided in the `exercise` folder. You may have a look at it and compare it with the previous `sanity_checks.py` script.

## Steps to complete the exercise

The exercise script already contains some code including some reused from the previous exercise. Missing code needs to be completed after the `# Step N` comments.

### Step 0 - Use a for loop to iterate over all devices of the testbed

When the testbed file is provided as an argument of the pyats run job command, it is accessible from the runtime
argument with `runtime.testbed`.

In the `1_job.py` file, use a `for` loop to iterate over all devices in the testbed.

### Step 1 - Run the AETest sanity_checks script on each device using the easypy run() method

An AEtest script can be run with the `run()` function of easypy as show below:

```python
from pyats.easypy import run

def main(runtime):
    result = run("my_test_script.py", argument1 = "A", argument2 = "B")
```

Any argument can be provided to the testscript, in this case the `device` argument must be provided as it's required by the test sections in the `1_sanity_check.py` AEtest script. `device` argument will be automatically passed to each test section. Below is an example.

 ```python
 run("1_sanity_checks.py", device = device)
 ```

For reporting purpose, the name of the task being run can be specified with the `taskid` parameter. Below is an example.

```python
run("1_sanity_checks.py", taskid = f"Sanity {device.name}", device = device)
```

If you want to run this job file at this point refer to the [Step 4 - Run the Job](#step-4---run-the-job)

### Step 2 - Exit the job if any of the sanity check failed

The `run()` method returns a `TestResult` object. It can be used as a boolean to check if the testscript passed (`True`) or failed (`False`).

```python
def main(runtime):
    result = run("my_test_script.py")
    if result:
        logger.info("Testscript passed")
    else:
        logger.info("Testscript failed")
```

If any of the `sanity_checks.py` testscript fails for one device, the `1_sr_policy.py` test script should not be run. The job should stop directly with a failure.
After each sanity checks execution, verify its result and if it failed the `main()` function should be exited with `return`.

If you want to run this job file at this point refer to the [Step 4 - Run the Job](#step-4---run-the-job)

### Step 3 - Run the SR Policy validation test script

If all the sanity checks have passed, run the SR Policy validation test script.
Use the easypy `run` method to run this testscript. Note that the `testbed` argument is automatically passed to the testscript.

```python
def main(runtime):
    run("my_test_script.py")
    # is equivalent 
    run("my_test_script.py", testbed = runtime.testbed)
```

For reporting purpose, the name of the task may be changed with the `taskid` parameter.

### Step 4 - Run the job

Using the pyats command line, run the job file. The testbed is passed as an argument with the `--testbed` argument `pyats run job 1_job.py --testbed testbed.yaml`.
There are many other arguments that can be used with the pyats command line, use `pyats run job --help` to see them.

### Step 5 - View the logs

Using the pyATS command line, use `pyats logs view` to see the results.

When the job has finished to run, a Task Result summary is printed. It shows the result of each task that was run and details the result of each test section.
All the execution logs are available in the terminal but it may be rather long and hard to read.

There are two ways to improve the log experience:

- You can use the command `pyats logs view` that will create a local web server that can be used to browse the logs interactively. Each Task is displayed in a separate tab.
- A static HTML report can be generated when executing a job by using the `--html-logs <directory>` option. It will generate a static HTML report that doesn't need a web server to be opened.

Refer to the documentation below for more information.

> https://pubhub.devnetcloud.com/media/pyats/docs/cli/pyats_logs.html

### Bonus - Modify the job file to run the sanity check in parallel on all devices

Modify the code of the `1_job.py` file to run the `1_sanity_checks.py` script in parallel on all devices (feel free to create another python file). 

All sanity checks can be executed independently of each other.
This is one of the advanced capability of Easypy, it allows to run testscript asynchronously and with better control over each task.

Instead of using the `run()` method, `Task` objects are created. An easypy `Task` is a subclass of a Python `multiprocessing.Process`.
Using multiprocessing can be quite complex and may require advanced programming skills to deal with resources and data sharing between process.
For example, we would not advise to run multiple `1_sr_policy.py` test in parallel, as the configuration is being modified and then rollback.
Nevertheless, when testscript are independent, like sanity checks, and do not rely on shared resources, it is safe to run them in parallel with an Easypy `Task`.

To launch a testscript, a `Task` object must be first created. Instantiating a `Task` object does not create the actual child process, the child process,
hence the script, is only launched when the method `start()` is called.
This method `return` directly, it does not wait for the child process to finish. To wait for the child process to finish,
the `wait()` method must be called. The `max_runtime` argument can be passed to specify a `timeout` to the task, so it does not run forever.

Below is an example of launching several tasks in parallel and waiting for them to finish.

```python
from pyats.easypy import Task
import logging

logger = logging.getLogger(__name__)

def main(runtime):
    my_tasks = []
    for i in range(5):
        task = Task("test_script.py", taskid = f"Task {i}", index = i)
        task.start()
        my_tasks.append(task)

    for task in my_tasks:
        task.wait()
        if not task.result:
            logger.warning(f"Task {task.index} failed")
```
