""" """

from __future__ import annotations
from typing import Any, Optional
from _typeshed import Incomplete

class PWM:
    """
    Construct and return a new PWM object using the following parameters:

       - *dest* is the entity on which the PWM is output, which is usually a
         :ref:`machine.Pin <machine.Pin>` object, but a port may allow other values,
         like integers.
       - *freq* should be an integer which sets the frequency in Hz for the
         PWM cycle.
       - *duty_u16* sets the duty cycle as a ratio ``duty_u16 / 65535``.
       - *duty_ns* sets the pulse width in nanoseconds.
       - *invert*  inverts the respective output if the value is True

    Setting *freq* may affect other PWM objects if the objects share the same
    underlying PWM generator (this is hardware specific).
    Only one of *duty_u16* and *duty_ns* should be specified at a time.
    *invert* is not available at all ports.
    """

    def __init__(self, dest, *, freq=0, duty=0, duty_u16=0, duty_ns=0, invert=False) -> None: ...
    def init(self, *, freq, duty_u16, duty_ns) -> None:
        """
        Modify settings for the PWM object.  See the above constructor for details
        about the parameters.
        """
        ...

    def deinit(self) -> None:
        """
        Disable the PWM output.
        """
        ...

    def freq(self, value: Optional[Any] = None) -> Incomplete:
        """
        Get or set the current frequency of the PWM output.

        With no arguments the frequency in Hz is returned.

        With a single *value* argument the frequency is set to that value in Hz.  The
        method may raise a ``ValueError`` if the frequency is outside the valid range.
        """
        ...

    def duty_u16(self, value: Optional[Any] = None) -> int:
        """
        Get or set the current duty cycle of the PWM output, as an unsigned 16-bit
        value in the range 0 to 65535 inclusive.

        With no arguments the duty cycle is returned.

        With a single *value* argument the duty cycle is set to that value, measured
        as the ratio ``value / 65535``.
        """
        ...

    def duty_ns(self, value: Optional[Any] = None) -> int:
        """
        Get or set the current pulse width of the PWM output, as a value in nanoseconds.

        With no arguments the pulse width in nanoseconds is returned.

        With a single *value* argument the pulse width is set to that value.
        """
        ...
