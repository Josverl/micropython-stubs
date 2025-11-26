# LOLIN S2 MINI MicroPython Helper Library

from micropython import const
from machine import Pin

# Pin Assignments

# SPI
SPI_MOSI = 11
SPI_MISO = 9
SPI_CLK = 7

# I2C
I2C_SDA = 33
I2C_SCL = 35

# DAC
DAC1 = 17
DAC2 = 18

# LED
LED = 15

# BUTTON
BUTTON = 0

# Helper methods for built in sensors

led = Pin(LED, Pin.OUT, value=0)

button = Pin(BUTTON, Pin.IN, Pin.PULL_UP)
