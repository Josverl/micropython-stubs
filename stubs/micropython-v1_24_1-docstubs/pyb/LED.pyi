""" """

from __future__ import annotations

from array import array
from typing import overload

from Accel import *
from ADC import *
from CAN import *
from DAC import *
from ExtInt import *
from Flash import *
from I2C import *
from LCD import *
from LED import *
from Pin import *
from RTC import *
from Servo import *
from SPI import *
from Switch import *
from Timer import *
from UART import *
from USB_HID import *
from USB_VCP import *

class LED:
    """
    The LED object controls an individual LED (Light Emitting Diode).
    """

    def __init__(self, id: int, /) -> None:
        """
        Create an LED object associated with the given LED:

          - ``id`` is the LED number, 1-4.
        """

    @overload
    def intensity(self) -> int:
        """
        Get or set the LED intensity.  Intensity ranges between 0 (off) and 255 (full on).
        If no argument is given, return the LED intensity.
        If an argument is given, set the LED intensity and return ``None``.

        *Note:* Only LED(3) and LED(4) can have a smoothly varying intensity, and
        they use timer PWM to implement it.  LED(3) uses Timer(2) and LED(4) uses
        Timer(3).  These timers are only configured for PWM if the intensity of the
        relevant LED is set to a value between 1 and 254.  Otherwise the timers are
        free for general purpose use.
        """

    @overload
    def intensity(self, value: int, /) -> None:
        """
        Get or set the LED intensity.  Intensity ranges between 0 (off) and 255 (full on).
        If no argument is given, return the LED intensity.
        If an argument is given, set the LED intensity and return ``None``.

        *Note:* Only LED(3) and LED(4) can have a smoothly varying intensity, and
        they use timer PWM to implement it.  LED(3) uses Timer(2) and LED(4) uses
        Timer(3).  These timers are only configured for PWM if the intensity of the
        relevant LED is set to a value between 1 and 254.  Otherwise the timers are
        free for general purpose use.
        """

    def off(self) -> None:
        """
        Turn the LED off.
        """
        ...

    def on(self) -> None:
        """
        Turn the LED on, to maximum intensity.
        """
        ...

    def toggle(self) -> None:
        """
        Toggle the LED between on (maximum intensity) and off.  If the LED is at
        non-zero intensity then it is considered "on" and toggle will turn it off.
        """
        ...
