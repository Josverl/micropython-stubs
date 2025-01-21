""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, Final, NoReturn, overload, Optional
from typing_extensions import TypeVar, TypeAlias, Awaitable
from .Pin import Pin
from machine.ADCBlock import ADCBlock
from machine.I2C import I2C
from machine.I2S import I2S
from machine.PWM import PWM
from machine.Pin import Pin
from machine.RTC import RTC
from machine.SD import SD
from machine.SDCard import SDCard
from machine.SPI import SPI
from machine.Signal import Signal
from machine.Timer import Timer
from machine.UART import UART
from machine.USBDevice import USBDevice
from machine.WDT import WDT

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

    def __init__(self, pin: int | Pin, /) -> None:
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

@overload
def freq() -> int:
    """
    Returns the CPU frequency in hertz.

    On some ports this can also be used to set the CPU frequency by passing in *hz*.
    """

@overload
def freq(hz: int, /) -> None:
    """
    Returns the CPU frequency in hertz.

    On some ports this can also be used to set the CPU frequency by passing in *hz*.
    """

@overload
def freq(self) -> int:
    """
    Get or set the current frequency of the PWM output.

    With no arguments the frequency in Hz is returned.

    With a single *value* argument the frequency is set to that value in Hz.  The
    method may raise a ``ValueError`` if the frequency is outside the valid range.
    """

@overload
def freq(
    self,
    value: int,
    /,
) -> None:
    """
    Get or set the current frequency of the PWM output.

    With no arguments the frequency in Hz is returned.

    With a single *value* argument the frequency is set to that value in Hz.  The
    method may raise a ``ValueError`` if the frequency is outside the valid range.
    """

@overload
def lightsleep() -> None:
    """
    Stops execution in an attempt to enter a low power state.

    If *time_ms* is specified then this will be the maximum time in milliseconds that
    the sleep will last for.  Otherwise the sleep can last indefinitely.

    With or without a timeout, execution may resume at any time if there are events
    that require processing.  Such events, or wake sources, should be configured before
    sleeping, like `Pin` change or `RTC` timeout.

    The precise behaviour and power-saving capabilities of lightsleep and deepsleep is
    highly dependent on the underlying hardware, but the general properties are:

    * A lightsleep has full RAM and state retention.  Upon wake execution is resumed
      from the point where the sleep was requested, with all subsystems operational.

    * A deepsleep may not retain RAM or any other state of the system (for example
      peripherals or network interfaces).  Upon wake execution is resumed from the main
      script, similar to a hard or power-on reset. The `reset_cause()` function will
      return `machine.DEEPSLEEP` and this can be used to distinguish a deepsleep wake
      from other resets.
    """

@overload
def lightsleep(time_ms: int, /) -> None:
    """
    Stops execution in an attempt to enter a low power state.

    If *time_ms* is specified then this will be the maximum time in milliseconds that
    the sleep will last for.  Otherwise the sleep can last indefinitely.

    With or without a timeout, execution may resume at any time if there are events
    that require processing.  Such events, or wake sources, should be configured before
    sleeping, like `Pin` change or `RTC` timeout.

    The precise behaviour and power-saving capabilities of lightsleep and deepsleep is
    highly dependent on the underlying hardware, but the general properties are:

    * A lightsleep has full RAM and state retention.  Upon wake execution is resumed
      from the point where the sleep was requested, with all subsystems operational.

    * A deepsleep may not retain RAM or any other state of the system (for example
      peripherals or network interfaces).  Upon wake execution is resumed from the main
      script, similar to a hard or power-on reset. The `reset_cause()` function will
      return `machine.DEEPSLEEP` and this can be used to distinguish a deepsleep wake
      from other resets.
    """

@overload
def deepsleep() -> NoReturn:
    """
    Stops execution in an attempt to enter a low power state.

    If *time_ms* is specified then this will be the maximum time in milliseconds that
    the sleep will last for.  Otherwise the sleep can last indefinitely.

    With or without a timeout, execution may resume at any time if there are events
    that require processing.  Such events, or wake sources, should be configured before
    sleeping, like `Pin` change or `RTC` timeout.

    The precise behaviour and power-saving capabilities of lightsleep and deepsleep is
    highly dependent on the underlying hardware, but the general properties are:

    * A lightsleep has full RAM and state retention.  Upon wake execution is resumed
      from the point where the sleep was requested, with all subsystems operational.

    * A deepsleep may not retain RAM or any other state of the system (for example
      peripherals or network interfaces).  Upon wake execution is resumed from the main
      script, similar to a hard or power-on reset. The `reset_cause()` function will
      return `machine.DEEPSLEEP` and this can be used to distinguish a deepsleep wake
      from other resets.
    """

@overload
def deepsleep(time_ms: int, /) -> NoReturn:
    """
    Stops execution in an attempt to enter a low power state.

    If *time_ms* is specified then this will be the maximum time in milliseconds that
    the sleep will last for.  Otherwise the sleep can last indefinitely.

    With or without a timeout, execution may resume at any time if there are events
    that require processing.  Such events, or wake sources, should be configured before
    sleeping, like `Pin` change or `RTC` timeout.

    The precise behaviour and power-saving capabilities of lightsleep and deepsleep is
    highly dependent on the underlying hardware, but the general properties are:

    * A lightsleep has full RAM and state retention.  Upon wake execution is resumed
      from the point where the sleep was requested, with all subsystems operational.

    * A deepsleep may not retain RAM or any other state of the system (for example
      peripherals or network interfaces).  Upon wake execution is resumed from the main
      script, similar to a hard or power-on reset. The `reset_cause()` function will
      return `machine.DEEPSLEEP` and this can be used to distinguish a deepsleep wake
      from other resets.
    """
