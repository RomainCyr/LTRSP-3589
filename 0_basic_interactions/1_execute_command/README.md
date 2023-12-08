# 1. Execute command

In this exercise, we are going to:

0. Connect to each device.
1. Send a sample IOS XR command `show version` and partially print the output in the terminal.
2. Disconnect from each device.

## Output example

```
2023-10-31T15:20:35: %SCRIPT-INFO: =====================================xrd-1======================================
2023-10-31T15:20:35: %SCRIPT-INFO: Cisco IOS XR Software, Version 7.9.2 LNT
2023-10-31T15:20:38: %SCRIPT-INFO: =====================================xrd-2======================================
2023-10-31T15:20:38: %SCRIPT-INFO: Cisco IOS XR Software, Version 7.9.2 LNT
2023-10-31T15:20:42: %SCRIPT-INFO: =====================================xrd-3======================================
2023-10-31T15:20:42: %SCRIPT-INFO: Cisco IOS XR Software, Version 7.9.2 LNT
2023-10-31T15:20:45: %SCRIPT-INFO: =====================================xrd-4======================================
2023-10-31T15:20:45: %SCRIPT-INFO: Cisco IOS XR Software, Version 7.9.2 LNT
2023-10-31T15:20:49: %SCRIPT-INFO: ===================================xrd-source===================================
2023-10-31T15:20:49: %SCRIPT-INFO: Cisco IOS XR Software, Version 7.8.2 LNT
2023-10-31T15:20:52: %SCRIPT-INFO: ====================================xrd-dest====================================
2023-10-31T15:20:52: %SCRIPT-INFO: Cisco IOS XR Software, Version 7.8.2 LNT
```

## Folders

The file with the exercise is in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## Steps to complete the exercise

### Step 0 - Load the testbed

In this first step, we are going to load the testbed using the `load` function from the `genie.testbed` module. Use the testbed in the same folder as your Python code.

Below is an example about how to use it.

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

### Step 2 - Send a sample command to each device: `show version`

Use the `execute()` method on each `device` object to send a CLI command to the `device`. Get the `show version` output, and save it in a variable.

More information about the `execute()` method here:

> https://pubhub.devnetcloud.com/media/pyats/docs/apidoc/connections/index.html#module-pyats.connections.bases

For brevity, we might want to only get a fraction of the output (see above output example, only the second line of the output is printed). 

If you use the ` splitlines()`  method on a `str` object, it returns a list of the lines in the string, breaking at line boundaries. Example below.

>  More information about `splitlines()` method in the documentation.
>
> https://docs.python.org/3/library/stdtypes.html

```python-repl
>>> my_str = '''Thu Oct 26 14:12:37.263 UTC
... Cisco IOS XR Software, Version 7.8.2 LNT
... Copyright (c) 2013-2023 by Cisco Systems, Inc.
... 
... Build Information:
...  Built By     : ingunawa
...  Built On     : Wed Mar 15 16:45:19 UTC 2023
...  Build Host   : iox-lnx-100
...  Workspace    : /auto/srcarchive13/prod/7.8.2/xrd-control-plane/ws
...  Version      : 7.8.2
...  Label        : 7.8.2
... 
... cisco XRd Control Plane
... cisco XRd-CP-C-01 processor with 28GB of memory
... xrd-dest uptime is 6 hours, 23 minutes
... XRd Control Plane Container'''
>>> 
>>> print(my_str.splitlines())
['Thu Oct 26 14:12:37.263 UTC', 'Cisco IOS XR Software, Version 7.8.2 LNT', 'Copyright (c) 2013-2023 by Cisco Systems, Inc.', '', 'Build Information:', ' Built By     : ingunawa', ' Built On     : Wed Mar 15 16:45:19 UTC 2023', ' Build Host   : iox-lnx-100', ' Workspace    : /auto/srcarchive13/prod/7.8.2/xrd-control-plane/ws', ' Version      : 7.8.2', ' Label        : 7.8.2', '', 'cisco XRd Control Plane', 'cisco XRd-CP-C-01 processor with 28GB of memory', 'xrd-dest uptime is 6 hours, 23 minutes', 'XRd Control Plane Container']
```

### Step 3 - Disconnect from all devices in the testbed

Don't forget to disconnect from all devices. Create a loop to disconnect from each device in the testbed.

It's very similar to `step 1`. The documentation can be found here:

> https://pubhub.devnetcloud.com/media/pyats/docs/connections/manager.html#method-disconnect

Each `device` object has a `connected` attribute which returns `True` or `False`. Use it to know if you are successfuly connected to the device.
