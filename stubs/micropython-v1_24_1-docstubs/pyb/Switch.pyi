""" """

from __future__ import annotations

from array import array
from typing import Callable

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

from .Pin import Pin

class Switch:
    """
    A Switch object is used to control a push-button switch.

    Usage::

         sw = pyb.Switch()       # create a switch object
         sw.value()              # get state (True if pressed, False otherwise)
         sw()                    # shorthand notation to get the switch state
         sw.callback(f)          # register a callback to be called when the
                                 #   switch is pressed down
         sw.callback(None)       # remove the callback

    Example::

         pyb.Switch().callback(lambda: pyb.LED(1).toggle())
    """

    def __init__(self) -> None:
        """
        Create and return a switch object.
        """

    def __call__(self) -> bool:
        """
        Call switch object directly to get its state: ``True`` if pressed down,
        ``False`` otherwise.
        """
        ...

    def value(self) -> bool:
        """
        Get the switch state.  Returns ``True`` if pressed down, otherwise ``False``.
        """
        ...

    def callback(self, fun: Callable[[], None] | None) -> None:
        """
        Register the given function to be called when the switch is pressed down.
        If ``fun`` is ``None``, then it disables the callback.
        """
        ...
