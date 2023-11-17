# ref: https://docs.micropython.org/en/latest/esp8266/quickref.html
# The machine module:

import machine

freq = machine.freq()  # get the current frequency of the CPU
machine.freq(160000000)  # set the CPU frequency to 160 MHz


# --------------------------------------------------------------------
import dht
import machine

d = dht.DHT11(machine.Pin(4))
d.measure()
d.temperature()  # eg. 23 (°C)
d.humidity()  # eg. 41 (% RH)

d = dht.DHT22(machine.Pin(4))
d.measure()
d.temperature()  # eg. 23.6 (°C)
d.humidity()  # eg. 41.3 (% RH)

# --------------------------------------------------------------------
#  I2C

from machine import Pin, I2C

# construct an I2C bus
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

i2c.readfrom(0x3A, 4)  # read 4 bytes from peripheral device with address 0x3a
i2c.writeto(0x3A, "12")  # write '12' to peripheral device with address 0x3a

buf = bytearray(10)  # create a buffer with 10 bytes
i2c.writeto(0x3A, buf)  # write the given buffer to the peripheral


# --------------------------------------------------------------------
from machine import WDT

# enable the WDT
wdt = WDT()
wdt.feed()

# --------------------------------------------------------------------

# --------------------------------------------------------------------

# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
