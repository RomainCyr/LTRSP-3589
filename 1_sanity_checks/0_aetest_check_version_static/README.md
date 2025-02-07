# 0. AETest - Check version (static)

In this exercise, the devices versions are collected and checked against an expected version. It reuses similar code as the previous exercises but this time structured in a AEtest test script. The test script contains a `CheckVersion` testcase that verifies that the devices are running the version `7.9.2`.

The test script is composed of 3 main sections with a few steps in each of them and only the one in bold are to be completed, the rest of the code and the testscript structure is already provided.

0. `CommonSetup`: Connect to the devices in the testbed.
1. **`CheckVersion`: Verify the devices are running the version `7.9.2` using Genie to parse the `show version` output.**
   1. **Parse `show version` output.**
   2. **Verify that the device version is `7.9.2`.**
   3. **Fail the test if one device is not running the right version.**
2. `CommonCleanup`: Disconnect from the devices.

The goal of this exercise and the following one is to gradually learn how AEtest is structured and what functionalities it provides. However, one may want to have a look at some theoretical concepts that are covered in the [Aetest](#aetest) paragraph.

## Output example

```plaintext
2024-01-19T18:16:59: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:16:59: %AETEST-INFO: |                            Starting common setup                             |
2024-01-19T18:16:59: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:16:59: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:16:59: %AETEST-INFO: |                    Starting subsection connect_to_devices                    |
2024-01-19T18:16:59: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:17:00: %SCRIPT-INFO: xrd-1 - connected
2024-01-19T18:17:01: %SCRIPT-INFO: xrd-2 - connected
2024-01-19T18:17:03: %SCRIPT-INFO: xrd-3 - connected
2024-01-19T18:17:04: %SCRIPT-INFO: xrd-4 - connected
2024-01-19T18:17:05: %SCRIPT-INFO: xrd-source - connected
2024-01-19T18:17:06: %SCRIPT-INFO: xrd-dest - connected
2024-01-19T18:17:06: %AETEST-INFO: The result of subsection connect_to_devices is => PASSED
2024-01-19T18:17:06: %AETEST-INFO: The result of common setup is => PASSED
2024-01-19T18:17:06: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:17:06: %AETEST-INFO: |                        Starting testcase CheckVersion                        |
2024-01-19T18:17:06: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:17:06: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:17:06: %AETEST-INFO: |                    Starting section check_current_version                    |
2024-01-19T18:17:06: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:17:08: %SCRIPT-INFO: =====================================xrd-1======================================
2024-01-19T18:17:08: %SCRIPT-INFO: software_version = 7.9.2
2024-01-19T18:17:09: %SCRIPT-INFO: =====================================xrd-2======================================
2024-01-19T18:17:09: %SCRIPT-INFO: software_version = 7.9.2
2024-01-19T18:17:09: %SCRIPT-INFO: =====================================xrd-3======================================
2024-01-19T18:17:09: %SCRIPT-INFO: software_version = 7.9.2
2024-01-19T18:17:10: %SCRIPT-INFO: =====================================xrd-4======================================
2024-01-19T18:17:10: %SCRIPT-INFO: software_version = 7.9.2
2024-01-19T18:17:10: %SCRIPT-INFO: ===================================xrd-source===================================
2024-01-19T18:17:10: %SCRIPT-INFO: software_version = 7.8.2
2024-01-19T18:17:10: %SCRIPT-WARNING: xrd-source is not running XR 7.9.2
2024-01-19T18:17:11: %SCRIPT-INFO: ====================================xrd-dest====================================
2024-01-19T18:17:11: %SCRIPT-INFO: software_version = 7.8.2
2024-01-19T18:17:11: %SCRIPT-WARNING: xrd-dest is not running XR 7.9.2
2024-01-19T18:17:11: %AETEST-ERROR: Failed reason: Some devices are running the wrong version
2024-01-19T18:17:11: %AETEST-INFO: The result of section check_current_version is => FAILED
2024-01-19T18:17:11: %AETEST-INFO: The result of testcase CheckVersion is => FAILED
2024-01-19T18:17:11: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:17:11: %AETEST-INFO: |                           Starting common cleanup                            |
2024-01-19T18:17:11: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:17:11: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:17:11: %AETEST-INFO: |                 Starting subsection disconnect_from_devices                  |
2024-01-19T18:17:11: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:17:11: %AETEST-INFO: The result of subsection disconnect_from_devices is => PASSED
2024-01-19T18:17:11: %AETEST-INFO: The result of common cleanup is => PASSED
2024-01-19T18:17:11: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:17:11: %AETEST-INFO: |                               Detailed Results                               |
2024-01-19T18:17:11: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:17:11: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
2024-01-19T18:17:11: %AETEST-INFO: --------------------------------------------------------------------------------
2024-01-19T18:17:11: %AETEST-INFO: .
2024-01-19T18:17:11: %AETEST-INFO: |-- common_setup                                                          PASSED
2024-01-19T18:17:11: %AETEST-INFO: |   `-- connect_to_devices                                                PASSED
2024-01-19T18:17:11: %AETEST-INFO: |-- CheckVersion                                                          FAILED
2024-01-19T18:17:11: %AETEST-INFO: |   `-- check_current_version                                             FAILED
2024-01-19T18:17:11: %AETEST-INFO: `-- common_cleanup                                                        PASSED
2024-01-19T18:17:11: %AETEST-INFO:     `-- disconnect_from_devices                                           PASSED
2024-01-19T18:17:11: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:17:11: %AETEST-INFO: |                                   Summary                                    |
2024-01-19T18:17:11: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-19T18:17:11: %AETEST-INFO:  Number of ABORTED                                                            0 
2024-01-19T18:17:11: %AETEST-INFO:  Number of BLOCKED                                                            0 
2024-01-19T18:17:11: %AETEST-INFO:  Number of ERRORED                                                            0 
2024-01-19T18:17:11: %AETEST-INFO:  Number of FAILED                                                             1 
2024-01-19T18:17:11: %AETEST-INFO:  Number of PASSED                                                             2 
2024-01-19T18:17:11: %AETEST-INFO:  Number of PASSX                                                              0 
2024-01-19T18:17:11: %AETEST-INFO:  Number of SKIPPED                                                            0 
2024-01-19T18:17:11: %AETEST-INFO:  Total Number                                                                 3 
2024-01-19T18:17:11: %AETEST-INFO:  Success Rate                                                             66.7% 
2024-01-19T18:17:11: %AETEST-INFO: --------------------------------------------------------------------------------
```

## Folders

The files with the exercise are in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## AEtest Execution

AEtest test script can be executed on its own or as part of an Easypy job. The later will be cover in the next exercises.

Below is how an AEtest script can be executed standalone. The `if __name__ == '__main__':` ensure that the script is executed only if it is called directly. It will not be executed if the script is imported as a module (for example, when used with Easypy).

```python
import aetest

if __name__ == '__main__':
    from genie.testbed import load
    testbed = load('testbed.yaml')
    aetest.main(testbed = testbed)
```

When running the `aetest.main()` the different AEtest classes present in the python script will be executed in the order they are defined in the script (except for `CommonSetup` and `CommonCleanup` which are always executed first and last respectively).

In each class, every decorated function with `@aetest.subsection` or `@aetest.test` will be executed in the order they are defined.

## Console Output

When using AETest it is recommended to use the `logger.info()` method. Using the `logging` module will print in the standard pyATS format. For instance, in order to print the below output, you can use  `logger.info('xrd-1 is connected')`.

```
2023-10-21T11:05:40: %SCRIPT-INFO: xrd-1 is connected
```

## Steps to complete the exercise

The exercise script already contains some code including some reused from the previous exercise. Missing code needs to be completed after the `# Step N` comments.

The steps to be completed are in a `for` loop that iterates over the `devices` in the `testbed`.

### Step 0 - Verify the version only if the device is connected

In the `CommonSetup` section, a `for` loop is used to connect to each `device`. If the connection to one device fails the test script still continues in order to connect to the other devices and verify their version.

**This behavior is done on purpose, and better ways will be covered in the next exercise.**

However, for this exercise, we must first check if the `device` is `connected` before we check its version. Use an `if` statement and the `connected` attribute of the `device` object to ensure that the execution continues only if the device is succesfully connected.

### Step 1 - Parse the `show version` output for the device and save it to a variable

Use the Genie `parse()` method on the `device` object to get the `show version` output and parse the output. Save the parsed `show version` output to a variable.

### Step 2 - Print device version to the console

Using the `logger.info()` method to print the device version to the console.

The device version is in the `software_version` key of the dictionary.

### Step 3 - Verify that the device version is 7.9.2

Use a condition to check if the device is running IOS XR 7.9.2 (using an `if` statement). The expected version should be statically defined in your code and all device will be compared against this version. 

Print a warning message to the console if the device is not running the right version using the `logger.warning()` method.

*Note that xrd-source and xrd-destination are running IOS XR 7.8.2, on purpose. This should fail the testcase.*

### Step 4 - Update the `test_failed` variable if the device is running the wrong version

Set the `test_failed` variable to `True` when the device is running the wrong version.

The `test_failed` variable will be used to fail the `testcase` if one of the devices is running the wrong version. Again, this is not ideal and the next exercises will cover how to improve it.

## AEtest

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

`Testcase` is a container/collection of smaller tests. Testcases are the workhorse of every test script, carrying out the assessments that determines the quality of the product under scrutiny.

`CommonCleanup` is the last section to run within each test script. Any configurations, initializations and environment changes that occurred during this script run should be cleaned up (removed) here.

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

Upon calling, the current section execution **terminates immediately** , returns and is set with the corresponding result. In other words, result apis can only be called **once** per script section, and all code immediately after it is not executed (similar to how `return` statement works). More information in the documentation below.

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
