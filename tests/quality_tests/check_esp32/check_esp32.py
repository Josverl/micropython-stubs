# The esp32 module:
import esp32

# esp32.hall_sensor()  # read the internal hall sensor
# Hal sensor (magnetometer) has been removed
# https://github.com/micropython/micropython/pull/11528

esp32.raw_temperature()  # read the internal temperature of the MCU, in Fahrenheit
esp32.ULP()  # access to the Ultra-Low-Power Co-processor


# RMT

from machine import Pin

import esp32

rmt = esp32.RMT(0, pin=Pin(18), clock_div=8)
print(rmt)
# # RMT(channel=0, pin=18, source_freq=80000000, clock_div=8)
# The channel resolution is 100ns (1/(source_freq/clock_div)).
rmt.write_pulses((1, 20, 2, 40), 0)  # Send 0 for 100ns, 1 for 2000ns, 0 for 200ns, 1 for 4000ns


## esp32/modules/flashbdev.py

from esp32 import Partition

# MicroPython's partition table uses "vfs", TinyUF2 uses "ffat".
bdev = Partition.find(Partition.TYPE_DATA, label="vfs")
if not bdev:
    bdev = Partition.find(Partition.TYPE_DATA, label="ffat")
bdev = bdev[0] if bdev else None
