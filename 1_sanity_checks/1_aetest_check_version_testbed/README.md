# 1. AETest - Check version (testbed)

In this second exercise, we will use AEtest to define and execute test cases. In our example, we will:

1. Connect to the devices,
2. Leverage pyATS Genie library to verify that the devices are running with the version defined in the testbed (IOS XR `7.9.2` and `7.8.2`),
3. Disconnect from the devices.

This second exercise is an improved version of the first one. The expected version is not defined statically in a variable but retrieve in the testbed from the device parameters. The testbed is our **source of truth**.
Moreover, instead of doing a loop in the testcase, the `aetest.loop` feature will be used.

## Output example

```plaintext
2023-11-06T14:17:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:19: %AETEST-INFO: |                            Starting common setup                             |
2023-11-06T14:17:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:19: %AETEST-INFO: |                Starting subsection connect[device_name=xrd-1]                |
2023-11-06T14:17:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:20: %SCRIPT-INFO: xrd-1 - connected
2023-11-06T14:17:20: %AETEST-INFO: The result of subsection connect[device_name=xrd-1] is => PASSED
2023-11-06T14:17:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:20: %AETEST-INFO: |                Starting subsection connect[device_name=xrd-2]                |
2023-11-06T14:17:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:21: %SCRIPT-INFO: xrd-2 - connected
2023-11-06T14:17:21: %AETEST-INFO: The result of subsection connect[device_name=xrd-2] is => PASSED
2023-11-06T14:17:21: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:21: %AETEST-INFO: |                Starting subsection connect[device_name=xrd-3]                |
2023-11-06T14:17:21: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:23: %SCRIPT-INFO: xrd-3 - connected
2023-11-06T14:17:23: %AETEST-INFO: The result of subsection connect[device_name=xrd-3] is => PASSED
2023-11-06T14:17:23: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:23: %AETEST-INFO: |                Starting subsection connect[device_name=xrd-4]                |
2023-11-06T14:17:23: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:24: %SCRIPT-INFO: xrd-4 - connected
2023-11-06T14:17:24: %AETEST-INFO: The result of subsection connect[device_name=xrd-4] is => PASSED
2023-11-06T14:17:24: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:24: %AETEST-INFO: |             Starting subsection connect[device_name=xrd-source]              |
2023-11-06T14:17:24: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:26: %SCRIPT-INFO: xrd-source - connected
2023-11-06T14:17:26: %AETEST-INFO: The result of subsection connect[device_name=xrd-source] is => PASSED
2023-11-06T14:17:26: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:26: %AETEST-INFO: |              Starting subsection connect[device_name=xrd-dest]               |
2023-11-06T14:17:26: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:28: %SCRIPT-INFO: xrd-dest - connected
2023-11-06T14:17:28: %AETEST-INFO: The result of subsection connect[device_name=xrd-dest] is => PASSED
2023-11-06T14:17:28: %AETEST-INFO: The result of common setup is => PASSED
2023-11-06T14:17:28: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:28: %AETEST-INFO: |                        Starting testcase CheckVersion                        |
2023-11-06T14:17:28: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:28: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:28: %AETEST-INFO: |              Starting section check_version[device_name=xrd-1]               |
2023-11-06T14:17:28: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:30: %AETEST-INFO: Passed reason: xrd-1 is running the correct version: 7.9.2
2023-11-06T14:17:30: %AETEST-INFO: The result of section check_version[device_name=xrd-1] is => PASSED
2023-11-06T14:17:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:30: %AETEST-INFO: |              Starting section check_version[device_name=xrd-2]               |
2023-11-06T14:17:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:31: %AETEST-INFO: Passed reason: xrd-2 is running the correct version: 7.9.2
2023-11-06T14:17:31: %AETEST-INFO: The result of section check_version[device_name=xrd-2] is => PASSED
2023-11-06T14:17:31: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:31: %AETEST-INFO: |              Starting section check_version[device_name=xrd-3]               |
2023-11-06T14:17:31: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:31: %AETEST-INFO: Passed reason: xrd-3 is running the correct version: 7.9.2
2023-11-06T14:17:31: %AETEST-INFO: The result of section check_version[device_name=xrd-3] is => PASSED
2023-11-06T14:17:31: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:31: %AETEST-INFO: |              Starting section check_version[device_name=xrd-4]               |
2023-11-06T14:17:31: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:32: %AETEST-INFO: Passed reason: xrd-4 is running the correct version: 7.9.2
2023-11-06T14:17:32: %AETEST-INFO: The result of section check_version[device_name=xrd-4] is => PASSED
2023-11-06T14:17:32: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:32: %AETEST-INFO: |            Starting section check_version[device_name=xrd-source]            |
2023-11-06T14:17:32: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:32: %AETEST-ERROR: Failed reason: xrd-source is not running 7.8.1, but 7.8.2
2023-11-06T14:17:32: %AETEST-INFO: The result of section check_version[device_name=xrd-source] is => FAILED
2023-11-06T14:17:32: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:32: %AETEST-INFO: |             Starting section check_version[device_name=xrd-dest]             |
2023-11-06T14:17:32: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:33: %AETEST-INFO: Passed reason: xrd-dest is running the correct version: 7.8.2
2023-11-06T14:17:33: %AETEST-INFO: The result of section check_version[device_name=xrd-dest] is => PASSED
2023-11-06T14:17:33: %AETEST-INFO: The result of testcase CheckVersion is => FAILED
2023-11-06T14:17:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:33: %AETEST-INFO: |                           Starting common cleanup                            |
2023-11-06T14:17:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:33: %AETEST-INFO: |              Starting subsection disconnect[device_name=xrd-1]               |
2023-11-06T14:17:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:33: %AETEST-INFO: The result of subsection disconnect[device_name=xrd-1] is => PASSED
2023-11-06T14:17:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:33: %AETEST-INFO: |              Starting subsection disconnect[device_name=xrd-2]               |
2023-11-06T14:17:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:33: %AETEST-INFO: The result of subsection disconnect[device_name=xrd-2] is => PASSED
2023-11-06T14:17:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:33: %AETEST-INFO: |              Starting subsection disconnect[device_name=xrd-3]               |
2023-11-06T14:17:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:33: %AETEST-INFO: The result of subsection disconnect[device_name=xrd-3] is => PASSED
2023-11-06T14:17:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:33: %AETEST-INFO: |              Starting subsection disconnect[device_name=xrd-4]               |
2023-11-06T14:17:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:33: %AETEST-INFO: The result of subsection disconnect[device_name=xrd-4] is => PASSED
2023-11-06T14:17:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:33: %AETEST-INFO: |            Starting subsection disconnect[device_name=xrd-source]            |
2023-11-06T14:17:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:34: %AETEST-INFO: The result of subsection disconnect[device_name=xrd-source] is => PASSED
2023-11-06T14:17:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:34: %AETEST-INFO: |             Starting subsection disconnect[device_name=xrd-dest]             |
2023-11-06T14:17:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:34: %AETEST-INFO: The result of subsection disconnect[device_name=xrd-dest] is => PASSED
2023-11-06T14:17:34: %AETEST-INFO: The result of common cleanup is => PASSED
2023-11-06T14:17:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:34: %AETEST-INFO: |                               Detailed Results                               |
2023-11-06T14:17:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:34: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
2023-11-06T14:17:34: %AETEST-INFO: --------------------------------------------------------------------------------
2023-11-06T14:17:34: %AETEST-INFO: .
2023-11-06T14:17:34: %AETEST-INFO: |-- common_setup                                                          PASSED
2023-11-06T14:17:34: %AETEST-INFO: |   |-- connect[device_name=xrd-1]                                        PASSED
2023-11-06T14:17:34: %AETEST-INFO: |   |-- connect[device_name=xrd-2]                                        PASSED
2023-11-06T14:17:34: %AETEST-INFO: |   |-- connect[device_name=xrd-3]                                        PASSED
2023-11-06T14:17:34: %AETEST-INFO: |   |-- connect[device_name=xrd-4]                                        PASSED
2023-11-06T14:17:34: %AETEST-INFO: |   |-- connect[device_name=xrd-source]                                   PASSED
2023-11-06T14:17:34: %AETEST-INFO: |   `-- connect[device_name=xrd-dest]                                     PASSED
2023-11-06T14:17:34: %AETEST-INFO: |-- CheckVersion                                                          FAILED
2023-11-06T14:17:34: %AETEST-INFO: |   |-- check_version[device_name=xrd-1]                                  PASSED
2023-11-06T14:17:34: %AETEST-INFO: |   |-- check_version[device_name=xrd-2]                                  PASSED
2023-11-06T14:17:34: %AETEST-INFO: |   |-- check_version[device_name=xrd-3]                                  PASSED
2023-11-06T14:17:34: %AETEST-INFO: |   |-- check_version[device_name=xrd-4]                                  PASSED
2023-11-06T14:17:34: %AETEST-INFO: |   |-- check_version[device_name=xrd-source]                             FAILED
2023-11-06T14:17:34: %AETEST-INFO: |   `-- check_version[device_name=xrd-dest]                               PASSED
2023-11-06T14:17:34: %AETEST-INFO: `-- common_cleanup                                                        PASSED
2023-11-06T14:17:34: %AETEST-INFO:     |-- disconnect[device_name=xrd-1]                                     PASSED
2023-11-06T14:17:34: %AETEST-INFO:     |-- disconnect[device_name=xrd-2]                                     PASSED
2023-11-06T14:17:34: %AETEST-INFO:     |-- disconnect[device_name=xrd-3]                                     PASSED
2023-11-06T14:17:34: %AETEST-INFO:     |-- disconnect[device_name=xrd-4]                                     PASSED
2023-11-06T14:17:34: %AETEST-INFO:     |-- disconnect[device_name=xrd-source]                                PASSED
2023-11-06T14:17:34: %AETEST-INFO:     `-- disconnect[device_name=xrd-dest]                                  PASSED
2023-11-06T14:17:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:34: %AETEST-INFO: |                                   Summary                                    |
2023-11-06T14:17:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T14:17:34: %AETEST-INFO:  Number of ABORTED                                                            0 
2023-11-06T14:17:34: %AETEST-INFO:  Number of BLOCKED                                                            0 
2023-11-06T14:17:34: %AETEST-INFO:  Number of ERRORED                                                            0 
2023-11-06T14:17:34: %AETEST-INFO:  Number of FAILED                                                             1 
2023-11-06T14:17:34: %AETEST-INFO:  Number of PASSED                                                             2 
2023-11-06T14:17:34: %AETEST-INFO:  Number of PASSX                                                              0 
2023-11-06T14:17:34: %AETEST-INFO:  Number of SKIPPED                                                            0 
2023-11-06T14:17:34: %AETEST-INFO:  Total Number                                                                 3 
2023-11-06T14:17:34: %AETEST-INFO:  Success Rate                                                             66.7% 
2023-11-06T14:17:34: %AETEST-INFO: --------------------------------------------------------------------------------
```

## Folders

The file with the exercise is in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## Testbed

The testbed contains the definition of the devices in the lab and how to connect to them. The testbed is also a good place to store any information related to the devices.
For example, the expected version of the device is stored in the testbed. This way, if the version changes, the script doesn't have to be updated and stays generic.
Any information can be stored in the `custom` section.

```yaml
xrd-1:
    role: "PE"
    os: iosxr
    type: router
    connections:
      cli:
        ip: 172.40.0.101
        protocol: ssh
        arguments:
          init_config_commands: []
        port: 22
        settings:
          GRACEFUL_DISCONNECT_WAIT_SEC: 0
          POST_DISCONNECT_WAIT_SEC: 0
      netconf:
        class: yang.connector.Netconf
        ip: 172.40.0.101
        port: 830
        settings:
          GRACEFUL_DISCONNECT_WAIT_SEC: 0
          POST_DISCONNECT_WAIT_SEC: 0
    custom:
      version: "7.9.2"
```

## AEtest loops

AEtest loops are a way to iterate a testcase or test section. It is a good way to avoid code duplication and provided better visibility to the test results in comparison with a for loop inside a test section. For example a test section can be looped for each device in the testbed.

When a for loop was use in an `aetest.test` to verify the version of the device, as soon as the test failed, any other remaining device were **not** tested. 
By using an `aetest.loop`, as the test will be run once for each device, if one test fails it will continue to run the test for any remaining device.

The python code below is an example of a loop in a test section.

```python
    @aetest.test
    @aetest.loop(device_name=["xrd-1", "xrd-2"])
    def loop_over_device(self,device_name):
        pass
```

Note that this is also possible for subsection in `CommonSetup` and `CommonCleanup`.

```python
    @aetest.subsection
    @aetest.loop(device_name=["xrd-1", "xrd-2"])
    def loop_over_device(self,device_name):
        pass
```

You can refer to the documentation below for more information.

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/loop.html

## Steps

To send information inline, in the output of your script, use the `logger.info()` method. For instance, in order to print the below output, you can use `logger.info('xrd-1 is connected')`

```
2023-10-21T11:05:40: %SCRIPT-INFO: xrd-1 is connected
```

### Step 0 - Connect to each device

The `CommonSetup` section is where we set up the common environment required and shared between the script’s testcases.

In this case we will use `aetest.loop()` instead of a python `for` loop, to run the `connect()` method for **ALL devices** in the testbed.
For simplicity, the devices list to loop over will be statically defined in the script with list of device name such as `["xrd-1","xrd-2","xrd-3"]`.
There are others ways to do this dynamically, and it will be covered in the next exercises.

#### Step 0.1 - Set the devices to loop over for connection

Use the `aetest.loop()` decorator to loop over the devices of the testbed. For simplicity, we will use a static list of device name such as `["xrd-1","xrd-2","xrd-3"]`.

#### Step 0.2 - Connect to the device

As the device name is provided as an argument of the function, to retrieve the device object you need then to use the `testbed.devices` dictionary as shown below:

```python
device = testbed.devices[device_name]
```

You can then use the `connect()` method of the device object to connect to the device.

### Step 1 - Verify the version of each device

A `Testcase` is defined in this step to verify the current IOS XR version of the device in the testbed.

Note that `xrd-source` expected version is set to 7.8.1, on purpose. This should return an error in your script.

#### Step 1.1 - Set the devices to loop over for version verification

One test section called `check_version` is used and looped for each device in the testbed.
As this test section is looped over for each device in the testbed, it comes down to testing the version for one device. The `device_name` variable is passed as an argument to the test section.

Use the `aetest.loop()` decorator to loop over **ALL devices** of the testbed. For simplicity, the devices list to loop over will be statically defined in the script with list of device name such as `["xrd-1","xrd-2","xrd-3"]`.
There are others ways to do this dynamically, and it will be covered in the next exercises.

#### Step 1.2 - Parse `show version` output for the device being tested

Parse the `show version` and save it to a variable.

#### Step 1.3 - Verify that the device is running the correct version

Use a condition to check if the device is running the correct version. The correct version is stored in the testbed, under the `custom` section. Any parameter stored in this section can be accessed via `device.custom.myparameter` (assuming the name is `myparameter`).

```yaml
xrd-1:
# Output omitted
  custom:
    color: "red"
```

In the above example, you can retrieve the value `red` by using `device.custom.color` (assuming `device` is linked to `xrd-1` in your testbed).

If the test is successful, use the AEtest `self.passed()` method to pass the test and provide the current running version.
If the test fails, use the `failed()` method to fail the test and provide detail on why it has failed.

Note that `xrd-source` expected version is set to 7.8.1, on purpose. This should return an error in your script.

### Step 2 - Disconnect from each connected device

#### Step 2.1 - Set the devices to loop over for disconnecting

Use the `aetest.loop()` decorator to loop over the devices of the testbed. For simplicity, we will use a static list of device name such as `["xrd-1","xrd-2","xrd-3"]`.

#### Step 2.2 - Disconnect from the device

Use the `disconnect()` method of the device object to disconnect to the device. Only do this, if the device is connected. You can use the attribute `connected` of the device object to check if the device is connected.

# AEtest documentation

The AEtest documentation can be found below.

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/index.html
