# 1. Execute command

This exercise is about executing a command on a device. It reuses some steps from the previous exercise such as loading the testbed and connecting to the devices.
The script is composed of 5 mains steps, only the bold ones are to be completed, the rest already is provided.

0. Load the testbed.
1. Connect to all devices in the testbed.
2. **Execute the `show version` command to the devices.**
3. **Print only the line of the output containing the device version.**
4. Disconnect from the devices.

## Output example

```
2024-01-18T21:18:27: %SCRIPT-INFO: =====================================xrd-1======================================
2024-01-18T21:18:27: %SCRIPT-INFO: Cisco IOS XR Software, Version 7.9.2 LNT
2024-01-18T21:18:29: %SCRIPT-INFO: =====================================xrd-2======================================
2024-01-18T21:18:29: %SCRIPT-INFO: Cisco IOS XR Software, Version 7.9.2 LNT
2024-01-18T21:18:30: %SCRIPT-INFO: =====================================xrd-3======================================
2024-01-18T21:18:30: %SCRIPT-INFO: Cisco IOS XR Software, Version 7.9.2 LNT
2024-01-18T21:18:32: %SCRIPT-INFO: =====================================xrd-4======================================
2024-01-18T21:18:32: %SCRIPT-INFO: Cisco IOS XR Software, Version 7.9.2 LNT
2024-01-18T21:18:33: %SCRIPT-INFO: ===================================xrd-source===================================
2024-01-18T21:18:33: %SCRIPT-INFO: Cisco IOS XR Software, Version 7.8.2 LNT
2024-01-18T21:18:35: %SCRIPT-INFO: ====================================xrd-dest====================================
2024-01-18T21:18:35: %SCRIPT-INFO: Cisco IOS XR Software, Version 7.8.2 LNT
```

## Folders

The files with the exercise are in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## Steps to complete the exercise

The exercise script already contains some code including some reused from the previous exercise. Missing code needs to be completed after the `# Step N` comments.

### Step 0 - Execute the `show version` command to the devices

Use the `execute()` method on each `device` object to send a CLI command to the `device`. Get the `show version` output, and save it in a variable.

Here, the `execute()` method will take one argument: a `str` which is the CLI command we want to send the device.

More information about the `execute()` method here:

> https://pubhub.devnetcloud.com/media/pyats/docs/apidoc/connections/index.html#module-pyats.connections.bases

### Step 1 - Print only the line of the output containing the device version

For simplicity, you can start by printing the whole output of the `show version` command (remember to use `logger.info(output)`). You will see that the output is a `str` object.

However, only a fraction of the output needs to be printed (see the secion **Output Example**, only the second line of the output is printed).

If you use the `splitlines()`  method on a `str` object, it returns a list of the lines in the string, breaking at line boundaries. Example below.

> More information about `splitlines()` method in the documentation.
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

Depending on how the parser is configured and what your CLI output looks like, the first element of the list might be an empty `str`.

## Nicely printing a `title` output

You might want to nicely print a Title output, like the `device.name` (`xrd-1`) as per the below example.

```
2024-01-18T21:18:27: %SCRIPT-INFO: =====================================xrd-1======================================
2024-01-18T21:18:27: %SCRIPT-INFO: Cisco IOS XR Software, Version 7.9.2 LNT
```

To do so, you should import the `pyats.log.utils.title` method and use it with `logger.info()`. See below example. `title` method takes a `str` as argument.

```python
from pyats.log.utils import title
logger.info(title(device.name))
```
