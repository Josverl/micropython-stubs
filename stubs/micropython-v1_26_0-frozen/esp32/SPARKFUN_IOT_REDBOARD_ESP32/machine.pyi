"""
Functions related to the hardware.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/machine.html

The ``machine`` module contains specific functions related to the hardware
on a particular board. Most functions in this module allow to achieve direct
and unrestricted access to and control of hardware blocks on a system
(like CPU, timers, buses, etc.). Used incorrectly, this can lead to
malfunction, lockups, crashes of your board, and in extreme cases, hardware
damage.
"""

from __future__ import annotations
from _typeshed import Incomplete
from micropython import const as const
from typing_extensions import deprecated, Awaitable, TypeAlias, TypeVar
from typing import NoReturn, Callable, overload, Any
from _mpy_shed import _IRQ, AnyReadableBuf, AnyWritableBuf
from vfs import AbstractBlockDev

_path: Incomplete
_PCNT_RANGE: int
ATTN_0DB: int = ...
ID_T: TypeAlias = int | str
PinLike: TypeAlias = Pin | int | str
IDLE: Incomplete
SLEEP: Incomplete
DEEPSLEEP: Incomplete
PWRON_RESET: Incomplete
HARD_RESET: Incomplete
WDT_RESET: Incomplete
DEEPSLEEP_RESET: Incomplete
SOFT_RESET: Incomplete
WLAN_WAKE: Incomplete
PIN_WAKE: Incomplete
RTC_WAKE: Incomplete
_IRQ_STATE: TypeAlias = int

class _CounterBase:
    _PCNT: Incomplete
    _INSTANCES: Incomplete
    def __new__(cls, unit_id, *_args, **_kwargs): ...
    _unit_id: Incomplete
    _pcnt: Incomplete
    _overflows: int
    _offset: int
    def __init__(self, unit_id, *args, filter_ns: int = 0, **kwargs) -> None: ...
    def _overflow(self, pcnt) -> None: ...
    def init(self, *args, **kwargs) -> None: ...
    def deinit(self) -> None: ...
    def value(self, value=None): ...

class Counter:
    """
    Returns the singleton Counter object for the the given *id*. Values of *id*
    depend on a particular port and its hardware. Values 0, 1, etc. are commonly
    used to select hardware block #0, #1, etc.

    Additional arguments are passed to the :meth:`init` method described below,
    and will cause the Counter instance to be re-initialised and reset.

    On ESP32, the *id* corresponds to a :ref:`PCNT unit <esp32.PCNT>`.
    """

    RISING: int
    FALLING: int
    UP: Incomplete
    DOWN: Incomplete
    def _configure(self, src, edge=..., direction=...) -> None: ...

class Encoder:
    """
    Returns the singleton Encoder object for the the given *id*. Values of *id*
    depend on a particular port and its hardware. Values 0, 1, etc. are commonly
    used to select hardware block #0, #1, etc.

    Additional arguments are passed to the :meth:`init` method described below,
    and will cause the Encoder instance to be re-initialised and reset.

    On ESP32, the *id* corresponds to a :ref:`PCNT unit <esp32.PCNT>`.
    """

    _phases: Incomplete
    def _configure(self, phase_a, phase_b, phases: int = 1) -> None: ...
    def phases(self): ...

def __getattr__(attr): ...

class I2C:
    @overload
    def __init__(self, id: ID_T, /, *, freq: int = 400_000):
        """
        Construct and return a new I2C object using the following parameters:

           - *id* identifies a particular I2C peripheral.  Allowed values for
             depend on the particular port/board
           - *scl* should be a pin object specifying the pin to use for SCL.
           - *sda* should be a pin object specifying the pin to use for SDA.
           - *freq* should be an integer which sets the maximum frequency
             for SCL.

        Note that some ports/boards will have default values of *scl* and *sda*
        that can be changed in this constructor.  Others will have fixed values
        of *scl* and *sda* that cannot be changed.
        """

    @overload
    def __init__(self, id: ID_T, /, *, scl: PinLike, sda: PinLike, freq: int = 400_000):
        """
        Construct and return a new I2C object using the following parameters:

           - *id* identifies a particular I2C peripheral.  Allowed values for
             depend on the particular port/board
           - *scl* should be a pin object specifying the pin to use for SCL.
           - *sda* should be a pin object specifying the pin to use for SDA.
           - *freq* should be an integer which sets the maximum frequency
             for SCL.

        Note that some ports/boards will have default values of *scl* and *sda*
        that can be changed in this constructor.  Others will have fixed values
        of *scl* and *sda* that cannot be changed.
        """

    @overload
    def __init__(self, *, scl: PinLike, sda: PinLike, freq: int = 400_000) -> None:
        """
        Initialise the I2C bus with the given arguments:

           - *scl* is a pin object for the SCL line
           - *sda* is a pin object for the SDA line
           - *freq* is the SCL clock rate

         In the case of hardware I2C the actual clock frequency may be lower than the
         requested frequency. This is dependent on the platform hardware. The actual
         rate may be determined by printing the I2C object.
        """

    @overload
    def init(self, *, freq: int = 400_000) -> None:
        """
        Initialise the I2C bus with the given arguments:

           - *scl* is a pin object for the SCL line
           - *sda* is a pin object for the SDA line
           - *freq* is the SCL clock rate

         In the case of hardware I2C the actual clock frequency may be lower than the
         requested frequency. This is dependent on the platform hardware. The actual
         rate may be determined by printing the I2C object.
        """

    @overload
    def init(self, *, scl: PinLike, sda: PinLike, freq: int = 400_000) -> None:
        """
        Initialise the I2C bus with the given arguments:

           - *scl* is a pin object for the SCL line
           - *sda* is a pin object for the SDA line
           - *freq* is the SCL clock rate

         In the case of hardware I2C the actual clock frequency may be lower than the
         requested frequency. This is dependent on the platform hardware. The actual
         rate may be determined by printing the I2C object.
        """

class Pin:
    @overload
    def value(self) -> int:
        """
        This method allows to set and get the value of the pin, depending on whether
        the argument ``x`` is supplied or not.

        If the argument is omitted then this method gets the digital logic level of
        the pin, returning 0 or 1 corresponding to low and high voltage signals
        respectively.  The behaviour of this method depends on the mode of the pin:

          - ``Pin.IN`` - The method returns the actual input value currently present
            on the pin.
          - ``Pin.OUT`` - The behaviour and return value of the method is undefined.
          - ``Pin.OPEN_DRAIN`` - If the pin is in state '0' then the behaviour and
            return value of the method is undefined.  Otherwise, if the pin is in
            state '1', the method returns the actual input value currently present
            on the pin.

        If the argument is supplied then this method sets the digital logic level of
        the pin.  The argument ``x`` can be anything that converts to a boolean.
        If it converts to ``True``, the pin is set to state '1', otherwise it is set
        to state '0'.  The behaviour of this method depends on the mode of the pin:

          - ``Pin.IN`` - The value is stored in the output buffer for the pin.  The
            pin state does not change, it remains in the high-impedance state.  The
            stored value will become active on the pin as soon as it is changed to
            ``Pin.OUT`` or ``Pin.OPEN_DRAIN`` mode.
          - ``Pin.OUT`` - The output buffer is set to the given value immediately.
          - ``Pin.OPEN_DRAIN`` - If the value is '0' the pin is set to a low voltage
            state.  Otherwise the pin is set to high-impedance state.

        When setting the value this method returns ``None``.
        """

    @overload
    def value(self, x: Any, /) -> None:
        """
        This method allows to set and get the value of the pin, depending on whether
        the argument ``x`` is supplied or not.

        If the argument is omitted then this method gets the digital logic level of
        the pin, returning 0 or 1 corresponding to low and high voltage signals
        respectively.  The behaviour of this method depends on the mode of the pin:

          - ``Pin.IN`` - The method returns the actual input value currently present
            on the pin.
          - ``Pin.OUT`` - The behaviour and return value of the method is undefined.
          - ``Pin.OPEN_DRAIN`` - If the pin is in state '0' then the behaviour and
            return value of the method is undefined.  Otherwise, if the pin is in
            state '1', the method returns the actual input value currently present
            on the pin.

        If the argument is supplied then this method sets the digital logic level of
        the pin.  The argument ``x`` can be anything that converts to a boolean.
        If it converts to ``True``, the pin is set to state '1', otherwise it is set
        to state '0'.  The behaviour of this method depends on the mode of the pin:

          - ``Pin.IN`` - The value is stored in the output buffer for the pin.  The
            pin state does not change, it remains in the high-impedance state.  The
            stored value will become active on the pin as soon as it is changed to
            ``Pin.OUT`` or ``Pin.OPEN_DRAIN`` mode.
          - ``Pin.OUT`` - The output buffer is set to the given value immediately.
          - ``Pin.OPEN_DRAIN`` - If the value is '0' the pin is set to a low voltage
            state.  Otherwise the pin is set to high-impedance state.

        When setting the value this method returns ``None``.
        """

    @overload
    def __call__(self) -> int:
        """
        Pin objects are callable.  The call method provides a (fast) shortcut to set
        and get the value of the pin.  It is equivalent to Pin.value([x]).
        See :meth:`Pin.value` for more details.
        """

    @overload
    def __call__(self, x: Any, /) -> None:
        """
        Pin objects are callable.  The call method provides a (fast) shortcut to set
        and get the value of the pin.  It is equivalent to Pin.value([x]).
        See :meth:`Pin.value` for more details.
        """

    @overload
    def mode(self) -> int:
        """
        Get or set the pin mode.
        See the constructor documentation for details of the ``mode`` argument.

        Availability: cc3200, stm32 ports.
        """

    @overload
    def mode(self, mode: int, /) -> None:
        """
        Get or set the pin mode.
        See the constructor documentation for details of the ``mode`` argument.

        Availability: cc3200, stm32 ports.
        """

    @overload
    def pull(self) -> int:
        """
        Get or set the pin pull state.
        See the constructor documentation for details of the ``pull`` argument.

        Availability: cc3200, stm32 ports.
        """

    @overload
    def pull(self, pull: int, /) -> None:
        """
        Get or set the pin pull state.
        See the constructor documentation for details of the ``pull`` argument.

        Availability: cc3200, stm32 ports.
        """

    @overload
    def drive(self, drive: int, /) -> None:
        """
        Get or set the pin drive strength.
        See the constructor documentation for details of the ``drive`` argument.

        Availability: cc3200 port.
        """
        ...

    @overload
    def drive(self, /) -> int:
        """
        Get or set the pin drive strength.
        See the constructor documentation for details of the ``drive`` argument.

        Availability: cc3200 port.
        """

class PWM:
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
    def duty_u16(self) -> int:
        """
        Get or set the current duty cycle of the PWM output, as an unsigned 16-bit
        value in the range 0 to 65535 inclusive.

        With no arguments the duty cycle is returned.

        With a single *value* argument the duty cycle is set to that value, measured
        as the ratio ``value / 65535``.
        """

    @overload
    def duty_u16(
        self,
        value: int,
        /,
    ) -> None:
        """
        Get or set the current duty cycle of the PWM output, as an unsigned 16-bit
        value in the range 0 to 65535 inclusive.

        With no arguments the duty cycle is returned.

        With a single *value* argument the duty cycle is set to that value, measured
        as the ratio ``value / 65535``.
        """

    @overload
    def duty_ns(self) -> int:
        """
        Get or set the current pulse width of the PWM output, as a value in nanoseconds.

        With no arguments the pulse width in nanoseconds is returned.

        With a single *value* argument the pulse width is set to that value.
        """

    @overload
    def duty_ns(
        self,
        value: int,
        /,
    ) -> None:
        """
        Get or set the current pulse width of the PWM output, as a value in nanoseconds.

        With no arguments the pulse width in nanoseconds is returned.

        With a single *value* argument the pulse width is set to that value.
        """

class RTC:
    @overload
    def __init__(self, id: int = 0):
        """
        Create an RTC object. See init for parameters of initialization.
        """

    @overload
    def __init__(self, id: int = 0, /, *, datetime: tuple[int, int, int]):
        """
        Create an RTC object. See init for parameters of initialization.

        The documentation for RTC is in a poor state; better to experiment and use `dir`!
        """

    @overload
    def __init__(self, id: int = 0, /, *, datetime: tuple[int, int, int, int]):
        """
        Create an RTC object. See init for parameters of initialization.

        The documentation for RTC is in a poor state; better to experiment and use `dir`!
        """

    @overload
    def __init__(self, id: int = 0, /, *, datetime: tuple[int, int, int, int, int]):
        """
        Create an RTC object. See init for parameters of initialization.

        The documentation for RTC is in a poor state; better to experiment and use `dir`!
        """

    @overload
    def __init__(self, id: int = 0, /, *, datetime: tuple[int, int, int, int, int, int]):
        """
        Create an RTC object. See init for parameters of initialization.

        The documentation for RTC is in a poor state; better to experiment and use `dir`!
        """

    @overload
    def __init__(self, id: int = 0, /, *, datetime: tuple[int, int, int, int, int, int, int]):
        """
        Create an RTC object. See init for parameters of initialization.

        The documentation for RTC is in a poor state; better to experiment and use `dir`!
        """

    @overload
    def __init__(self, id: int = 0, /, *, datetime: tuple[int, int, int, int, int, int, int, int]):
        """
        Create an RTC object. See init for parameters of initialization.

        The documentation for RTC is in a poor state; better to experiment and use `dir`!
        """

    @overload
    def init(self) -> None:
        """
        Initialise the RTC. Datetime is a tuple of the form:

           ``(year, month, day, hour, minute, second, microsecond, tzinfo)``

        All eight arguments must be present. The ``microsecond`` and ``tzinfo``
        values are currently ignored but might be used in the future.

        Availability: CC3200, ESP32, MIMXRT, SAMD. The rtc.init() method on
        the stm32 and renesas-ra ports just (re-)starts the RTC and does not
        accept arguments.
        """

    @overload
    def init(self, datetime: tuple[int, int, int], /) -> None:
        """
        Initialise the RTC. Datetime is a tuple of the form:

           ``(year, month, day, hour, minute, second, microsecond, tzinfo)``

        All eight arguments must be present. The ``microsecond`` and ``tzinfo``
        values are currently ignored but might be used in the future.

        Availability: CC3200, ESP32, MIMXRT, SAMD. The rtc.init() method on
        the stm32 and renesas-ra ports just (re-)starts the RTC and does not
        accept arguments.
        """

    @overload
    def init(self, datetime: tuple[int, int, int, int], /) -> None:
        """
        Initialise the RTC. Datetime is a tuple of the form:

           ``(year, month, day, hour, minute, second, microsecond, tzinfo)``

        All eight arguments must be present. The ``microsecond`` and ``tzinfo``
        values are currently ignored but might be used in the future.

        Availability: CC3200, ESP32, MIMXRT, SAMD. The rtc.init() method on
        the stm32 and renesas-ra ports just (re-)starts the RTC and does not
        accept arguments.
        """

    @overload
    def init(self, datetime: tuple[int, int, int, int, int], /) -> None:
        """
        Initialise the RTC. Datetime is a tuple of the form:

           ``(year, month, day, hour, minute, second, microsecond, tzinfo)``

        All eight arguments must be present. The ``microsecond`` and ``tzinfo``
        values are currently ignored but might be used in the future.

        Availability: CC3200, ESP32, MIMXRT, SAMD. The rtc.init() method on
        the stm32 and renesas-ra ports just (re-)starts the RTC and does not
        accept arguments.
        """

    @overload
    def init(self, datetime: tuple[int, int, int, int, int, int], /) -> None:
        """
        Initialise the RTC. Datetime is a tuple of the form:

           ``(year, month, day, hour, minute, second, microsecond, tzinfo)``

        All eight arguments must be present. The ``microsecond`` and ``tzinfo``
        values are currently ignored but might be used in the future.

        Availability: CC3200, ESP32, MIMXRT, SAMD. The rtc.init() method on
        the stm32 and renesas-ra ports just (re-)starts the RTC and does not
        accept arguments.
        """

    @overload
    def init(self, datetime: tuple[int, int, int, int, int, int, int], /) -> None:
        """
        Initialise the RTC. Datetime is a tuple of the form:

           ``(year, month, day, hour, minute, second, microsecond, tzinfo)``

        All eight arguments must be present. The ``microsecond`` and ``tzinfo``
        values are currently ignored but might be used in the future.

        Availability: CC3200, ESP32, MIMXRT, SAMD. The rtc.init() method on
        the stm32 and renesas-ra ports just (re-)starts the RTC and does not
        accept arguments.
        """

    @overload
    def init(self, datetime: tuple[int, int, int, int, int, int, int, int], /) -> None:
        """
        Initialise the RTC. Datetime is a tuple of the form:

           ``(year, month, day, hour, minute, second, microsecond, tzinfo)``

        All eight arguments must be present. The ``microsecond`` and ``tzinfo``
        values are currently ignored but might be used in the future.

        Availability: CC3200, ESP32, MIMXRT, SAMD. The rtc.init() method on
        the stm32 and renesas-ra ports just (re-)starts the RTC and does not
        accept arguments.
        """

    @overload
    def alarm(self, id: int, time: int, /, *, repeat: bool = False) -> None:
        """
        Set the RTC alarm. Time might be either a millisecond value to program the alarm to
        current time + time_in_ms in the future, or a datetimetuple. If the time passed is in
        milliseconds, repeat can be set to ``True`` to make the alarm periodic.
        """

    @overload
    def alarm(self, id: int, time: tuple[int, int, int], /) -> None:
        """
        Set the RTC alarm. Time might be either a millisecond value to program the alarm to
        current time + time_in_ms in the future, or a datetimetuple. If the time passed is in
        milliseconds, repeat can be set to ``True`` to make the alarm periodic.
        """

    @overload
    def alarm(self, id: int, time: tuple[int, int, int, int], /) -> None:
        """
        Set the RTC alarm. Time might be either a millisecond value to program the alarm to
        current time + time_in_ms in the future, or a datetimetuple. If the time passed is in
        milliseconds, repeat can be set to ``True`` to make the alarm periodic.
        """

    @overload
    def alarm(self, id: int, time: tuple[int, int, int, int, int], /) -> None:
        """
        Set the RTC alarm. Time might be either a millisecond value to program the alarm to
        current time + time_in_ms in the future, or a datetimetuple. If the time passed is in
        milliseconds, repeat can be set to ``True`` to make the alarm periodic.
        """

    @overload
    def alarm(self, id: int, time: tuple[int, int, int, int, int, int], /) -> None:
        """
        Set the RTC alarm. Time might be either a millisecond value to program the alarm to
        current time + time_in_ms in the future, or a datetimetuple. If the time passed is in
        milliseconds, repeat can be set to ``True`` to make the alarm periodic.
        """

    @overload
    def alarm(self, id: int, time: tuple[int, int, int, int, int, int, int], /) -> None:
        """
        Set the RTC alarm. Time might be either a millisecond value to program the alarm to
        current time + time_in_ms in the future, or a datetimetuple. If the time passed is in
        milliseconds, repeat can be set to ``True`` to make the alarm periodic.
        """

    @overload
    def alarm(self, id: int, time: tuple[int, int, int, int, int, int, int, int], /) -> None:
        """
        Set the RTC alarm. Time might be either a millisecond value to program the alarm to
        current time + time_in_ms in the future, or a datetimetuple. If the time passed is in
        milliseconds, repeat can be set to ``True`` to make the alarm periodic.
        """

class SDCard:
    @overload
    def readblocks(self, block_num: int, buf: bytearray) -> bool:
        """
        The first form reads aligned, multiples of blocks.
        Starting at the block given by the index *block_num*, read blocks from
        the device into *buf* (an array of bytes).
        The number of blocks to read is given by the length of *buf*,
        which will be a multiple of the block size.
        """

    @overload
    def readblocks(self, block_num: int, buf: bytearray, offset: int) -> bool:
        """
        The second form allows reading at arbitrary locations within a block,
        and arbitrary lengths.
        Starting at block index *block_num*, and byte offset within that block
        of *offset*, read bytes from the device into *buf* (an array of bytes).
        The number of bytes to read is given by the length of *buf*.
        """

    @overload
    def writeblocks(self, block_num: int, buf: bytes | bytearray, /) -> None:
        """
        The first form writes aligned, multiples of blocks, and requires that the
        blocks that are written to be first erased (if necessary) by this method.
        Starting at the block given by the index *block_num*, write blocks from
        *buf* (an array of bytes) to the device.
        The number of blocks to write is given by the length of *buf*,
        which will be a multiple of the block size.
        """

    @overload
    def writeblocks(self, block_num: int, buf: bytes | bytearray, offset: int, /) -> None:
        """
        The second form allows writing at arbitrary locations within a block,
        and arbitrary lengths.  Only the bytes being written should be changed,
        and the caller of this method must ensure that the relevant blocks are
        erased via a prior ``ioctl`` call.
        Starting at block index *block_num*, and byte offset within that block
        of *offset*, write bytes from *buf* (an array of bytes) to the device.
        The number of bytes to write is given by the length of *buf*.

        Note that implementations must never implicitly erase blocks if the offset
        argument is specified, even if it is zero.
        """

class Signal:
    @overload
    def __init__(self, pin_obj: PinLike, invert: bool = False, /):
        """
        Create a Signal object. There're two ways to create it:

        * By wrapping existing Pin object - universal method which works for
          any board.
        * By passing required Pin parameters directly to Signal constructor,
          skipping the need to create intermediate Pin object. Available on
          many, but not all boards.

        The arguments are:

          - ``pin_obj`` is existing Pin object.

          - ``pin_arguments`` are the same arguments as can be passed to Pin constructor.

          - ``invert`` - if True, the signal will be inverted (active low).
        """

    @overload
    def __init__(
        self,
        id: PinLike,
        /,
        mode: int = -1,
        pull: int = -1,
        *,
        value: Any = None,
        drive: int | None = None,
        alt: int | None = None,
        invert: bool = False,
    ):
        """
        Create a Signal object. There're two ways to create it:

        * By wrapping existing Pin object - universal method which works for
          any board.
        * By passing required Pin parameters directly to Signal constructor,
          skipping the need to create intermediate Pin object. Available on
          many, but not all boards.

        The arguments are:

          - ``pin_obj`` is existing Pin object.

          - ``pin_arguments`` are the same arguments as can be passed to Pin constructor.

          - ``invert`` - if True, the signal will be inverted (active low).
        """

    @overload
    def value(self) -> int:
        """
        This method allows to set and get the value of the signal, depending on whether
        the argument ``x`` is supplied or not.

        If the argument is omitted then this method gets the signal level, 1 meaning
        signal is asserted (active) and 0 - signal inactive.

        If the argument is supplied then this method sets the signal level. The
        argument ``x`` can be anything that converts to a boolean. If it converts
        to ``True``, the signal is active, otherwise it is inactive.

        Correspondence between signal being active and actual logic level on the
        underlying pin depends on whether signal is inverted (active-low) or not.
        For non-inverted signal, active status corresponds to logical 1, inactive -
        to logical 0. For inverted/active-low signal, active status corresponds
        to logical 0, while inactive - to logical 1.
        """

    @overload
    def value(self, x: Any, /) -> None:
        """
        This method allows to set and get the value of the signal, depending on whether
        the argument ``x`` is supplied or not.

        If the argument is omitted then this method gets the signal level, 1 meaning
        signal is asserted (active) and 0 - signal inactive.

        If the argument is supplied then this method sets the signal level. The
        argument ``x`` can be anything that converts to a boolean. If it converts
        to ``True``, the signal is active, otherwise it is inactive.

        Correspondence between signal being active and actual logic level on the
        underlying pin depends on whether signal is inverted (active-low) or not.
        For non-inverted signal, active status corresponds to logical 1, inactive -
        to logical 0. For inverted/active-low signal, active status corresponds
        to logical 0, while inactive - to logical 1.
        """

class SPI:
    @overload
    def __init__(self, id: int, /):
        """
        Construct an SPI object on the given bus, *id*. Values of *id* depend
        on a particular port and its hardware. Values 0, 1, etc. are commonly used
        to select hardware SPI block #0, #1, etc.

        With no additional parameters, the SPI object is created but not
        initialised (it has the settings from the last initialisation of
        the bus, if any).  If extra arguments are given, the bus is initialised.
        See ``init`` for parameters of initialisation.
        """

    @overload
    def __init__(
        self,
        id: int,
        /,
        baudrate: int = 1_000_000,
        *,
        polarity: int = 0,
        phase: int = 0,
        bits: int = 8,
        firstbit: int = MSB,
        sck: PinLike | None = None,
        mosi: PinLike | None = None,
        miso: PinLike | None = None,
    ):
        """
        Construct an SPI object on the given bus, *id*. Values of *id* depend
        on a particular port and its hardware. Values 0, 1, etc. are commonly used
        to select hardware SPI block #0, #1, etc.

        With no additional parameters, the SPI object is created but not
        initialised (it has the settings from the last initialisation of
        the bus, if any).  If extra arguments are given, the bus is initialised.
        See ``init`` for parameters of initialisation.
        """

    @overload
    def __init__(
        self,
        id: int,
        /,
        baudrate: int = 1_000_000,
        *,
        polarity: int = 0,
        phase: int = 0,
        bits: int = 8,
        firstbit: int = MSB,
        pins: tuple[PinLike, PinLike, PinLike] | None = None,
    ):
        """
        Construct an SPI object on the given bus, *id*. Values of *id* depend
        on a particular port and its hardware. Values 0, 1, etc. are commonly used
        to select hardware SPI block #0, #1, etc.

        With no additional parameters, the SPI object is created but not
        initialised (it has the settings from the last initialisation of
        the bus, if any).  If extra arguments are given, the bus is initialised.
        See ``init`` for parameters of initialisation.
        """

    @overload
    def init(
        self,
        baudrate: int = 1_000_000,
        *,
        polarity: int = 0,
        phase: int = 0,
        bits: int = 8,
        firstbit: int = MSB,
        sck: PinLike | None = None,
        mosi: PinLike | None = None,
        miso: PinLike | None = None,
    ) -> None:
        """
        Initialise the SPI bus with the given parameters:

          - ``baudrate`` is the SCK clock rate.
          - ``polarity`` can be 0 or 1, and is the level the idle clock line sits at.
          - ``phase`` can be 0 or 1 to sample data on the first or second clock edge
            respectively.
          - ``bits`` is the width in bits of each transfer. Only 8 is guaranteed to be supported by all hardware.
          - ``firstbit`` can be ``SPI.MSB`` or ``SPI.LSB``.
          - ``sck``, ``mosi``, ``miso`` are pins (machine.Pin) objects to use for bus signals. For most
            hardware SPI blocks (as selected by ``id`` parameter to the constructor), pins are fixed
            and cannot be changed. In some cases, hardware blocks allow 2-3 alternative pin sets for
            a hardware SPI block. Arbitrary pin assignments are possible only for a bitbanging SPI driver
            (``id`` = -1).
          - ``pins`` - WiPy port doesn't ``sck``, ``mosi``, ``miso`` arguments, and instead allows to
            specify them as a tuple of ``pins`` parameter.

        In the case of hardware SPI the actual clock frequency may be lower than the
        requested baudrate. This is dependent on the platform hardware. The actual
        rate may be determined by printing the SPI object.
        """

    @overload
    def init(
        self,
        baudrate: int = 1_000_000,
        *,
        polarity: int = 0,
        phase: int = 0,
        bits: int = 8,
        firstbit: int = MSB,
        pins: tuple[PinLike, PinLike, PinLike] | None = None,
    ) -> None:
        """
        Initialise the SPI bus with the given parameters:

          - ``baudrate`` is the SCK clock rate.
          - ``polarity`` can be 0 or 1, and is the level the idle clock line sits at.
          - ``phase`` can be 0 or 1 to sample data on the first or second clock edge
            respectively.
          - ``bits`` is the width in bits of each transfer. Only 8 is guaranteed to be supported by all hardware.
          - ``firstbit`` can be ``SPI.MSB`` or ``SPI.LSB``.
          - ``sck``, ``mosi``, ``miso`` are pins (machine.Pin) objects to use for bus signals. For most
            hardware SPI blocks (as selected by ``id`` parameter to the constructor), pins are fixed
            and cannot be changed. In some cases, hardware blocks allow 2-3 alternative pin sets for
            a hardware SPI block. Arbitrary pin assignments are possible only for a bitbanging SPI driver
            (``id`` = -1).
          - ``pins`` - WiPy port doesn't ``sck``, ``mosi``, ``miso`` arguments, and instead allows to
            specify them as a tuple of ``pins`` parameter.

        In the case of hardware SPI the actual clock frequency may be lower than the
        requested baudrate. This is dependent on the platform hardware. The actual
        rate may be determined by printing the SPI object.
        """

class Timer:
    @overload
    def __init__(self, id: int, /):
        """
        Construct a new timer object of the given ``id``. ``id`` of -1 constructs a
        virtual timer (if supported by a board).
        ``id`` shall not be passed as a keyword argument.

        See ``init`` for parameters of initialisation.
        """

    @overload
    def __init__(
        self,
        id: int,
        /,
        *,
        mode: int = PERIODIC,
        period: int | None = None,
        callback: Callable[[Timer], None] | None = None,
    ):
        """
        Construct a new timer object of the given ``id``. ``id`` of -1 constructs a
        virtual timer (if supported by a board).
        ``id`` shall not be passed as a keyword argument.

        See ``init`` for parameters of initialisation.
        """

    @overload
    def __init__(
        self,
        id: int,
        /,
        *,
        mode: int = PERIODIC,
        freq: int | None = None,
        callback: Callable[[Timer], None] | None = None,
    ):
        """
        Construct a new timer object of the given ``id``. ``id`` of -1 constructs a
        virtual timer (if supported by a board).
        ``id`` shall not be passed as a keyword argument.

        See ``init`` for parameters of initialisation.
        """

    @overload
    def __init__(
        self,
        id: int,
        /,
        *,
        mode: int = PERIODIC,
        tick_hz: int | None = None,
        callback: Callable[[Timer], None] | None = None,
    ):
        """
        Construct a new timer object of the given ``id``. ``id`` of -1 constructs a
        virtual timer (if supported by a board).
        ``id`` shall not be passed as a keyword argument.

        See ``init`` for parameters of initialisation.
        """

    @overload
    def init(
        self,
        *,
        mode: int = PERIODIC,
        period: int | None = None,
        callback: Callable[[Timer], None] | None = None,
    ) -> None: ...
    @overload
    def init(
        self,
        *,
        mode: int = PERIODIC,
        freq: int | None = None,
        callback: Callable[[Timer], None] | None = None,
    ) -> None: ...
    @overload
    def init(
        self,
        *,
        mode: int = PERIODIC,
        tick_hz: int | None = None,
        callback: Callable[[Timer], None] | None = None,
    ) -> None:
        """
        Initialise the timer. Example::

            def mycallback(t):
                pass

            # periodic at 1kHz
            tim.init(mode=Timer.PERIODIC, freq=1000, callback=mycallback)

            # periodic with 100ms period
            tim.init(period=100, callback=mycallback)

            # one shot firing after 1000ms
            tim.init(mode=Timer.ONE_SHOT, period=1000, callback=mycallback)

        Keyword arguments:

          - ``mode`` can be one of:

            - ``Timer.ONE_SHOT`` - The timer runs once until the configured
              period of the channel expires.
            - ``Timer.PERIODIC`` - The timer runs periodically at the configured
              frequency of the channel.

          - ``freq`` - The timer frequency, in units of Hz.  The upper bound of
            the frequency is dependent on the port.  When both the ``freq`` and
            ``period`` arguments are given, ``freq`` has a higher priority and
            ``period`` is ignored.

          - ``period`` - The timer period, in milliseconds.

          - ``callback`` - The callable to call upon expiration of the timer period.
            The callback must take one argument, which is passed the Timer object.
            The ``callback`` argument shall be specified. Otherwise an exception
            will occur upon timer expiration:
            ``TypeError: 'NoneType' object isn't callable``
        """
        ...

class UART:
    @overload
    def __init__(
        self,
        id: ID_T,
        /,
        baudrate: int = 9600,
        bits: int = 8,
        parity: int | None = None,
        stop: int = 1,
        *,
        tx: PinLike | None = None,
        rx: PinLike | None = None,
        txbuf: int | None = None,
        rxbuf: int | None = None,
        timeout: int | None = None,
        timeout_char: int | None = None,
        invert: int | None = None,
    ):
        """
        Construct a UART object of the given id.
        """

    @overload
    def __init__(
        self,
        id: ID_T,
        /,
        baudrate: int = 9600,
        bits: int = 8,
        parity: int | None = None,
        stop: int = 1,
        *,
        pins: tuple[PinLike, PinLike] | None = None,
    ):
        """
        Construct a UART object of the given id from a tuple of two pins.
        """

    @overload
    def __init__(
        self,
        id: ID_T,
        /,
        baudrate: int = 9600,
        bits: int = 8,
        parity: int | None = None,
        stop: int = 1,
        *,
        pins: tuple[PinLike, PinLike, PinLike, PinLike] | None = None,
    ):
        """
        Construct a UART object of the given id from a tuple of four pins.
        """

    @overload
    def init(
        self,
        /,
        baudrate: int = 9600,
        bits: int = 8,
        parity: int | None = None,
        stop: int = 1,
        *,
        tx: PinLike | None = None,
        rx: PinLike | None = None,
        txbuf: int | None = None,
        rxbuf: int | None = None,
        timeout: int | None = None,
        timeout_char: int | None = None,
        invert: int | None = None,
    ) -> None:
        """
        Initialise the UART bus with the given parameters:

          - *baudrate* is the clock rate.
          - *bits* is the number of bits per character, 7, 8 or 9.
          - *parity* is the parity, ``None``, 0 (even) or 1 (odd).
          - *stop* is the number of stop bits, 1 or 2.

        Additional keyword-only parameters that may be supported by a port are:

          - *tx* specifies the TX pin to use.
          - *rx* specifies the RX pin to use.
          - *rts* specifies the RTS (output) pin to use for hardware receive flow control.
          - *cts* specifies the CTS (input) pin to use for hardware transmit flow control.
          - *txbuf* specifies the length in characters of the TX buffer.
          - *rxbuf* specifies the length in characters of the RX buffer.
          - *timeout* specifies the time to wait for the first character (in ms).
          - *timeout_char* specifies the time to wait between characters (in ms).
          - *invert* specifies which lines to invert.

              - ``0`` will not invert lines (idle state of both lines is logic high).
              - ``UART.INV_TX`` will invert TX line (idle state of TX line now logic low).
              - ``UART.INV_RX`` will invert RX line (idle state of RX line now logic low).
              - ``UART.INV_TX | UART.INV_RX`` will invert both lines (idle state at logic low).

          - *flow* specifies which hardware flow control signals to use. The value
            is a bitmask.

              - ``0`` will ignore hardware flow control signals.
              - ``UART.RTS`` will enable receive flow control by using the RTS output pin to
                signal if the receive FIFO has sufficient space to accept more data.
              - ``UART.CTS`` will enable transmit flow control by pausing transmission when the
                CTS input pin signals that the receiver is running low on buffer space.
              - ``UART.RTS | UART.CTS`` will enable both, for full hardware flow control.

        On the WiPy only the following keyword-only parameter is supported:

          - *pins* is a 4 or 2 item list indicating the TX, RX, RTS and CTS pins (in that order).
            Any of the pins can be None if one wants the UART to operate with limited functionality.
            If the RTS pin is given the RX pin must be given as well. The same applies to CTS.
            When no pins are given, then the default set of TX and RX pins is taken, and hardware
            flow control will be disabled. If *pins* is ``None``, no pin assignment will be made.

        .. note::
          It is possible to call ``init()`` multiple times on the same object in
          order to reconfigure  UART on the fly. That allows using single UART
          peripheral to serve different devices attached to different GPIO pins.
          Only one device can be served at a time in that case.
          Also do not call ``deinit()`` as it will prevent calling ``init()``
          again.
        """

    @overload
    def init(
        self,
        /,
        baudrate: int = 9600,
        bits: int = 8,
        parity: int | None = None,
        stop: int = 1,
        *,
        pins: tuple[PinLike, PinLike] | None = None,
    ) -> None:
        """
        Initialise the UART bus with the given parameters:

          - *baudrate* is the clock rate.
          - *bits* is the number of bits per character, 7, 8 or 9.
          - *parity* is the parity, ``None``, 0 (even) or 1 (odd).
          - *stop* is the number of stop bits, 1 or 2.

        Additional keyword-only parameters that may be supported by a port are:

          - *tx* specifies the TX pin to use.
          - *rx* specifies the RX pin to use.
          - *rts* specifies the RTS (output) pin to use for hardware receive flow control.
          - *cts* specifies the CTS (input) pin to use for hardware transmit flow control.
          - *txbuf* specifies the length in characters of the TX buffer.
          - *rxbuf* specifies the length in characters of the RX buffer.
          - *timeout* specifies the time to wait for the first character (in ms).
          - *timeout_char* specifies the time to wait between characters (in ms).
          - *invert* specifies which lines to invert.

              - ``0`` will not invert lines (idle state of both lines is logic high).
              - ``UART.INV_TX`` will invert TX line (idle state of TX line now logic low).
              - ``UART.INV_RX`` will invert RX line (idle state of RX line now logic low).
              - ``UART.INV_TX | UART.INV_RX`` will invert both lines (idle state at logic low).

          - *flow* specifies which hardware flow control signals to use. The value
            is a bitmask.

              - ``0`` will ignore hardware flow control signals.
              - ``UART.RTS`` will enable receive flow control by using the RTS output pin to
                signal if the receive FIFO has sufficient space to accept more data.
              - ``UART.CTS`` will enable transmit flow control by pausing transmission when the
                CTS input pin signals that the receiver is running low on buffer space.
              - ``UART.RTS | UART.CTS`` will enable both, for full hardware flow control.

        On the WiPy only the following keyword-only parameter is supported:

          - *pins* is a 4 or 2 item list indicating the TX, RX, RTS and CTS pins (in that order).
            Any of the pins can be None if one wants the UART to operate with limited functionality.
            If the RTS pin is given the RX pin must be given as well. The same applies to CTS.
            When no pins are given, then the default set of TX and RX pins is taken, and hardware
            flow control will be disabled. If *pins* is ``None``, no pin assignment will be made.

        .. note::
          It is possible to call ``init()`` multiple times on the same object in
          order to reconfigure  UART on the fly. That allows using single UART
          peripheral to serve different devices attached to different GPIO pins.
          Only one device can be served at a time in that case.
          Also do not call ``deinit()`` as it will prevent calling ``init()``
          again.
        """

    @overload
    def init(
        self,
        /,
        baudrate: int = 9600,
        bits: int = 8,
        parity: int | None = None,
        stop: int = 1,
        *,
        pins: tuple[PinLike, PinLike, PinLike, PinLike] | None = None,
    ) -> None:
        """
        Initialise the UART bus with the given parameters:

          - *baudrate* is the clock rate.
          - *bits* is the number of bits per character, 7, 8 or 9.
          - *parity* is the parity, ``None``, 0 (even) or 1 (odd).
          - *stop* is the number of stop bits, 1 or 2.

        Additional keyword-only parameters that may be supported by a port are:

          - *tx* specifies the TX pin to use.
          - *rx* specifies the RX pin to use.
          - *rts* specifies the RTS (output) pin to use for hardware receive flow control.
          - *cts* specifies the CTS (input) pin to use for hardware transmit flow control.
          - *txbuf* specifies the length in characters of the TX buffer.
          - *rxbuf* specifies the length in characters of the RX buffer.
          - *timeout* specifies the time to wait for the first character (in ms).
          - *timeout_char* specifies the time to wait between characters (in ms).
          - *invert* specifies which lines to invert.

              - ``0`` will not invert lines (idle state of both lines is logic high).
              - ``UART.INV_TX`` will invert TX line (idle state of TX line now logic low).
              - ``UART.INV_RX`` will invert RX line (idle state of RX line now logic low).
              - ``UART.INV_TX | UART.INV_RX`` will invert both lines (idle state at logic low).

          - *flow* specifies which hardware flow control signals to use. The value
            is a bitmask.

              - ``0`` will ignore hardware flow control signals.
              - ``UART.RTS`` will enable receive flow control by using the RTS output pin to
                signal if the receive FIFO has sufficient space to accept more data.
              - ``UART.CTS`` will enable transmit flow control by pausing transmission when the
                CTS input pin signals that the receiver is running low on buffer space.
              - ``UART.RTS | UART.CTS`` will enable both, for full hardware flow control.

        On the WiPy only the following keyword-only parameter is supported:

          - *pins* is a 4 or 2 item list indicating the TX, RX, RTS and CTS pins (in that order).
            Any of the pins can be None if one wants the UART to operate with limited functionality.
            If the RTS pin is given the RX pin must be given as well. The same applies to CTS.
            When no pins are given, then the default set of TX and RX pins is taken, and hardware
            flow control will be disabled. If *pins* is ``None``, no pin assignment will be made.

        .. note::
          It is possible to call ``init()`` multiple times on the same object in
          order to reconfigure  UART on the fly. That allows using single UART
          peripheral to serve different devices attached to different GPIO pins.
          Only one device can be served at a time in that case.
          Also do not call ``deinit()`` as it will prevent calling ``init()``
          again.
        """

    @overload
    def read(self) -> bytes | None:
        """
        Read characters.  If ``nbytes`` is specified then read at most that many bytes,
        otherwise read as much data as possible. It may return sooner if a timeout
        is reached. The timeout is configurable in the constructor.

        Return value: a bytes object containing the bytes read in.  Returns ``None``
        on timeout.
        """

    @overload
    def read(self, nbytes: int, /) -> bytes | None:
        """
        Read characters.  If ``nbytes`` is specified then read at most that many bytes,
        otherwise read as much data as possible. It may return sooner if a timeout
        is reached. The timeout is configurable in the constructor.

        Return value: a bytes object containing the bytes read in.  Returns ``None``
        on timeout.
        """

    @overload
    def readinto(self, buf: AnyWritableBuf, /) -> int | None:
        """
        Read bytes into the ``buf``.  If ``nbytes`` is specified then read at most
        that many bytes.  Otherwise, read at most ``len(buf)`` bytes. It may return sooner if a timeout
        is reached. The timeout is configurable in the constructor.

        Return value: number of bytes read and stored into ``buf`` or ``None`` on
        timeout.
        """

    @overload
    def readinto(self, buf: AnyWritableBuf, nbytes: int, /) -> int | None:
        """
        Read bytes into the ``buf``.  If ``nbytes`` is specified then read at most
        that many bytes.  Otherwise, read at most ``len(buf)`` bytes. It may return sooner if a timeout
        is reached. The timeout is configurable in the constructor.

        Return value: number of bytes read and stored into ``buf`` or ``None`` on
        timeout.
        """

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
    Returns the CPU frequency in hertz.

    On some ports this can also be used to set the CPU frequency by passing in *hz*.
    """

@overload
def freq(
    self,
    value: int,
    /,
) -> None:
    """
    Returns the CPU frequency in hertz.

    On some ports this can also be used to set the CPU frequency by passing in *hz*.
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
