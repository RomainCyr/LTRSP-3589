# 2. Structured output

In this exercise, we are going to:

0. Connect to each device.
1. Leverage the pyATS librairies, parse the `show version` output and print the IOS XR version in the console.
2. Disconnect from each device.

## Output example

```
2023-10-31T15:18:15: %SCRIPT-INFO: =====================================xrd-1======================================
2023-10-31T15:18:15: %SCRIPT-INFO: software_version = 7.9.2
2023-10-31T15:18:23: %SCRIPT-INFO: =====================================xrd-2======================================
2023-10-31T15:18:23: %SCRIPT-INFO: software_version = 7.9.2
2023-10-31T15:18:28: %SCRIPT-INFO: =====================================xrd-3======================================
2023-10-31T15:18:28: %SCRIPT-INFO: software_version = 7.9.2
2023-10-31T15:18:32: %SCRIPT-INFO: =====================================xrd-4======================================
2023-10-31T15:18:32: %SCRIPT-INFO: software_version = 7.9.2
2023-10-31T15:18:36: %SCRIPT-INFO: ===================================xrd-source===================================
2023-10-31T15:18:36: %SCRIPT-INFO: software_version = 7.8.2
2023-10-31T15:18:41: %SCRIPT-INFO: ====================================xrd-dest====================================
2023-10-31T15:18:41: %SCRIPT-INFO: software_version = 7.8.2
```

## Folders

The file with the exercise is in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## Steps to complete the exercise

### Step 0 - Load the testbed

In this first step, we are going to load the testbed using the `load` function from the `genie.testbed` module. Use the testbed in the same folder as your Python code.

Below is a example about how to use it.

```
testbed = testbed.load('/path/to/your/testbed.yaml')
```

### Step 1 - Connect to all devices in the testbed

Now we are going to connect to each device in the testbed (using a loop).

The `connect()` method is explained here:

> https://pubhub.devnetcloud.com/media/pyats/docs/connections/manager.html#method-instantiate-connect

The below arguments avoid printing the full device log to `stdout` and sets the `connection_timeout` to 10 seconds (so you don't wait for a minute if you can't connect to a device).

```
device.connect(log_stdout=False, connection_timeout=10)
```

Note that if the `device.connect()` method fails, you will get a `unicon.core.errors.ConnectionError` exception like below. You can try to catch this error in case the `device.connect()` doesn't work.

```
The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/anorsoni/Documents/Programmability/cisco_live_pyats_lab/0_basic_interactions/0_connect/sample_solution/0_connect.py", line 22, in <module>
    device.connect(via='cli', log_stdout=False, connection_timeout=10)
  File "src/pyats/connections/manager.py", line 454, in pyats.connections.manager.ConnectionManager.connect
  File "src/unicon/bases/connection.py", line 799, in unicon.bases.connection.Connection.connect
unicon.core.errors.ConnectionError: failed to connect to xrd-1
Failed while bringing device to "any" state
```

You can read more about errors and exceptions in the below documentation.

> https://docs.python.org/3/tutorial/errors.html

Each `device` object has a `connected` attribute which returns `True` or `False`. Use it to know if you are successfuly connected to the device.

Each `device` object also has a `name` attribute which returns the device name (as per the name in the testbed).

### Step 2 - Use the pyATS librairies to parse the output of the `show version` command

Use the `parse()` method on each `device` object to send the `show version` command to the `device` and parse the output using pyATS librairies. Get the `show version` output, and save it in a variable.

Documentation about `parse()` method can be found here:

> https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/explore.html?highlight=parse#

Available parsers can be found here:

> https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers

The `parse()` method will return a dictionary. No need to print it all. Only print the IOS XR version in the console (see sample output above).

### Step 3 - Disconnect from all devices in the testbed

Don't forget to disconnect from all devices. Create a loop to disconnect from each device in the testbed.

It's very similar to `step 1`. The documentation can be found here:

> https://pubhub.devnetcloud.com/media/pyats/docs/connections/manager.html#method-disconnect

Each `device` object has a `connected` attribute which returns `True` or `False`. Use it to know if you are successfuly connected to the device.
