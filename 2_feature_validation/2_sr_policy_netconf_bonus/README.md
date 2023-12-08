# 2. Segment Routing Policy Validation with NETCONF

This is a bonus exercise, it is the same AEtest script for Segment Routing Policy Validation as the first exercise, but this time using NETCONF to connect to the devices.
There were situation in the first exercise where no parser was available for a specific command, and we did very simple checks on the raw output. While this is working, it is not ideal and it may lead to issues when working on real life situation. 
Using NETCONF is one option as the output data is always structured following a YANG model. It is also more consistent when it comes to configuration because it is less prone to errors.

Note that there is no good or bad option between pyATS libraries (parsers) and pyATS NETCONF module. As long as it works and you understand the pros and cons for each.

The same steps as the first exercise will be followed:

1. Connect to the devices using NETCONF
2. Verify the forwarding path is as expected using the XR traceroute action model
3. Set an On-Demand Next-Hop (ODN) segment-routing policy with a NETCONF edit-config RPC
4. Verify the new forwarding path using the XR traceroute action model
5. Rollback the configuration using the NETCONF XR rollback action
6. Disconnect from the devices.

## Output example

```plaintext
2023-11-10T17:07:10: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:10: %AETEST-INFO: |                            Starting common setup                             |
2023-11-10T17:07:10: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:10: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:10: %AETEST-INFO: |                         Starting subsection connect                          |
2023-11-10T17:07:10: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:10: %SCRIPT-INFO: Connecting to devices
2023-11-10T17:07:15: %AETEST-INFO: The result of subsection connect is => PASSED
2023-11-10T17:07:15: %AETEST-INFO: The result of common setup is => PASSED
2023-11-10T17:07:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:15: %AETEST-INFO: |                   Starting testcase ODNSRPolicyValidation                    |
2023-11-10T17:07:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:15: %AETEST-INFO: |             Starting section check_no_policy[device_name=xrd-1]              |
2023-11-10T17:07:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:15: %AETEST-INFO: The result of section check_no_policy[device_name=xrd-1] is => PASSED
2023-11-10T17:07:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:15: %AETEST-INFO: |             Starting section check_no_policy[device_name=xrd-2]              |
2023-11-10T17:07:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:15: %AETEST-INFO: The result of section check_no_policy[device_name=xrd-2] is => PASSED
2023-11-10T17:07:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:15: %AETEST-INFO: |    Starting section verify_traceroute_before[destination=192.168.20.1,dev    |
2023-11-10T17:07:15: %AETEST-INFO: |    ice_name=xrd-source,expected=['10.0.1.0',_'10.0.14.1',_'10.0.34.0',_'1    |
2023-11-10T17:07:15: %AETEST-INFO: |                 0.0.23.0',_'10.0.2.1'],source=192.168.10.1]                  |
2023-11-10T17:07:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:18: %AETEST-INFO: The result of section verify_traceroute_before[destination=192.168.20.1,device_name=xrd-source,expected=['10.0.1.0',_'10.0.14.1',_'10.0.34.0',_'10.0.23.0',_'10.0.2.1'],source=192.168.10.1] is => PASSED
2023-11-10T17:07:18: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:18: %AETEST-INFO: |    Starting section verify_traceroute_before[destination=172.16.20.1,devi    |
2023-11-10T17:07:18: %AETEST-INFO: |    ce_name=xrd-source,expected=['10.0.1.0',_'10.0.14.1',_'10.0.34.0',_'10    |
2023-11-10T17:07:18: %AETEST-INFO: |                  .0.23.0',_'10.0.2.1'],source=172.16.10.1]                   |
2023-11-10T17:07:18: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:22: %AETEST-INFO: The result of section verify_traceroute_before[destination=172.16.20.1,device_name=xrd-source,expected=['10.0.1.0',_'10.0.14.1',_'10.0.34.0',_'10.0.23.0',_'10.0.2.1'],source=172.16.10.1] is => PASSED
2023-11-10T17:07:22: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:22: %AETEST-INFO: |    Starting section verify_traceroute_before[destination=192.168.10.1,dev    |
2023-11-10T17:07:22: %AETEST-INFO: |    ice_name=xrd-dest,expected=['10.0.2.0',_'10.0.23.1',_'10.0.34.1',_'10.    |
2023-11-10T17:07:22: %AETEST-INFO: |                  0.14.0',_'10.0.1.1'],source=192.168.20.1]                   |
2023-11-10T17:07:22: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:26: %AETEST-INFO: The result of section verify_traceroute_before[destination=192.168.10.1,device_name=xrd-dest,expected=['10.0.2.0',_'10.0.23.1',_'10.0.34.1',_'10.0.14.0',_'10.0.1.1'],source=192.168.20.1] is => PASSED
2023-11-10T17:07:26: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:26: %AETEST-INFO: |    Starting section verify_traceroute_before[destination=172.16.10.1,devi    |
2023-11-10T17:07:26: %AETEST-INFO: |    ce_name=xrd-dest,expected=['10.0.2.0',_'10.0.23.1',_'10.0.34.1',_'10.0    |
2023-11-10T17:07:26: %AETEST-INFO: |                   .14.0',_'10.0.1.1'],source=172.16.20.1]                    |
2023-11-10T17:07:26: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:29: %AETEST-INFO: The result of section verify_traceroute_before[destination=172.16.10.1,device_name=xrd-dest,expected=['10.0.2.0',_'10.0.23.1',_'10.0.34.1',_'10.0.14.0',_'10.0.1.1'],source=172.16.20.1] is => PASSED
2023-11-10T17:07:29: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:29: %AETEST-INFO: |           Starting section configure_sr_policy[device_name=xrd-1]            |
2023-11-10T17:07:29: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:29: %SCRIPT-INFO: Configuring SR Policy
2023-11-10T17:07:29: %NCCLIENT-INFO: [host 172.40.0.101 session-id 833683439] Requesting 'Lock'
2023-11-10T17:07:29: %NCCLIENT-INFO: [host 172.40.0.101 session-id 833683439] Requesting 'EditConfig'
2023-11-10T17:07:30: %NCCLIENT-INFO: [host 172.40.0.101 session-id 833683439] Requesting 'Commit'
2023-11-10T17:07:30: %NCCLIENT-INFO: [host 172.40.0.101 session-id 833683439] Requesting 'Get'
2023-11-10T17:07:30: %NCCLIENT-INFO: [host 172.40.0.101 session-id 833683439] Requesting 'Unlock'
2023-11-10T17:07:30: %AETEST-INFO: The result of section configure_sr_policy[device_name=xrd-1] is => PASSED
2023-11-10T17:07:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:30: %AETEST-INFO: |           Starting section configure_sr_policy[device_name=xrd-2]            |
2023-11-10T17:07:30: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:30: %SCRIPT-INFO: Configuring SR Policy
2023-11-10T17:07:30: %NCCLIENT-INFO: [host 172.40.0.102 session-id 1788082925] Requesting 'Lock'
2023-11-10T17:07:30: %NCCLIENT-INFO: [host 172.40.0.102 session-id 1788082925] Requesting 'EditConfig'
2023-11-10T17:07:31: %NCCLIENT-INFO: [host 172.40.0.102 session-id 1788082925] Requesting 'Commit'
2023-11-10T17:07:31: %NCCLIENT-INFO: [host 172.40.0.102 session-id 1788082925] Requesting 'Get'
2023-11-10T17:07:31: %NCCLIENT-INFO: [host 172.40.0.102 session-id 1788082925] Requesting 'Unlock'
2023-11-10T17:07:31: %AETEST-INFO: The result of section configure_sr_policy[device_name=xrd-2] is => PASSED
2023-11-10T17:07:31: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:31: %AETEST-INFO: |                  Starting section wait_sr_policy_installed                   |
2023-11-10T17:07:31: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:31: %SCRIPT-INFO: Waiting 10 seconds for the SR policy to be installed
2023-11-10T17:07:41: %AETEST-INFO: The result of section wait_sr_policy_installed is => PASSED
2023-11-10T17:07:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:42: %AETEST-INFO: |    Starting section verify_odn_policy[device_name=xrd-1,policy_name=srte_    |
2023-11-10T17:07:42: %AETEST-INFO: |                             c_10_ep_10.10.10.2]                              |
2023-11-10T17:07:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:42: %NCCLIENT-INFO: [host 172.40.0.101 session-id 833683439] Requesting 'Get'
2023-11-10T17:07:42: %AETEST-INFO: Passed reason: ODN policy srte_c_10_ep_10.10.10.2 is operational
2023-11-10T17:07:42: %AETEST-INFO: The result of section verify_odn_policy[device_name=xrd-1,policy_name=srte_c_10_ep_10.10.10.2] is => PASSED
2023-11-10T17:07:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:42: %AETEST-INFO: |    Starting section verify_odn_policy[device_name=xrd-2,policy_name=srte_    |
2023-11-10T17:07:42: %AETEST-INFO: |                             c_10_ep_10.10.10.1]                              |
2023-11-10T17:07:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:42: %NCCLIENT-INFO: [host 172.40.0.102 session-id 1788082925] Requesting 'Get'
2023-11-10T17:07:42: %AETEST-INFO: Passed reason: ODN policy srte_c_10_ep_10.10.10.1 is operational
2023-11-10T17:07:42: %AETEST-INFO: The result of section verify_odn_policy[device_name=xrd-2,policy_name=srte_c_10_ep_10.10.10.1] is => PASSED
2023-11-10T17:07:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:42: %AETEST-INFO: |    Starting section verify_traceroute_after[destination=192.168.20.1,devi    |
2023-11-10T17:07:42: %AETEST-INFO: |    ce_name=xrd-source,expected=['10.0.1.0',_'10.0.14.1',_'10.0.34.0',_'10    |
2023-11-10T17:07:42: %AETEST-INFO: |                  .0.23.0',_'10.0.2.1'],source=192.168.10.1]                  |
2023-11-10T17:07:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:45: %AETEST-INFO: The result of section verify_traceroute_after[destination=192.168.20.1,device_name=xrd-source,expected=['10.0.1.0',_'10.0.14.1',_'10.0.34.0',_'10.0.23.0',_'10.0.2.1'],source=192.168.10.1] is => PASSED
2023-11-10T17:07:45: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:45: %AETEST-INFO: |    Starting section verify_traceroute_after[destination=172.16.20.1,devic    |
2023-11-10T17:07:45: %AETEST-INFO: |    e_name=xrd-source,expected=['10.0.1.0',_'10.0.12.1',_'10.0.2.1'],sourc    |
2023-11-10T17:07:45: %AETEST-INFO: |                                e=172.16.10.1]                                |
2023-11-10T17:07:45: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:49: %AETEST-INFO: The result of section verify_traceroute_after[destination=172.16.20.1,device_name=xrd-source,expected=['10.0.1.0',_'10.0.12.1',_'10.0.2.1'],source=172.16.10.1] is => PASSED
2023-11-10T17:07:49: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:49: %AETEST-INFO: |    Starting section verify_traceroute_after[destination=192.168.10.1,devi    |
2023-11-10T17:07:49: %AETEST-INFO: |    ce_name=xrd-dest,expected=['10.0.2.0',_'10.0.23.1',_'10.0.34.1',_'10.0    |
2023-11-10T17:07:49: %AETEST-INFO: |                   .14.0',_'10.0.1.1'],source=192.168.20.1]                   |
2023-11-10T17:07:49: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:52: %AETEST-INFO: The result of section verify_traceroute_after[destination=192.168.10.1,device_name=xrd-dest,expected=['10.0.2.0',_'10.0.23.1',_'10.0.34.1',_'10.0.14.0',_'10.0.1.1'],source=192.168.20.1] is => PASSED
2023-11-10T17:07:52: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:52: %AETEST-INFO: |    Starting section verify_traceroute_after[destination=172.16.10.1,devic    |
2023-11-10T17:07:52: %AETEST-INFO: |    e_name=xrd-dest,expected=['10.0.2.0',_'10.0.12.0',_'10.0.1.1'],source=    |
2023-11-10T17:07:52: %AETEST-INFO: |                                 172.16.20.1]                                 |
2023-11-10T17:07:52: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:56: %AETEST-INFO: The result of section verify_traceroute_after[destination=172.16.10.1,device_name=xrd-dest,expected=['10.0.2.0',_'10.0.12.0',_'10.0.1.1'],source=172.16.20.1] is => PASSED
2023-11-10T17:07:56: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:56: %AETEST-INFO: |          Starting section rollback_configuration[device_name=xrd-1]          |
2023-11-10T17:07:56: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:56: %SCRIPT-INFO: Rolling back configuration
2023-11-10T17:07:57: %AETEST-INFO: The result of section rollback_configuration[device_name=xrd-1] is => PASSED
2023-11-10T17:07:57: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:57: %AETEST-INFO: |          Starting section rollback_configuration[device_name=xrd-2]          |
2023-11-10T17:07:57: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:57: %SCRIPT-INFO: Rolling back configuration
2023-11-10T17:07:57: %AETEST-INFO: The result of section rollback_configuration[device_name=xrd-2] is => PASSED
2023-11-10T17:07:57: %AETEST-INFO: The result of testcase ODNSRPolicyValidation is => PASSED
2023-11-10T17:07:57: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:57: %AETEST-INFO: |                           Starting common cleanup                            |
2023-11-10T17:07:57: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:57: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:57: %AETEST-INFO: |                        Starting subsection disconnect                        |
2023-11-10T17:07:57: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:57: %SCRIPT-INFO: Disconnecting from devices
2023-11-10T17:07:57: %AETEST-INFO: The result of subsection disconnect is => PASSED
2023-11-10T17:07:57: %AETEST-INFO: The result of common cleanup is => PASSED
2023-11-10T17:07:57: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:57: %AETEST-INFO: |                               Detailed Results                               |
2023-11-10T17:07:57: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:57: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
2023-11-10T17:07:57: %AETEST-INFO: --------------------------------------------------------------------------------
2023-11-10T17:07:57: %AETEST-INFO: .
2023-11-10T17:07:57: %AETEST-INFO: |-- common_setup                                                          PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   `-- connect                                                           PASSED
2023-11-10T17:07:57: %AETEST-INFO: |-- ODNSRPolicyValidation                                                 PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- check_no_policy[device_name=xrd-1]                                PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- check_no_policy[device_name=xrd-2]                                PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- verify_traceroute_before[destination=192.168.20.1,device_na...    PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- verify_traceroute_before[destination=172.16.20.1,device_nam...    PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- verify_traceroute_before[destination=192.168.10.1,device_na...    PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- verify_traceroute_before[destination=172.16.10.1,device_nam...    PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- configure_sr_policy[device_name=xrd-1]                            PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- configure_sr_policy[device_name=xrd-2]                            PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- wait_sr_policy_installed                                          PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- verify_odn_policy[device_name=xrd-1,policy_name=srte_c_10_e...    PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- verify_odn_policy[device_name=xrd-2,policy_name=srte_c_10_e...    PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- verify_traceroute_after[destination=192.168.20.1,device_nam...    PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- verify_traceroute_after[destination=172.16.20.1,device_name...    PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- verify_traceroute_after[destination=192.168.10.1,device_nam...    PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- verify_traceroute_after[destination=172.16.10.1,device_name...    PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   |-- rollback_configuration[device_name=xrd-1]                         PASSED
2023-11-10T17:07:57: %AETEST-INFO: |   `-- rollback_configuration[device_name=xrd-2]                         PASSED
2023-11-10T17:07:57: %AETEST-INFO: `-- common_cleanup                                                        PASSED
2023-11-10T17:07:57: %AETEST-INFO:     `-- disconnect                                                        PASSED
2023-11-10T17:07:57: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:57: %AETEST-INFO: |                                   Summary                                    |
2023-11-10T17:07:57: %AETEST-INFO: +------------------------------------------------------------------------------+
2023-11-10T17:07:57: %AETEST-INFO:  Number of ABORTED                                                            0 
2023-11-10T17:07:57: %AETEST-INFO:  Number of BLOCKED                                                            0 
2023-11-10T17:07:57: %AETEST-INFO:  Number of ERRORED                                                            0 
2023-11-10T17:07:57: %AETEST-INFO:  Number of FAILED                                                             0 
2023-11-10T17:07:57: %AETEST-INFO:  Number of PASSED                                                             3 
2023-11-10T17:07:57: %AETEST-INFO:  Number of PASSX                                                              0 
2023-11-10T17:07:57: %AETEST-INFO:  Number of SKIPPED                                                            0 
2023-11-10T17:07:57: %AETEST-INFO:  Total Number                                                                 3 
2023-11-10T17:07:57: %AETEST-INFO:  Success Rate                                                            100.0% 
2023-11-10T17:07:57: %AETEST-INFO: --------------------------------------------------------------------------------
```

## Reseting the Configuration

It could happen that you configured something you shouldn't. In this case, you can run the script `reset_config.py` at in the root folder of this project. Each device's configuration will be reset to default configuration.

## Segment Routing Policy

In this exercise, we will use an **On-Demand Next-hop (ODN) Segment Routing Policy** to steer traffic from **xrd-source** to **xrd-dest** through a specific path.
By default, the IGP metrics are set so that this traffic is taking the longest path (through **xrd-1**, **xrd-4**, **xrd-3** and **xrd-2**) with supposedly the highest bandwidth.

The ODN policy will be created so that the traffic will take the low latency path (through **xrd-1** and **xrd-2**). In this lab, the delay of each link is statically set to 10 usec.

As ODN is used, the L3VPN prefixes of **xrd-source** and **xrd-dest** will be colored with the color **10** using a route-policy. Only the prefixes in the subnet 172.16.0.0/16 should use the low latency path, therefore the route-policy will color only those prefixes.

## AEtest Goto Statement
When a test section fails, there are situation where the full testcase should be stopped. This can be achieved by using a goto statement.
Goto statement enables early flow termination in case executing the test further would be conditioned by the result of a previous test.
Goto jumps can be invoked as optional arguments to Result APIs. A list of goto must be provided as there can be multiple goto target.
There are four different goto target available:
 - **cleanup**: jumps to the testcase cleanup section, by-passing all other test sections
 - **next_tc**:jumps to the next testcase in line 
 - **common_cleanup**: jumps to the script’s CommonCleanup section. 
 - **exit**: terminates the testscript immediately without going further.
	
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
    # test failed, move onto next testcase
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

## NETCONF RPC

NETCONF use SSH as transport to send request to the device. Those request are formatted in XML. There are many ways to generate XML NETCONF RPC, one of them is using YANGSuite. 
YANGSuite is a tool that can be used to explore YANG models and generate XML NETCONF RPC. Refer to the documentation below for more information.

>https://developer.cisco.com/yangsuite/

Another option is using the pyang command line utility.

>https://github.com/mbj4668/pyang

For this exercise, you can either try building your own XML NETCONF RPC or use the one provided in the `solution_example/netconf` folder. Some of them requires arguments that needs to be provided using the python string method `.format(argument="myarg")`.

Working with NETCONF means handling a lot of XML, there are many python libraries to deal with XML format. `xmltodict` is one of them. Refer to the documentation below for more information.

>https://github.com/martinblech/xmltodict

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

For this exercise, we will connect to **xrd-1**, **xrd-2**, **xrd-source** and **xrd-dest** using the `netconf` method, you can check the testbed to see how this connection is defined.

Refer to the documentation below for more information.

> https://pubhub.devnetcloud.com/media/pyats/docs/topology/usage.html#connect-to-all-devices

### Step 1 - Initial Verification Testcase

In this step, we will verify that the lab is in the correct initial conditions before we start the test.
The `must_pass` variable is set to `True` in the Testcase class. It ensures that the testscript will fail and return if one of the test section fails.
More information is available in the documentation below.

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/control.html#requisite-testcase

There should be not SR policy configured and the forwarding should follow the longest path through **xrd-4** and **xrd-3**
In the previous exercise only the path from **xrd-source** to **xrd-dest** was checked. In this second version, the path from **xrd-dest** to **xrd-source** will also be checked.

Traceroute will be used to check the forwarding path. On **xrd-source** the following traceroute will be executed:
- from `192.168.10.1` to `192.168.20.1`
- from `172.168.10.1` to `172.168.20.1`

On **xrd-dest** the following traceroute will be executed:
- from `192.168.20.1` to `192.168.10.1`
- from `172.168.20.1` to `172.168.10.1`

#### Step 1.0 - Verify no SR policy is configured

##### Step 1.0.0 - Loop the test section to have it executed on **xrd-1** and **xrd-2**

It is expected that you run the same test section on both device, **xrd-1** and **xrd-2** using an `aetest.loop`

##### Step 1.0.1 - Verify that not SR policy is configured on the device

Verify that not SR policy is configured on the `xrd-1` and `xrd-2`. Use the YANG model **Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policy-summary** that provide the `total-policy-count`.
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

If this test section fails, you should stop the execution of the testcase. You can use the `goto` argument of the `failed()` method to do so, as no change was done to the testbed the goto target should be `next_tc`.

#### Step 1.1 - Verify the forwarding path

Now we will verify the forwarding path from **xrd-source** to **xrd-dest** and from **xrd-dest** to **xrd-source**

Two traceroutes will be run on `xrd-source`:
- from `192.168.10.1` to `192.168.20.1`: which would be the equivalent of `traceroute 192.168.20.1 source 192.168.10.1`,
- from `172.16.10.1` to `172.16.20.1`: which would be the equivalent of `traceroute 172.16.10.1 source 172.16.20.1`.

In both cases, the expected hops are: `10.0.1.0, 10.0.14.1, 10.0.34.0, 10.0.23.0, 10.0.2.1`.

Two traceroutes will be run on `xrd-dest`:
- from `192.168.20.1` to `192.168.10.1`: which would be the equivalent of `traceroute 192.168.10.1 source 192.168.20.1`,
- from `172.16.20.1` to `172.16.10.1`: which would be the equivalent of `traceroute 172.16.10.1 source 172.16.20.1`.

In both cases, the expected hops are: `10.0.2.0, 10.0.23.1, 10.0.34.1, 10.0.14.0, 10.0.1.1`

##### Step 1.1.0 - Loop the test section to have it executed for each pair of source and destination prefixes

The test section `verify_traceroute` should be executed four times, once for each pair of source and destination prefixes on both **xrd-source** and **xrd-dest**. You can use an `aetest.loop` to do so.
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

A traceroute can be executing using NETCONF with the following YANG model **Cisco-IOS-XR-traceroute-act**.
The inputs parameters are the following, only the `destination` argument is mandatory, but in our case the `source` must also be specified.
```
pyang -f tree Cisco-IOS-XR-traceroute-act.yang --tree-path traceroute/input/ipv4
module: Cisco-IOS-XR-traceroute-act

  rpcs:
    +---x traceroute
       +---w input
          +---w ipv4!
             +---w destination    string
             +---w source?        string
             +---w timeout?       uint32
             +---w probe?         uint16
             +---w numeric?       boolean
             +---w vrf-name?      string
             +---w min-ttl?       uint16
             +---w max-ttl?       uint16
             +---w port?          uint32
             +---w verbose?       boolean
```
The output looks like this:
```
pyang -f tree Cisco-IOS-XR-traceroute-act.yang --tree-path traceroute/output/traceroute-response/ipv4
module: Cisco-IOS-XR-traceroute-act

  rpcs:
    +---x traceroute
       +--ro output
          +--ro traceroute-response
             +--ro ipv4!
                +--ro destination?      string
                +--ro hops
                |  +--ro hop* [hop-index]
                |     +--ro hop-index       uint32
                |     +--ro hop-address?    string
                |     +--ro hop-hostname?   string
                |     +--ro probes
                |        +--ro probe* [probe-index]
                |           +--ro probe-index     uint32
                |           +--ro result?         string
                |           +--ro delta-time?     uint32
                |           +--ro hop-address?    string
                |           +--ro hop-hostname?   string
                |           +--ro srv6-header
                |              +--ro destination-address?   uint32
                |              +--ro segments-left?         uint32
                |              +--ro segments
                |                 +--ro segment*   string
                +--ro verbose-output?   string
```

Execute traceroutes on **xrd-source** and **xrd-dest** and verify that the hops are as expected. Two list can easily be compared in python by using the `==` operator.

```python
['a','b','c'] == ['a','b','c'] # Return True
['a','b','c'] == ['a','b','d'] # Return False
```

To execute a raw RPC using NETCONF, the `device.netconf.request()` method is used. Below is an example on how to do a ping using NETCONF and the **Cisco-IOS-XR-ping-act** model.
The raw reply is return as string when using this method.

```python
xml_query='''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101">
  <ping xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ping-act">
    <ipv4>
      <destination>10.10.10.1</destination>
    </ipv4>
  </ping>
</rpc>
'''
test = device.netconf.request(xml_query)
```

If this test section fails, you should stop the execution of the testcase. You can use the `goto` argument of the `failed()` method to do so, as no change was done to the testbed the goto target should be `next_tc`.

### Step 2 - Configure the SR Policy

The same Segment Routing ODN configuration will be applied on both **xrd-1** and **xrd-2**. This configuration will mark the prefixes in `172.16.0.0/16` subnet with the color `10`.
The color `10` is using the low latency (`xrd-1` -> `xrd-2`) path.

#### Step 2.0 - Configure the SR Policy on **xrd-1** and **xrd-2**

The Segment Routing policy configuration in the XML format is provided in the `solution_example/netconf/configure_sr_policy.xml` file. It contains the SR-TE on-demand config as well as the route-policy used to color the prefixes.

##### Step 2.0.0 - Loop the test section to have it executed on **xrd-1** and **xrd-2**

Using an `aetest.loop()` send the configuration on both **xrd-1** and **xrd-2**.

##### Step 2.0.1 - Configure the SR Policy

Using the `edit-config` NETCONF method send the configuration of the `sr_policy_config.txt` file to the device.

You can open and read the content of a file by using the below code. `file_content` will be a `str` containing the content of our file.

```python
with open('/path/to/file') as file:
    file_content = file.read()
```

To configure a device using NETCONF use the `edit_config()` method. There are two arguments:
- `target` - on which datastore to apply the config. On IOS XR, the candidate datastore must be used. The configuration is not applied to the device until a `device.netconf.commit()` is run.
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

#### Step 2.1 - Wait for the SR policy to be installed

This test section is just there to wait 10 seconds for the SR policy to be installed.
It is an easy way to ensure that the SR policy will have time to be installed before we verify the forwarding path.

You can use the `time.sleep()` method to pause the execution for 10 seconds. Don't forget to `import time` to be able to use it.

#### Step 2.2 - Verify the SR policy is installed

If the on-demand policies have been correctly configured, we should see a policy installed on **xrd-1** toward **xrd-2** and the same reverse policy on **xrd-2** toward **xrd-1**.
This can be verified with the YANG model **Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policies**. In our case the `policy_name` will be:

- `srte_c_10_ep_10.10.10.2` for the policy installed on **xrd-1**,
- `srte_c_10_ep_10.10.10.1` for the policy installed on **xrd-2**.

Those names are deterministic and can be easily computed from the configuration. Indeed, they have the following format: `srte_c_<color>_ep_<endpoint_ip>`.

##### Step 2.2.0 - Loop the test section to have it executed on **xrd-1** and **xrd-2**

Loop the `verify_odn_policy` test section to have it executed on both **xrd-1** and **xrd-2** and check the policy have been correctly installed.

##### Step 2.2.1 - Verify the policy is installed

Using the NETCONF `get` method with the `subtree` option, get a filtered data of the model **Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policies** for the policy name passed as an argument.
Verify that the status of the policy is UP with the attribute `operational-up` attribute. The model **Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policies** is provided below.

```
pyang -f tree Cisco-IOS-XR-infra-xtc-agent-oper.yang --tree-path xtc/policies/policy --tree-depth 4
module: Cisco-IOS-XR-infra-xtc-agent-oper
  +--ro xtc
     +--ro policies
        +--ro policy* [id]
           +--ro id                                    uint32
           +--ro destination-address
           |     ...
           +--ro binding-sid
           |     ...
           +--ro per-flow
           |     ...
           +--ro last-notify
           |     ...
           +--ro policy-name?                          string
           +--ro administrative-up?                    uint32
           +--ro operational-up?                       uint32
           +--ro color?                                uint32
           +--ro transition-count?                     uint32
           +--ro created-ls-ps-count?                  uint32
           +--ro completed-reoptimizations-count?      uint32
           +--ro forward-class?                        uint32
           +--ro up-time?                              uint64
           +--ro up-age?                               uint64
           +--ro down-time?                            uint64
           +--ro down-age?                             uint64
           +--ro steering-bgp-disabled?                boolean
           +--ro steering-labeled-services-disabled?   boolean
           +--ro invalidation-drop-enabled?            boolean
           +--ro invalidated-traffic-dropping?         boolean
           +--ro interface-handle?                     uint32
           +--ro profile-id?                           uint16
           +--ro ipv6-caps-enabled?                    boolean
           +--ro max-install-standby-cpaths?           uint32
           +--ro candidate-path* []
           |     ...
           +--ro ls-ps* []
                 ...
``` 

If this test section fails, you should stop the execution of the testcase. You can use the `goto` argument of the `failed()` method to do so, this time because configuration may have been done on the devices, the goto target must be `cleanup` to ensure that we go through the cleanup section.


### Step 3 - Verify the forwarding after the policy is installed

Once the policy is installed, the forwarding for the prefixes in `172.16.0.0/16` should be different.
In this section we will verify that the forwarding has indeed changed for the prefix `172.16.20.1` and `172.16.10.1` but that it is unchanged for the prefix `192.168.20.1` and `192.168.10.1`.

On **xrd-source** the expected hops in the traceroute are the following:

- from `192.168.10.1` to `192.168.20.1`: `10.0.1.0, 10.0.14.1, 10.0.34.0, 10.0.23.0, 10.0.2.1`
- from `172.16.10.1` to `172.16.20.1` : `10.0.1.0, 10.0.12.1, 10.0.2.1`

On **xrd-dest** the expected hops in the traceroute are the following:
- from `192.168.20.1` to `192.168.10.1`: `10.0.2.0, 10.0.23.1, 10.0.34.1, 10.0.14.0, 10.0.1.1`
- from `172.16.20.1` to `172.16.10.1`: `10.0.2.0, 10.0.12.0 , 10.0.1.1`

This testcase is very similar to the one in Step 1, and it should be pretty much the same code.

#### Step 3.0 - Loop the test section to have it executed for both prefixes

The test section `verify_traceroute` should be executed four times, once for each pair of source and destination prefixes on both **xrd-source** and **xrd-dest**. You can use an `aetest.loop` to do so.

#### Step 3.1 - Verify the traceroute path

Using NETCONF execute a traceroute with the following YANG model **Cisco-IOS-XR-traceroute-act**.
Execute traceroutes on **xrd-source** and **xrd-dest** and verify that the hops are as expected. Two list can easily be compared in python by using the `==` operator.

### Step 4 - Clean configuration

The `aetest.cleanup` test section is used to revert the lab to its original state.
In our case, we will rollback the configuration to leave the lab in the original state.

The configuration can be rollback using the YANG model **Cisco-IOS-XR-cfgmgr-rollback-act**.

##### Step 4.0.0 - Loop the test section to have it executed for both **xrd-1** and **xrd-2**

This test section should be done for both **xrd-1** and **xrd-2**, use the `aetest.loop` decorator.

##### Step 4.0.1 - Rollback the configuration

Note that this section will always be executed even if no configuration have been done. Therefore, it is important to check that the configuration have indeed been done before running it.
You must modify the `configure_sr_policy` section to retrieve the commit id of the configuration that was done and set it to a variable.

A new variable can be set on the device object and later checked.

```python

def test_section_a(device):
    device.custom_variable = True

def test_section_b(device):
    if getattr(device, 'custom_variable', None):
        # do something
        pass
```

The `getattr()` method returns the value of the named attribute of an object. If not found, it returns the default value provided to the function. Here, it would check if the device has `custom_variable` attribute and return its value. If the device doesn't have the attribute, it would return `None`.

More information about `getattr()`in the documentation below:

>  https://docs.python.org/3/library/functions.html#getattr

We can use the `self.skipped()` result of an aetest section to mark this test section as skipped if it was not executed.

```python
def rollback(device):
    self.skipped("No configuration to rollback")
```


The last commit id can be retrieved using the **Cisco-IOS-XR-config-cfgmgr-exec-oper** YANG model:
```
pyang -f tree Cisco-IOS-XR-config-cfgmgr-exec* --tree-path config-manager/global/config-commit
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
Once the last commit id is retrieve, the rollback can be done using a NETCONF `request()` on the following model:
```
pyang -f tree Cisco-IOS-XR-cfgmgr-rollback-act.yang --tree-path roll-back-configuration
module: Cisco-IOS-XR-cfgmgr-rollback-act

  rpcs:
    +---x roll-back-configuration
       +---w input
          +---w commit-id      string
          +---w force?         boolean
          +---w best-effort?   boolean
          +---w label?         string
          +---w comment?       string
```


#### Step 5 - Disconnect from the devices

As for the `testbed.connect()` method, there is a `testbed.disconnect()` method that can be used to disconnect simultaneously from multiple devices and without doing a `for` loop

Use this method to disconnect from the four devices. Below is an example, for the devices `uut` and `helper`.

```python
testbed.disconnect(testbed.devices['uut'],
                   testbed.devices['helper'])
```
