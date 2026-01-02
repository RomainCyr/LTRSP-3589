# 1. AETest - Check version (testbed)

This second exercise on AEtest is an improvement of the first one with the same goal. The devices versions are collected and checked against an expected version.
This time, the expected version is not defined statically in the code but retrieved in the `testbed` from the device custom data.

Moreover, instead of doing a `for` loop in the testcase we will use the `@aetest.loop` feature to run the `testcase` for each `device`.

The test script is still composed of 3 main sections with a few steps in each of them. Only the one in bold are to be completed, the rest of the code and the testscript structure is already provided.

0. `CommonSetup`: Connect to the devices in the testbed.
1. **`CheckVersion`: Verify the devices are running the correct version using Genie to parse the `show version` output.**
   1. **Parse `show version` output.**
   2. **Verify that the device is running the version defined in the testbed.**
   3. **Pass or Fail the test depending on the device version.**
2. `CommonCleanup`: Disconnect from the devices.

## Output example

Output has been truncated for brevity.

```plaintext
2024-01-20T15:36:36: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:36: %AETEST-INFO: |                            Starting common setup                             |
2024-01-20T15:36:36: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:36: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:36: %AETEST-INFO: |                    Starting subsection connect_to_devices                    |
2024-01-20T15:36:36: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:37: %SCRIPT-INFO: xrd-1 - connected
2024-01-20T15:36:38: %SCRIPT-INFO: xrd-2 - connected
2024-01-20T15:36:40: %SCRIPT-INFO: xrd-3 - connected
2024-01-20T15:36:41: %SCRIPT-INFO: xrd-4 - connected
2024-01-20T15:36:42: %SCRIPT-INFO: xrd-source - connected
2024-01-20T15:36:43: %SCRIPT-INFO: xrd-dest - connected
2024-01-20T15:36:43: %AETEST-INFO: The result of subsection connect_to_devices is => PASSED
2024-01-20T15:36:43: %AETEST-INFO: The result of common setup is => PASSED
2024-01-20T15:36:43: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:43: %AETEST-INFO: |                        Starting testcase CheckVersion                        |
2024-01-20T15:36:43: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:43: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:43: %AETEST-INFO: |              Starting section check_version[device_name=xrd-1]               |
2024-01-20T15:36:43: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:46: %AETEST-INFO: Passed reason: xrd-1 is running the correct version: 24.4.2
2024-01-20T15:36:46: %AETEST-INFO: The result of section check_version[device_name=xrd-1] is => PASSED
2024-01-20T15:36:46: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:46: %AETEST-INFO: |              Starting section check_version[device_name=xrd-2]               |
2024-01-20T15:36:46: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:46: %AETEST-INFO: Passed reason: xrd-2 is running the correct version: 24.4.2
2024-01-20T15:36:46: %AETEST-INFO: The result of section check_version[device_name=xrd-2] is => PASSED
[...]
2024-01-20T15:36:48: %AETEST-INFO: |                           Starting common cleanup                            |
2024-01-20T15:36:48: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:48: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:48: %AETEST-INFO: |                 Starting subsection disconnect_from_devices                  |
2024-01-20T15:36:48: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:49: %AETEST-INFO: The result of subsection disconnect_from_devices is => PASSED
2024-01-20T15:36:49: %AETEST-INFO: The result of common cleanup is => PASSED
2024-01-20T15:36:49: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:49: %AETEST-INFO: |                               Detailed Results                               |
2024-01-20T15:36:49: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:49: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
2024-01-20T15:36:49: %AETEST-INFO: --------------------------------------------------------------------------------
2024-01-20T15:36:49: %AETEST-INFO: .
2024-01-20T15:36:49: %AETEST-INFO: |-- common_setup                                                          PASSED
2024-01-20T15:36:49: %AETEST-INFO: |   `-- connect_to_devices                                                PASSED
2024-01-20T15:36:49: %AETEST-INFO: |-- CheckVersion                                                          FAILED
2024-01-20T15:36:49: %AETEST-INFO: |   |-- check_version[device_name=xrd-1]                                  PASSED
2024-01-20T15:36:49: %AETEST-INFO: |   |-- check_version[device_name=xrd-2]                                  PASSED
2024-01-20T15:36:49: %AETEST-INFO: |   |-- check_version[device_name=xrd-3]                                  PASSED
2024-01-20T15:36:49: %AETEST-INFO: |   |-- check_version[device_name=xrd-4]                                  PASSED
2024-01-20T15:36:49: %AETEST-INFO: |   |-- check_version[device_name=xrd-source]                             FAILED
2024-01-20T15:36:49: %AETEST-INFO: |   `-- check_version[device_name=xrd-dest]                               PASSED
2024-01-20T15:36:49: %AETEST-INFO: `-- common_cleanup                                                        PASSED
2024-01-20T15:36:49: %AETEST-INFO:     `-- disconnect_from_devices                                           PASSED
2024-01-20T15:36:49: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:49: %AETEST-INFO: |                                   Summary                                    |
2024-01-20T15:36:49: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-20T15:36:49: %AETEST-INFO:  Number of ABORTED                                                            0 
2024-01-20T15:36:49: %AETEST-INFO:  Number of BLOCKED                                                            0 
2024-01-20T15:36:49: %AETEST-INFO:  Number of ERRORED                                                            0 
2024-01-20T15:36:49: %AETEST-INFO:  Number of FAILED                                                             1 
2024-01-20T15:36:49: %AETEST-INFO:  Number of PASSED                                                             2 
2024-01-20T15:36:49: %AETEST-INFO:  Number of PASSX                                                              0 
2024-01-20T15:36:49: %AETEST-INFO:  Number of SKIPPED                                                            0 
2024-01-20T15:36:49: %AETEST-INFO:  Total Number                                                                 3 
2024-01-20T15:36:49: %AETEST-INFO:  Success Rate                                                             66.7% 
2024-01-20T15:36:49: %AETEST-INFO: --------------------------------------------------------------------------------
```

## Folders

The files with the exercise are in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## Testbed

The `testbed` contains the definition of the devices in the lab and how to connect to them. The testbed is also a good place to store any information related to the devices.
For example, the expected version of the device can be stored in the testbed. This way, if the version changes, the script doesn't have to be updated and stays generic.
Any information can be stored in the `custom` section, such as the `version`.

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
    custom:
      version: "24.4.2"
```

## AEtest loops

AEtest loops are a way to iterate a testcase or test section. It is a good way to avoid code duplication. It provides better visibility to the test results in comparison with a `for` loop inside a test section. For example, a test section
can be looped for each `device` in the `testbed`.

When a `for` loop is used in an `@aetest.test` to verify the version of the device, if the test section is failed when a device is running the wrong version, any other remaining device would **not** be tested.

By using an `@aetest.loop`, as the test section can be run once for each device, if one test fails, the others continue to run for the remaining devices.

The python code below is an example of a loop in a test section.

```python
    @aetest.test
    @aetest.loop(device_name=["xrd-1", "xrd-2"])
    def loop_over_device(self,device_name):
        pass
```

**Note that the variable used in the loop is passed as an argument of the test section and their name must match. In this example it is `device_name`.**

Looping a section is also possible for subsection in `CommonSetup` and `CommonCleanup`.

```python
    @aetest.subsection
    @aetest.loop(device_name=["xrd-1", "xrd-2"])
    def loop_over_device(self,device_name):
        pass
```

You can refer to the documentation below for more information.

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/loop.html

## Steps to complete the exercise

The exercise script already contains some code including some reused from the previous exercise. Missing code needs to be completed after the `# Step N` comments.

### Step 0 - Set the devices to loop over for the test section

The test section called `check_version` should be looped for each `device` in the `testbed`.
As this test section is looped over for each `device`, the logic inside comes down to testing the version for one device.
The `device_name` variable should be passed as an argument to the test section.

Use the `aetest.loop()` decorator to loop over **ALL devices** of the testbed. For simplicity, the devices list to loop
over should be statically defined in the script with list of device name such as `["xrd-1","xrd-2","xrd-3"]`.
There are others ways to do this dynamically, and it will be covered in the next exercises.

### Step 1 - Verify if the device is running its expected version

Use a `if` statement to verify that the device is running its expected version.
The device version is in the `software_version` key of the parsed output dictionary.

The expected version is stored in the testbed, under the `custom` section.
Any parameter stored in this section can be accessed via `device.custom.myparameter` (assuming the name is `myparameter`).

In the below example, you can retrieve the value `red` by using `device.custom.color` (assuming `device` object correspond to the `xrd-1` device in the testbed).

```yaml
xrd-1:
# Output omitted
  custom:
    color: "red"
```


### Step 2 - Fail the testcase if the device is running the wrong version

If the device is not running its expected version, use the `self.failed()` method to fail the test and provide detail on why it has failed.

Note that `xrd-source` expected version is set to `24.4.1`, on purpose. The testcase should fail for `xrd-source` in your script.

### Step 3 - Pass the testcase if the device is running the correct version

If the device is running its expected version, use the AEtest `self.passed()` method to pass the test and provide the current running version.
