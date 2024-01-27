# 3. Diff between two config files

This exercise utilize the Genie `Diff` module to compare two BGP configurations. 
The first configuration is the expected one, the second one is collected from **xrd-1**.
It reuses some steps from the previous exercise such as loading the testbed and connecting to the device.
The script is composed of 6 mains steps, only the bold ones are to be completed, the rest already is provided.

0. Convert the expected config to a Genie `Config` object.
1. Load the testbed and connect to `xrd-1`.
2. **Collect `xrd-1` BGP configuration.**
3. **Compare it with the expected BGP configuration.**
4. **Print the differences between the two.**
5. Disconnect from `xrd-1`.

## Output example

```
2024-01-21T20:36:18: %SCRIPT-INFO:  router bgp 65000:
2024-01-21T20:36:18: %SCRIPT-INFO:   vrf A:
2024-01-21T20:36:18: %SCRIPT-INFO:    address-family ipv4 unicast:
2024-01-21T20:36:18: %SCRIPT-INFO: +   redistribute ospf A route-policy IMPORT_A:
2024-01-21T20:36:18: %SCRIPT-INFO: -   redistribute ospf A route-policy IMPORT_B:
2024-01-21T20:36:18: %SCRIPT-INFO: + bgp router-id 10.10.10.1:
2024-01-21T20:36:18: %SCRIPT-INFO: - bgp router-id 10.10.10.2:
2024-01-21T20:36:18: %SCRIPT-INFO: + neighbor 10.10.10.2:
2024-01-21T20:36:18: %SCRIPT-INFO: +  address-family vpnv4 unicast:
2024-01-21T20:36:18: %SCRIPT-INFO: +  remote-as 65000:
2024-01-21T20:36:18: %SCRIPT-INFO: +  update-source Loopback0:
2024-01-21T20:36:18: %SCRIPT-INFO: - neighbor 10.10.10.4:
2024-01-21T20:36:18: %SCRIPT-INFO: -  address-family vpnv4 unicast:
2024-01-21T20:36:18: %SCRIPT-INFO: -  remote-as 65000:
2024-01-21T20:36:18: %SCRIPT-INFO: -  update-source Loopback0:
```

## Folders

The files with the exercise are in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## Genie `Config` Object

A Genie `Config` object convert a string `str` to a `dict` object. Below is an example of how to use it and the output of the parsed config.

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

## Steps to complete the exercise

The exercise script already contains some code including some reused from the previous exercise. Missing code needs to be completed after the `# Step N` comments.

### Step 0 - Collect the BGP configuration from **xrd-1**

Using the `execute()` method, collect the `show running router bgp` from **xrd-1** and save it in a variable.

By default, on IOS XR, the first line of a `show` command output contains the timestamps, which shouldn't be compared. 
It can be removed with the following code that use python list comprehension on a string:  `config = config[config.index('\n'):]`


### Step 1 - Convert the BGP config output to a `Config` object

Convert the config output which is a string `str` to a `Config` object using the Genie `Config()` class constructor.
Then parse the config using the `config.tree()` method.

You can refer to the documentation below.

> https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#config

### Step 2 - Use the `Diff` module to print the differences between the two configurations

Use the `Diff` module to find the differences between the two configurations. 
Create a `Diff` object using the Genie `Diff()` class constructor and pass the two `Config` objects as arguments.
Then use the `diff.findDiff()` method to get the differences between the two configurations.

You can refer to the below documentation.

> https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#diff

The `Diff` module cannot compare two `str` objects, it only compares `dict` objects. If you try, it will raise a `TypeError`. 
That's why the `str` variable were converted using the Genie `Config` object which helps to convert a device config to a `dict` object.

### Step 3 - Print the differences between the two configurations

Print the output in the terminal using the `logger.info()` method. 
It if works, feel free to adapt the `expected_conf_str` to whatever you like to see how the differences are displayed.

