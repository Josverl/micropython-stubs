# LOLIN S2 PICO MicroPython Helper Library

from micropython import const
from machine import Pin, I2C, Signal
from s2pico_oled import OLED

# Pin Assignments

# SPI
SPI_MOSI = 35
SPI_MISO = 36
SPI_CLK = 37

# I2C
I2C_SDA = 8
I2C_SCL = 9

# DAC
DAC1 = 17
DAC2 = 18

# LED
LED = 10

# OLED
OLED_RST = 18

# BUTTON
BUTTON = 0

# Helper methods for built in sensors

led = Signal(LED, Pin.OUT, value=0, invert=True)

button = Pin(BUTTON, Pin.IN, Pin.PULL_UP)

i2c = I2C(0)
oled = OLED(i2c, Pin(OLED_RST))
