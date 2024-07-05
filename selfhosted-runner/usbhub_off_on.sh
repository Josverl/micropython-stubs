#!/bin/bash
# reset the power to the USB hub 
mpremote connect /dev/ttyRELAY exec "import time; relay[0].off(); time.sleep(1);relay[0].on();"
# mpremote connect /dev/serial/by-path/pci-0000:00:14.0-usb-0:2:1.0 exec "relais[0].off()"