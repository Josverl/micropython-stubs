# Self hosted runner on linux X64 / ARM64

This is a guide to setup a self hosted runner on a linux X64 / ARM64 machine. 
The guide is based on the [official documentation](https://docs.github.com/en/actions/hosting-your-own-runners) 
and my own experience setting up a runner on a Raspberry Pi 4 and x64 using Ubuntu 22.04.


## create a seperate user for the runner
Create a user `runner` that is member of the dialout and sudo groups
```bash

# create user
sudo useradd -m -s /bin/bash runner
# add to dialout group
sudo usermod -a -G dialout runner
# add to sudo group
sudo usermod -a -G sudo runner
# change to user
su - runner
```

## Install tools 
### pipx 
```bash
sudo apt update
# pipx
sudo apt install pipx -y
pipx ensurepath
```

### Remove conflicting packages
```bash
# remove braille support as it conflicts with esp8266
sudo apt remove brltty
``` 

### Install Github Actions runner
This installs the runner in the home directory of the runner user.
In this example a runner with `Repository` scope  is created. 

- Install self hosted runner 
- Configure environment 
> `.../actions_runner/.env`
```
LANG=en_US.UTF-8 
# Below is used by actions/setup-python to install python
AGENT_TOOLSDIRECTORY=/home/runner/actions-runner/_tools
```
- testrun  
    `./run.sh`
- configure to run as a service  
    `sudo ./svc.sh install`

- start service  
  `sudo ./svc.sh start`
   ref: https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/configuring-the-self-hosted-runner-application-as-a-service#installing-the-service


https://docs.github.com/en/actions/hosting-your-own-runners
[check if additional permissions are needed](https://github.com/actions/setup-python/blob/main/docs/advanced-usage.md#linux)


# known issues

### actions/setup-python does not support linux-arm64
The `actions/setup-python` action does not support installing/configuring Python on linux-arm64.

The workaround is to use the `deadsnakes/action` action to install python.
https://github.com/deadsnakes/action?tab=readme-ov-file#deadsnakesaction

see:  https://github.com/temporalio/sdk-python/pull/172/files#diff-e0c5149ab771083cacddbeaf3336656118f582f6311228e0b8652c3209a7dd2eR32-R39


```yaml


### esp8266 devices not recognized 
By default the brltty service is running and it blocks the usb port used by an esp8266.

the below log shows the service blocking the port
```bash
$ sudo dmesg | tail
[981998.822746] usb 1-2.1.1: new full-speed USB device number 67 using xhci_hcd
[981998.924954] usb 1-2.1.1: New USB device found, idVendor=1a86, idProduct=7523, bcdDevice= 2.64
[981998.924971] usb 1-2.1.1: New USB device strings: Mfr=0, Product=2, SerialNumber=0
[981998.924978] usb 1-2.1.1: Product: USB Serial
[981998.928861] ch341 1-2.1.1:1.0: ch341-uart converter detected
[981998.929906] usb 1-2.1.1: ch341-uart converter now attached to ttyUSB0
[981999.500370] input: BRLTTY 6.4 Linux Screen Driver Keyboard as /devices/virtual/input/input49
[981999.503750] usb 1-2.1.1: usbfs: interface 0 claimed by ch341 while 'brltty' sets config #1
[981999.504577] ch341-uart ttyUSB0: ch341-uart convert
``` 

You should remove the service with the following command
```
sudo apt remove brltty
```
Test by connecting an esp8266 and checking visibility using `mpremote devs`

```bash	
$ sudo dmesg | tail
[981999.503750] usb 1-2.1.1: usbfs: interface 0 claimed by ch341 while 'brltty' sets config #1
[981999.504577] ch341-uart ttyUSB0: ch341-uart converter now disconnected from ttyUSB0
[981999.504650] ch341 1-2.1.1:1.0: device disconnected
[982067.295761] usb 1-2.1.1: USB disconnect, device number 67
[982068.985562] usb 1-2.1.1: new full-speed USB device number 68 using xhci_hcd
[982069.087315] usb 1-2.1.1: New USB device found, idVendor=1a86, idProduct=7523, bcdDevice= 2.64
[982069.087323] usb 1-2.1.1: New USB device strings: Mfr=0, Product=2, SerialNumber=0
[982069.087326] usb 1-2.1.1: Product: USB Serial
[982069.088862] ch341 1-2.1.1:1.0: ch341-uart converter detected
[982069.089422] usb 1-2.1.1: ch341-uart converter now attached to ttyUSB0

$ mpremote devs
/dev/ttyUSB0 None 1a86:7523 None USB Serial
```	
also see: https://stackoverflow.com/questions/70123431/why-would-ch341-uart-is-disconnected-from-ttyusb
