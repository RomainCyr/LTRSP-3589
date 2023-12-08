# 2. AEtest: Automated Easy Testing

In this third exercise, we will use AEtest to define and execute test cases. In our example, we will:

1. Connect to the devices
2. Leverage pyATS Genie library to verify that they are running with the version defined in the testbed
3. Verify that the IGP configuration is correct for the P and PE routers
4. Disconnect from the devices

This third exercise is a follow-up  of the second one with additional testcase and improvement.

IGP configuration will be compared against an expected one using the `Genie Diff` utility.

## Output example

```plaintext
2023-11-06T18:05:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:14: %AETEST-INFO: |                            Starting common setup                             |
2023-11-06T18:05:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:14: %AETEST-INFO: |                          Starting subsection setup                           |
2023-11-06T18:05:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:14: %AETEST-INFO: The result of subsection setup is => PASSED
2023-11-06T18:05:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:14: %AETEST-INFO: |        Starting subsection connect[device=Device_xrd-1,_type_router]         |
2023-11-06T18:05:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:16: %SCRIPT-INFO: xrd-1 - connected
2023-11-06T18:05:16: %AETEST-INFO: The result of subsection connect[device=Device_xrd-1,_type_router] is => PASSED
2023-11-06T18:05:16: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:16: %AETEST-INFO: |        Starting subsection connect[device=Device_xrd-2,_type_router]         |
2023-11-06T18:05:16: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:18: %SCRIPT-INFO: xrd-2 - connected
2023-11-06T18:05:18: %AETEST-INFO: The result of subsection connect[device=Device_xrd-2,_type_router] is => PASSED
2023-11-06T18:05:18: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:18: %AETEST-INFO: |        Starting subsection connect[device=Device_xrd-3,_type_router]         |
2023-11-06T18:05:18: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:20: %SCRIPT-INFO: xrd-3 - connected
2023-11-06T18:05:20: %AETEST-INFO: The result of subsection connect[device=Device_xrd-3,_type_router] is => PASSED
2023-11-06T18:05:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:20: %AETEST-INFO: |        Starting subsection connect[device=Device_xrd-4,_type_router]         |
2023-11-06T18:05:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:22: %SCRIPT-INFO: xrd-4 - connected
2023-11-06T18:05:22: %AETEST-INFO: The result of subsection connect[device=Device_xrd-4,_type_router] is => PASSED
2023-11-06T18:05:22: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:22: %AETEST-INFO: |      Starting subsection connect[device=Device_xrd-source,_type_router]      |
2023-11-06T18:05:22: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:24: %SCRIPT-INFO: xrd-source - connected
2023-11-06T18:05:24: %AETEST-INFO: The result of subsection connect[device=Device_xrd-source,_type_router] is => PASSED
2023-11-06T18:05:24: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:24: %AETEST-INFO: |       Starting subsection connect[device=Device_xrd-dest,_type_router]       |
2023-11-06T18:05:24: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:26: %SCRIPT-INFO: xrd-dest - connected
2023-11-06T18:05:26: %AETEST-INFO: The result of subsection connect[device=Device_xrd-dest,_type_router] is => PASSED
2023-11-06T18:05:26: %AETEST-INFO: The result of common setup is => PASSED
2023-11-06T18:05:26: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:26: %AETEST-INFO: |                        Starting testcase CheckVersion                        |
2023-11-06T18:05:26: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:26: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:26: %AETEST-INFO: |                            Starting section setup                            |
2023-11-06T18:05:26: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:26: %AETEST-INFO: The result of section setup is => PASSED
2023-11-06T18:05:26: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:26: %AETEST-INFO: |       Starting section check_version[device=Device_xrd-1,_type_router]       |
2023-11-06T18:05:26: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:28: %AETEST-INFO: Passed reason: xrd-1 is running the correct version: 7.9.2
2023-11-06T18:05:28: %AETEST-INFO: The result of section check_version[device=Device_xrd-1,_type_router] is => PASSED
2023-11-06T18:05:28: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:28: %AETEST-INFO: |       Starting section check_version[device=Device_xrd-2,_type_router]       |
2023-11-06T18:05:28: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:29: %AETEST-INFO: Passed reason: xrd-2 is running the correct version: 7.9.2
2023-11-06T18:05:29: %AETEST-INFO: The result of section check_version[device=Device_xrd-2,_type_router] is => PASSED
2023-11-06T18:05:29: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:29: %AETEST-INFO: |       Starting section check_version[device=Device_xrd-3,_type_router]       |
2023-11-06T18:05:29: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:29: %AETEST-INFO: Passed reason: xrd-3 is running the correct version: 7.9.2
2023-11-06T18:05:29: %AETEST-INFO: The result of section check_version[device=Device_xrd-3,_type_router] is => PASSED
2023-11-06T18:05:29: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:29: %AETEST-INFO: |       Starting section check_version[device=Device_xrd-4,_type_router]       |
2023-11-06T18:05:29: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:29: %AETEST-INFO: Passed reason: xrd-4 is running the correct version: 7.9.2
2023-11-06T18:05:29: %AETEST-INFO: The result of section check_version[device=Device_xrd-4,_type_router] is => PASSED
2023-11-06T18:05:29: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:29: %AETEST-INFO: |    Starting section check_version[device=Device_xrd-source,_type_router]     |
2023-11-06T18:05:29: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:30: %AETEST-ERROR: Failed reason: xrd-source is not running 7.8.1, but 7.8.2
2023-11-06T18:05:30: %AETEST-INFO: The result of section check_version[device=Device_xrd-source,_type_router] is => FAILED
2023-11-06T18:05:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:30: %AETEST-INFO: |     Starting section check_version[device=Device_xrd-dest,_type_router]      |
2023-11-06T18:05:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:30: %AETEST-INFO: Passed reason: xrd-dest is running the correct version: 7.8.2
2023-11-06T18:05:30: %AETEST-INFO: The result of section check_version[device=Device_xrd-dest,_type_router] is => PASSED
2023-11-06T18:05:30: %AETEST-INFO: The result of testcase CheckVersion is => FAILED
2023-11-06T18:05:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:30: %AETEST-INFO: |                          Starting testcase CheckIGP                          |
2023-11-06T18:05:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:30: %AETEST-INFO: |                            Starting section setup                            |
2023-11-06T18:05:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:30: %AETEST-INFO: The result of section setup is => PASSED
2023-11-06T18:05:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:30: %AETEST-INFO: |     Starting section check_isis_config[device=Device_xrd-1,_type_router]     |
2023-11-06T18:05:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:31: %SCRIPT-WARNING: Found difference in ISIS config:
2023-11-06T18:05:31: %SCRIPT-WARNING:  router isis core
2023-11-06T18:05:31: %SCRIPT-WARNING: - net 49.0000.0100.1001.0001.00
2023-11-06T18:05:31: %SCRIPT-WARNING: + net 49.0000.0100.1001.0010.00
2023-11-06T18:05:31: %AETEST-ERROR: Failed reason: Unexpected ISIS configuration found on device.
2023-11-06T18:05:31: %AETEST-INFO: The result of section check_isis_config[device=Device_xrd-1,_type_router] is => FAILED
2023-11-06T18:05:31: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:31: %AETEST-INFO: |     Starting section check_isis_config[device=Device_xrd-2,_type_router]     |
2023-11-06T18:05:31: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:32: %AETEST-INFO: The result of section check_isis_config[device=Device_xrd-2,_type_router] is => PASSED
2023-11-06T18:05:32: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:32: %AETEST-INFO: |     Starting section check_isis_config[device=Device_xrd-3,_type_router]     |
2023-11-06T18:05:32: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:33: %AETEST-INFO: The result of section check_isis_config[device=Device_xrd-3,_type_router] is => PASSED
2023-11-06T18:05:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:33: %AETEST-INFO: |     Starting section check_isis_config[device=Device_xrd-4,_type_router]     |
2023-11-06T18:05:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:33: %AETEST-INFO: The result of section check_isis_config[device=Device_xrd-4,_type_router] is => PASSED
2023-11-06T18:05:33: %AETEST-INFO: The result of testcase CheckIGP is => FAILED
2023-11-06T18:05:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:33: %AETEST-INFO: |                           Starting common cleanup                            |
2023-11-06T18:05:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:33: %AETEST-INFO: |                          Starting subsection setup                           |
2023-11-06T18:05:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:33: %AETEST-INFO: The result of subsection setup is => PASSED
2023-11-06T18:05:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:33: %AETEST-INFO: |       Starting subsection disconnect[device=Device_xrd-1,_type_router]       |
2023-11-06T18:05:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:34: %AETEST-INFO: The result of subsection disconnect[device=Device_xrd-1,_type_router] is => PASSED
2023-11-06T18:05:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:34: %AETEST-INFO: |       Starting subsection disconnect[device=Device_xrd-2,_type_router]       |
2023-11-06T18:05:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:34: %AETEST-INFO: The result of subsection disconnect[device=Device_xrd-2,_type_router] is => PASSED
2023-11-06T18:05:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:34: %AETEST-INFO: |       Starting subsection disconnect[device=Device_xrd-3,_type_router]       |
2023-11-06T18:05:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:34: %AETEST-INFO: The result of subsection disconnect[device=Device_xrd-3,_type_router] is => PASSED
2023-11-06T18:05:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:34: %AETEST-INFO: |       Starting subsection disconnect[device=Device_xrd-4,_type_router]       |
2023-11-06T18:05:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:34: %AETEST-INFO: The result of subsection disconnect[device=Device_xrd-4,_type_router] is => PASSED
2023-11-06T18:05:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:34: %AETEST-INFO: |    Starting subsection disconnect[device=Device_xrd-source,_type_router]     |
2023-11-06T18:05:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:34: %AETEST-INFO: The result of subsection disconnect[device=Device_xrd-source,_type_router] is => PASSED
2023-11-06T18:05:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:34: %AETEST-INFO: |     Starting subsection disconnect[device=Device_xrd-dest,_type_router]      |
2023-11-06T18:05:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:35: %AETEST-INFO: The result of subsection disconnect[device=Device_xrd-dest,_type_router] is => PASSED
2023-11-06T18:05:35: %AETEST-INFO: The result of common cleanup is => PASSED
2023-11-06T18:05:35: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:35: %AETEST-INFO: |                               Detailed Results                               |
2023-11-06T18:05:35: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:35: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
2023-11-06T18:05:35: %AETEST-INFO: --------------------------------------------------------------------------------
2023-11-06T18:05:35: %AETEST-INFO: .
2023-11-06T18:05:35: %AETEST-INFO: |-- common_setup                                                          PASSED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- setup                                                             PASSED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- connect[device=Device_xrd-1,_type_router]                         PASSED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- connect[device=Device_xrd-2,_type_router]                         PASSED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- connect[device=Device_xrd-3,_type_router]                         PASSED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- connect[device=Device_xrd-4,_type_router]                         PASSED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- connect[device=Device_xrd-source,_type_router]                    PASSED
2023-11-06T18:05:35: %AETEST-INFO: |   `-- connect[device=Device_xrd-dest,_type_router]                      PASSED
2023-11-06T18:05:35: %AETEST-INFO: |-- CheckVersion                                                          FAILED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- setup                                                             PASSED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- check_version[device=Device_xrd-1,_type_router]                   PASSED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- check_version[device=Device_xrd-2,_type_router]                   PASSED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- check_version[device=Device_xrd-3,_type_router]                   PASSED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- check_version[device=Device_xrd-4,_type_router]                   PASSED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- check_version[device=Device_xrd-source,_type_router]              FAILED
2023-11-06T18:05:35: %AETEST-INFO: |   `-- check_version[device=Device_xrd-dest,_type_router]                PASSED
2023-11-06T18:05:35: %AETEST-INFO: |-- CheckIGP                                                              FAILED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- setup                                                             PASSED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- check_isis_config[device=Device_xrd-1,_type_router]               FAILED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- check_isis_config[device=Device_xrd-2,_type_router]               PASSED
2023-11-06T18:05:35: %AETEST-INFO: |   |-- check_isis_config[device=Device_xrd-3,_type_router]               PASSED
2023-11-06T18:05:35: %AETEST-INFO: |   `-- check_isis_config[device=Device_xrd-4,_type_router]               PASSED
2023-11-06T18:05:35: %AETEST-INFO: `-- common_cleanup                                                        PASSED
2023-11-06T18:05:35: %AETEST-INFO:     |-- setup                                                             PASSED
2023-11-06T18:05:35: %AETEST-INFO:     |-- disconnect[device=Device_xrd-1,_type_router]                      PASSED
2023-11-06T18:05:35: %AETEST-INFO:     |-- disconnect[device=Device_xrd-2,_type_router]                      PASSED
2023-11-06T18:05:35: %AETEST-INFO:     |-- disconnect[device=Device_xrd-3,_type_router]                      PASSED
2023-11-06T18:05:35: %AETEST-INFO:     |-- disconnect[device=Device_xrd-4,_type_router]                      PASSED
2023-11-06T18:05:35: %AETEST-INFO:     |-- disconnect[device=Device_xrd-source,_type_router]                 PASSED
2023-11-06T18:05:35: %AETEST-INFO:     `-- disconnect[device=Device_xrd-dest,_type_router]                   PASSED
2023-11-06T18:05:35: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:35: %AETEST-INFO: |                                   Summary                                    |
2023-11-06T18:05:35: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-06T18:05:35: %AETEST-INFO:  Number of ABORTED                                                            0 
2023-11-06T18:05:35: %AETEST-INFO:  Number of BLOCKED                                                            0 
2023-11-06T18:05:35: %AETEST-INFO:  Number of ERRORED                                                            0 
2023-11-06T18:05:35: %AETEST-INFO:  Number of FAILED                                                             2 
2023-11-06T18:05:35: %AETEST-INFO:  Number of PASSED                                                             2 
2023-11-06T18:05:35: %AETEST-INFO:  Number of PASSX                                                              0 
2023-11-06T18:05:35: %AETEST-INFO:  Number of SKIPPED                                                            0 
2023-11-06T18:05:35: %AETEST-INFO:  Total Number                                                                 4 
2023-11-06T18:05:35: %AETEST-INFO:  Success Rate                                                             50.0% 
2023-11-06T18:05:35: %AETEST-INFO: --------------------------------------------------------------------------------
```

## Folders

The file with the exercise is in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## Testbed

The testbed contains the definition of the devices in the lab and how to connect to them. The lab topology can also be described in the testbed file.
The physical and/or logical connections between the different devices are then documented and can be used as reference data for testing.

Below is an example of a topology section in a testbed file.

```yaml
topology:
  xrd-source:
    interfaces:
      Loopback0:
        type: loopback
        ipv4: 192.168.10.1/24
      GigabitEthernet0/0/0/0:
        link: xrd-1_to_xrd-source_1
        ipv4: 10.0.1.1/31
        type: ethernet
```

## AEtest loop dynamic marking

In the previous exercise, we did a loop using `@aetest.loop()` decorator directly within the test scripts. It works well but it is very static.
In addition, it is also possible to dynamically mark sections for looping during runtime based on information that is only available when the script is running.
To do this, use the `loop.mark()` function as the example below. Note that the first parameter it takes is the function where we will run the loop (`loop_over_device` in the below example).

```python
    @aetest.setup
    def setup(self,testbed):
        aetest.loop.mark(self.loop_over_device,device=[device for device in testbed])

    @aetest.test
    def loop_over_device(self,device):
        pass
```

Note that this is also possible for a subsection in `CommonSetup` and `CommonCleanup`.

```python
    @aetest.subsection
    def setup(self,testbed):
        aetest.loop.mark(self.loop_over_device,device=[device for device in testbed])

    @aetest.subsection
    def loop_over_device(self,device):
        pass
```

You can refer to the documentation below for more information.

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/loop.html#dynamic-loop-marking

## Steps

To send information inline, in the output of your script, use the `logger.info()` method. For instance, in order to print the below output, you can use `logger.info('xrd-1 is connected')`

```
2023-10-21T11:05:40: %SCRIPT-INFO: xrd-1 is connected
```

### Step 0 - Connect to each device

The `CommonSetup` section is where we set up the common environment required and shared between the script’s testcases.

In this case we will use `aetest.loop` instead of a python `for` loop, to run the `connect()` method for all devices in the testbed.

This step is very similar to the previous exercise. The only difference is that the devices to loop over are not defined statically in the script but generated from the devices in the testbed.

#### Step 0.1 - Set the devices to loop over for connection

The first subsection in the `CommonSetup` called `setup` is used to mark dynamically the second subsection to loop over devices in the tested.

The list of devices in the testbed can be retrieved with a for loop as shown below:

```python
devices =  [device for device in testbed]
```

Using the `aetest.loop.mark()` function, set the second subsection to loop over the devices in the testbed.

#### Step 0.2 - Connect to the device

You can then use the `connect()` method of the device object to connect to the device.

### Step 1 - Verify the version of each device

A `Testcase` is defined in this step to verify the current IOS XR version of the devices in the testbed.  One test section called `check_version` is used and looped for each device.
As this test section is looped over for each device, it comes down to testing the version for one device.

This step is very similar to the previous exercise. The only difference is that the devices to loop over are not defined statically in the script but generated from the devices in the testbed.

Note that `xrd-source` expected version is set to 7.8.1, on purpose. This should return an error in your script.

#### Step 1.0 - Set the devices to loop over for version verification

The devices list to loop over is not defined statically in the script but generated from the devices in the testbed. For this exercise, create the loop dynamically using the `aetest.loop.mark()` function.

This is done in a specific section of the Testcase called `setup`. The setup is identified using the decorator `@aetest.setup`. Note that the function itself does not need to be called `setup`.
The test section `setup` is a specific section that is always executed before all other test sections. It can be used to perform all the common configuration, prerequisites and initializations specific to that testcase.

#### Step 1.1 - Parse `show version` output for the device being tested

Parse the `show version` and save it to a variable.

#### Step 1.2 - Verify that the device is running the correct version

Use a condition to check if the device is running the correct version. The correct version is stored in the testbed. It can be accessed with the following code `device.custom.version`.

If the test is successful, use the AEtest `self.passed()` method to pass the test and provide the current running version.
If the test fails, use the `failed()` method to fail the test and provide detail on why it has failed.

### Step 2 - Verify the IGP configuration

This `Testcase` will verify that the ISIS configuration is correct and as expected. For simplicity, only the global ISIS configuration will be compared, the interface sections will be ignored.

The Genie Diff utility will be used to compare the ISIS configuration of the device with the expected one per device role.

Note that `xrd-1` expected configuration is different that the lab, on purpose. This should return an error in your script.

#### ISIS configuration

Below is a reference output of the `show run router isis` command. The `net 49.0000.0100.1001.0001.00` line is the ISIS NET (Network Entity Title) address.
It follows the addressing scheme used by the CLNS protocol which is used by ISIS. It must be unique per router and it is often derived from a Loopback address.

The NET address is composed of the three parts:

- The first 3 bytes (6 digits) is the Area ID. The first byte is the Address Family Identifier (AFI) and the next two bytes are the Area ID. The AFI is always 49 for private networks.
- The next 6 bytes (12 digits) represent the system ID. This is unique to each router within the IS-IS domain. It is quivalent to the host or address portion on an IP address.
- The last bytes (2 digits), "00", represent the NSEL (Network Service Access Point Selector) which is normally set to 00 for network layer routing, to indicate 'this system'

When the system ID is derived from an IP address, the IP address is padded with 0 and rearrange in block of 4 digits.
For example, 192.168.1.1 become 1921.6800.1001.

```plaintext
router isis core
 is-type level-2-only
 net 49.0000.0100.1001.0001.00
 distribute link-state
 address-family ipv4 unicast
  metric-style wide
  advertise passive-only
  mpls traffic-eng router-id Loopback0
  router-id Loopback0
  segment-routing mpls sr-prefer
 !
 interface Bundle-Ether14
  point-to-point
  address-family ipv4 unicast
   metric 5000
  !
 !
 interface Loopback0
  passive
  address-family ipv4 unicast
   prefix-sid index 1
  !
 !
 interface GigabitEthernet0/0/0/2
  point-to-point
  address-family ipv4 unicast
   metric 50000
```

#### Step 2.0 - Set the devices to loop over for IGP verification

The ISIS configuration must be checked only for the **P** and **PE** routers in the topology. The role of the device are defined in the testbed and can be access with `device.role`.

Again, the next test section called `check_isis_config` must be loop over and mark dynamically using `aetest.loop.mark`. As this test section is looped over for each device in the testbed, this test section will come down to verifying the configuration for one device

#### Step 2.1 - Collect the isis configuration from the device

Collect the output of the `show run router isis` with the method `device.execute()` and save it to a variable.
By default on IOS XR, the first line of a `show running` output contains the timestamps, which shouldn't be compared. It can be removed with the following code that use python list comprehension on a string:  `config = config[config.index('\n'):]`

This output need to be converted to a Genie Config object to be later compared with the expected isis configuration.

Below is an example of using a Genie Config object:

```python
import json
from genie.utils.config import Config

config_str = """router isis core
 is-type level-2-only
 net 49.0000.0100.1001.0001.00
 distribute link-state
 address-family ipv4 unicast
  metric-style wide
  advertise passive-only
  mpls traffic-eng router-id Loopback0
  router-id Loopback0
  segment-routing mpls sr-prefer
"""

config = Config(config_str)

#parse the config
config.tree()

print(json.dumps(config.config,indent=2))
```

And the parsed output of the config

```json
{
  "router isis core": {
    "is-type level-2-only": {},
    "net 49.0000.0100.1001.0001.00": {},
    "distribute link-state": {},
    "address-family ipv4 unicast": {
      "metric-style wide": {},
      "advertise passive-only": {},
      "mpls traffic-eng router-id Loopback0": {},
      "router-id Loopback0": {},
      "segment-routing mpls sr-prefer": {}
    }
  }
}
```

#### Step 2.2 - Generate the expected ISIS configuration

The expected configuration varies depending on the router role. There are two files provided that contain the expected configuration for the P and PE routers:

- igp_expected_config_p.txt
- igp_expected_config_pe.txt

Some ISIS configuration varies between the routers, the ISIS NET address is one of them. In those file the `{net}` variable must be replaced using the `.format()` function.
We can derive it from the `Loopback0` IP address and the function `isis_net_from_ip()` is provided to do this. The area used in the lab is the area 0.

The IP address of the Loopback0 is available in the topology section of the testbed. It can be accessed with the following code: `device.interfaces.Loopback0.ipv4.ip`.

Below is the example on how to generate the net address from the Loopback0 IP address:

```python
net = isis_net_from_ip("0",device.interfaces.Loopback0.ipv4.ip.compressed)
```

Once the expected configuration has been generated, it must be converted to Genie Config object.

For more information, refer to the documentation below.

> https://pubhub.devnetcloud.com/media/pyats/docs/topology/usage.html#device-interface-aliases
>
> https://pubhub.devnetcloud.com/media/pyats/docs/topology/concept.html#interface-objects

#### Step 2.3 - Compare the expected and the actual configuration using the Genie Diff utility

Using the Genie Diff utility compare the two Genie Config objects created.
In order to compare only the global config, the interface sections must be ignored. To do so, use the `exclude` parameter of the `Diff` class constructor.

Below is an example on how to use the Genie Diff utility with the `exclude` parameter. The `exclude` parameter is a list of string to ignore, it can be a regex if it is put in parentheses.

```python
from genie.utils.diff import Diff
from genie.utils.config import Config

config_a = Config("""router bgp 65000
 bgp router-id 10.10.10.1
 address-family vpnv4 unicast
    network 192.168.1.1/32
""")
config_a.tree()

config_b = Config("""router bgp 65000
 bgp router-id 10.10.10.2
""")
config_b.tree()

dd = Diff(config_a, config_b,exclude=['(^address-family.*)'])
dd.findDiff()
```

For more information, refer to the documentation below.

> https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#diff

#### Step 2.5 - Verify if any configuration differences are found

Now that the config diff has been generated, check if there are any differences. To do so you can check the length of the `.diffs` attribute of a Diff object.
The `.diffs` attribute is a list of differences found between the two Genie Config objects. You can also log it to see the differences.
If any difference is found, the test failed, use the `failed()` method to fail the test.

### Step 3 - Disconnect from each connected device

#### Step 3.0 - Set the devices to loop over for disconnecting

This step is very similar to the `CommonSetup`, use the `aetest.loop.mark()` function to mark the subsection to loop over the devices in the testbed.

Set the devices to loop over for the next subsection `disconnect`.

#### Step 3.1 - Disconnect from the device

Use the `disconnect()` method of the device object to disconnect to the device. Only do this, if the device is connected. You can use the attribute `connected` of the device object to check if the device is connected.

# AEtest documentation

The AEtest documentation can be found below.

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/index.html
