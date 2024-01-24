# 2. Segment Routing Policy Validation with NETCONF

This bonus exercise is the same AEtest script for Segment Routing Policy Validation as the first exercise, but this time 
using NETCONF to collect data and configure the devices.
There were situation in the first exercise where no parser was available for a specific command, and we did very simple 
checks on the raw output. While this is working, it is not ideal, and it may lead to issues when working on real life situation. 
Using NETCONF is one option as the output data is always structured following a YANG model. 
It is also more consistent when it comes to configuration because it is less prone to errors.

Note that there is no good or bad option between pyATS libraries (parsers) and pyATS NETCONF module. 
As long as it works and you understand the pros and cons for each.

The same steps as the first exercise will be followed, only teh bold one are to be completed, the rest is already prodived.

1. **Connect to the devices under test.**
2. **Verify that no SR policy is configured**
3. Verify the initial forwarding path is as expected.
4. **Configure the On-Demand Next-Hop (ODN) SR policy.**
5. Verify the SR policy is installed.
6. Verify the new forwarding path is as expected.
7. Rollback the configuration.
8. Disconnect from the devices.


## Output example

Output have been truncated for brevity.

```plaintext
2024-01-22T15:36:16: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:16: %AETEST-INFO: |                            Starting common setup                             |
2024-01-22T15:36:16: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:16: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:16: %AETEST-INFO: |                         Starting subsection connect                          |
2024-01-22T15:36:16: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:16: %SCRIPT-INFO: Connecting to devices
2024-01-22T15:36:19: %AETEST-INFO: The result of subsection connect is => PASSED
2024-01-22T15:36:19: %AETEST-INFO: The result of common setup is => PASSED
2024-01-22T15:36:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:19: %AETEST-INFO: |                   Starting testcase ODNSRPolicyValidation                    |
2024-01-22T15:36:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:19: %AETEST-INFO: |             Starting section check_no_policy[device_name=xrd-1]              |
2024-01-22T15:36:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:19: %AETEST-INFO: The result of section check_no_policy[device_name=xrd-1] is => PASSED
2024-01-22T15:36:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:19: %AETEST-INFO: |             Starting section check_no_policy[device_name=xrd-2]              |
2024-01-22T15:36:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:19: %AETEST-INFO: The result of section check_no_policy[device_name=xrd-2] is => PASSED
2024-01-22T15:36:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:19: %AETEST-INFO: |    Starting section verify_traceroute_before[destination=192.168.20.1,dev    |
2024-01-22T15:36:19: %AETEST-INFO: |    ice_name=xrd-source,expected=['10.0.1.0',_'10.0.14.1',_'10.0.34.0',_'1    |
2024-01-22T15:36:19: %AETEST-INFO: |                 0.0.23.0',_'10.0.2.1'],source=192.168.10.1]                  |
2024-01-22T15:36:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:20: %AETEST-INFO: The result of section verify_traceroute_before[destination=192.168.20.1,device_name=xrd-source,expected=['10.0.1.0',_'10.0.14.1',_'10.0.34.0',_'10.0.23.0',_'10.0.2.1'],source=192.168.10.1] is => PASSED
[...]
2024-01-22T15:36:21: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:21: %AETEST-INFO: |           Starting section configure_sr_policy[device_name=xrd-1]            |
2024-01-22T15:36:21: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:21: %SCRIPT-INFO: Configuring SR Policy
2024-01-22T15:36:21: %NCCLIENT-INFO: [host 172.40.0.101 session-id 2855672928] Requesting 'Lock'
2024-01-22T15:36:21: %NCCLIENT-INFO: [host 172.40.0.101 session-id 2855672928] Requesting 'EditConfig'
2024-01-22T15:36:22: %NCCLIENT-INFO: [host 172.40.0.101 session-id 2855672928] Requesting 'Commit'
2024-01-22T15:36:22: %NCCLIENT-INFO: [host 172.40.0.101 session-id 2855672928] Requesting 'Get'
2024-01-22T15:36:22: %NCCLIENT-INFO: [host 172.40.0.101 session-id 2855672928] Requesting 'Unlock'
2024-01-22T15:36:22: %AETEST-INFO: The result of section configure_sr_policy[device_name=xrd-1] is => PASSED
[...]
2024-01-22T15:36:36: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:36: %AETEST-INFO: |                               Detailed Results                               |
2024-01-22T15:36:36: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:36: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
2024-01-22T15:36:36: %AETEST-INFO: --------------------------------------------------------------------------------
2024-01-22T15:36:36: %AETEST-INFO: .
2024-01-22T15:36:36: %AETEST-INFO: |-- common_setup                                                          PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   `-- connect                                                           PASSED
2024-01-22T15:36:36: %AETEST-INFO: |-- ODNSRPolicyValidation                                                 PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- check_no_policy[device_name=xrd-1]                                PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- check_no_policy[device_name=xrd-2]                                PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- verify_traceroute_before[destination=192.168.20.1,device_na...    PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- verify_traceroute_before[destination=172.16.20.1,device_nam...    PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- verify_traceroute_before[destination=192.168.10.1,device_na...    PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- verify_traceroute_before[destination=172.16.10.1,device_nam...    PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- configure_sr_policy[device_name=xrd-1]                            PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- configure_sr_policy[device_name=xrd-2]                            PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- wait_sr_policy_installed                                          PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- verify_odn_policy[device_name=xrd-1,policy_name=srte_c_10_e...    PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- verify_odn_policy[device_name=xrd-2,policy_name=srte_c_10_e...    PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- verify_traceroute_after[destination=192.168.20.1,device_nam...    PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- verify_traceroute_after[destination=172.16.20.1,device_name...    PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- verify_traceroute_after[destination=192.168.10.1,device_nam...    PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- verify_traceroute_after[destination=172.16.10.1,device_name...    PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   |-- rollback_configuration[device_name=xrd-1]                         PASSED
2024-01-22T15:36:36: %AETEST-INFO: |   `-- rollback_configuration[device_name=xrd-2]                         PASSED
2024-01-22T15:36:36: %AETEST-INFO: `-- common_cleanup                                                        PASSED
2024-01-22T15:36:36: %AETEST-INFO:     `-- disconnect                                                        PASSED
2024-01-22T15:36:36: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:36: %AETEST-INFO: |                                   Summary                                    |
2024-01-22T15:36:36: %AETEST-INFO: +------------------------------------------------------------------------------+
2024-01-22T15:36:36: %AETEST-INFO:  Number of ABORTED                                                            0 
2024-01-22T15:36:36: %AETEST-INFO:  Number of BLOCKED                                                            0 
2024-01-22T15:36:36: %AETEST-INFO:  Number of ERRORED                                                            0 
2024-01-22T15:36:36: %AETEST-INFO:  Number of FAILED                                                             0 
2024-01-22T15:36:36: %AETEST-INFO:  Number of PASSED                                                             3 
2024-01-22T15:36:36: %AETEST-INFO:  Number of PASSX                                                              0 
2024-01-22T15:36:36: %AETEST-INFO:  Number of SKIPPED                                                            0 
2024-01-22T15:36:36: %AETEST-INFO:  Total Number                                                                 3 
2024-01-22T15:36:36: %AETEST-INFO:  Success Rate                                                            100.0% 
2024-01-22T15:36:36: %AETEST-INFO: --------------------------------------------------------------------------------
```

## Reseting the configuration

The script `reset_config.py` in the root folder of this project can we use to reset the lab configuration whenever needed.
Each device's configuration will be reset to default configuration.

It may be required when testing the script as some configuration may have been applied to the devices.

## Segment Routing Policy

In this exercise, we will use an **On-Demand Next-hop (ODN) Segment Routing Policy** to steer traffic from **xrd-source** to **xrd-dest** through a specific path.
By default, the IGP metrics are set so that this traffic is taking the longest path (through **xrd-1**, **xrd-4**, **xrd-3** and **xrd-2**) with supposedly the highest bandwidth.

The ODN policy will be created so that the traffic will take the low latency path (through **xrd-1** and **xrd-2**). In this lab, the delay of each link is statically set to 10 usec.

As ODN is used, the L3VPN prefixes of **xrd-source** and **xrd-dest** will be colored with the color **10** using a route-policy. Only the prefixes in the subnet 172.16.0.0/16 should use the low latency path, therefore the route-policy will color only those prefixes.

## Folders

The files with the exercise are in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## NETCONF RPC

NETCONF use SSH as transport to send request to the device. Those request are formatted in XML. There are many ways to generate XML NETCONF RPC, one of them is using YANGSuite. 
YANGSuite is a tool that can be used to explore YANG models and generate XML NETCONF RPC. Refer to the documentation below for more information.

>https://developer.cisco.com/yangsuite/

Another option is using the pyang command line utility.

>https://github.com/mbj4668/pyang

For this exercise, you can either try building your own XML NETCONF RPC or use the one provided in the `netconf` folder. Some of them requires arguments that needs to be provided using the python string method `.format(argument="myarg")`.

Working with NETCONF means handling a lot of XML, there are many python libraries to deal with XML format. `xmltodict` is one of them. Refer to the documentation below for more information.

>https://github.com/martinblech/xmltodict

## Steps to complete the exercise

The exercise script already contains some code including some reused from the previous exercise. Missing code needs to be completed after the `# Step N` comments.

### Step 0 - Connect to each device using `testbed.connect()`

In the `CommonSetup` section, connect only to the device that we will use in this testcase, that is **xrd-1**, **xrd-2**, **xrd-source** and **xrd-dest**.
To connect simultaneously to multiple devices and without doing a `for` loop or `@aetest.loop()`,  you can use the `testbed.connect()` method as below.

In this example, we would connect to two devices in the testbed: `uut` and `helper`. We would connect to `uut` and 
to `helper` using respectively the `cli` and `console` methods as described in the testbed. For both device, we would 
not print the device's connection logs.

The `vias` argument is only required when there are multiples connections available in the testbed. 
In the testbed for this exercise, there are two connection defined: `cli` and `netconf`, therefore you must specify 
which connection method to use.

```python
testbed.connect(testbed.devices['uut'],
                testbed.devices['helper'],
                vias = {'uut': 'cli',
                        'helper': 'console'},
                log_stdout = False)
```

For this exercise, we will connect to **xrd-1**, **xrd-2**, **xrd-source** and **xrd-dest** using the `netconf` method, 
you can check the testbed to see how this connection is defined.

Refer to the documentation below for more information.

> https://pubhub.devnetcloud.com/media/pyats/docs/topology/usage.html#connect-to-all-devices

### Step 1 - Retrieve the SR policy summary model using Netconf

The Segment Routing policy summary can be retrieved using the YANG model **Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policy-summary**.

To get the operational data using NETCONF, the `get` method is used, the `subtree` option allow to filter on a certain path of the YANG model.
Below is an example on using the get method with the `subtree` option. Note that a tuple must be provided to the `get` function `("subtree",xml_query)`.

```python
xml_query='''
  <interfaces xmlns="http://openconfig.net/yang/interfaces">
    <interface>
      <name>GigabitEthernet0/0/0/0</name>
      <state>
      </state>
    </interface>
  </interfaces>
'''

device.netconf.get(("subtree",xml_query))
```

Use the netconf `get()` method to retrieve the Segment Routing policy summary, the xml query required is provided in the file `netconf/filter_policy_summary.xml`.
Save the output of the `get()` method in a variable.

### Step 2 - Access the total policy count attribute

The model **Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policy-summary** provide the attribute `total-policy-count` as show below.

```
pyang -f tree Cisco-IOS-XR-infra-xtc-agent-oper.yang --tree-path xtc/policy-summary
module: Cisco-IOS-XR-infra-xtc-agent-oper
  +--ro xtc
     +--ro policy-summary
        +--ro total-policy-count?              uint32
        +--ro up-policy-count?                 uint32
        +--ro down-policy-count?               uint32
        +--ro total-candidate-path-count?      uint32
        +--ro active-candidate-path-count?     uint32
        +--ro inactive-candidate-path-count?   uint32
        +--ro total-lsp-count?                 uint32
        +--ro active-lsp-count?                uint32
        +--ro reoptimized-lsp-count?           uint32
        +--ro cleanup-lsp-count?               uint32
        +--ro oor-lsp-count?                   uint32
        +--ro pdp-count?                       uint32
        +--ro up-pdp-count?                    uint32
        +--ro down-pdp-count?                  uint32
        +--ro pfp-count?                       uint32
        +--ro up-pfp-count?                    uint32
        +--ro down-pfp-count?                  uint32
        +--ro standby-candidate-path-count?    uint32
        +--ro standby-lsp-count?               uint32
```

Use the `xmltodict` library to parse the xml output of the `get()` method and access the attribute `total-policy-count`.
Below is an example on how to use the `xmltodict` library and access data in the parsed xml.

```python
interface_data = xmltodict.parse(output.xml)
interface_status = interface_data["rpc-reply"]["data"]["interfaces"]["interface"]['state']["oper-status"]
```

For the `total-policy-count` the path is `rpc-reply/data/xtc/policy-summary/total-policy-count`.
Save the `total-policy-count` to a variable.

### Step 3 - Fail the test if the policy count is not 0

Fail the testcase using the `self.failed()` method, if the `total-policy-count` is not 0. 
The full testcase should be stopped as the initial conditions are not met. Use the `goto` argument of the `failed()` 
method to do so, as no change was done to the testbed the goto target should be `next_tc`.

### Step 4 - Define a Lock context for the target configuration to ensure that the requests are atomic

This next steps will require to configure the devices using NETCONF, it focuses on the `netconf_configure` function.
This function is defined as followed: `def netconf_configure(device: Device,target: str,config: str):`.

When using NETCONF, the device configuration can be locked using the `device.netconf.lock()` method. 
This method is used to ensure that the configuration is not modified by another process while we are configuring the device.

This is done is this exercise because the last commit id need to be retrieved and atomicity is required to ensure that 
the last commit id retrieved is indeed the one from the configuration done by the previous request.

To ease the locking and unlocking of the configuration, the python `with` statement is used. 
This is a context manager that allows for setup and cleanup actions to be taken automatically.
In our case the following code blocks are equivalent:

```python
with device.netconf.lock(target="candidate"):
    # do something

# is equivalent to

device.netconf.lock(target="candidate")
# do something
device.netconf.unlock()
```

Use the `with` statement to create a context where the configuration of the device is locked, the target configuration 
argument is provided as an argument of the `netconf_configure` function.

#### Step 5 - Apply the configuration using the NETCONF `edit-config` method

To configure a device using NETCONF use the `edit_config()` method. There are two arguments:
- `target` - on which datastore to apply the config. On IOS XR, the candidate datastore must be used. 
The configuration is not applied to the device until a `device.netconf.commit()` is called.
- `config` - the raw NETCONF XML config

Below is an example of config to shutdown an interface using NETCONF.

```python
config_raw='''
<config>
  <interfaces xmlns="http://openconfig.net/yang/interfaces">
    <interface>
      <name>GigabitEthernet0/0/0/0</name>
      <config>
        <enabled>false</enabled>
      </config>
    </interface>
  </interfaces>
</config>
'''
device.netconf.edit_config(target="candidate",config=config_raw)
device.netconf.commit()
```

Use the netconf `edit-config()` method to apply the `config` provided as an argument of the `netconf_configure` function.
The `target` configuration argument is also provided as an argument of the `netconf_configure` function.

### Step 6 - Commit the configuration

Use the netconf `commit()` method to commit the configuration.

### Step 7 - Retrieve the last commit id

The last commit id can be retrieved with the following YANG model **Cisco-IOS-XR-config-cfgmgr-exec-oper/config-manager/global/config-commit**.
It provides the attribute `last-commit-id` as show below.

```plaintext
pyang -f tree Cisco-IOS-XR-config-cfgmgr-exec-augmented-oper.yang Cisco-IOS-XR-config-cfgmgr-exec-oper.yang --tree-path config-manager/global/config-commit
module: Cisco-IOS-XR-config-cfgmgr-exec-oper
  +--ro config-manager
     +--ro global
        +--ro config-commit
           +--ro commits
           |  +--ro commit* [commit]
           |     +--ro commit         xr:Cisco-ios-xr-string
           |     +--ro timestamp?     string
           |     +--ro commit-id?     string
           |     +--ro user-id?       string
           |     +--ro line?          string
           |     +--ro client-name?   string
           |     +--ro label?         string
           |     +--ro comment?       string
           +--ro config-cfgmgr-exec-augmented-oper:last-commit-id?   string
```

Use the netconf `get()` method to retrieve config-commit data, the xml query required is provided in the file `netconf/filter_last_commit_id.xml`.
Save the output of the `get()` method in a variable.

Then, use the `xmltodict` library to parse the xml output and access the attribute `last-commit-id`.
The path is `rpc-reply/data/config-manager/global/config/commit/last-commit-id`.
Save the `last-commit-id` to a variable.

### Step 8 - Return the last commit ID

The function `netconf_configure` must return the last commit id retrieved.
Return the `last-commit-id` value that was saved in a variable.