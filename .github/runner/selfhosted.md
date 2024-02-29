

# Self hosted runner un linux

# install tools 


## pipx 
```bash
sudo apt update
# pipx
sudo apt install pipx
pipx ensurepath
``` 

# install 
https://docs.github.com/en/actions/hosting-your-own-runners

- Install self hosted runner 
- Configure environment 
> `.../actions_runner/.env`
```
# Add 
LANG=en_US.UTF-8
AGENT_TOOLSDIRECTORY=/home/jos/actions-runner/_tools
```
- [check if additional permissions are needed](https://github.com/actions/setup-python/blob/main/docs/advanced-usage.md#linux)
- testrun 
- configure to run as a service 
- start service 


# esp8266 devices not recognized 
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
