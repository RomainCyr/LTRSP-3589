# 0. Connect to each device

In this very first exercise, we are going to:

0. Connect to each device.
1. Verify we are connected to each device.
2. Disconnect from each device.

## Output example

Output has been truncated for brievety.

```2023-10-26T11:55:25:
2023-10-26T11:55:27: %SCRIPT-INFO: Connected to xrd-1.
2023-10-26T11:55:27: %SCRIPT-INFO: Trying to connect to xrd-2.
2023-10-26T11:55:30: %SCRIPT-INFO: Connected to xrd-2.
2023-10-26T11:55:30: %SCRIPT-INFO: Trying to connect to xrd-3.
2023-10-26T11:55:32: %SCRIPT-INFO: Connected to xrd-3.
[...]
2023-10-26T11:55:40: %SCRIPT-INFO: We have been able to connect to all devices!
2023-10-26T11:55:40: %SCRIPT-INFO: Trying to connect to xrd-1.
2023-10-26T11:55:40: %SCRIPT-INFO: Disconnected from xrd-1.
2023-10-26T11:55:40: %SCRIPT-INFO: Trying to connect to xrd-2.
2023-10-26T11:55:40: %SCRIPT-INFO: Disconnected from xrd-2.
2023-10-26T11:55:40: %SCRIPT-INFO: Trying to connect to xrd-3.
2023-10-26T11:55:40: %SCRIPT-INFO: Disconnected from xrd-3.
[...]
```

## Folders

The file with the exercise is in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

# PyATS Testbed

The pyATS testbed is a YAML file that describes and captures all the details about the network devices and topology such as device information, connection details, credentials, and more.
It serves as an inventory of the network, it can be used to save information about devices and is used by pyATS to connect to devices.

Below is a simple testbed file.

``` yaml   
testbed:
  name: lab     #Optional Testbed Name
  credentials:  # Default credentials used by every device in the testbed
    default:             
        username: cisco
        password: cisco    
devices:
  RouterA:     
    connections:
      cli:
        arguments:                      
            init_config_commands: [] # Disable default init config commands such as 'logging console disable'
        host: 192.168.1.10           # Device Connection Information
        protocol: ssh
    os: iosxr                        # Device OS
```

The testbed file for the lab is already provided, you can have a look at it to see how it looks like.

You can read more about the testbed file in the documentation below.

>https://pubhub.devnetcloud.com/media/pyats/docs/topology/index.html

## Steps to complete the exercise

### Step 0 - Load the testbed

In this first step, we are going to load the testbed using the `load` function from the `genie.testbed` module. Use the testbed in the same folder as your Python code.

Below is a example about how to use it.

```
testbed = testbed.load('/path/to/your/testbed.yaml')
```

### Step 1 - Connect to all devices in the testbed

Now we are going to connect to each device in the testbed (using a loop) and verify we are actually connected by pritting the device name and the confirmation we are connected.

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

Each `device` object has a `connected` attribute which returns `True` or `False`. Use it to know if you are successfully connected to the device.

Each `device` object also has a `name` attribute which returns the device name (as per the name in the testbed).

By default, you should be able to connect to all devices. Try to modify an IP address in the testbed to make a device `connect()` method fail for one device and see if you are able to handle the exception properly.

### Step 2 - Use Python logic to confirm we are successfully connected to all devices

Use the Python logic you want to confirm (i.e. printing in the terminal) we are successfully connected to **all** devices in the testbed.

### Step 3 - Disconnect from all devices in the testbed

Don't forget to disconnect from all devices. Create a loop to disconnect from each device in the testbed. Verify we are actually disconnected by pritting the device name and the confirmation we are disconnected.

It's very similar to `step 1`. The documentation can be found here:

> https://pubhub.devnetcloud.com/media/pyats/docs/connections/manager.html#method-disconnect

Each `device` object has a `connected` attribute which returns `True` or `False`. Use it to know if you are successfuly connected to the device.

Each `device` object also has a `name` attribute which returns the device name (as per the name in the testbed).
