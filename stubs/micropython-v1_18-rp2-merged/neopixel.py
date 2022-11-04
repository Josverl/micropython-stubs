"""
control of WS2812 / NeoPixel LEDs. See: https://docs.micropython.org/en/v1.18/library/neopixel.html

This module provides a driver for WS2818 / NeoPixel LEDs.

``Note:`` This module is only included by default on the ESP8266 and ESP32
   ports. On STM32 / Pyboard, you can `download the module
   <https://github.com/micropython/micropython/blob/master/drivers/neopixel/neopixel.py>`_
   and copy it to the filesystem.
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.18.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2', 'ver': 'v1.18', 'release': '1.18.0'}
# Stubber: 1.5.3
from typing import Any


def bitstream(*args, **kwargs) -> Any:
    ...


class NeoPixel:
    """
    Construct an NeoPixel object.  The parameters are:

        - *pin* is a machine.Pin instance.
        - *n* is the number of LEDs in the strip.
        - *bpp* is 3 for RGB LEDs, and 4 for RGBW LEDs.
        - *timing* is 0 for 400KHz, and 1 for 800kHz LEDs (most are 800kHz).
    """

    def __init__(self, pin, n, *, bpp=3, timing=1) -> None:
        """"""
        ...

    def write(self) -> None:
        """
        Writes the current pixel data to the strip.
        """
        ...

    def fill(self, pixel) -> None:
        """
        Sets the value of all pixels to the specified *pixel* value (i.e. an
        RGB/RGBW tuple).
        """
        ...

    ORDER = ()  # type: tuple
