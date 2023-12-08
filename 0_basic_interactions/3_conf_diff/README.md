# 3. Diff between two config files

In this fourth exercise, we will :

0. Connect to `xrd-1`,
1. Parse `xrd-1` BGP's configuration,
2. Compare it with the expected BGP configuration,
3. Print the differences between the two.

## Output example

```
2023-10-31T16:16:36: %SCRIPT-INFO:  router bgp 65000:
2023-10-31T16:16:36: %SCRIPT-INFO:   vrf A:
2023-10-31T16:16:36: %SCRIPT-INFO:    address-family ipv4 unicast:
2023-10-31T16:16:36: %SCRIPT-INFO: +   redistribute ospf A route-policy IMPORT_A:
2023-10-31T16:16:36: %SCRIPT-INFO: -   redistribute ospf A route-policy IMPORT_B:
2023-10-31T16:16:36: %SCRIPT-INFO: + bgp router-id 10.[3_conf_diff.py](solution_example%2F3_conf_diff.py)10.10.1:
2023-10-31T16:16:36: %SCRIPT-INFO: - bgp router-id 10.10.10.2:
2023-10-31T16:16:36: %SCRIPT-INFO: + neighbor 10.10.10.2:
2023-10-31T16:16:36: %SCRIPT-INFO: +  address-family vpnv4 unicast:
2023-10-31T16:16:36: %SCRIPT-INFO: +  remote-as 65000:
2023-10-31T16:16:36: %SCRIPT-INFO: +  update-source Loopback0:
2023-10-31T16:16:36: %SCRIPT-INFO: - neighbor 10.10.10.4:
2023-10-31T16:16:36: %SCRIPT-INFO: -  address-family vpnv4 unicast:
2023-10-31T16:16:36: %SCRIPT-INFO: -  remote-as 65000:
2023-10-31T16:16:36: %SCRIPT-INFO: -  update-source Loopback0:
```

## Folders

The file with the exercise is in the `exercise` folder. An example of solution can be found in the `solution_example` folder.

## Steps

In this exercise, we will:

1. Convert the `expected_conf_str` to a Genie `Config` object. This configuration has been changed on purpose to be different from the one on `xrd-1`. You can change it later if you want.
2. Execute the `show running config router bgp` on `xrd-1` and convert it to a Genie `Config` object
3. Compare the `expected_conf` and the configuration we received from the device using the Genie `Diff` module.

The `Diff` module cannot compare two `str` objects, it only compares `dict` objects. If you try, it will return a `TypeError` like below. That's why we first need to convert the `str `objects to a Genie `Config` objects which helps to convert a device config to a `dict` object.

```
TypeError: Type <class 'str'> is not supported
```

### Step 0 - Convert the `expected_conf_str` to a `Config` object

The `expected_conf_str` is the expected BGP configuration. Do not change it and do not change the indentation.

First, we need to convert the `expected_conf_str` (which is type `str`) to a `Config` object. You can refer to the documentation below.

> https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#config

### Step 1 - Load the testbed and connect to `xrd-1`

Load the testbed in the current folder and connect to `xrd-1`. You can refer to the previous exercises if you don't remember how to do it.

### Step 2 - Get the `show running config router bgp` output and convert it to a `Config` object

Get the `show running config router bgp` output from `xrd-1` and convert it to a `Config` object.

Refer to the previous exercises and to `Step 0` to do it.

### Step 3 - Use the `Diff` module to print the differences between the two configurations

Use the `Diff` module to get the differences between the two configurations. You can refer to the below documentation.

> https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#diff

Now, print the output in the terminal. It if works, feel free to adapt the `expected_conf_str` to whatever you like.

### Step 4 - Disconnect from `xrd-1`

Don't forget to disconnect from `xrd-1`.
