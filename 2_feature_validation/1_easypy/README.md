# 1. Easypy: Automated Easy Testing

In this last exercise, we will use Easypy. Easypy is a framework that simplifies the execution of AEtest scripts and provides standardized runtime environment for testscript execution.
It provides additional features and functionality such as **built-in logging**, **result reporting**, and **error handling capabilities**. Easypy also offers the ability to easily **run tasks in parallel**. A task could be the execution of an AETest script.

We are going to proceed with the following step on this exercise:

1. Modify the `sanity check` script to handle only one device at a time,
2. Create a job file that first run the `sanity check` on all devices and then the `Segment Routing Policy validation script`,
3. Modify the job file to run the `sanity check` in parallel on all devices.

## Output example

Only the report example is shown below. The full output would be too long.

```plaintext
2023-11-10T17:16:13: %EASYPY-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:16:13: %EASYPY-INFO: |                                Easypy Report                                 |
2023-11-10T17:16:13: %EASYPY-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:16:13: %EASYPY-INFO: pyATS Instance   : /home/cisco/.virtualenvs/cisco_live_pyats_lab
2023-11-10T17:16:13: %EASYPY-INFO: Python Version   : cpython-3.10.12 (64bit)
2023-11-10T17:16:13: %EASYPY-INFO: CLI Arguments    : /home/cisco/.virtualenvs/cisco_live_pyats_lab/bin/pyats run job 1_job.py --testbed testbed.yaml
2023-11-10T17:16:13: %EASYPY-INFO: User             : cisco
2023-11-10T17:16:13: %EASYPY-INFO: Host Server      : xrd-server
2023-11-10T17:16:13: %EASYPY-INFO: Host OS Version  : Ubuntu 22.04 jammy (x86_64)
2023-11-10T17:16:13: %EASYPY-INFO: 
2023-11-10T17:16:13: %EASYPY-INFO: Job Information
2023-11-10T17:16:13: %EASYPY-INFO:     Name         : 1_job
2023-11-10T17:16:13: %EASYPY-INFO:     Start time   : 2023-11-10 17:14:45.349866+00:00
2023-11-10T17:16:13: %EASYPY-INFO:     Stop time    : 2023-11-10 17:16:12.352822+00:00
2023-11-10T17:16:13: %EASYPY-INFO:     Elapsed time : 87.002956
2023-11-10T17:16:13: %EASYPY-INFO:     Archive      : /home/cisco/.pyats/archive/23-11/1_job.2023Nov10_17:14:39.867222.zip
2023-11-10T17:16:13: %EASYPY-INFO: 
2023-11-10T17:16:13: %EASYPY-INFO: Total Tasks    : 7 
2023-11-10T17:16:13: %EASYPY-INFO: 
2023-11-10T17:16:13: %EASYPY-INFO: Overall Stats
2023-11-10T17:16:13: %EASYPY-INFO:     Passed     : 25
2023-11-10T17:16:13: %EASYPY-INFO:     Passx      : 0
2023-11-10T17:16:13: %EASYPY-INFO:     Failed     : 0
2023-11-10T17:16:13: %EASYPY-INFO:     Aborted    : 0
2023-11-10T17:16:13: %EASYPY-INFO:     Blocked    : 0
2023-11-10T17:16:13: %EASYPY-INFO:     Skipped    : 2
2023-11-10T17:16:13: %EASYPY-INFO:     Errored    : 0
2023-11-10T17:16:13: %EASYPY-INFO: 
2023-11-10T17:16:13: %EASYPY-INFO:     TOTAL      : 27
2023-11-10T17:16:13: %EASYPY-INFO: 
2023-11-10T17:16:13: %EASYPY-INFO: Success Rate   : 100.00 %
2023-11-10T17:16:13: %EASYPY-INFO: 
2023-11-10T17:16:13: %EASYPY-INFO: Section Stats
2023-11-10T17:16:13: %EASYPY-INFO:     Passed     : 37
2023-11-10T17:16:13: %EASYPY-INFO:     Passx      : 0
2023-11-10T17:16:13: %EASYPY-INFO:     Failed     : 0
2023-11-10T17:16:13: %EASYPY-INFO:     Aborted    : 0
2023-11-10T17:16:13: %EASYPY-INFO:     Blocked    : 0
2023-11-10T17:16:13: %EASYPY-INFO:     Skipped    : 2
2023-11-10T17:16:13: %EASYPY-INFO:     Errored    : 0
2023-11-10T17:16:13: %EASYPY-INFO: 
2023-11-10T17:16:13: %EASYPY-INFO:     TOTAL      : 39
2023-11-10T17:16:13: %EASYPY-INFO: 
2023-11-10T17:16:13: %EASYPY-INFO: Section Success Rate   : 100.00 %
2023-11-10T17:16:13: %EASYPY-INFO: 
2023-11-10T17:16:13: %EASYPY-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:16:13: %EASYPY-INFO: |                             Task Result Summary                              |
2023-11-10T17:16:13: %EASYPY-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-1: 1_sanity_checks.common_setup                                PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-1: 1_sanity_checks.CheckVersion                                PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-1: 1_sanity_checks.CheckIGP                                    PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-1: 1_sanity_checks.common_cleanup                              PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-2: 1_sanity_checks.common_setup                                PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-2: 1_sanity_checks.CheckVersion                                PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-2: 1_sanity_checks.CheckIGP                                    PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-2: 1_sanity_checks.common_cleanup                              PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-3: 1_sanity_checks.common_setup                                PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-3: 1_sanity_checks.CheckVersion                                PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-3: 1_sanity_checks.CheckIGP                                    PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-3: 1_sanity_checks.common_cleanup                              PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-4: 1_sanity_checks.common_setup                                PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-4: 1_sanity_checks.CheckVersion                                PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-4: 1_sanity_checks.CheckIGP                                    PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-4: 1_sanity_checks.common_cleanup                              PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-source: 1_sanity_checks.common_setup                           PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-source: 1_sanity_checks.CheckVersion                           PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-source: 1_sanity_checks.CheckIGP                              SKIPPED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-source: 1_sanity_checks.common_cleanup                         PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-dest: 1_sanity_checks.common_setup                             PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-dest: 1_sanity_checks.CheckVersion                             PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-dest: 1_sanity_checks.CheckIGP                                SKIPPED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-dest: 1_sanity_checks.common_cleanup                           PASSED
2023-11-10T17:16:13: %EASYPY-INFO: SR Policy Test: 1_sr_policy.common_setup                                  PASSED
2023-11-10T17:16:13: %EASYPY-INFO: SR Policy Test: 1_sr_policy.ODNSRPolicyValidation                         PASSED
2023-11-10T17:16:13: %EASYPY-INFO: SR Policy Test: 1_sr_policy.common_cleanup                                PASSED
2023-11-10T17:16:13: %EASYPY-INFO: 
2023-11-10T17:16:13: %EASYPY-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:16:13: %EASYPY-INFO: |                             Task Result Details                              |
2023-11-10T17:16:13: %EASYPY-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-1: 1_sanity_checks
2023-11-10T17:16:13: %EASYPY-INFO: |-- common_setup                                                          PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- connect                                                           PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |-- CheckVersion                                                          PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- check_version                                                     PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |-- CheckIGP                                                              PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- check_igp_config                                                  PASSED
2023-11-10T17:16:13: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
2023-11-10T17:16:13: %EASYPY-INFO:     `-- disconnect                                                        PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-2: 1_sanity_checks
2023-11-10T17:16:13: %EASYPY-INFO: |-- common_setup                                                          PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- connect                                                           PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |-- CheckVersion                                                          PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- check_version                                                     PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |-- CheckIGP                                                              PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- check_igp_config                                                  PASSED
2023-11-10T17:16:13: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
2023-11-10T17:16:13: %EASYPY-INFO:     `-- disconnect                                                        PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-3: 1_sanity_checks
2023-11-10T17:16:13: %EASYPY-INFO: |-- common_setup                                                          PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- connect                                                           PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |-- CheckVersion                                                          PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- check_version                                                     PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |-- CheckIGP                                                              PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- check_igp_config                                                  PASSED
2023-11-10T17:16:13: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
2023-11-10T17:16:13: %EASYPY-INFO:     `-- disconnect                                                        PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-4: 1_sanity_checks
2023-11-10T17:16:13: %EASYPY-INFO: |-- common_setup                                                          PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- connect                                                           PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |-- CheckVersion                                                          PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- check_version                                                     PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |-- CheckIGP                                                              PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- check_igp_config                                                  PASSED
2023-11-10T17:16:13: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
2023-11-10T17:16:13: %EASYPY-INFO:     `-- disconnect                                                        PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-source: 1_sanity_checks
2023-11-10T17:16:13: %EASYPY-INFO: |-- common_setup                                                          PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- connect                                                           PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |-- CheckVersion                                                          PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- check_version                                                     PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |-- CheckIGP                                                             SKIPPED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- check_igp_config                                                 SKIPPED
2023-11-10T17:16:13: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
2023-11-10T17:16:13: %EASYPY-INFO:     `-- disconnect                                                        PASSED
2023-11-10T17:16:13: %EASYPY-INFO: Sanity xrd-dest: 1_sanity_checks
2023-11-10T17:16:13: %EASYPY-INFO: |-- common_setup                                                          PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- connect                                                           PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |-- CheckVersion                                                          PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- check_version                                                     PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |-- CheckIGP                                                             SKIPPED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- check_igp_config                                                 SKIPPED
2023-11-10T17:16:13: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
2023-11-10T17:16:13: %EASYPY-INFO:     `-- disconnect                                                        PASSED
2023-11-10T17:16:13: %EASYPY-INFO: SR Policy Test: 1_sr_policy
2023-11-10T17:16:13: %EASYPY-INFO: |-- common_setup                                                          PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- connect                                                           PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |-- ODNSRPolicyValidation                                                 PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   |-- check_no_policy[device_name=xrd-1]                                PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   |-- check_no_policy[device_name=xrd-2]                                PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   |-- verify_traceroute_before[destination=192.168.20.1,source=19...    PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   |-- verify_traceroute_before[destination=172.16.20.1,source=172...    PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   |-- configure_sr_policy[device_name=xrd-1]                            PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   |-- configure_sr_policy[device_name=xrd-2]                            PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   |-- wait_sr_policy_installed                                          PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   |-- verify_odn_policy[device_name=xrd-1,policy_name=srte_c_10_e...    PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   |-- verify_odn_policy[device_name=xrd-2,policy_name=srte_c_10_e...    PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   |-- verify_traceroute_after[destination=192.168.20.1,expected=[...    PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   |-- verify_traceroute_after[destination=172.16.20.1,expected=['...    PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   |-- rollback_configuration[device_name=xrd-1]                         PASSED
2023-11-10T17:16:13: %EASYPY-INFO: |   `-- rollback_configuration[device_name=xrd-2]                         PASSED
2023-11-10T17:16:13: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
2023-11-10T17:16:13: %EASYPY-INFO:     `-- disconnect                                                        PASSED
```

## Folders

The file with the exercise is in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## Easypy Job file

A job file allows the aggregation of multiple test scripts together and executed within the same runtime environment that will run your testscript.
It can be used to run multiple test scripts in a row, or to run the same testscript multiple times with different parameters.

In this exercise, a job file will be used to chain the execution of the `sanity check` script on all device and then the `SR Policy validation` script.

A job file is run using the pyats command line. The job file is passed as an argument to the `pyats run job` command. For example, to run the job file `1_job.py` on the file `./testbed.yaml`, the following command is used `pyats run job 1_job.py --testbed testbed.yaml`.

There are many other arguments available and even custom one can be created. Refer to the documentation below for more information.

> https://pubhub.devnetcloud.com/media/pyats/docs/easypy/usages.html


## Steps

To send information inline, in the output of your script, use the `logger.info()` method. For instance, in order to print the below output, you can use `logger.info('xrd-1 is connected')`

```
2023-10-21T11:05:40: %SCRIPT-INFO: xrd-1 is connected
```

### Step 0 - Modify the sanity check script (1_sanity_check.py) to handle only one device at a time

The `job.py` file will be used to launch the `1_sanity_checks.py` test script for each device. Therefore, the `1_sanity_checks.py` should not handle a list of device but only one.
This is done because the `1_sanity_checks.py` script is only doing verification that are device specific. It concerns only one device at a time and does not need to look at multiples devices.
The `job.py` file will be used to ensure that the `1_sanity_checks.py` script is executed on all devices.

When executing the test script standalone, the `testbed` argument was passed to the `aetest.main()` function, and it was available to all test sections as an argument. Running the test script with a job file, there will be no more `testbed` argument passed, but only a `device` argument.

You can reuse the `sanity_checks.py` script you wrote during the previous exercise, or you can use the one provided that comes from solution example.

When the `sanity_checks.py` was launched before, each `testcase` contained a `setup` function that would dynamically mark the test section to be loop over for a list of device.
Now that the job file will be used to loop over the list of device, the `setup` function is no longer needed.

#### Step 0.0 - Modify the `CommonSetup` function to handle only one device

In the `CommonSetup` section, remove the `setup()` function. The `connect()` function is already good as it take one device as an argument.

#### Step 0.1 - Modify the `CheckVersion` testcase to handle only one device

Modify the `CheckVersion` testcase so it is only handling one device. The `setup()` function is no longer needed and the `check_version` already accept a single device as an argument.

#### Step 0.2 - Modify the `CheckIGP` testcase to handle only one device

Modify the `CheckIGP` testcase so it is run only for a single device when its role is **P** or **PE**. Remember, you can retrieve the device `role` by accessing the `device.role` attribute.

The `setup()` function needs to be removed as it is no longer needed. The `check_isis_config()` needs to check first if the device is a P or PE router and skip the testcase otherwise.
If the testcase should be skipped (for non P or PE routers) use the `self.skipped()` method.

#### Step 0.3 - Modify the disconnect function to handle only one device

In the `CommonCleanup` section, remove the `setup` function. The `disconnect()` method only take one device as an argument.

### Step 1 - Create a job file (1_job.py)

A job file must satisfy the following requirements:

- A `main()` function must be defined, it is the main entry point of the job file run.
- A `runtime` argument is passed to the `main(runtime)` function. It will be automatically passed and is used to provide the runtime environment.

The runtime provides multiple information about the current job and environment. For example the testbed is accessible from the runtime with `runtime.testbed`, the job name can be accessed with `runtime.job.name` and modified.

Refer to the documentation below for more information.

> https://pubhub.devnetcloud.com/media/pyats/docs/easypy/jobfile.html#run-api

#### Step 1.0 - Run the sanity check test script on all devices

Using a for loop, launch the `1_sanity_checks.py` script for each device in the testbed. The testbed is accessible from the runtime argument with `runtime.testbed`. An AEtest script can be run with the `run()` function of easypy as show below:

```python
from pyats.easypy import run

def main(runtime):
    result = run("my_test_script.py", argument1 = "A", argument2 = "B")
```

Any argument can be provided to the testscript, in this case the `device` argument must be provided `run("1_sanity_checks.py", device = device)`. It will be automatically passed to the test section functions of the AEtest script.
For reporting purpose, the name of the task being run can be specified with the `taskid` parameter. For example: `run("1_sanity_checks.py",taskid=f"Sanity {device.name}", device=device)`

If you want to run this job file at this point refer to the [Step 1.3 Run the Job](#step-13-run-the-job) 

#### Step 1.1 - Exit the job if any of the sanity check failed

The `run()` method returns a `TestResult` object. It can be used as a boolean to check if the testscript passed or failed.

```python
def main(runtime):
    result = run("my_test_script.py")
    if result:
        logger.info("Testscript passed")
    else:
        logger.info("Testscript failed")
```
If any of the sanity check on the devices fail, the `1_sr_policy.py` test script should not be run. The job should stop directly with a failure.
After each sanity check is run, verify its result and if it failed the `main()` function should be exited with `return`.

If you want to run this job file at this point refer to the [Step 1.3 Run the Job](#step-13-run-the-job) 

#### Step 1.2 - Run the SR Policy validation test script

If all the sanity checks have passed, run the SR Policy validation test script. The `1_sr_policy.py` test script you wrote during the previous exercise can be reused, or use the one provided that comes from solution example.

Use the easypy `run` method to run this testscript. Note that the `testbed` argument is automatically passed to the testscript.

```python
def main(runtime):
    run("my_test_script.py")
    # is equivalent 
    run("my_test_script.py", testbed = runtime.testbed)
```

#### Step 1.3 Run the job

Using the pyats command line, run the job file. The testbed is passed as an argument with the `--testbed` argument `pyats run job 1_job.py --testbed testbed.yaml`.
There are many other arguments that can be used with the pyats command line, use `pyats run job --help` to see them.

When the job has finished to run, a Task Result summary is printed. It shows the result of each task that was run and details the result of each test section.
All the execution logs are available in the terminal but it may be rather long and hard to read.

There are two ways to improve the log experience:

- You can use the command `pyats logs view` that will create a local web server that can be used to browse the logs interactively. Each Task is displayed in a separate tab.
- A static HTML report can be generated when executing a job by using the `--html-logs <directory>` option. It will generate a static HTML report that doesn't need a web server to be opened.

Refer to the documentation below for more information.

> https://pubhub.devnetcloud.com/media/pyats/docs/cli/pyats_logs.html

### Step 2 - Modify the job file to run the sanity check in parallel on all devices 

This step will use the `1_job_parallel.py` file.

The code of the `1_job.py` file can be modified to run the `1_sanity_checks.py` script in parallel on all devices. Indeed, all sanity checks can be executed independently of each other.
This is one of the advanced capability of Easypy, it allows to run testscript asynchronously and with better control over each task.

Instead of using the `run()` method, `Task` objects are created. An easypy `Task` is a subclass of a Python `multiprocessing.Process`.
Using multiprocessing can be quite complex and may require advanced programming skills to deal with resources and data sharing between process. For example, we would not advise to run multiple `1_sr_policy.py` test in parallel, as the configuration is being modified and then rollbacked.
Nevertheless, when testscript are independent, like sanity checks, and do not rely on shared resources, it is safe to run them in parallel with an Easypy `Task`.

#### Step 2.0 - Create a sanity check task for each device and start them

To launch a testscript, a `Task` object must be first created. Instantiating a `Task` object does not create the actual child process, the child process, hence the script, is only launched when the method `start()` is called.
This method `return` directly, it does not wait for the child process to finish. To wait for the child process to finish, the `wait()` method must be called. The `max_runtime` argument can be passed to specify a `timeout` to the task, so it does not run forever.

Below is an example of launching several tasks in parallel and waiting for them to finish.

```python
from pyats.easypy import Task


def main(runtime):
    tasks = []
    for i in range(5):
        task = Task("test_script.py",taskid=f"Task {i}" index=i)
        task.start()
        tasks.append(task)

    for task in tasks:
        task.wait()
        if not task.result:
            logger.warning(f"Task {task.index} failed")
```

Using a `for` loop create a task for each device that run the sanity checks test script. The taskid should be set to `Sanity {device.name}`. Launch the task immediately after it is created.

#### Step 2.1 - Wait for all tasks to finish

Using a second `for` loop that iterates over the task created, wait for all task to finish using the `wait()` method.

When all the tasks have finished, if any of them has failed exit the job. The `result` attribute of the task can be used to check if the task passed or failed.

#### Step  2.2 Run the SR Policy validation test script

If all the sanity checks have passed, run the SR Policy validation test script. This is the same as for the step 1.1.

#### Step 2.3 Run the job

As for the step 1.2, run the job `1_job_parallel.py`, that you just wrote, using the pyats command line.
As the sanity checks task are run simultaneously, the terminal log output may be a bit messy as each test script will output logs at the same time.
Therefore, it is better to read the logs once the execution is finished using the `pyats logs view` command.
