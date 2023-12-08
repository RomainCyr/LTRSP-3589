# 0. Segment Routing Policy Validation

In this first exercise, we will use AEtest to verify an initial state, modify the configuration and verify the new state is as expected:

1. Connect to the devices,
2. Verify the forwarding path is as expected,
3. Set an On-Demand Next-Hop (ODN) segment-routing policy,
4. Verify the new forwarding path is as expected,
5. Rollback the configuration,
6. Disconnect from the devices.

## Output example

```plaintext
2023-11-10T17:10:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:30: %AETEST-INFO: |                            Starting common setup                             |
2023-11-10T17:10:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:30: %AETEST-INFO: |                         Starting subsection connect                          |
2023-11-10T17:10:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:30: %SCRIPT-INFO: Connecting to devices
2023-11-10T17:10:33: %AETEST-INFO: The result of subsection connect is => PASSED
2023-11-10T17:10:33: %AETEST-INFO: The result of common setup is => PASSED
2023-11-10T17:10:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:33: %AETEST-INFO: |                   Starting testcase ODNSRPolicyValidation                    |
2023-11-10T17:10:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:33: %AETEST-INFO: |             Starting section check_no_policy[device_name=xrd-1]              |
2023-11-10T17:10:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:34: %AETEST-INFO: The result of section check_no_policy[device_name=xrd-1] is => PASSED
2023-11-10T17:10:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:34: %AETEST-INFO: |             Starting section check_no_policy[device_name=xrd-2]              |
2023-11-10T17:10:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:34: %AETEST-INFO: The result of section check_no_policy[device_name=xrd-2] is => PASSED
2023-11-10T17:10:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:34: %AETEST-INFO: |    Starting section verify_traceroute_before[destination=192.168.20.1,sou    |
2023-11-10T17:10:34: %AETEST-INFO: |                              rce=192.168.10.1]                               |
2023-11-10T17:10:34: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:38: %AETEST-INFO: The result of section verify_traceroute_before[destination=192.168.20.1,source=192.168.10.1] is => PASSED
2023-11-10T17:10:38: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:38: %AETEST-INFO: |    Starting section verify_traceroute_before[destination=172.16.20.1,sour    |
2023-11-10T17:10:38: %AETEST-INFO: |                               ce=172.16.10.1]                                |
2023-11-10T17:10:38: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:42: %AETEST-INFO: The result of section verify_traceroute_before[destination=172.16.20.1,source=172.16.10.1] is => PASSED
2023-11-10T17:10:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:42: %AETEST-INFO: |           Starting section configure_sr_policy[device_name=xrd-1]            |
2023-11-10T17:10:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:42: %SCRIPT-INFO: Configuring SR Policy
2023-11-10T17:10:44: %AETEST-INFO: The result of section configure_sr_policy[device_name=xrd-1] is => PASSED
2023-11-10T17:10:44: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:44: %AETEST-INFO: |           Starting section configure_sr_policy[device_name=xrd-2]            |
2023-11-10T17:10:44: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:44: %SCRIPT-INFO: Configuring SR Policy
2023-11-10T17:10:48: %AETEST-INFO: The result of section configure_sr_policy[device_name=xrd-2] is => PASSED
2023-11-10T17:10:48: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:48: %AETEST-INFO: |                  Starting section wait_sr_policy_installed                   |
2023-11-10T17:10:48: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:48: %SCRIPT-INFO: Waiting 10 seconds for the SR policy to be installed
2023-11-10T17:10:58: %AETEST-INFO: The result of section wait_sr_policy_installed is => PASSED
2023-11-10T17:10:58: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:58: %AETEST-INFO: |    Starting section verify_odn_policy[device_name=xrd-1,policy_name=srte_    |
2023-11-10T17:10:58: %AETEST-INFO: |                             c_10_ep_10.10.10.2]                              |
2023-11-10T17:10:58: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:58: %AETEST-INFO: The result of section verify_odn_policy[device_name=xrd-1,policy_name=srte_c_10_ep_10.10.10.2] is => PASSED
2023-11-10T17:10:58: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:58: %AETEST-INFO: |    Starting section verify_odn_policy[device_name=xrd-2,policy_name=srte_    |
2023-11-10T17:10:58: %AETEST-INFO: |                             c_10_ep_10.10.10.1]                              |
2023-11-10T17:10:58: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:58: %AETEST-INFO: The result of section verify_odn_policy[device_name=xrd-2,policy_name=srte_c_10_ep_10.10.10.1] is => PASSED
2023-11-10T17:10:58: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:10:58: %AETEST-INFO: |    Starting section verify_traceroute_after[destination=192.168.20.1,expe    |
2023-11-10T17:10:58: %AETEST-INFO: |    cted=['10.0.1.0',_'10.0.14.1',_'10.0.34.0',_'10.0.23.0',_'10.0.2.1'],s    |
2023-11-10T17:10:58: %AETEST-INFO: |                             ource=192.168.10.1]                              |
2023-11-10T17:10:58: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:11:03: %AETEST-INFO: The result of section verify_traceroute_after[destination=192.168.20.1,expected=['10.0.1.0',_'10.0.14.1',_'10.0.34.0',_'10.0.23.0',_'10.0.2.1'],source=192.168.10.1] is => PASSED
2023-11-10T17:11:03: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:11:03: %AETEST-INFO: |    Starting section verify_traceroute_after[destination=172.16.20.1,expec    |
2023-11-10T17:11:03: %AETEST-INFO: |        ted=['10.0.1.0',_'10.0.12.1',_'10.0.2.1'],source=172.16.10.1]         |
2023-11-10T17:11:03: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:11:08: %AETEST-INFO: The result of section verify_traceroute_after[destination=172.16.20.1,expected=['10.0.1.0',_'10.0.12.1',_'10.0.2.1'],source=172.16.10.1] is => PASSED
2023-11-10T17:11:08: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:11:08: %AETEST-INFO: |          Starting section rollback_configuration[device_name=xrd-1]          |
2023-11-10T17:11:08: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:11:08: %SCRIPT-INFO: Rolling back configuration
2023-11-10T17:11:12: %AETEST-INFO: The result of section rollback_configuration[device_name=xrd-1] is => PASSED
2023-11-10T17:11:12: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:11:12: %AETEST-INFO: |          Starting section rollback_configuration[device_name=xrd-2]          |
2023-11-10T17:11:12: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:11:12: %SCRIPT-INFO: Rolling back configuration
2023-11-10T17:11:15: %AETEST-INFO: The result of section rollback_configuration[device_name=xrd-2] is => PASSED
2023-11-10T17:11:15: %AETEST-INFO: The result of testcase ODNSRPolicyValidation is => PASSED
2023-11-10T17:11:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:11:15: %AETEST-INFO: |                           Starting common cleanup                            |
2023-11-10T17:11:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:11:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:11:15: %AETEST-INFO: |                        Starting subsection disconnect                        |
2023-11-10T17:11:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:11:15: %SCRIPT-INFO: Disconnecting from devices
2023-11-10T17:11:15: %AETEST-INFO: The result of subsection disconnect is => PASSED
2023-11-10T17:11:15: %AETEST-INFO: The result of common cleanup is => PASSED
2023-11-10T17:11:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:11:15: %AETEST-INFO: |                               Detailed Results                               |
2023-11-10T17:11:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:11:15: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
2023-11-10T17:11:15: %AETEST-INFO: --------------------------------------------------------------------------------
2023-11-10T17:11:15: %AETEST-INFO: .
2023-11-10T17:11:15: %AETEST-INFO: |-- common_setup                                                          PASSED
2023-11-10T17:11:15: %AETEST-INFO: |   `-- connect                                                           PASSED
2023-11-10T17:11:15: %AETEST-INFO: |-- ODNSRPolicyValidation                                                 PASSED
2023-11-10T17:11:15: %AETEST-INFO: |   |-- check_no_policy[device_name=xrd-1]                                PASSED
2023-11-10T17:11:15: %AETEST-INFO: |   |-- check_no_policy[device_name=xrd-2]                                PASSED
2023-11-10T17:11:15: %AETEST-INFO: |   |-- verify_traceroute_before[destination=192.168.20.1,source=19...    PASSED
2023-11-10T17:11:15: %AETEST-INFO: |   |-- verify_traceroute_before[destination=172.16.20.1,source=172...    PASSED
2023-11-10T17:11:15: %AETEST-INFO: |   |-- configure_sr_policy[device_name=xrd-1]                            PASSED
2023-11-10T17:11:15: %AETEST-INFO: |   |-- configure_sr_policy[device_name=xrd-2]                            PASSED
2023-11-10T17:11:15: %AETEST-INFO: |   |-- wait_sr_policy_installed                                          PASSED
2023-11-10T17:11:15: %AETEST-INFO: |   |-- verify_odn_policy[device_name=xrd-1,policy_name=srte_c_10_e...    PASSED
2023-11-10T17:11:15: %AETEST-INFO: |   |-- verify_odn_policy[device_name=xrd-2,policy_name=srte_c_10_e...    PASSED
2023-11-10T17:11:15: %AETEST-INFO: |   |-- verify_traceroute_after[destination=192.168.20.1,expected=[...    PASSED
2023-11-10T17:11:15: %AETEST-INFO: |   |-- verify_traceroute_after[destination=172.16.20.1,expected=['...    PASSED
2023-11-10T17:11:15: %AETEST-INFO: |   |-- rollback_configuration[device_name=xrd-1]                         PASSED
2023-11-10T17:11:15: %AETEST-INFO: |   `-- rollback_configuration[device_name=xrd-2]                         PASSED
2023-11-10T17:11:15: %AETEST-INFO: `-- common_cleanup                                                        PASSED
2023-11-10T17:11:15: %AETEST-INFO:     `-- disconnect                                                        PASSED
2023-11-10T17:11:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:11:15: %AETEST-INFO: |                                   Summary                                    |
2023-11-10T17:11:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:11:15: %AETEST-INFO:  Number of ABORTED                                                            0 
2023-11-10T17:11:15: %AETEST-INFO:  Number of BLOCKED                                                            0 
2023-11-10T17:11:15: %AETEST-INFO:  Number of ERRORED                                                            0 
2023-11-10T17:11:15: %AETEST-INFO:  Number of FAILED                                                             0 
2023-11-10T17:11:15: %AETEST-INFO:  Number of PASSED                                                             3 
2023-11-10T17:11:15: %AETEST-INFO:  Number of PASSX                                                              0 
2023-11-10T17:11:15: %AETEST-INFO:  Number of SKIPPED                                                            0 
2023-11-10T17:11:15: %AETEST-INFO:  Total Number                                                                 3 
2023-11-10T17:11:15: %AETEST-INFO:  Success Rate                                                            100.0% 
2023-11-10T17:11:15: %AETEST-INFO: --------------------------------------------------------------------------------
```

## Reseting the Configuration

It could happen that you configured something you shouldn't. In this case, you can run the script `reset_config.py` at in the root folder of this project. Each device's configuration will be reset to default configuration.

## Segment Routing Policy

In this exercise, we will use an **On-Demand Next-hop (ODN) Segment Routing Policy** to steer traffic from **xrd-source** to **xrd-dest** through a specific path.
By default, the IGP metrics are set so that this traffic is taking the longest path (through **xrd-1**, **xrd-4**, **xrd-3** and **xrd-2**) with supposedly the highest bandwidth.

The ODN policy will be created so that the traffic will take the low latency path (through **xrd-1** and **xrd-2**). In this lab, the delay of each link is statically set to 10 usec.

As ODN is used, the L3VPN prefixes of **xrd-source** and **xrd-dest** will be colored with the color **10** using a route-policy. Only the prefixes in the subnet 172.16.0.0/16 should use the low latency path, therefore the route-policy will color only those prefixes.

## AEtest `goto` Statement
When a test section fails, there are situation where the full testcase should be stopped. This can be achieved by using a `goto` statement.
`goto` statement enables early flow termination in case executing the test further would be conditioned by the result of a previous test.
`goto` jumps can be invoked as optional arguments to **Result APIs**. A list of `goto` must be provided as there can be multiple `goto` target.
There are four different `goto` targets available:
 - `cleanup`: jumps to the testcase cleanup section, by-passing all other test sections
 - `next_tc`:jumps to the next testcase in line 
 - `common_cleanup`: jumps to the script’s CommonCleanup section. 
 - `exit`: terminates the testscript immediately without going further.
	
Below is an python example of what can be done:

```python
class TestcaseOne(aetest.Testcase):
    @aetest.setup
    def setup(self):
        # setup failed, go to next testcase
        self.failed('test failed', goto = ['next_tc'])
    @aetest.test
    def test(self):
        # Not executed
        pass
    
class TestcaseTwo(aetest.Testcase):
    # Executed because it is the next testcase 
    @aetest.test
    def test_one(self):
        self.failed(goto = ['cleanup'])
    
    @aetest.test
    def test_two(self):
        # Not Executed
        pass
        
    @aetest.cleanup
    def cleanup(self):
        #Executed as it is the cleanup
        pass
```

More information is available in the documentation below.

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/control.html#aetest-goto

## Folders

The file with the exercise is in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## Steps

To send information inline, in the output of your script, use the `logger.info()` method. For instance, in order to print the below output, you can use `logger.info('xrd-1 is connected')`

```
2023-10-21T11:05:40: %SCRIPT-INFO: xrd-1 is connected
```

### Step 0 - Connect to each device using `testbed.connect()`

In the `CommonSetup` section, connect only to the device that we will use in this testcase, that is **xrd-1**, **xrd-2**, **xrd-source** and **xrd-dest**.
To connect simultaneously to multiple devices and without doing a `for` loop or `@aetest.loop()`,  you can use the `testbed.connect()` method as below.

In this example, we would connect to two devices in the testbed: `uut` and `helper`. We would connect to `uut` and to `helper` using respectively the `cli` and `console` methods as described in the testbed. For both device, we would not print the device's connection logs.

The `vias` argument is only required when there are multiples connections available in the testbed. In the testbed for this exercise, there are two connection defined: `cli` and `netconf`, therefore you must specify which connection method to use.

```python
testbed.connect(testbed.devices['uut'],
                testbed.devices['helper'],
                vias = {'uut': 'cli',
                        'helper': 'console'},
                log_stdout = False)
```

For this exercise, we will connect to **xrd-1**, **xrd-2**, **xrd-source** and **xrd-dest** using the `cli` method, you can check the testbed to see how this connection is defined.

Refer to the documentation below for more information.

> https://pubhub.devnetcloud.com/media/pyats/docs/topology/usage.html#connect-to-all-devices

### Step 1 - Initial Verification

In this step, we will verify that the lab is in the correct initial conditions before we start the test.

There should be not SR policy configured and the forwarding should follow the longest path through **xrd-4** and **xrd-3**
For simplicity we will only check the path from **xrd-source** to **xrd-dest**. Thought, it should be tested in both direction.

Traceroute will be used to check the forwarding path. The path from to `192.168.20.1` and to `172.16.20.1` will be checked.
The source address used will be respectively `192.168.10.1` and `172.16.10.1`.

#### Step 1.0 - Verify no SR policy is configured

##### Step 1.0.0 - Loop the test section to have it executed on **xrd-1** and **xrd-2**

It is expected that you run the same test section on both device, **xrd-1** and **xrd-2** using an `aetest.loop`

##### Step 1.0.1 - Verify that not SR policy is configured on the device

Verify that not SR policy is configured on the **xrd-1** and **xrd-2**. You can use the `show segment-routing traffic-eng policy summary `command. The total number of policies should be 0. Unfortunately, there are no existing Genie parser available for this command, you will have to use the `execute()` and verify with a simple verification the number of policies. Use the method of your choice.

Below and example of `show segment-routing traffic-eng policy summary` output.

```
Tue Nov  7 09:45:13.728 UTC

SR-TE policy database summary:
----------------------------

Total policies: 0
  Operational: up 0 down 0

Per-Destination Policies Summary:
  Total configured: 0
  Operational: up 0 down 0

Per-Flow Policies Summary:
  Total configured: 0
  Operational: up 0 down 0

Total candidate paths: 0
  State: active 0 standby 0 inactive 0
```

If this test section fails, you should stop the execution of the testcase. You can use the `goto` argument of the `failed()` method to do so, as no change was done to the testbed the `goto` target should be `next_tc`.

#### Step 1.1 - Verify the forwarding path

Now we will verify the forwarding path from **xrd-source** to **xrd-dest**. As mentioned before, we will only test this direction for our exercise, but it would make sense in a field situation to test both directions.

We will run two traceroutes on **xrd-source**:

- from `192.168.10.1` to `192.168.20.1`: which would be the equivalent of `traceroute 192.168.20.1 source 192.168.10.1`,
- from `172.16.10.1` to `172.16.20.1`: which would be the equivalent of `traceroute 172.16.20.1 source 172.16.10.1`.

In both cases, the expected hops are: `10.0.1.0, 10.0.14.1, 10.0.34.0, 10.0.23.0, 10.0.2.1`.

##### Step 1.1.0 - Loop the test section to have it executed for both prefixes: `192.168.20.1` and `172.16.20.1`

The test section `verify_traceroute` should be executed twice, once for each pair of source and destination prefixes. You can use an `aetest.loop` to do so.
When using an `aetest.loop`, multiples `parameters` can be provided as show below:

```python
# loop with 2 iterations using parameters argument
# ------------------------------------------------
#   iteration 1: a=1, b=4
#   iteration 2: a=2, b=5

@aetest.loop(a = [1, 2], b = [4, 5])
def test(a,b):
    pass
```

Refer to the documentation below for more information.

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/loop.html#loop-parameters

##### Step 1.1.1 - Verify the traceroute path

The function `parse_traceroute` is provided with a simple parsing of the traceroute output. It returns the list of hops in the traceroute.

Below is an example of output from a traceroute command and the result when it gets out of the `parse_traceroute` function.

```
Example:
    RP/0/RP0/CPU0:xrd-1#traceroute 10.10.10.2 source 10.10.10.1
        1  10.0.14.1 [MPLS: Label 16002 Exp 0] 19 msec  11 msec  12 msec
        2  10.0.34.0 [MPLS: Label 16002 Exp 0] 9 msec  10 msec  10 msec
        3  10.0.23.0 14 msec  *  8 msec
    RP/0/RP0/CPU0:xrd-1#

    Returns ["10.0.14.0","10.0.34.0","10.0.23.0"]
```

Execute the traceroute on **xrd-source** and parse it and verify that the hops are as expected. Two list can easily be compared in python by using the `==` operator.

```python
['a','b','c'] == ['a','b','c'] # Return True
['a','b','c'] == ['a','b','d'] # Return False
```

If this test section fails, you should stop the execution of the testcase. You can use the `goto` argument of the `failed()` method to do so, as no change was done to the testbed the `goto` target should be `next_tc`.

### Step 2 - Configure the SR Policy

The same Segment Routing ODN configuration will be applied on both **xrd-1** and **xrd-2**. This configuration will mark the prefixes in `172.16.0.0/16` subnet with the color `10`.
The color `10` is using the low latency (**xrd-1** -> **xrd-2**) path.

#### Step 2.0 - Configure the SR Policy on **xrd-1** and **xrd-2**

The Segment Routing policy configuration is provided in the `sr_policy_config.txt` file. It contains the SR-TE on-demand config as well as the route-policy used to color the prefixes.

##### Step 2.0.0 - Loop the test section to have it executed on **xrd-1** and **xrd-2**

Using an `aetest.loop()` send the configuration on both **xrd-1** and **xrd-2**.

##### Step 2.0.1 - Configure the SR Policy

Using the method `device.configure()` send the configuration of the `sr_policy_config.txt` file to the device.
This method will automatically commit the configuration.

You can open and read the content of a file by using the below code. `file_content` will be a `str` containing the content of our file.

```python
with open('/path/to/file') as file:
    file_content = file.read()
```

More information about the `device.configure()` method can be found in the below documentation.

> https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/quickstart/configuredevices.html

#### Step 2.1 - Wait for the SR policy to be installed

This test section is just there to wait 10 seconds for the SR policy to be installed.
It is an easy way to ensure that the SR policy will have time to be installed before we verify the forwarding path.

You can use the `time.sleep()` method to pause the execution for 10 seconds. Don't forget to `import time` to be able to use it.

#### Step 2.2 - Verify the SR policy is installed

If the on-demand policies have been correctly configured, we should see a policy installed on **xrd-1** toward **xrd-2** and the same reverse policy on **xrd-2** toward **xrd-1**.
This can be verified with the command `show segment-routing traffic-eng policy name <policy_name>`. In our case the `policy_name` will be:

- `srte_c_10_ep_10.10.10.2` for the policy installed on **xrd-1**,
- `srte_c_10_ep_10.10.10.1` for the policy installed on **xrd-2**.

Those names are deterministic and can be easily computed from the configuration. Indeed, they have the following format: `srte_c_<color>_ep_<endpoint_ip>`.

##### Step 2.2.0 - Loop the test section to have it executed on **xrd-1** and **xrd-2**

Loop the `verify_odn_policy` test section to have it executed on both **xrd-1** and **xrd-2** and check the policy have been correctly installed.

##### Step 2.2.1 - Verify the policy is installed

Use the command `show segment-routing traffic-eng policy name <policy_name>` to verify that the policy is installed.
Unfortunately, there are no existing Genie parser available for this command, you will have to use the `execute()` and verify with a simple verification that the policy is up.

Below is a sample output of `show segment-routing traffic-eng policy name srte_c_10_ep_10.10.10.2`.

```
Tue Nov  7 16:16:43.360 UTC

SR-TE policy database
---------------------

Color: 10, End-point: 10.10.10.2
  Name: srte_c_10_ep_10.10.10.2
  Status:
    Admin: up  Operational: up for 00:00:06 (since Nov  7 16:16:37.285)
  Candidate-paths:
    Preference: 200 (BGP ODN) (active)
      Requested BSID: dynamic
      Constraints:
        Protection Type: protected-preferred
        Maximum SID Depth: 10 
      Dynamic (valid)
        Metric Type: LATENCY,   Path Accumulated Metric: 10 
          SID[0]: 24001 [Adjacency-SID, 10.0.12.0 - 10.0.12.1]
    Preference: 100 (BGP ODN) (inactive)
      Requested BSID: dynamic
      PCC info:
        Symbolic name: bgp_c_10_ep_10.10.10.2_discr_100
        PLSP-ID: 15
      Constraints:
        Protection Type: protected-preferred
        Maximum SID Depth: 10 
      Dynamic (pce) (inactive)
        Metric Type: NONE,   Path Accumulated Metric: 0 
  Attributes:
    Binding SID: 24013
    Forward Class: Not Configured
    Steering labeled-services disabled: no
    Steering BGP disabled: no
    IPv6 caps enable: yes
    Invalidation drop enabled: no
    Max Install Standby Candidate Paths: 0
```

If this test section fails, you should stop the execution of the testcase. You can use the `goto` argument of the `failed()` method to do so, this time because configuration may have been done on the devices, the `goto` target must be `cleanup` to ensure that we go through the cleanup section.

### Step 3 - Verify the forwarding after the policy is installed

Once the policy is installed, the forwarding for the prefixes in `172.16.0.0/16` should be different.
In this section we will verify that the forwarding has indeed changed for the prefix `172.16.20.1` but that it is unchanged for the prefix `192.168.20.1`.

The expected hops in the traceroute are the following:

- from `192.168.10.1` to `192.168.20.1`: `10.0.1.0, 10.0.14.1, 10.0.34.0, 10.0.23.0, 10.0.2.1`
- from `172.16.10.1` to `172.16.20.1` : `10.0.1.0, 10.0.12.1, 10.0.2.1`

This testcase is very similar to first one, and it should be pretty much the same code.

#### Step 3.0 - Loop the test section to have it executed for both prefixes

The test section `verify_traceroute` should be executed twice, once for each prefix. You can use an `aetest.loop` with multiples parameters to do so.

As the `expected` path is not the same for both prefix, you might need to add it to the `aetest.loop` decorator; if you reuse the code from the previous step.

#### Step 3.1 - Verify the traceroute path

The function `parse_traceroute` is provided with a simple parsing of the traceroute output. It returns the list of hops in the traceroute.
Execute the traceroute on **xrd-source** and parse it and verify that the hops are as expected. Two list can easily be compared in python by using the `==` operator.

### Step 4 - Clean configuration

The `aetest.cleanup` test section is used to revert the lab to its original state.
In our case, we will rollback the configuration to leave the lab in the original state.

For simplicity here, we will assume that using the rollback functionality of XR is enough.
Configuration can be rollback by executing the command `rollback configuration last 1` on the device with the `device.execute()` method.

##### Step 4.0.0 - Loop the test section to have it executed for both **xrd-1** and **xrd-2**

This test section should be done for both **xrd-1** and **xrd-2**, use the `aetest.loop` decorator.

##### Step 4.0.1 - Rollback the configuration

Note that this section may be executed even if no configuration have been done on a device. Therefore, it is important to check that the configuration have indeed been done before running it.
You can for example set a flag at the end of the `configure_sr_policy` section (if it was successful) and check this flag in the `rollback_configuration` section.

A new variable can be set on the device object and later checked.

```python

def test_section_a(device):
    device.custom_variable = True

def test_section_b(device):
    if getattr(device, 'custom_variable', False):
        # do something
        pass
```

The `getattr()` method returns the value of the named attribute of an object. If not found, it returns the default value provided to the function. Here, it would check if the device has `custom_variable` attribute and return its value. If the device doesn't have the attribute, it would return `False`.

More information about `getattr()`in the documentation below:

>  https://docs.python.org/3/library/functions.html#getattr

We can use the `self.skipped()` result of an aetest section to mark this test section as skipped if it was not executed.

```python
def rollback(device):
    self.skipped("No configuration to rollback")
```

If configuration needs to be rollback, execute the command `rollback configuration last 1` using the `device.execute()` method.

#### Step 5 - Disconnect from the devices

As for the `testbed.connect()` method, there is a `testbed.disconnect()` method that can be used to disconnect simultaneously from multiple devices and without doing a `for` loop

Use this method to disconnect from the four devices. Below is an example, for the devices `uut` and `helper`.

```python
testbed.disconnect(testbed.devices['uut'],
                   testbed.devices['helper'])
```
