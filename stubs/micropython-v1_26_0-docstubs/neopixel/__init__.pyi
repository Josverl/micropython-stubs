"""
Control of WS2812 / NeoPixel LEDs.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/neopixel.html

This module provides a driver for WS2818 / NeoPixel LEDs.

``Note:`` This module is only included by default on the ESP8266, ESP32 and RP2
   ports. On STM32 / Pyboard and others, you can either install the
   ``neopixel`` package using :term:`mip`, or you can download the module
   directly from :term:`micropython-lib` and copy it to the filesystem.
"""

# source version: v1.26.0
# origin module:: repos/micropython/docs/library/neopixel.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing import Tuple
from typing_extensions import TypeVar, TypeAlias, Awaitable
from _mpy_shed import _NeoPixelBase
from machine import Pin

_Color: TypeAlias = tuple[int, int, int] | tuple[int, int, int, int]

class NeoPixel(_NeoPixelBase):
    """
    This class stores pixel data for a WS2812 LED strip connected to a pin. The
    application should set pixel data and then call :meth:`NeoPixel.write`
    when it is ready to update the strip.

    For example::

        import neopixel

        # 32 LED strip connected to X8.
        p = machine.Pin.board.X8
        n = neopixel.NeoPixel(p, 32)

        # Draw a red gradient.
        for i in range(32):
            n[i] = (i * 8, 0, 0)

        # Update the strip.
        n.write()
    """

    def __init__(self, pin: Pin, n: int, /, *, bpp: int = 3, timing: int = 1) -> None:
        """
        Construct an NeoPixel object.  The parameters are:

            - *pin* is a machine.Pin instance.
            - *n* is the number of LEDs in the strip.
            - *bpp* is 3 for RGB LEDs, and 4 for RGBW LEDs.
            - *timing* is 0 for 400KHz, and 1 for 800kHz LEDs (most are 800kHz).
        """

    def fill(self, pixel: _Color, /) -> None:
        """
        Sets the value of all pixels to the specified *pixel* value (i.e. an
        RGB/RGBW tuple).
        """
        ...

    def __len__(self) -> int:
        """
        Returns the number of LEDs in the strip.
        """
        ...

    def __setitem__(self, index: int, val: _Color, /) -> None:
        """
        Set the pixel at *index* to the value, which is an RGB/RGBW tuple.
        """
        ...

    def __getitem__(self, index: int, /) -> Tuple:
        """
        Returns the pixel at *index* as an RGB/RGBW tuple.
        """
        ...

    def write(self) -> None:
        """
        Writes the current pixel data to the strip.
        """
        ...
