# 0. AETest - Check version (static)

In this first exercise, we will use AEtest to define and execute one test case. In our example, we will:

1. Connect to the devices,
2. Leverage pyATS Genie library to verify that their current version is IOS XR 7.9.2,
3. Disconnect from the devices.

The goal of this exercise and the following one is to gradually learn how AEtest is structured and what functionnalities it provides. Though, one may want to have a look at some therorical concepts that are covered in the [Aetest](#aetest) paragraph.

## Output example

```plaintext
2023-10-30T13:58:54: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:58:54: %AETEST-INFO: |                            Starting common setup                             |
2023-10-30T13:58:54: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:58:54: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:58:54: %AETEST-INFO: |                    Starting subsection connect_to_devices                    |
2023-10-30T13:58:54: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:58:59: %SCRIPT-INFO: xrd-1 - connected.
2023-10-30T13:59:02: %SCRIPT-INFO: xrd-2 - connected.
2023-10-30T13:59:05: %SCRIPT-INFO: xrd-3 - connected.
2023-10-30T13:59:09: %SCRIPT-INFO: xrd-4 - connected.
2023-10-30T13:59:12: %SCRIPT-INFO: xrd-source - connected.
2023-10-30T13:59:14: %SCRIPT-INFO: xrd-dest - connected.
2023-10-30T13:59:14: %AETEST-INFO: The result of subsection connect_to_devices is => PASSED
2023-10-30T13:59:14: %AETEST-INFO: The result of common setup is => PASSED
2023-10-30T13:59:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:59:14: %AETEST-INFO: |                        Starting testcase CheckVersion                        |
2023-10-30T13:59:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:59:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:59:14: %AETEST-INFO: |                    Starting section check_current_version                    |
2023-10-30T13:59:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:59:15: %SCRIPT-INFO: --- xrd-1 ---
2023-10-30T13:59:15: %SCRIPT-INFO: software_version = 7.9.2
2023-10-30T13:59:16: %SCRIPT-INFO: --- xrd-2 ---
2023-10-30T13:59:16: %SCRIPT-INFO: software_version = 7.9.2
2023-10-30T13:59:17: %SCRIPT-INFO: --- xrd-3 ---
2023-10-30T13:59:17: %SCRIPT-INFO: software_version = 7.9.2
2023-10-30T13:59:18: %SCRIPT-INFO: --- xrd-4 ---
2023-10-30T13:59:18: %SCRIPT-INFO: software_version = 7.9.2
2023-10-30T13:59:19: %SCRIPT-INFO: --- xrd-source ---
2023-10-30T13:59:19: %SCRIPT-INFO: software_version = 7.8.2
2023-10-30T13:59:19: %SCRIPT-WARNING: xrd-source is not running XR 7.9.2.
2023-10-30T13:59:20: %SCRIPT-INFO: --- xrd-dest ---
2023-10-30T13:59:20: %SCRIPT-INFO: software_version = 7.8.2
2023-10-30T13:59:20: %SCRIPT-WARNING: xrd-dest is not running XR 7.9.2.
2023-10-30T13:59:20: %AETEST-ERROR: Failed reason: Some devices are running the wrong OS version.
2023-10-30T13:59:20: %AETEST-INFO: The result of section check_current_version is => FAILED
2023-10-30T13:59:20: %AETEST-INFO: The result of testcase CheckVersion is => FAILED
2023-10-30T13:59:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:59:20: %AETEST-INFO: |                           Starting common cleanup                            |
2023-10-30T13:59:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:59:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:59:20: %AETEST-INFO: |                 Starting subsection disconnect_from_devices                  |
2023-10-30T13:59:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:59:22: %AETEST-INFO: The result of subsection disconnect_from_devices is => PASSED
2023-10-30T13:59:22: %AETEST-INFO: The result of common cleanup is => PASSED
2023-10-30T13:59:22: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:59:22: %AETEST-INFO: |                               Detailed Results                               |
2023-10-30T13:59:22: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:59:22: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
2023-10-30T13:59:22: %AETEST-INFO: --------------------------------------------------------------------------------
2023-10-30T13:59:22: %AETEST-INFO: .
2023-10-30T13:59:22: %AETEST-INFO: |-- common_setup                                                          PASSED
2023-10-30T13:59:22: %AETEST-INFO: |   `-- connect_to_devices                                                PASSED
2023-10-30T13:59:22: %AETEST-INFO: |-- CheckVersion                                                          FAILED
2023-10-30T13:59:22: %AETEST-INFO: |   `-- check_current_version                                             FAILED
2023-10-30T13:59:22: %AETEST-INFO: `-- common_cleanup                                                        PASSED
2023-10-30T13:59:22: %AETEST-INFO:     `-- disconnect_from_devices                                           PASSED
2023-10-30T13:59:22: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:59:22: %AETEST-INFO: |                                   Summary                                    |
2023-10-30T13:59:22: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-10-30T13:59:22: %AETEST-INFO:  Number of ABORTED                                                            0 
2023-10-30T13:59:22: %AETEST-INFO:  Number of BLOCKED                                                            0 
2023-10-30T13:59:22: %AETEST-INFO:  Number of ERRORED                                                            0 
2023-10-30T13:59:22: %AETEST-INFO:  Number of FAILED                                                             1 
2023-10-30T13:59:22: %AETEST-INFO:  Number of PASSED                                                             2 
2023-10-30T13:59:22: %AETEST-INFO:  Number of PASSX                                                              0 
2023-10-30T13:59:22: %AETEST-INFO:  Number of SKIPPED                                                            0 
2023-10-30T13:59:22: %AETEST-INFO:  Total Number                                                                 3 
2023-10-30T13:59:22: %AETEST-INFO:  Success Rate                                                             66.7% 
2023-10-30T13:59:22: %AETEST-INFO: --------------------------------------------------------------------------------
```

## Folders

The file with the exercise is in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## AEtest Execution

AEtest test script can be executed on its own or as part of an easypy job. The later will be cover in the next exercises.
Below is how an AEtest script can be executed standalone. The `if __name__ == '__main__':` ensure that the script is executed only if it is called directly. It will not be executed if the script is imported as a module.

```python
import aetest

if __name__ == '__main__':
    from genie.testbed import load
    testbed = load('testbed.yaml')
    aetest.main(testbed = testbed)
```

When running the `aetest.main()` the different AEtest sections present in the python script will be executed in the order they are defined in the script (except for `CommonSetup` and `CommonCleanup` which are always executed first and last respectively)

## Steps

To send information inline, in the output of your script, use the `logger.info()` method. For instance, in order to print the below output, you can use `logger.info('xrd-1 is connected')`

```
2023-10-21T11:05:40: %SCRIPT-INFO: xrd-1 is connected
```

### Step 0 - Connect to each device

The `CommonSetup` section is where we set up the common environment required and shared between the script’s testcases.

In this case we will just use a loop to `connect()` to each device of the testbed.

### Step 1 - Verify parsed output of 'show version' and verify the device is running IOS XR 7.9.2

A `Testcase` is defined in this step to verify the current version of the device in the testbed. It is expected for this exercise to verify that **all** devices should be running IOS XR 7.9.2.

The expected version will be statically defined in the `check_current_version` section and all device will be compared against this version.

Note that `xrd-source` and `xrd-destination` are running IOS XR 7.8.2, on purpose. This should return an error in your script.

### Step 1.0 - Parse `show version` output from all connected devices

For each device in the testbed, we first need to parse the `show version` output. You can refer to the documentation below to see available parsers for IOS XR.

> https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers

### Step 1.1 - Verify IOS XR version is equal to `7.9.2`

Use a condition to check if the device is running IOS XR 7.9.2. If not, the test should fail.

For each device that passes the test, print a message similar as the output below.

```plaintext
2023-10-30T13:59:17: %SCRIPT-INFO: --- xrd-1 ---
2023-10-30T13:59:17: %SCRIPT-INFO: software_version = 7.9.2
```

Use the `logger.info()` or `logger.warning()` method to send an output to the terminal.

### Step 1.2 - Fail the test

If a device is not running the right IOS version, make the test fail.
If the version is not compliant, use the `self.failed()` method to fail the test.

```python
@aetest.test
def test(self):
    self.failed('This is a failure message')
```

Upon calling, the current section execution **terminates immediately** , returns and is set with the corresponding result. In other words, result apis can only be called **once** per script section, and all code immediately after it is not executed (similar to how `return`s statement works). More information in the documentation below.

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/results.html#result-apis

### Step 1.3 - Bonus

What if one device fails, but you want to continue to test the others? Change your algo so that all the devices are tested. At the end, fail the test if one of them is not compliant.

In the solution example, note that we are using a simple solution. There are more elegant ways. We want to keep it simple for this part. We will see it in an upcoming exercise how you can use `aetest.loop`.

## Step 2 - Disconnect from each connected device

In the `CommonCleanup` section, use a loop to `disconnect()` from each device of the testbed.

# AEtest

AEtest (Automated Easy Testing) is a test framework specifically design for network testing where a python file is used as a test script.
The architectural design of AEtest module drew inspiration from Python [unittest](https://docs.python.org/3.4/library/unittest.html) and [pytest](http://pytest.org/latest/) libraries which provide Python unit-testing infrastructure.

The AEtest documentation can be found below.

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/index.html

## Structure

An AEtest test script is composed of 3 main sections:

* `CommonSetup` with Subsections
* `Testcases` with setup/tests/cleanup
* `CommonCleanup` with Subsections

`CommonSetup` is where all the common configurations, prerequisites and initializations shared between the script’s testcases should be performed.

`Testcase` is a container/collection of smaller tests. Testcases are the workhorse of every testscript, carrying out the assessments that determines the quality of the product under scrutiny.

`CommonCleanup` is the last section to run within each testscript. Any configurations, initializations and environment changes that occurred during this script run should be cleaned up (removed) here.

```python
from pyats import aetest

# CommonSetup is always run as the first section in the script
class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect_to_device(self, testbed):
        testbed.connect()
 
# Testcase is where test logic is defined, multiple testcase can be defined
class SimpleTestcase(aetest.Testcase):
    @aetest.test
    def simple_test(self, testbed):
        for device in testbed.devices.values():
            interfaces = device.parse("show interfaces")
            for interface in interfaces:
                check_crc(interface)
                
# CommonCleanup is always run as the last section in the script              
class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        testbed.disconnect()
```

More information about each section can be found in the documentation below:

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/structure.html

## Possible Test Results

It's possible to manually provide section results by calling one of the `TestItem` static method.

`TestItem.passed(reason, goto, from_exception, data)`

`TestItem.failed(reason, goto, from_exception, data)`

`TestItem.errored(reason, goto, from_exception, data)`

`TestItem.skipped(reason, goto, from_exception, data)`

`TestItem.blocked(reason, goto, from_exception, data)`

`TestItem.aborted(reason, goto, from_exception, data)`

`TestItem.passx(reason, goto, from_exception, data)`

Upon calling, the current section execution **terminates immediately** , returns and is set with the corresponding result. In other words, result apis can only be called **once** per script section, and all code immediately after it is not executed (similar to how `return`s statement works). More information in the documentation below.

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/results.html#result-apis

## AEtest python examples

Examples can be found here:

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/examples.html#feature-usage

## Passing a test without checking

If your test is not yet coded, but you would like it to pass so your whole code doesn't fail, you can use `pass` as below. Anything below `pass` will not be executed. Once you have coded your test, do not forget to remove it.

```python
def connect_to_devices(self, testbed):
    pass
```
