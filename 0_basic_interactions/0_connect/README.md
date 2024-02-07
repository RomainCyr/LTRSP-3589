# 0. Connect to each device

The first exercise focuses on connecting and disconnecting from each device in the testbed.
The script contains 3 mains steps, only the bold ones are to be completed, the rest already is provided.

0. **Load the testbed**.
1. **Connect to all devices in the testbed**.
2. Disconnect from all devices in the testbed.

## Output example

Output has been truncated for brevity.

```2023-10-26T11:55:25:
2024-01-18T20:56:41: %SCRIPT-INFO: Trying to connect to xrd-1.
2024-01-18T20:56:42: %SCRIPT-INFO: Connected to xrd-1.
2024-01-18T20:56:42: %SCRIPT-INFO: Trying to connect to xrd-2.
2024-01-18T20:56:43: %SCRIPT-INFO: Connected to xrd-2.
2024-01-18T20:56:43: %SCRIPT-INFO: Trying to connect to xrd-3.
2024-01-18T20:56:44: %SCRIPT-INFO: Connected to xrd-3.
[...]
2024-01-18T20:56:48: %SCRIPT-INFO: Trying to disconnect from xrd-1.
2024-01-18T20:56:48: %SCRIPT-INFO: Disconnected from xrd-1.
2024-01-18T20:56:49: %SCRIPT-INFO: Trying to disconnect from xrd-2.
2024-01-18T20:56:49: %SCRIPT-INFO: Disconnected from xrd-2.
2024-01-18T20:56:49: %SCRIPT-INFO: Trying to disconnect from xrd-3.
2024-01-18T20:56:49: %SCRIPT-INFO: Disconnected from xrd-3.
[...]
```

## Folders

The files with the exercise are in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

# PyATS Testbed

The pyATS testbed is a YAML file that describes and captures all the details about the network devices and topology such as device information, connection details, credentials, and more.
It serves as an inventory of the network, it can be used to save information about devices and is used by pyATS to connect to devices.

Below is a simple testbed file.

```yaml
testbed:
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

The testbed file for the lab `testbed.yaml` is already provided, you can have a look at it to see how it looks like.

You can read more about the testbed file in the documentation below.

> https://pubhub.devnetcloud.com/media/pyats/docs/topology/index.html

## Steps to complete the exercise

To get you started, the exercise script already contains some code, missing code needs to be completed after the `# Step N` comments.

This `disconnect` part is already provided, it can be used as an example for the connection part and for reference on handling disconnection

### Step 0 - Load the testbed

In this first step, we are going to load the testbed using the `load` function from the `genie.testbed` module.
The testbed file is located in the same folder as the python script.

Below is an example on how to use load the testbed.

```python
from genie.testbed import load
testbed = load('testbed.yaml')
```

### Step 1 - Connect to all devices in the testbed

Now we are going to connect to each device in the testbed (using a `for` loop). The testbed object contains a dictionary of devices. You can access the devices using the `devices` attribute of the testbed object. For example, the `xrd-1 `device can be accessed using `testbed.devices['xrd-1']`.

The testbed also provide an iterator to loop over the devices dictionary. You can use it as shown below:

```python
for device in testbed:
    logger.info(f'Trying to connect on: {device.name}')
```

To initiate the device connection use the `connect()` method. More information can be found here:

> https://pubhub.devnetcloud.com/media/pyats/docs/connections/manager.html#method-instantiate-connect

The below arguments avoid printing the full device log to `stdout` and sets the `connection_timeout` to 10 seconds (so you don't wait for a minute if you can't connect to a device).

```
device.connect(log_stdout=False, connection_timeout=10)
```

Each `device` object has a `connected` attribute (`device.connected`) which returns `True` or `False`. Each `device` object also has a `name` attribute (`device.name`) which returns the device name (as per the name in the testbed).

### Bonus - Exception Handling

Note that if the `device.connect()` method fails, you will get a `unicon.core.errors.ConnectionError` exception like below. If this happens, the script will stop and you may not have try to connect to the all the devices.

You can try to catch this error in case the `device.connect()` doesn't work and ensure that the script continues to run.

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

By default, you should be able to connect to all devices. Try to modify an IP address in the testbed to make a device `connect()` method fail for one device and see if you are able to handle the exception properly.
