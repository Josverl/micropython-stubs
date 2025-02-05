""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import TypeVar, TypeAlias, Awaitable
from .Pin import Pin
from machine.Pin import Pin, PinLike

ATTN_0DB: int = ...

class ADC:
    """
    The ADC class provides an interface to analog-to-digital convertors, and
    represents a single endpoint that can sample a continuous voltage and
    convert it to a discretised value.

    Example usage::

       import machine

       adc = machine.ADC(pin)   # create an ADC object acting on a pin
       val = adc.read_u16()     # read a raw analog value in the range 0-65535
    """

    def __init__(self, pin: PinLike, /) -> None:
        """
        Access the ADC associated with a source identified by *id*.  This
        *id* may be an integer (usually specifying a channel number), a
        :ref:`Pin <machine.Pin>` object, or other value supported by the
        underlying machine.
        .. note::

        WiPy has a custom implementation of ADC, see ADCWiPy for details.
        """

    def init(self, *, sample_ns, atten) -> Incomplete:
        """
        Apply the given settings to the ADC.  Only those arguments that are
        specified will be changed.  See the ADC constructor above for what the
        arguments are.
        """
        ...

    def block(self) -> Incomplete:
        """
        Return the :ref:`ADCBlock <machine.ADCBlock>` instance associated with
        this ADC object.

        This method only exists if the port supports the
        :ref:`ADCBlock <machine.ADCBlock>` class.
        """
        ...

    def read_u16(self) -> int:
        """
        Take an analog reading and return an integer in the range 0-65535.
        The return value represents the raw reading taken by the ADC, scaled
        such that the minimum value is 0 and the maximum value is 65535.
        """
        ...

    def read_uv(self) -> int:
        """
        Take an analog reading and return an integer value with units of
        microvolts.  It is up to the particular port whether or not this value
        is calibrated, and how calibration is done.
        """
        ...
