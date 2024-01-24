# 2. Structured output

In this exercise, a command will be executed on the devices and returned as a structured output. The device output is parsed by the Genie module.
It reuses some steps from the previous exercise such as loading the testbed and connecting to the devices.
The script is composed of 5 mains steps, only the bold ones are to be completed, the rest already is provided.

0. Load the testbed.
1. Connect to all devices in the testbed.
2. **Use Genie to execute the `show version` command to the devices and parse it.**
3. **Print only the device version**
4. Disconnect from the devices.

## Output example

```
2024-01-21T20:36:54: %SCRIPT-INFO: =====================================xrd-1======================================
2024-01-21T20:36:54: %SCRIPT-INFO: software_version = 7.9.2
2024-01-21T20:36:55: %SCRIPT-INFO: =====================================xrd-2======================================
2024-01-21T20:36:55: %SCRIPT-INFO: software_version = 7.9.2
2024-01-21T20:36:57: %SCRIPT-INFO: =====================================xrd-3======================================
2024-01-21T20:36:57: %SCRIPT-INFO: software_version = 7.9.2
2024-01-21T20:36:58: %SCRIPT-INFO: =====================================xrd-4======================================
2024-01-21T20:36:58: %SCRIPT-INFO: software_version = 7.9.2
2024-01-21T20:37:00: %SCRIPT-INFO: ===================================xrd-source===================================
2024-01-21T20:37:00: %SCRIPT-INFO: software_version = 7.8.2
2024-01-21T20:37:01: %SCRIPT-INFO: ====================================xrd-dest====================================
2024-01-21T20:37:01: %SCRIPT-INFO: software_version = 7.8.2
```

## Folders

The files with the exercise are in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## Steps to complete the exercise

The exercise script already contains some code including some reused from the previous exercise. Missing code needs to be completed after the `# Step N` comments.

### Step 0 - Use Genie to execute and parse the output of the `show version` command

Use the `parse()` method on each `device` object to send the `show version` command to the `device` and parse the output using pyATS libraries. Save the parsed `show version` output, and save it in a variable.

Here, the `parse()` method will take one argument: a `str` which is the CLI command we want to send the device. 

Documentation about `parse()` method can be found here:

> https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/explore.html?highlight=parse#

**Not all CLI commands have a Genie parser**. Available parsers can be found here:

> https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers

### Step 1 - Print only the device version

The `parse()` method will return a dictionary. For simplicity and to check how it is structured, you can print the whole dictionary.

However, only the IOS XR version needs to be printed, it corresponds to `software_version` key of the dictionary.