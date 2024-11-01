""" """

from __future__ import annotations
from _typeshed import Incomplete

class ExtInt:
    """
    Create an ExtInt object:

      - ``pin`` is the pin on which to enable the interrupt (can be a pin object or any valid pin name).
      - ``mode`` can be one of:
        - ``ExtInt.IRQ_RISING`` - trigger on a rising edge;
        - ``ExtInt.IRQ_FALLING`` - trigger on a falling edge;
        - ``ExtInt.IRQ_RISING_FALLING`` - trigger on a rising or falling edge.
      - ``pull`` can be one of:
        - ``pyb.Pin.PULL_NONE`` - no pull up or down resistors;
        - ``pyb.Pin.PULL_UP`` - enable the pull-up resistor;
        - ``pyb.Pin.PULL_DOWN`` - enable the pull-down resistor.
      - ``callback`` is the function to call when the interrupt triggers.  The
        callback function must accept exactly 1 argument, which is the line that
        triggered the interrupt.
    """

    IRQ_FALLING: Incomplete
    """interrupt on a falling edge"""
    IRQ_RISING: Incomplete
    """interrupt on a rising edge"""
    IRQ_RISING_FALLING: Incomplete
    """interrupt on a rising or falling edge"""
    def __init__(self, pin, mode, pull, callback) -> None: ...
    @classmethod
    def regs(cls) -> Incomplete:
        """
        Dump the values of the EXTI registers.
        """
        ...

    def disable(self) -> None:
        """
        Disable the interrupt associated with the ExtInt object.
        This could be useful for debouncing.
        """
        ...

    def enable(self) -> None:
        """
        Enable a disabled interrupt.
        """
        ...

    def line(self) -> int:
        """
        Return the line number that the pin is mapped to.
        """
        ...

    def swint(self) -> Incomplete:
        """
        Trigger the callback from software.
        """
        ...
