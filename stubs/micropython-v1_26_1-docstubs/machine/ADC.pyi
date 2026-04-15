""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import deprecated, TypeVar, TypeAlias, Awaitable
from .Pin import Pin
from _mpy_shed import mp_available
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

    VREF: int = ...
    CORE_VREF: int = ...
    CORE_VBAT: int = ...
    CORE_TEMP: int = ...
    ATTN_0DB: int = 0
    ATTN_2_5DB: int = 1
    ATTN_6DB: int = 2
    ATTN_11DB: int = 3
    WIDTH_9BIT: int = 9
    WIDTH_10BIT: int = 10
    WIDTH_11BIT: int = 11
    WIDTH_12BIT: int = 12
    def __init__(self, pin: PinLike, *, sample_ns: int | None = None, atten=ATTN_0DB) -> None:
        """
        Access the ADC associated with a source identified by *id*.  This
        *id* may be an integer (usually specifying a channel number), a
        :ref:`Pin <machine.Pin>` object, or other value supported by the
        underlying machine.
        .. note::

        WiPy has a custom implementation of ADC, see ADCWiPy for details.

        on ESP32 :  `atten` specifies the attenuation level for the ADC input.
        """
    def init(self, *, sample_ns: int | None = None, atten=ATTN_0DB) -> Incomplete:
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

    # ESP32 specific
    @mp_available(port="esp32")
    @deprecated("Use ADC.block().init(bits=bits) instead.")
    def width(self, bits: int) -> None:
        """
        Equivalent to ADC.block().init(bits=bits).
        The only chip that can switch resolution to a lower one is the normal esp32. The C2 & S3 are stuck at 12 bits, while the S2 is at 13 bits.

        For compatibility, the ADC object also provides constants matching the supported ADC resolutions, per chip:

        ESP32:
            ADC.WIDTH_9BIT = 9
            ADC.WIDTH_10BIT = 10
            ADC.WIDTH_11BIT = 11
            ADC.WIDTH_12BIT = 12

        ESP32 C3 & S3:
            ADC.WIDTH_12BIT = 12

        ESP32 S2:
            ADC.WIDTH_13BIT = 13

        Available : ESP32
        """
        ...

    @mp_available(port="esp32")
    @deprecated("Use read_u16() instead.")
    def read(self) -> int:
        """
        Take an analog reading and return an integer in the range 0-4095.
        The return value represents the raw reading taken by the ADC, scaled
        such that the minimum value is 0 and the maximum value is 4095.

        This method is deprecated, use `read_u16()` instead.

        Available : ESP32
        """
        ...

    @mp_available(port="esp32")
    @deprecated("Use ADC.init(atten=atten) instead.")
    def atten(self, atten: int) -> None:
        """
        Set the attenuation level for the ADC input.

        Available : ESP32
        """
        ...
