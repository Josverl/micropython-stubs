# board : ESP32
# ref : https://docs.micropython.org/en/latest/esp32/quickref.html
import utime as time

import machine

machine.freq()  # get the current frequency of the CPU
machine.freq(240000000)  # set the CPU frequency to 240 MHz


# Pins and GPIO
# Use the machine.Pin class:

from machine import Pin

p0 = Pin(0, Pin.OUT)  # create output pin on GPIO0
p0.on()  # set pin to "on" (high) level
p0.off()  # set pin to "off" (low) level
p0.value(1)  # set pin to on/high

p2 = Pin(2, Pin.IN)  # create input pin on GPIO2
print(p2.value())  # get value, 0 or 1

p4 = Pin(4, Pin.IN, Pin.PULL_UP)  # enable internal pull-up resistor
p5 = Pin(5, Pin.OUT, value=1)  # set pin high on creation

# UART (serial bus)
# See machine.UART.

from machine import UART

uart1 = UART(1, baudrate=9600, tx=33, rx=32)
uart1.write("hello")  # write 5 bytes
uart1.read(5)  # read up to 5 bytes


# Software SPI bus


from machine import Pin, SoftSPI

# construct a SoftSPI bus on the given pins
# polarity is the idle state of SCK
# phase=0 means sample on the first edge of SCK, phase=1 means the second
spi = SoftSPI(baudrate=100000, polarity=1, phase=0, sck=Pin(0), mosi=Pin(2), miso=Pin(4))

spi.init(baudrate=200000)  # set the baudrate

spi.read(10)  # read 10 bytes on MISO
spi.read(10, 0xFF)  # read 10 bytes while outputting 0xff on MOSI

buf = bytearray(50)  # create a buffer
spi.readinto(buf)  # read into the given buffer (reads 50 bytes in this case)
spi.readinto(buf, 0xFF)  # read into the given buffer and output 0xff on MOSI

spi.write(b"12345")  # write 5 bytes on MOSI

buf = bytearray(4)  # create a buffer
spi.write_readinto(b"1234", buf)  # write to MOSI and read from MISO into the buffer
spi.write_readinto(buf, buf)  # write buf to MOSI and read MISO back into buf

# Hardware SPI
from machine import Pin, SPI

hspi = SPI(1, 10000000)
hspi = SPI(1, 10000000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
vspi = SPI(2, baudrate=80000000, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))


# Software I2C

from machine import Pin, SoftI2C

i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=100000)

i2c.scan()  # scan for devices

i2c.readfrom(0x3A, 4)  # read 4 bytes from device with address 0x3a
i2c.writeto(0x3A, "12")  # write '12' to device with address 0x3a

buf = bytearray(10)  # create a buffer with 10 bytes


# Hardware I2C bus

from machine import Pin, I2C

i2c = I2C(0)
i2c = I2C(1, scl=Pin(5), sda=Pin(4), freq=400000)





# WDT (Watchdog timer)

from machine import WDT

# enable the WDT with a timeout of 5s (1s is the minimum)
wdt = WDT(timeout=5000)
wdt.feed()




