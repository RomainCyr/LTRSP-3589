# 0. Segment Routing Policy Validation

This exercise aims to provide a complete example of a SR (Segment Routing) policy validation. 
Using an AEtest script, the initial state is verified, the SR-TE configuration is applied and the new state is verified to be as expected.

This exercise is composed of several steps, only the bold ones are to be completed, the rest is already provided.

1. **Connect to the devices under test.**
2. Verify that no SR policy is configured
3. Verify the initial forwarding path is as expected.
4. **Configure the On-Demand Next-Hop (ODN) SR policy.**
5. **Verify the SR policy is installed.**
6. Verify the new forwarding path is as expected.
7. Rollback the configuration.
8. Disconnect from the devices.

## Output example

Output have been truncated for brevity.

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
[...]
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

## Reseting the configuration

The script `reset_config.py` in the root folder of this project can we use to reset the lab configuration whenever needed.
Each device's configuration will be reset to default configuration.

It may be required when testing the script as some configuration may have been applied to the devices.

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

The files with the exercise are in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

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

For this exercise, we will connect to **xrd-1**, **xrd-2**, **xrd-source** and **xrd-dest** using the `cli` method, 
you can check the testbed to see how this connection is defined.

Refer to the documentation below for more information.

> https://pubhub.devnetcloud.com/media/pyats/docs/topology/usage.html#connect-to-all-devices

### Step 1 - Open the SR policy configuration file

The configuration required to instantiate the SR policy is provided in the `sr_policy_config.txt` file located in the 
same folder of the python script. This configuration is the same for **xrd-1** and **xrd-2**. 

Open the file and save its content to a variable. Below is an example on how to do it, `file_content` will be a string containing the content of the file:

```python
with open('myfile.txt') as file:
    file_content = file.read()
```
### Step 2 - Configure the SR policy

Using the method `device.configure()` send the configuration of the `sr_policy_config.txt` file to the device.
On XR a `commit` is required to confirm the configuration is installed on the device. With this `configure()` method the commit 
is automatically sent at the end of the configuration.

More information about the `device.configure()` method can be found in the below documentation.

> https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/quickstart/configuredevices.html

### Step 3 - Mark the device for rollback

In the cleanup section, the configuration is rollback to remove it. However, the rollback should be done only
if the device configuration was changed. Therefore, a flag should be set at the end of `configure_sr_policy` section.

This flag is later checked during the cleanup to determine if the section should be skipped or not.
Below is an example on how a new variable can be set on the device object and later checked.

```python

def test_section_a(device):
    device.custom_variable = True

def test_section_b(device):
    if getattr(device, 'custom_variable', False):
        # do something
        pass
```

Set on the device object a `rollback` attribute to `True` on the device object if the configuration was successful.

### Step 4 - Set the loop parameters for the `verify_odn_policy` section

If the On-Demand policies have been correctly configured, we should see a policy installed on **xrd-1** toward **xrd-2** and the same reverse policy on **xrd-2** toward **xrd-1**.
This can be verified with the command `show segment-routing traffic-eng policy name <policy_name>`. In our case the `policy_name` will be:

- `srte_c_10_ep_10.10.10.2` for the policy installed on **xrd-1**,
- `srte_c_10_ep_10.10.10.1` for the policy installed on **xrd-2**.

Those names are deterministic and can be easily computed from the configuration. Indeed, they have the following format: `srte_c_<color>_ep_<endpoint_ip>`.

The test section `verify_odn_policy` should be executed twice, once for each pair of device and policy name. An `@aetest.loop()` can be used.
When using an `@aetest.loop()`, multiples `parameters` can be provided as show below:

```python
# loop with 2 iterations using parameters argument
# ------------------------------------------------
#   iteration 1: a=1, b=4
#   iteration 2: a=2, b=5

@aetest.loop(a = [1, 2], b = [4, 5])
def test(a,b):
    pass
```

Set the loop parameters so that the `verify_odn_policy` section is executed twice, once for each pair of device and policy name.

### Step 5 - Execute the `show segment-routing traffic-eng policy name <policy_name>` command

Use the command `show segment-routing traffic-eng policy name <policy_name>` to verify that the policy is installed.
Unfortunately, there are no existing Genie parser available for this command, the `execute()` method should be used and  
a simple verification will be done to verify that the policy is up.

### Step 6 - Fail the testcase if the policy is not installed

The testcase should fail if the policy is not installed. This can be done by using the `self.failed()` method. 

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

Checking that the policy is up can easily be done with the following python statement `"Admin: up  Operational: up" in output`

Fail the testcase if the policy is not up. If this test section fails, the execution should be stopped. 
Indeed, the next test section become unnecessary as it would surely fail.  However, as configuration may have been
pushed to the device, one must ensure that the cleanup section is executed.  Use the `goto` argument of the `failed()`
method to do so, the `goto` target must be `cleanup`.
