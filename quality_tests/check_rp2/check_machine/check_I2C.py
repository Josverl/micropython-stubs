# Software I2C

from machine import Pin, SoftI2C

i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=100_000)

i2c.scan()  # scan for devices

i2c.readfrom(0x3A, 4)  # read 4 bytes from device with address 0x3a
i2c.writeto(0x3A, "12")  # write '12' to device with address 0x3a

buf = bytearray(10)  # create a buffer with 10 bytes
i2c.writeto(0x3A, buf)  # write the given buffer to the peripheral

# Hardware I2C
from machine import Pin, I2C

i2c = I2C(0)  # default assignment: scl=Pin(9), sda=Pin(8)
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400_000)