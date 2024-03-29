# LOLIN C3 MINI MicroPython Helper Library

from micropython import const
from machine import Pin

# Pin Assignments

# SPI
SPI_MOSI = 4
SPI_MISO = 3
SPI_CLK = 2

# I2C
I2C_SDA = 8
I2C_SCL = 10

# LED
LED = 7

# BUTTON
BUTTON = 0

# Built-in peripherals

led = Pin(LED, Pin.OUT, value=0)
button = Pin(BUTTON, Pin.IN, Pin.PULL_UP)
