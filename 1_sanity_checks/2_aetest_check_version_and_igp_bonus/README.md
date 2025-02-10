# 2. AETest - Check version and IGP (Bonus)

This third exercise on AEtest is an improvement of the second one with an additional testcase: IGP configurations are
compared against an expected one using the Genie `Diff` module.
Moreover, the `@aetest.loop` is defined dynamically based on the devices in the testbed.
The test script is composed of 4 main sections with a few steps in each of them and only the one in bold are to be
completed, the rest of the code and the testscript structure is already provided.

0. CommonSetup: Connect to the devices in the testbed.
1. CheckVersion: Verify the devices are running the correct version using Genie to parse the `show version` output.
   1. Parse `show version` output.
   2. Verify that the device is running the version defined in the testbed.
   3. Pass or Fail the test depending on the device version.
2. **CheckIGP: Verify the IGP configuration using Genie Diff.**
   1. **Collect `show run router isis` output.**
   2. **Convert the output to a Genie `Config` object.**
   3. **Convert the expected ISIS configuration to a Genie `Config` object.**
   4. **Compare the collected IGP configuration against the expected one.**
   5. **Pass or Fail the test depending on the IGP configuration.**
3. CommonCleanup: Disconnect from the devices.

## Output example

Output has been truncated for brevity.

```plaintext
2024-01-21T21:09:41: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:41: %AETEST-INFO: |                            Starting common setup                             |
2024-01-21T21:09:41: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:41: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:41: %AETEST-INFO: |                          Starting subsection setup                           |
2024-01-21T21:09:41: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:41: %AETEST-INFO: The result of subsection setup is => PASSED
2024-01-21T21:09:41: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:41: %AETEST-INFO: |        Starting subsection connect[device=Device_xrd-1,_type_router]         |
2024-01-21T21:09:41: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:43: %AETEST-INFO: Passed reason: xrd-1 - connected
2024-01-21T21:09:43: %AETEST-INFO: The result of subsection connect[device=Device_xrd-1,_type_router] is => PASSED
[...]
2024-01-21T21:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:53: %AETEST-INFO: |                          Starting testcase CheckIGP                          |
2024-01-21T21:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:53: %AETEST-INFO: |                            Starting section setup                            |
2024-01-21T21:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:53: %AETEST-INFO: The result of section setup is => PASSED
2024-01-21T21:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:53: %AETEST-INFO: |     Starting section check_igp_config[device=Device_xrd-1,_type_router]      |
2024-01-21T21:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:53: %SCRIPT-WARNING: Found difference in ISIS config:
2024-01-21T21:09:53: %SCRIPT-WARNING:  router isis core
2024-01-21T21:09:53: %SCRIPT-WARNING: - net 49.0000.0100.1001.0001.00
2024-01-21T21:09:53: %SCRIPT-WARNING: + net 49.0000.0100.1001.0010.00
2024-01-21T21:09:53: %AETEST-ERROR: Failed reason: Unexpected ISIS configuration found on device.
2024-01-21T21:09:53: %AETEST-INFO: The result of section check_igp_config[device=Device_xrd-1,_type_router] is => FAILED
2024-01-21T21:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:53: %AETEST-INFO: |     Starting section check_igp_config[device=Device_xrd-2,_type_router]      |
2024-01-21T21:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:54: %AETEST-INFO: The result of section check_igp_config[device=Device_xrd-2,_type_router] is => PASSED
2024-01-21T21:09:54: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:54: %AETEST-INFO: |     Starting section check_igp_config[device=Device_xrd-3,_type_router]      |
2024-01-21T21:09:54: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:55: %AETEST-INFO: The result of section check_igp_config[device=Device_xrd-3,_type_router] is => PASSED
2024-01-21T21:09:55: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:55: %AETEST-INFO: |     Starting section check_igp_config[device=Device_xrd-4,_type_router]      |
2024-01-21T21:09:55: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:55: %AETEST-INFO: The result of section check_igp_config[device=Device_xrd-4,_type_router] is => PASSED
2024-01-21T21:09:55: %AETEST-INFO: The result of testcase CheckIGP is => FAILED
[...]
2024-01-21T21:09:56: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:56: %AETEST-INFO: |                               Detailed Results                               |
2024-01-21T21:09:56: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:56: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
2024-01-21T21:09:56: %AETEST-INFO: --------------------------------------------------------------------------------
2024-01-21T21:09:56: %AETEST-INFO: .
2024-01-21T21:09:56: %AETEST-INFO: |-- common_setup                                                          PASSED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- setup                                                             PASSED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- connect[device=Device_xrd-1,_type_router]                         PASSED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- connect[device=Device_xrd-2,_type_router]                         PASSED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- connect[device=Device_xrd-3,_type_router]                         PASSED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- connect[device=Device_xrd-4,_type_router]                         PASSED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- connect[device=Device_xrd-source,_type_router]                    PASSED
2024-01-21T21:09:56: %AETEST-INFO: |   `-- connect[device=Device_xrd-dest,_type_router]                      PASSED
2024-01-21T21:09:56: %AETEST-INFO: |-- CheckVersion                                                          FAILED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- setup                                                             PASSED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- check_version[device=Device_xrd-1,_type_router]                   PASSED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- check_version[device=Device_xrd-2,_type_router]                   PASSED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- check_version[device=Device_xrd-3,_type_router]                   PASSED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- check_version[device=Device_xrd-4,_type_router]                   PASSED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- check_version[device=Device_xrd-source,_type_router]              FAILED
2024-01-21T21:09:56: %AETEST-INFO: |   `-- check_version[device=Device_xrd-dest,_type_router]                PASSED
2024-01-21T21:09:56: %AETEST-INFO: |-- CheckIGP                                                              FAILED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- setup                                                             PASSED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- check_igp_config[device=Device_xrd-1,_type_router]                FAILED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- check_igp_config[device=Device_xrd-2,_type_router]                PASSED
2024-01-21T21:09:56: %AETEST-INFO: |   |-- check_igp_config[device=Device_xrd-3,_type_router]                PASSED
2024-01-21T21:09:56: %AETEST-INFO: |   `-- check_igp_config[device=Device_xrd-4,_type_router]                PASSED
2024-01-21T21:09:56: %AETEST-INFO: `-- common_cleanup                                                        PASSED
2024-01-21T21:09:56: %AETEST-INFO:     |-- setup                                                             PASSED
2024-01-21T21:09:56: %AETEST-INFO:     |-- disconnect[device=Device_xrd-1,_type_router]                      PASSED
2024-01-21T21:09:56: %AETEST-INFO:     |-- disconnect[device=Device_xrd-2,_type_router]                      PASSED
2024-01-21T21:09:56: %AETEST-INFO:     |-- disconnect[device=Device_xrd-3,_type_router]                      PASSED
2024-01-21T21:09:56: %AETEST-INFO:     |-- disconnect[device=Device_xrd-4,_type_router]                      PASSED
2024-01-21T21:09:56: %AETEST-INFO:     |-- disconnect[device=Device_xrd-source,_type_router]                 PASSED
2024-01-21T21:09:56: %AETEST-INFO:     `-- disconnect[device=Device_xrd-dest,_type_router]                   PASSED
2024-01-21T21:09:56: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:56: %AETEST-INFO: |                                   Summary                                    |
2024-01-21T21:09:56: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-21T21:09:56: %AETEST-INFO:  Number of ABORTED                                                            0 
2024-01-21T21:09:56: %AETEST-INFO:  Number of BLOCKED                                                            0 
2024-01-21T21:09:56: %AETEST-INFO:  Number of ERRORED                                                            0 
2024-01-21T21:09:56: %AETEST-INFO:  Number of FAILED                                                             2 
2024-01-21T21:09:56: %AETEST-INFO:  Number of PASSED                                                             2 
2024-01-21T21:09:56: %AETEST-INFO:  Number of PASSX                                                              0 
2024-01-21T21:09:56: %AETEST-INFO:  Number of SKIPPED                                                            0 
2024-01-21T21:09:56: %AETEST-INFO:  Total Number                                                                 4 
2024-01-21T21:09:56: %AETEST-INFO:  Success Rate                                                             50.0% 
2024-01-21T21:09:56: %AETEST-INFO: --------------------------------------------------------------------------------
```

## Folders

The files with the exercise are in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

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

## ISIS configuration

Below is a reference output of the `show run router isis` command. The `net 49.0000.0100.1001.0001.00` line is the ISIS NET (Network Entity Title) address.
It follows the addressing scheme used by the CLNS protocol which is used by ISIS. It must be unique per router and it is often derived from a Loopback address.

The NET address is composed of the three parts:

- The first 3 bytes (6 digits) is the **Area ID**. The first byte is the Address Family Identifier (AFI) and the next two bytes are the Area ID. The AFI is always 49 for private networks.
- The next 6 bytes (12 digits) represent the **S****ystem ID**. This is unique to each router within the IS-IS domain. It is equivalent to the host or address portion on an IP address.
- The last bytes (2 digits), "00", represent the **NSEL** (Network Service Access Point Selector) which is normally set to 00 for network layer routing, to indicate 'this system'

When the system ID is derived from an IP address, the IP address is padded with 0 and rearrange in block of 4 digits.
For example, 192.168.1.1 become 1921.6800.1001.

```plaintext
router isis core
 is-type level-2-only
 net 49.0000.1921.6800.1001.00
 distribute link-state
 address-family ipv4 unicast
  metric-style wide
  advertise passive-only
  mpls traffic-eng router-id Loopback0
  router-id Loopback0
  segment-routing mpls sr-prefer
 !
```

## Steps to complete the exercise

The exercise script already contains some code including some reused from the previous exercise. Missing code needs to be completed after the `# Step N` comments.

### Step 0 - Set the devices to loop over for IGP verification

The `setup` test section is used to define dynamically the devices to loop over for the next test section `check_igp_config`.

The ISIS configuration must be checked only for the **P** and **PE** routers in the topology.
The role of each device is defined in the testbed and can be access with `device.role`.
The following statement is only true when device are a **P** or a **PE**: `device.role in ["PE","P"]`

Using a `for` loop over the devices in the testbed, save only the **P** and **PE** devices in a list.

### Step 1 - Mark the `check_igp_config` test section to loop over the list of device to be checked

The next test section called `check_igp_config` must be loop over only for the **P** and **PE** devices.
Using the `aetest.loop.mark()` function and the device list previously defined mark the `check_igp_config` test section.

*Note that the variable used to mark the loop is passed as an argument of the test section and their name must match.
Here the expected argument is `device` and it must pass a `Device` object.*

### Step 2 - Collect the ISIS configuration

Collect the output of the `show run router isis` with the method `device.execute()` and save it to a variable.
By default, on IOS XR, the first line of a `show` command output contains the timestamps, which shouldn't be compared.
It can be removed with the following code that use python list comprehension on a string:  `config = config[config.index('\n'):]`

### Step 3 - Convert the ISIS config output to a `Config` object

The configuration output need to be converted to a Genie `Config` object to be later compared with the expected isis configuration.
Convert the config output using the `Config()` class constructor and save it to a variable.
Then parse the config using the `config.tree()` method

### Step 4 - Generate the expected ISIS configuration and convert it to a `Config` object

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

Once the expected configuration has been generated, it must be converted to Genie `Config` object.

For more information, refer to the documentation below.

> https://pubhub.devnetcloud.com/media/pyats/docs/topology/usage.html#device-interface-aliases
>
> https://pubhub.devnetcloud.com/media/pyats/docs/topology/concept.html#interface-objects

### Step 5 - Compare the expected and the actual configuration using the Genie `Diff` utility

Using the Genie `Diff` utility compare the two Genie `Config` objects created.
Create a `Diff` object using the Genie `Diff()` class constructor and pass the two `Config` objects as arguments.
Then use the `diff.findDiff()` method to get the differences between the two configurations.
In order to compare only the global config, the interface sections must be ignored. To do so, use the `exclude` parameter of the `Diff` class constructor.

Below is an example on how to use the Genie Diff utility with the `exclude` parameter.
The `exclude` parameter is a list of string to ignore, it can be a regex if it is put in parentheses. In the below example, we would ignore any section starting with `address-family`.

> Don't forget that you can connect on a device to have a look at the full IGP configuration, if needed.

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

### Step 6 - Verify if any configuration differences are found

Now that the config diff has been generated, check if there are any differences. To do so you can check the length of the `.diffs` attribute of a `Diff` object. In our case, the `Diff` object is `dd`. `len(dd.diffs)` would return `0` if there are no differences.

The `.diffs` attribute is a list of differences found between the two Genie `Config` objects. You can use `logger.info(dd.diffs)` to see the differences. 

In our scenario, if any difference is found, the test should be `failed`. Use the `failed()` method to fail the test.

*Note that for `xrd-1` the wrong `loopback 0` address was specified in the testbed. This is done on purpose to have the `check_igp_config` test section failed for this router.*
