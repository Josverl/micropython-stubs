"""
Functions related to the hardware.

MicroPython module: https://docs.micropython.org/en/v1.29.0/library/machine.html

The ``machine`` module contains specific functions related to the hardware
on a particular board. Most functions in this module allow to achieve direct
and unrestricted access to and control of hardware blocks on a system
(like CPU, timers, buses, etc.). Used incorrectly, this can lead to
malfunction, lockups, crashes of your board, and in extreme cases, hardware
damage.

---
Module: 'machine' on micropython-v1.29.0-nrf-SEEED_XIAO_NRF52
"""

# MCU: {'variant': '', 'build': '', 'arch': 'armv7emsp', 'port': 'nrf', 'board': 'SEEED_XIAO_NRF52', 'board_id': 'SEEED_XIAO_NRF52', 'mpy': 'v6.3', 'ver': '1.29.0', 'family': 'micropython', 'cpu': 'NRF52840', 'version': '1.29.0'}
# Stubber: v1.28.6
from __future__ import annotations

from typing import Any, Callable, Final, Iterable, NoReturn, Optional, Sequence, Tuple, overload

from _mpy_shed import _IRQ, AnyReadableBuf, AnyWritableBuf, mp_available
from _mpy_shed.mp_mem import _MemoryObject as _MemoryObject
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar, deprecated
from vfs import AbstractBlockDev

PWRON_RESET: Final[int] = 16
"""Reset causes."""
LOCKUP_RESET: Final[int] = 3
LPCOMP_RESET: Final[int] = 17
NFC_RESET: Final[int] = 19
SOFT_RESET: Final[int] = 2
"""Reset causes."""
WDT_RESET: Final[int] = 1
"""Reset causes."""
DEBUG_IF_RESET: Final[int] = 18
HARD_RESET: Final[int] = 0
"""Reset causes."""
IDLE: Incomplete
"""IRQ wake values."""
SLEEP: Incomplete
"""IRQ wake values."""
DEEPSLEEP: Incomplete
"""IRQ wake values."""
DEEPSLEEP_RESET: Incomplete
"""Reset causes."""
WLAN_WAKE: Incomplete
"""Wake-up reasons."""
PIN_WAKE: Incomplete
"""Wake-up reasons."""
RTC_WAKE: Incomplete
"""Wake-up reasons."""
_IRQ_STATE: TypeAlias = int
ATTN_0DB: int = ...
__CANFilter: TypeAlias = tuple[int, int, int] | list[int]
__CANRecvResult: TypeAlias = tuple[int, memoryview, int, int]
__CANCounters: TypeAlias = list[int | None]
__CANTimings: TypeAlias = list[int | list[int] | None]
ID_T: TypeAlias = int | str
_PinLike: TypeAlias = Pin | int | str

def info(*args, **kwargs) -> Incomplete: ...
def idle() -> None:
    """
    Gates the clock to the CPU, useful to reduce power consumption at any time
    during short or long periods. Peripherals continue working and execution
    resumes as soon as any interrupt is triggered, or at most one millisecond
    after the CPU was paused.

    It is recommended to call this function inside any tight loop that is
    continuously checking for an external change (i.e. polling). This will reduce
    power consumption without significantly impacting performance. To reduce
    power consumption further then see the :func:`lightsleep`,
    :func:`time.sleep()` and :func:`time.sleep_ms()` functions.
    """
    ...

def disable_irq() -> _IRQ_STATE:
    """
    Disable interrupt requests.
    Returns the previous IRQ state which should be considered an opaque value.
    This return value should be passed to the `enable_irq()` function to restore
    interrupts to their original state, before `disable_irq()` was called.
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

def enable_irq(state: _IRQ_STATE, /) -> None:
    """
    Re-enable interrupt requests.
    The *state* parameter should be the value that was returned from the most
    recent call to the `disable_irq()` function.
    """
    ...

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

@deprecated("use :func:`lightsleep()` instead.")
def sleep() -> None:
    """
    ``Note:`` This function is deprecated, use :func:`lightsleep()` instead with no arguments.
    """
    ...

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

def soft_reset() -> NoReturn:
    """
    Performs a :ref:`soft reset <soft_reset>` of the interpreter, deleting all
    Python objects and resetting the Python heap.
    """
    ...

def mem_backup(region=0) -> Tuple:
    """
    Return a writable `memoryview` over a persistent hardware memory region that
    survives at least :ref:`soft_reset` on all ports; battery-backed ports also
    survive power-off. Per-port persistence guarantees vary, see the table below.

    *region* selects which backup region to access (default 0, the primary region).
    Pass ``-1`` to get a tuple of all available regions instead.

    The element type depends on the port's hardware alignment requirements:
    ``'B'`` (unsigned byte) on ports with byte-addressable backup memory,
    ``'I'`` (unsigned 32-bit) on ports backed by word-sized registers.
    Use ``mem.itemsize`` to discover the access granularity at runtime.

    The total size in bytes is ``len(mem) * mem.itemsize``, where ``len(mem)``
    is the number of elements and ``mem.itemsize`` is the size of each element.
    For example, on a port with 4 word-sized registers, ``len(mem)`` is 4 and
    ``mem.itemsize`` is 4, giving 16 bytes total. On a port with 4096 bytes
    of byte-addressable backup SRAM, ``len(mem)`` is 4096 and ``mem.itemsize``
    is 1.

    Cross-port guarantees for portable code: ``mem.itemsize`` is either ``1``
    or ``4``; valid indices are ``0..len(mem)-1``; out-of-range access raises
    ``IndexError``; values are stored in host-native byte order. Region index
    semantics are not portable, see notes below for ``stm32`` in particular.

    Usage::

       import machine

       mem = machine.mem_backup()
       mem[0] = 0x12345678                # write element 0
       print(hex(mem[0]))                 # read element 0
       print(len(mem))                    # number of elements
       print(mem.itemsize)                # bytes per element
       print(len(mem) * mem.itemsize)     # total bytes available

       # Discover all available regions
       for i, r in enumerate(machine.mem_backup(-1)):
           print(i, len(r), r.itemsize)

    The total byte size and backing hardware vary by port:

    ======  ===============================================  ===========  ==============
    Port    Backing storage                                  Total bytes  Battery-backed
    ======  ===============================================  ===========  ==============
    alif    Backup SRAM                                      4080         yes
    esp32   RTC slow memory                                  2048         no
    mimxrt  SNVS LPGPR registers (4 per chip)                12-16        yes
    nrf     POWER GPREGRET registers                         1-2          no
    rp2     Watchdog scratch registers                       28-60        no
    samd    Backup RAM (SAMD51 only)                         8192         yes
    stm32   Backup SRAM + BKP registers (F4/F7/H5/H7/U5/N6)  2048-8192    yes
    stm32   RTC BKP registers (other families)               20-128       yes
    ======  ===============================================  ===========  ==============

    .. note::

       On esp32 and rp2, data persists across :ref:`soft_reset`,
       `machine.reset()` and `machine.deepsleep()` wake but is lost on
       power-off and on poweron-style resets. On esp32 in particular this
       includes pressing the EN/RESET button on most dev boards, which the
       chip reports as a power-on reset.

    Some ports split backup storage across multiple regions, or exclude
    registers reserved by the bootloader or system firmware:

    ======  ====================  ================================================
    Port    Register(s)           Note
    ======  ====================  ================================================
    mimxrt  LPGPR[3]              Excluded; used by TinyUF2 (when used)
    rp2     scratch[4]            Excluded; used by pico-sdk on reset
    rp2     powman scratch[0..7]  Region 2 on RP2350 only
    stm32   BKP registers         Region 1 on BKPSRAM families (F4/F7/H5/H7/U5/N6)
    ======  ====================  ================================================

    Use ``machine.mem_backup(-1)`` to discover available regions and their sizes.

    On stm32 the region index does not have a uniform meaning across boards:
    region 0 is BKPSRAM (``itemsize=1``) on BKPSRAM families and BKP registers
    (``itemsize=4``) on others. Portable code should branch on ``mem.itemsize``
    before structuring data.

    Some registers within a region are accessible but reserved by convention
    and should not be overwritten.  The BKP register file is region 1 on
    BKPSRAM families and region 0 on the others:

    ======  ==============  =========================================================
    Port    Register(s)     Used by
    ======  ==============  =========================================================
    stm32   BKP0R           Arduino bootloader (Portenta H7, Giga, Opta, Nicla)
    stm32   BKP16R-BKP18R   ``rfcore_firmware.py`` on STM32WB
    stm32   last BKP reg    clock frequency (``MICROPY_HW_CLK_LAST_FREQ``)
    stm32   BKP31R (N6)     mboot bootloader entry
    ======  ==============  =========================================================

    The buffer allows direct register access and can be combined with
    ``uctypes`` for structured layouts::

       import machine, uctypes

       mem = machine.mem_backup()

       # Structured access via uctypes (check len(mem) for your board)
       layout = {
           "flags": (0 * 4, uctypes.UINT32),    # register 0
           "counter": (1 * 4, uctypes.UINT32),  # register 1
       }
       regs = uctypes.struct(uctypes.addressof(mem), layout)
       regs.flags = 0x01
       print(regs.counter)

    Availability: alif, esp32, mimxrt, nrf, rp2, samd, stm32 ports.
    """
    ...

def reset_cause() -> int:
    """
    Get the reset cause. See :ref:`constants <machine_constants>` for the possible return values.
    """
    ...

def reset() -> NoReturn:
    """
    :ref:`Hard resets <hard_reset>` the device in a manner similar to pushing the
    external RESET button.
    """
    ...

def unique_id() -> bytes:
    """
    Returns a byte string with a unique identifier of a board/SoC. It will vary
    from a board/SoC instance to another, if underlying hardware allows. Length
    varies by hardware (so use substring of a full value if you expect a short
    ID). In some MicroPython ports, ID corresponds to the network MAC address.
    """
    ...

def bootloader(value: Optional[Any] = None) -> None:
    """
    Reset the device and enter its bootloader.  This is typically used to put the
    device into a state where it can be programmed with new firmware.

    Some ports support passing in an optional *value* argument which can control
    which bootloader to enter, what to pass to it, or other things.
    """
    ...

class RTCounter:
    ONESHOT: Final[int] = 0
    FREQUENCY: Final[int] = 8
    PERIODIC: Final[int] = 1
    def counter(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def stop(self, *args, **kwargs) -> Incomplete: ...
    def start(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Pin:
    """
    A pin object is used to control I/O pins (also known as GPIO - general-purpose
    input/output).  Pin objects are commonly associated with a physical pin that can
    drive an output voltage and read input voltages.  The pin class has methods to set the mode of
    the pin (IN, OUT, etc) and methods to get and set the digital logic level.
    For analog control of a pin, see the :class:`ADC` class.

    A pin object is constructed by using an identifier which unambiguously
    specifies a certain I/O pin.  The allowed forms of the identifier and the
    physical pin that the identifier maps to are port-specific.  Possibilities
    for the identifier are an integer, a string or a tuple with port and pin
    number.

    Usage Model::

        from machine import Pin

        # create an output pin on pin #0
        p0 = Pin(0, Pin.OUT)

        # set the value low then high
        p0.value(0)
        p0.value(1)

        # create an input pin on pin #2, with a pull up resistor
        p2 = Pin(2, Pin.IN, Pin.PULL_UP)

        # read and print the pin value
        print(p2.value())

        # reconfigure pin #0 in input mode with a pull down resistor
        p0.init(p0.IN, p0.PULL_DOWN)

        # configure an irq callback
        p0.irq(lambda p:print(p))
    """

    PULL_DOWN: Final[int] = 1
    """\
    Selects whether there is a pull up/down resistor.  Use the value
    ``None`` for no pull.
    
    Some ports have a different constants set that can be used to select
    hardware-specific behaviour:
    
    - The esp8266 port does not have pull-down resistors on GPIO pins, hence
    ``Pin.PULL_DOWN`` is not supported.
    - The mimxrt port has several extra constants to enable different pull
    modes: ``Pin.PULL_UP_22K`` enables a 22KΩ pull-up on the pin,
    ``Pin.PULL_UP_47K`` enables a 47KΩ pull-up on the pin, and
    ``Pin.PULL_HOLD`` that puts the pin into high-impedance mode.  The
    ``Pin.PULL_UP`` and ``Pin.PULL_DOWN`` constants will use a 100KΩ internal
    resistor.
    """
    IRQ_RISING: Final[int] = 1
    """Selects the IRQ trigger type."""
    OUT: Final[int] = 1
    """Selects the pin mode."""
    PULL_DISABLED: Final[int] = 0
    PULL_UP: Final[int] = 3
    """\
    Selects whether there is a pull up/down resistor.  Use the value
    ``None`` for no pull.
    
    Some ports have a different constants set that can be used to select
    hardware-specific behaviour:
    
    - The esp8266 port does not have pull-down resistors on GPIO pins, hence
    ``Pin.PULL_DOWN`` is not supported.
    - The mimxrt port has several extra constants to enable different pull
    modes: ``Pin.PULL_UP_22K`` enables a 22KΩ pull-up on the pin,
    ``Pin.PULL_UP_47K`` enables a 47KΩ pull-up on the pin, and
    ``Pin.PULL_HOLD`` that puts the pin into high-impedance mode.  The
    ``Pin.PULL_UP`` and ``Pin.PULL_DOWN`` constants will use a 100KΩ internal
    resistor.
    """
    IRQ_FALLING: Final[int] = 2
    """Selects the IRQ trigger type."""
    IN: Final[int] = 0
    """Selects the pin mode."""
    OPEN_DRAIN: Incomplete
    ALT: Incomplete
    ALT_OPEN_DRAIN: Incomplete
    ANALOG: Incomplete
    DRIVE_0: int
    DRIVE_1: int
    DRIVE_2: int
    IRQ_LOW_LEVEL: Incomplete
    IRQ_HIGH_LEVEL: Incomplete
    PULL_HOLD: int
    def name(self, *args, **kwargs) -> Incomplete: ...
    def names(self, *args, **kwargs) -> Incomplete: ...
    @overload
    def mode(self) -> int:
        """
        Get or set the pin mode.
        See the constructor documentation for details of the ``mode`` argument.

        Availability: cc3200, psoc-edge, stm32 ports.
        """

    @overload
    def mode(self, mode: int, /) -> None:
        """
        Get or set the pin mode.
        See the constructor documentation for details of the ``mode`` argument.

        Availability: cc3200, psoc-edge, stm32 ports.
        """
    def low(self) -> None:
        """
        Set pin to "0" output level.

        Availability: mimxrt, nrf, psoc-edge, renesas-ra, rp2, samd, stm32 ports.
        """
        ...

    @overload
    def pull(self) -> int:
        """
        Get or set the pin pull state.
        See the constructor documentation for details of the ``pull`` argument.

        Availability: cc3200, psoc-edge, stm32 ports.
        """

    @overload
    def pull(self, pull: int, /) -> None:
        """
        Get or set the pin pull state.
        See the constructor documentation for details of the ``pull`` argument.

        Availability: cc3200, psoc-edge, stm32 ports.
        """
    def off(self) -> None:
        """
        Set pin to "0" output level.
        """
        ...
    def port(self, *args, **kwargs) -> Incomplete: ...
    def pin(self, *args, **kwargs) -> Incomplete: ...
    def on(self) -> None:
        """
        Set pin to "1" output level.
        """
        ...
    def irq(
        self,
        /,
        handler: Callable[[Pin], None] | None = None,
        trigger: int = (IRQ_FALLING | IRQ_RISING),
        *,
        priority: int = 1,
        wake: int | None = None,
        hard: bool = False,
    ) -> _IRQ:
        """
           Configure an interrupt handler to be called when the trigger source of the
           pin is active.  If the pin mode is ``Pin.IN`` then the trigger source is
           the external value on the pin.  If the pin mode is ``Pin.OUT`` then the
           trigger source is the output buffer of the pin.  Otherwise, if the pin mode
           is ``Pin.OPEN_DRAIN`` then the trigger source is the output buffer for
           state '0' and the external pin value for state '1'.

           The arguments are:

             - ``handler`` is an optional function to be called when the interrupt
               triggers. The handler must take exactly one argument which is the
               ``Pin`` instance.

             - ``trigger`` configures the event which can generate an interrupt.
               Possible values are:

               - ``Pin.IRQ_FALLING`` interrupt on falling edge.
               - ``Pin.IRQ_RISING`` interrupt on rising edge.
               - ``Pin.IRQ_LOW_LEVEL`` interrupt on low level.
               - ``Pin.IRQ_HIGH_LEVEL`` interrupt on high level.

               These values can be OR'ed together to trigger on multiple events.

             - ``priority`` sets the priority level of the interrupt.  The values it
               can take are port-specific, but higher values always represent higher
               priorities.

             - ``wake`` selects the power mode in which this interrupt can wake up the
               system.  It can be ``machine.IDLE``, ``machine.SLEEP`` or ``machine.DEEPSLEEP``.
               These values can also be OR'ed together to make a pin generate interrupts in
               more than one power mode.

             - ``hard`` if true a hardware interrupt is used. This reduces the delay
               between the pin change and the handler being called. Hard interrupt
               handlers may not allocate memory; see :ref:`isr_rules`.
               Not all ports support this argument.

           This method returns a callback object.

        The following methods are not part of the core Pin API and only implemented on certain ports.
        """
        ...
    def af_list(self, *args, **kwargs) -> Incomplete: ...
    def af(self, *args, **kwargs) -> Incomplete: ...
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
    def high(self) -> None:
        """
        Set pin to "1" output level.

        Availability: mimxrt, nrf, psoc-edge, renesas-ra, rp2, samd, stm32 ports.
        """
        ...
    def init(
        self,
        mode: int = -1,
        pull: int = -1,
        *,
        value: Any = None,
        drive: int | None = None,
        alt: int | None = None,
    ) -> None:
        """
        Re-initialise the pin using the given parameters.  Only those arguments that
        are specified will be set.  The rest of the pin peripheral state will remain
        unchanged.  See the constructor documentation for details of the arguments.

        Returns ``None``.
        """
        ...
    @classmethod
    def dict(cls, *args, **kwargs) -> Incomplete: ...

    class cpu:
        P37: Pin  ## = Pin(37, mode=IN, pull=PULL_DISABLED)
        P9: Pin  ## = Pin(9, mode=IN, pull=PULL_DISABLED)
        P36: Pin  ## = Pin(36, mode=IN, pull=PULL_DISABLED)
        P4: Pin  ## = Pin(4, mode=IN, pull=PULL_DISABLED)
        P38: Pin  ## = Pin(38, mode=IN, pull=PULL_DISABLED)
        P39: Pin  ## = Pin(39, mode=IN, pull=PULL_DISABLED)
        P31: Pin  ## = Pin(31, mode=IN, pull=PULL_DISABLED)
        P35: Pin  ## = Pin(35, mode=IN, pull=PULL_DISABLED)
        P30: Pin  ## = Pin(30, mode=OUT, pull=PULL_DISABLED)
        P34: Pin  ## = Pin(34, mode=IN, pull=PULL_DISABLED)
        P32: Pin  ## = Pin(32, mode=IN, pull=PULL_DISABLED)
        P33: Pin  ## = Pin(33, mode=IN, pull=PULL_DISABLED)
        P5: Pin  ## = Pin(5, mode=IN, pull=PULL_DISABLED)
        P40: Pin  ## = Pin(40, mode=OUT, pull=PULL_DISABLED)
        P47: Pin  ## = Pin(47, mode=IN, pull=PULL_DISABLED)
        P8: Pin  ## = Pin(8, mode=IN, pull=PULL_DISABLED)
        P6: Pin  ## = Pin(6, mode=OUT, pull=PULL_DISABLED)
        P7: Pin  ## = Pin(7, mode=IN, pull=PULL_DISABLED)
        P42: Pin  ## = Pin(42, mode=IN, pull=PULL_DISABLED)
        P46: Pin  ## = Pin(46, mode=IN, pull=PULL_DISABLED)
        P41: Pin  ## = Pin(41, mode=IN, pull=PULL_DISABLED)
        P45: Pin  ## = Pin(45, mode=IN, pull=PULL_DISABLED)
        P43: Pin  ## = Pin(43, mode=IN, pull=PULL_DISABLED)
        P44: Pin  ## = Pin(44, mode=IN, pull=PULL_DISABLED)
        P15: Pin  ## = Pin(15, mode=IN, pull=PULL_DISABLED)
        P3: Pin  ## = Pin(3, mode=IN, pull=PULL_DISABLED)
        P14: Pin  ## = Pin(14, mode=IN, pull=PULL_DISABLED)
        P18: Pin  ## = Pin(18, mode=IN, pull=PULL_DISABLED)
        P16: Pin  ## = Pin(16, mode=IN, pull=PULL_DISABLED)
        P17: Pin  ## = Pin(17, mode=OUT, pull=PULL_DISABLED)
        P1: Pin  ## = Pin(1, mode=IN, pull=PULL_DISABLED)
        P13: Pin  ## = Pin(13, mode=IN, pull=PULL_DISABLED)
        P0: Pin  ## = Pin(0, mode=IN, pull=PULL_DISABLED)
        P12: Pin  ## = Pin(12, mode=IN, pull=PULL_DISABLED)
        P10: Pin  ## = Pin(10, mode=IN, pull=PULL_DISABLED)
        P11: Pin  ## = Pin(11, mode=IN, pull=PULL_DISABLED)
        P26: Pin  ## = Pin(26, mode=OUT, pull=PULL_DISABLED)
        P19: Pin  ## = Pin(19, mode=IN, pull=PULL_DISABLED)
        P25: Pin  ## = Pin(25, mode=IN, pull=PULL_DISABLED)
        P29: Pin  ## = Pin(29, mode=IN, pull=PULL_DISABLED)
        P27: Pin  ## = Pin(27, mode=IN, pull=PULL_DISABLED)
        P28: Pin  ## = Pin(28, mode=IN, pull=PULL_DISABLED)
        P20: Pin  ## = Pin(20, mode=IN, pull=PULL_DISABLED)
        P24: Pin  ## = Pin(24, mode=IN, pull=PULL_DISABLED)
        P2: Pin  ## = Pin(2, mode=IN, pull=PULL_DISABLED)
        P23: Pin  ## = Pin(23, mode=IN, pull=PULL_DISABLED)
        P21: Pin  ## = Pin(21, mode=IN, pull=PULL_DISABLED)
        P22: Pin  ## = Pin(22, mode=IN, pull=PULL_DISABLED)
        def __init__(self, *argv, **kwargs) -> None: ...

    @classmethod
    def mapper(cls, *args, **kwargs) -> Incomplete: ...

    class board:
        P42: Pin  ## = Pin(42, mode=IN, pull=PULL_DISABLED)
        UART1_TX: Pin  ## = Pin(43, mode=IN, pull=PULL_DISABLED)
        P41: Pin  ## = Pin(41, mode=IN, pull=PULL_DISABLED)
        PDM_CLK: Pin  ## = Pin(32, mode=IN, pull=PULL_DISABLED)
        P6: Pin  ## = Pin(6, mode=OUT, pull=PULL_DISABLED)
        P8: Pin  ## = Pin(8, mode=IN, pull=PULL_DISABLED)
        P35: Pin  ## = Pin(35, mode=IN, pull=PULL_DISABLED)
        P39: Pin  ## = Pin(39, mode=IN, pull=PULL_DISABLED)
        P34: Pin  ## = Pin(34, mode=IN, pull=PULL_DISABLED)
        P38: Pin  ## = Pin(38, mode=IN, pull=PULL_DISABLED)
        P36: Pin  ## = Pin(36, mode=IN, pull=PULL_DISABLED)
        P37: Pin  ## = Pin(37, mode=IN, pull=PULL_DISABLED)
        SPI0_MISO: Pin  ## = Pin(46, mode=IN, pull=PULL_DISABLED)
        PDM_DATA: Pin  ## = Pin(16, mode=IN, pull=PULL_DISABLED)
        READ_BAT: Pin  ## = Pin(14, mode=IN, pull=PULL_DISABLED)
        UART1_RX: Pin  ## = Pin(44, mode=IN, pull=PULL_DISABLED)
        SPI0_MOSI: Pin  ## = Pin(47, mode=IN, pull=PULL_DISABLED)
        SPI0_SCK: Pin  ## = Pin(45, mode=IN, pull=PULL_DISABLED)
        QSPI_D0: Pin  ## = Pin(20, mode=IN, pull=PULL_DISABLED)
        QSPI_SCK: Pin  ## = Pin(21, mode=IN, pull=PULL_DISABLED)
        QSPI_CS: Pin  ## = Pin(25, mode=IN, pull=PULL_DISABLED)
        QSPI_D3: Pin  ## = Pin(23, mode=IN, pull=PULL_DISABLED)
        QSPI_D1: Pin  ## = Pin(24, mode=IN, pull=PULL_DISABLED)
        QSPI_D2: Pin  ## = Pin(22, mode=IN, pull=PULL_DISABLED)
        IMU_INT1: Pin  ## = Pin(11, mode=IN, pull=PULL_DISABLED)
        P33: Pin  ## = Pin(33, mode=IN, pull=PULL_DISABLED)
        D5_A5: Pin  ## = Pin(5, mode=IN, pull=PULL_DISABLED)
        IMU_SDA: Pin  ## = Pin(7, mode=IN, pull=PULL_DISABLED)
        IMU_PWR: Pin  ## = Pin(40, mode=OUT, pull=PULL_DISABLED)
        IMU_SCL: Pin  ## = Pin(27, mode=IN, pull=PULL_DISABLED)
        D0_A0: Pin  ## = Pin(2, mode=IN, pull=PULL_DISABLED)
        D4_A4: Pin  ## = Pin(4, mode=IN, pull=PULL_DISABLED)
        ADC0_BAT: Pin  ## = Pin(31, mode=IN, pull=PULL_DISABLED)
        D3_A3: Pin  ## = Pin(29, mode=IN, pull=PULL_DISABLED)
        D1_A1: Pin  ## = Pin(3, mode=IN, pull=PULL_DISABLED)
        D2_A2: Pin  ## = Pin(28, mode=IN, pull=PULL_DISABLED)
        P18: Pin  ## = Pin(18, mode=IN, pull=PULL_DISABLED)
        NFC1: Pin  ## = Pin(9, mode=IN, pull=PULL_DISABLED)
        P17: Pin  ## = Pin(17, mode=OUT, pull=PULL_DISABLED)
        P30: Pin  ## = Pin(30, mode=OUT, pull=PULL_DISABLED)
        P19: Pin  ## = Pin(19, mode=IN, pull=PULL_DISABLED)
        P26: Pin  ## = Pin(26, mode=OUT, pull=PULL_DISABLED)
        P0: Pin  ## = Pin(0, mode=IN, pull=PULL_DISABLED)
        P15: Pin  ## = Pin(15, mode=IN, pull=PULL_DISABLED)
        NFC2: Pin  ## = Pin(10, mode=IN, pull=PULL_DISABLED)
        P13: Pin  ## = Pin(13, mode=IN, pull=PULL_DISABLED)
        P1: Pin  ## = Pin(1, mode=IN, pull=PULL_DISABLED)
        P12: Pin  ## = Pin(12, mode=IN, pull=PULL_DISABLED)
        def __init__(self, *argv, **kwargs) -> None: ...

    def __init__(
        self,
        id: Any,
        /,
        mode: int = -1,
        pull: int = -1,
        *,
        value: Any = None,
        drive: int | None = None,
        alt: int | None = None,
    ) -> None:
        """
        Access the pin peripheral (GPIO pin) associated with the given ``id``.  If
        additional arguments are given in the constructor then they are used to initialise
        the pin.  Any settings that are not specified will remain in their previous state.

        The arguments are:

          - ``id`` is mandatory and can be an arbitrary object.  Among possible value
            types are: int (an internal Pin identifier), str (a Pin name), and tuple
            (pair of [port, pin]).

          - ``mode`` specifies the pin mode, which can be one of:

            - ``Pin.IN`` - Pin is configured for input.  If viewed as an output the pin
              is in high-impedance state.

            - ``Pin.OUT`` - Pin is configured for (normal) output.

            - ``Pin.OPEN_DRAIN`` - Pin is configured for open-drain output. Open-drain
              output works in the following way: if the output value is set to 0 the pin
              is active at a low level; if the output value is 1 the pin is in a high-impedance
              state.  Not all ports implement this mode, or some might only on certain pins.

            - ``Pin.ALT`` - Pin is configured to perform an alternative function, which is
              port specific.  For a pin configured in such a way any other Pin methods
              (except :meth:`Pin.init`) are not applicable (calling them will lead to undefined,
              or a hardware-specific, result).  Not all ports implement this mode.

            - ``Pin.ALT_OPEN_DRAIN`` - The Same as ``Pin.ALT``, but the pin is configured as
              open-drain.  Not all ports implement this mode.

            - ``Pin.ANALOG`` - Pin is configured for analog input, see the :class:`ADC` class.

          - ``pull`` specifies if the pin has a (weak) pull resistor attached, and can be
            one of:

            - ``None`` - No pull up or down resistor.
            - ``Pin.PULL_UP`` - Pull up resistor enabled.
            - ``Pin.PULL_DOWN`` - Pull down resistor enabled.

          - ``value`` is valid only for Pin.OUT and Pin.OPEN_DRAIN modes and specifies initial
            output pin value if given, otherwise the state of the pin peripheral remains
            unchanged.

          - ``drive`` specifies the output power of the pin and can be one of: ``Pin.LOW_POWER``,
            ``Pin.MED_POWER`` or ``Pin.HIGH_POWER``.  The actual current driving capabilities
            are port dependent.  Not all ports implement this argument.

          - ``alt`` specifies an alternate function for the pin and the values it can take are
            port dependent.  This argument is valid only for ``Pin.ALT`` and ``Pin.ALT_OPEN_DRAIN``
            modes.  It may be used when a pin supports more than one alternate function.  If only
            one pin alternate function is supported the this argument is not required.  Not all
            ports implement this argument.

        As specified above, the Pin class allows to set an alternate function for a particular
        pin, but it does not specify any further operations on such a pin.  Pins configured in
        alternate-function mode are usually not used as GPIO but are instead driven by other
        hardware peripherals.  The only operation supported on such a pin is re-initialising,
        by calling the constructor or :meth:`Pin.init` method.  If a pin that is configured in
        alternate-function mode is re-initialised with ``Pin.IN``, ``Pin.OUT``, or
        ``Pin.OPEN_DRAIN``, the alternate function will be removed from the pin.
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
    def drive(self, drive: int, /) -> None:
        """
        Get or set the pin drive strength.
        See the constructor documentation for details of the ``drive`` argument.

        Availability: cc3200, psoc-edge ports.
        """
        ...

    @overload
    def drive(self, /) -> int:
        """
        Get or set the pin drive strength.
        See the constructor documentation for details of the ``drive`` argument.

        Availability: cc3200, psoc-edge ports.
        """

mem8: Incomplete  ## <class 'mem'> = <8-bit memory>
"""Read/write 8 bits of memory."""

class UART:
    """
    UART implements the standard UART/USART duplex serial communications protocol.  At
    the physical level it consists of 2 lines: RX and TX.  The unit of communication
    is a character (not to be confused with a string character) which can be 8 or 9
    bits wide.

    UART objects can be created and initialised using::

        from machine import UART

        uart = UART(1, 9600)                         # init with given baudrate
        uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters

    Supported parameters differ on a board:

    Pyboard: Bits can be 7, 8 or 9. Stop can be 1 or 2. With *parity=None*,
    only 8 and 9 bits are supported.  With parity enabled, only 7 and 8 bits
    are supported.

    WiPy/CC3200: Bits can be 5, 6, 7, 8. Stop can be 1 or 2.

    A UART object acts like a `stream` object and reading and writing is done
    using the standard stream methods::

        uart.read(10)       # read 10 characters, returns a bytes object
        uart.read()         # read all available characters
        uart.readline()     # read a line
        uart.readinto(buf)  # read and store into the given buffer
        uart.write('abc')   # write the 3 characters
    """

    IRQ_RX: Final[int] = 2
    """\
    IRQ trigger sources.
    
    Availability: renesas-ra, stm32, esp32, rp2040, mimxrt, samd, cc3200, psoc-edge.
    """
    IRQ_TXIDLE: Final[int] = 1
    """\
    IRQ trigger sources.
    
    Availability: renesas-ra, stm32, esp32, rp2040, mimxrt, samd, cc3200, psoc-edge.
    """
    RTS: Incomplete
    CTS: Incomplete
    IRQ_RXIDLE: Incomplete
    IRQ_BREAK: Incomplete
    IDLE: int = ...
    INV_TX: int = ...
    INV_RX: int = ...
    def writechar(self, *args, **kwargs) -> Incomplete: ...
    def flush(self) -> None:
        """
        Waits until all data has been sent. In case of a timeout, an exception is raised. The timeout
        duration depends on the tx buffer size and the baud rate. Unless flow control is enabled, a timeout
        should not occur.

        .. note::

            For the esp8266 and nrf ports the call returns while the last byte is sent.
            If required, a one character wait time has to be added in the calling script.

        Availability: rp2, esp32, esp8266, mimxrt, cc3200, stm32, nrf ports, psoc-edge, renesas-ra
        """
        ...

    @overload
    def init(
        self,
        /,
        baudrate: int = 9600,
        bits: int = 8,
        parity: int | None = None,
        stop: int = 1,
        *,
        tx: _PinLike | None = None,
        rx: _PinLike | None = None,
        txbuf: int | None = None,
        rxbuf: int | None = None,
        timeout: int | None = None,
        timeout_char: int | None = None,
        invert: int | None = None,
        flow: int | None = None,
        rts: _PinLike | None = None,
        cts: _PinLike | None = None,
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
        pins: tuple[_PinLike, _PinLike] | None = None,
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
        pins: tuple[_PinLike, _PinLike, _PinLike, _PinLike] | None = None,
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
    def txdone(self) -> bool:
        """
        Tells whether all data has been sent or no data transfer is happening. In this case,
        it returns ``True``. If a data transmission is ongoing it returns ``False``.

        .. note::

            For the esp8266 and nrf ports the call may return ``True`` even if the last byte
            of a transfer is still being sent. If required, a one character wait time has to be
            added in the calling script.

        Availability: rp2, esp32, esp8266, mimxrt, cc3200, stm32, nrf ports, psoc-edge, renesas-ra
        """
        ...
    def readchar(self, *args, **kwargs) -> Incomplete: ...
    def irq(
        self,
        handler: Callable[[UART], None] | None = None,
        trigger: int = 0,
        hard: bool = False,
        /,
    ) -> _IRQ:
        """
        Configure an interrupt handler to be called when a UART event occurs.

        The arguments are:

          - *handler* is an optional function to be called when the interrupt event
            triggers.  The handler must take exactly one argument which is the
            ``UART`` instance.

          - *trigger* configures the event(s) which can generate an interrupt.
            Possible values are a mask of one or more of the following:

            - ``UART.IRQ_RXIDLE`` interrupt after receiving at least one character
              and then the RX line goes idle.
            - ``UART.IRQ_RX`` interrupt after each received character.
            - ``UART.IRQ_TXIDLE`` interrupt after or while the last character(s) of
              a message are or have been sent.
            - ``UART.IRQ_BREAK`` interrupt when a break state is detected at RX

          - *hard* if true a hardware interrupt is used.  This reduces the delay
            between the pin change and the handler being called. Hard interrupt
            handlers may not allocate memory; see :ref:`isr_rules`.

        Returns an irq object.

        Due to limitations of the hardware not all trigger events are available on all ports.
        """
        ...

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
    def deinit(self) -> None:
        """
        Turn off the UART bus.

        .. note::
          You will not be able to call ``init()`` on the object after ``deinit()``.
          A new instance needs to be created in that case.
        """
        ...
    def any(self) -> int:
        """
        Returns an integer counting the number of characters that can be read without
        blocking.  It will return 0 if there are no characters available and a positive
        number if there are characters.  The method may return 1 even if there is more
        than one character available for reading.

        For more sophisticated querying of available characters use select.poll::

         poll = select.poll()
         poll.register(uart, select.POLLIN)
         poll.poll(timeout)
        """
        ...
    def write(self, buf: AnyReadableBuf, /) -> int | None:
        """
        Write the buffer of bytes to the bus.

        Return value: number of bytes written or ``None`` on timeout.
        """
        ...

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
    def readline(self) -> bytes | None:
        """
        Read a line, ending in a newline character. It may return sooner if a timeout
        is reached. The timeout is configurable in the constructor.

        Return value: the line read or ``None`` on timeout.
        """
        ...
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
        tx: _PinLike | None = None,
        rx: _PinLike | None = None,
        txbuf: int | None = None,
        rxbuf: int | None = None,
        timeout: int | None = None,
        timeout_char: int | None = None,
        invert: int | None = None,
        flow: int | None = None,
        rts: _PinLike | None = None,
        cts: _PinLike | None = None,
    ):
        """
        Construct a UART object of the given id.
        """

    @overload
    def __init__(
        self,
        id: ID_T = ...,
        /,
        baudrate: int = 9600,
        bits: int = 8,
        parity: int | None = None,
        stop: int = 1,
        *,
        tx: _PinLike | None = None,
        rx: _PinLike | None = None,
        txbuf: int | None = None,
        rxbuf: int | None = None,
        timeout: int | None = None,
        timeout_char: int | None = None,
        invert: int | None = None,
        flow: int | None = None,
        rts: _PinLike | None = None,
        cts: _PinLike | None = None,
    ):
        """
        Construct a UART object for the default ID.
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
        pins: tuple[_PinLike, _PinLike] | None = None,
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
        pins: tuple[_PinLike, _PinLike, _PinLike, _PinLike] | None = None,
    ):
        """
        Construct a UART object of the given id from a tuple of four pins.
        """

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
    WIDTH_13BIT: int = 13
    def battery_level(self, *args, **kwargs) -> Incomplete: ...
    def read_u16(self) -> int:
        """
        Take an analog reading and return an integer in the range 0-65535.
        The return value represents the raw reading taken by the ADC, scaled
        such that the minimum value is 0 and the maximum value is 65535.
        """
        ...
    def value(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, id: int | _PinLike, *, sample_ns: int = ..., atten: int = ...) -> None:
        """
        Access the ADC associated with a source identified by *id*.  This
        *id* may be an integer (usually specifying a channel number), a
        :ref:`Pin <machine.Pin>` object, or other value supported by the
        underlying machine.
        .. note::

        WiPy has a custom implementation of ADC, see ADCWiPy for details.

        on ESP32 :  `atten` specifies the attenuation level for the ADC input.
        """

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

class PWM:
    """
    This class provides pulse width modulation output.

    Example usage::

        from machine import PWM

        pwm = PWM(pin)          # create a PWM object on a pin
        pwm.duty_u16(32768)     # set duty to 50%

        # reinitialise with a period of 200us, duty of 5us
        pwm.init(freq=5000, duty_ns=5000)

        pwm.duty_ns(3000)       # set pulse width to 3us

        pwm.deinit()


    Limitations of PWM
    ------------------

    * Not all frequencies can be generated with absolute accuracy due to
      the discrete nature of the computing hardware.  Typically the PWM frequency
      is obtained by dividing some integer base frequency by an integer divider.
      For example, if the base frequency is 80MHz and the required PWM frequency is
      300kHz the divider must be a non-integer number 80000000 / 300000 = 266.67.
      After rounding the divider is set to 267 and the PWM frequency will be
      80000000 / 267 = 299625.5 Hz, not 300kHz.  If the divider is set to 266 then
      the PWM frequency will be 80000000 / 266 = 300751.9 Hz, but again not 300kHz.

    * The duty cycle has the same discrete nature and its absolute accuracy is not
      achievable.  On most hardware platforms the duty will be applied at the next
      frequency period.  Therefore, you should wait more than "1/frequency" before
      measuring the duty.

    * The frequency and the duty cycle resolution are usually interdependent.
      The higher the PWM frequency the lower the duty resolution which is available,
      and vice versa. For example, a 300kHz PWM frequency can have a duty cycle
      resolution of 8 bit, not 16-bit as may be expected.  In this case, the lowest
      8 bits of *duty_u16* are insignificant. So::

        pwm=PWM(Pin(13), freq=300_000, duty_u16=2**16//2)

      and::

        pwm=PWM(Pin(13), freq=300_000, duty_u16=2**16//2 + 255)

      will generate PWM with the same 50% duty cycle.
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
    def init(self, *, freq: int = ..., duty_u16: int = ..., duty_ns: int = ..., invert: bool = ...) -> None:
        """
        Modify settings for the PWM object.  See the above constructor for details
        about the parameters.
        """
        ...

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
    def deinit(self) -> None:
        """
        Disable the PWM output.
        """
        ...

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
    def duty(self, *args, **kwargs) -> Incomplete: ...
    def __init__(
        self,
        dest: _PinLike,
        /,
        *,
        freq: int = ...,
        duty_u16: int = ...,
        duty_ns: int = ...,
        invert: bool = ...,
    ) -> None:
        """
        Construct and return a new PWM object using the following parameters:

           - *dest* is the entity on which the PWM is output, which is usually a
             :ref:`machine.Pin <machine.Pin>` object, but a port may allow other values,
             like integers.
           - *freq* should be an integer which sets the frequency in Hz for the
             PWM cycle.
           - *duty_u16* sets the duty cycle as a ratio ``duty_u16 / 65535``.
           - *duty_ns* sets the pulse width in nanoseconds.

        Setting *freq* may affect other PWM objects if the objects share the same
        underlying PWM generator (this is hardware specific).
        Only one of *duty_u16* and *duty_ns* should be specified at a time.
        """

class I2C:
    """
    I2C is a two-wire protocol for communicating between devices.  At the physical
    level it consists of 2 wires: SCL and SDA, the clock and data lines respectively.

    I2C objects are created attached to a specific bus.  They can be initialised
    when created, or initialised later on.

    Printing the I2C object gives you information about its configuration.

    Both hardware and software I2C implementations exist via the
    :ref:`machine.I2C <machine.I2C>` and `machine.SoftI2C` classes.  Hardware I2C uses
    underlying hardware support of the system to perform the reads/writes and is
    usually efficient and fast but may have restrictions on which pins can be used.
    Software I2C is implemented by bit-banging and can be used on any pin but is not
    as efficient.  These classes have the same methods available and differ primarily
    in the way they are constructed.

    Example usage::

        from machine import I2C

        i2c = I2C(freq=400000)          # create I2C peripheral at frequency of 400kHz
                                        # depending on the port, extra parameters may be required
                                        # to select the peripheral and/or pins to use

        i2c.scan()                      # scan for peripherals, returning a list of 7-bit addresses

        i2c.writeto(42, b'123')         # write 3 bytes to peripheral with 7-bit address 42
        i2c.readfrom(42, 4)             # read 4 bytes from peripheral with 7-bit address 42

        i2c.readfrom_mem(42, 8, 3)      # read 3 bytes from memory of peripheral 42,
                                        #   starting at memory-address 8 in the peripheral
        i2c.writeto_mem(42, 2, b'\x10') # write 1 byte to memory of peripheral 42
                                        #   starting at address 2 in the peripheral
    """
    def readfrom_mem(self, addr: int, memaddr: int, nbytes: int, /, *, addrsize: int = 8) -> bytes:
        """
        Read *nbytes* from the peripheral specified by *addr* starting from the memory
        address specified by *memaddr*.
        The argument *addrsize* specifies the address size in bits.
        Returns a `bytes` object with the data read.
        """
        ...
    def readfrom_mem_into(self, addr: int, memaddr: int, buf: AnyWritableBuf, /, *, addrsize: int = 8) -> None:
        """
        Read into *buf* from the peripheral specified by *addr* starting from the
        memory address specified by *memaddr*.  The number of bytes read is the
        length of *buf*.
        The argument *addrsize* specifies the address size in bits (on ESP8266
        this argument is not recognised and the address size is always 8 bits).

        The method returns ``None``.
        """
        ...
    def readfrom_into(self, addr: int, buf: AnyWritableBuf, stop: bool = True, /) -> None:
        """
        Read into *buf* from the peripheral specified by *addr*.
        The number of bytes read will be the length of *buf*.
        If *stop* is true then a STOP condition is generated at the end of the transfer.

        The method returns ``None``.
        """
        ...
    def writevto(self, addr: int, vector: Sequence[AnyReadableBuf], stop: bool = True, /) -> int:
        """
        Write the bytes contained in *vector* to the peripheral specified by *addr*.
        *vector* should be a tuple or list of objects with the buffer protocol.
        The *addr* is sent once and then the bytes from each object in *vector*
        are written out sequentially.  The objects in *vector* may be zero bytes
        in length in which case they don't contribute to the output.

        If a NACK is received following the write of a byte from one of the
        objects in *vector* then the remaining bytes, and any remaining objects,
        are not sent.  If *stop* is true then a STOP condition is generated at
        the end of the transfer, even if a NACK is received.  The function
        returns the number of ACKs that were received.
        """
        ...
    def writeto_mem(self, addr: int, memaddr: int, buf: AnyReadableBuf, /, *, addrsize: int = 8) -> None:
        """
        Write *buf* to the peripheral specified by *addr* starting from the
        memory address specified by *memaddr*.
        The argument *addrsize* specifies the address size in bits (on ESP8266
        this argument is not recognised and the address size is always 8 bits).

        The method returns ``None``.
        """
        ...
    def scan(self) -> list[int]:
        """
        Scan all I2C addresses between 0x08 and 0x77 inclusive and return a list of
        those that respond.  A device responds if it pulls the SDA line low after
        its address (including a write bit) is sent on the bus.
        """
        ...
    def writeto(self, addr: int, buf: AnyReadableBuf, stop: bool = True, /) -> int:
        """
        Write the bytes from *buf* to the peripheral specified by *addr*.  If a
        NACK is received following the write of a byte from *buf* then the
        remaining bytes are not sent.  If *stop* is true then a STOP condition is
        generated at the end of the transfer, even if a NACK is received.
        The function returns the number of ACKs that were received.
        """
        ...
    def start(self) -> None:
        """
        Generate a START condition on the bus (SDA transitions to low while SCL is high).
        """
        ...
    def stop(self) -> None:
        """
        Generate a STOP condition on the bus (SDA transitions to high while SCL is high).
        """
        ...
    def readinto(self, buf: AnyWritableBuf, nack: bool = True, /) -> None:
        """
        Reads bytes from the bus and stores them into *buf*.  The number of bytes
        read is the length of *buf*.  An ACK will be sent on the bus after
        receiving all but the last byte.  After the last byte is received, if *nack*
        is true then a NACK will be sent, otherwise an ACK will be sent (and in this
        case the peripheral assumes more bytes are going to be read in a later call).
        """
        ...
    def readfrom(self, addr: int, nbytes: int, stop: bool = True, /) -> bytes:
        """
        Read *nbytes* from the peripheral specified by *addr*.
        If *stop* is true then a STOP condition is generated at the end of the transfer.
        Returns a `bytes` object with the data read.
        """
        ...

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
    def init(self, *, scl: _PinLike, sda: _PinLike, freq: int = 400_000) -> None:
        """
        Initialise the I2C bus with the given arguments:

           - *scl* is a pin object for the SCL line
           - *sda* is a pin object for the SDA line
           - *freq* is the SCL clock rate

         In the case of hardware I2C the actual clock frequency may be lower than the
         requested frequency. This is dependent on the platform hardware. The actual
         rate may be determined by printing the I2C object.
        """
    def write(self, buf: AnyReadableBuf, /) -> int:
        """
        Write the bytes from *buf* to the bus.  Checks that an ACK is received
        after each byte and stops transmitting the remaining bytes if a NACK is
        received.  The function returns the number of ACKs that were received.
        """
        ...
    def deinit(self) -> None:
        """
        Turn off the I2C bus.
        """
        ...

    @overload
    def __init__(self, id: ID_T, /, *, freq: int = 400_000, timeout: int = 50_000):
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
    def __init__(self, id: ID_T, /, *, scl: _PinLike, sda: _PinLike, freq: int = 400_000, timeout: int = 50_000):
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
    def __init__(self, *, scl: _PinLike, sda: _PinLike, freq: int = 400_000) -> None:
        """
        Initialise the I2C bus with the given arguments:

           - *scl* is a pin object for the SCL line
           - *sda* is a pin object for the SDA line
           - *freq* is the SCL clock rate

         In the case of hardware I2C the actual clock frequency may be lower than the
         requested frequency. This is dependent on the platform hardware. The actual
         rate may be determined by printing the I2C object.
        """

class Temp:
    def read(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class SoftI2C(I2C):
    """
    Construct a new software I2C object.  The parameters are:

       - *scl* should be a pin object specifying the pin to use for SCL.
       - *sda* should be a pin object specifying the pin to use for SDA.
       - *freq* should be an integer which sets the maximum frequency
         for SCL.
       - *timeout* is the maximum time in microseconds to wait for clock
         stretching (SCL held low by another device on the bus), after
         which an ``OSError(ETIMEDOUT)`` exception is raised.
    """
    def readfrom_mem(self, *args, **kwargs) -> Incomplete: ...
    def readfrom_mem_into(self, *args, **kwargs) -> Incomplete: ...
    def readfrom_into(self, *args, **kwargs) -> Incomplete: ...
    def writevto(self, *args, **kwargs) -> Incomplete: ...
    def writeto_mem(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def writeto(self, *args, **kwargs) -> Incomplete: ...
    def start(self, *args, **kwargs) -> Incomplete: ...
    def stop(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def readfrom(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, scl: _PinLike, sda: _PinLike, *, freq: int = 400_000, timeout: int = 50_000) -> None: ...

class Timer:
    """
    Hardware timers deal with timing of periods and events. Timers are perhaps
    the most flexible and heterogeneous kind of hardware in MCUs and SoCs,
    differently greatly from a model to a model. MicroPython's Timer class
    defines a baseline operation of executing a callback with a given period
    (or once after some delay), and allow specific boards to define more
    non-standard behaviour (which thus won't be portable to other boards).

    See discussion of :ref:`important constraints <machine_callbacks>` on
    Timer callbacks.

    .. note::

        Memory can't be allocated inside irq handlers (an interrupt) and so
        exceptions raised within a handler don't give much information.  See
        :func:`micropython.alloc_emergency_exception_buf` for how to get around this
        limitation.

    If you are using a WiPy board please refer to :ref:`machine.TimerWiPy <machine.TimerWiPy>`
    instead of this class.
    """

    PERIODIC: Final[int] = 1
    """Timer operating mode."""
    ONESHOT: Final[int] = 0
    ONE_SHOT: Incomplete
    def deinit(self) -> None:
        """
        Deinitialises the timer. Stops the timer, and disables the timer peripheral.
        """
        ...
    def period(self, *args, **kwargs) -> Incomplete: ...
    def time(self, *args, **kwargs) -> Incomplete: ...
    def stop(self, *args, **kwargs) -> Incomplete: ...
    def start(self, *args, **kwargs) -> Incomplete: ...
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
        hard: bool | None = None,
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
        hard: bool | None = None,
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
        hard: bool | None = None,
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
        hard: bool | None = None,
    ) -> None: ...
    @overload
    def init(
        self,
        *,
        mode: int = PERIODIC,
        freq: int | None = None,
        callback: Callable[[Timer], None] | None = None,
        hard: bool | None = None,
    ) -> None: ...
    @overload
    def init(
        self,
        *,
        mode: int = PERIODIC,
        tick_hz: int | None = None,
        callback: Callable[[Timer], None] | None = None,
        hard: bool | None = None,
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

          - ``hard`` can be one of:

            - ``True`` - The callback will be executed in hard interrupt context,
              which minimises delay and jitter but is subject to the limitations
              described in :ref:`isr_rules`. Not all ports support hard interrupts,
              see the port documentation for more information.
            - ``False`` - The callback will be scheduled as a soft interrupt,
              allowing it to allocate but possibly also introducing
              garbage-collection delays and jitter.

            The default value of this parameter is port-specific for historical reasons.
        """
        ...

mem32: Incomplete  ## <class 'mem'> = <32-bit memory>
"""\
Read/write 32 bits of memory.

Use subscript notation ``[...]`` to index these objects with the address of
interest. Note that the address is the byte address, regardless of the size of
memory being accessed.

Example use (registers are specific to an stm32 microcontroller):
"""
mem16: Incomplete  ## <class 'mem'> = <16-bit memory>
"""Read/write 16 bits of memory."""

class Signal(Pin):
    """
    The Signal class is a simple extension of the `Pin` class. Unlike Pin, which
    can be only in "absolute" 0 and 1 states, a Signal can be in "asserted"
    (on) or "deasserted" (off) states, while being inverted (active-low) or
    not. In other words, it adds logical inversion support to Pin functionality.
    While this may seem a simple addition, it is exactly what is needed to
    support wide array of simple digital devices in a way portable across
    different boards, which is one of the major MicroPython goals. Regardless
    of whether different users have an active-high or active-low LED, a normally
    open or normally closed relay - you can develop a single, nicely looking
    application which works with each of them, and capture hardware
    configuration differences in few lines in the config file of your app.

    Example::

        from machine import Pin, Signal

        # Suppose you have an active-high LED on pin 0
        led1_pin = Pin(0, Pin.OUT)
        # ... and active-low LED on pin 1
        led2_pin = Pin(1, Pin.OUT)

        # Now to light up both of them using Pin class, you'll need to set
        # them to different values
        led1_pin.value(1)
        led2_pin.value(0)

        # Signal class allows to abstract away active-high/active-low
        # difference
        led1 = Signal(led1_pin, invert=False)
        led2 = Signal(led2_pin, invert=True)

        # Now lighting up them looks the same
        led1.value(1)
        led2.value(1)

        # Even better:
        led1.on()
        led2.on()

    Following is the guide when Signal vs Pin should be used:

    * Use Signal: If you want to control a simple on/off (including software
      PWM!) devices like LEDs, multi-segment indicators, relays, buzzers, or
      read simple binary sensors, like normally open or normally closed buttons,
      pulled high or low, Reed switches, moisture/flame detectors, etc. etc.
      Summing up, if you have a real physical device/sensor requiring GPIO
      access, you likely should use a Signal.

    * Use Pin: If you implement a higher-level protocol or bus to communicate
      with more complex devices.

    The split between Pin and Signal come from the use cases above and the
    architecture of MicroPython: Pin offers the lowest overhead, which may
    be important when bit-banging protocols. But Signal adds additional
    flexibility on top of Pin, at the cost of minor overhead (much smaller
    than if you implemented active-high vs active-low device differences in
    Python manually!). Also, Pin is a low-level object which needs to be
    implemented for each support board, while Signal is a high-level object
    which comes for free once Pin is implemented.

    If in doubt, give the Signal a try! Once again, it is offered to save
    developers from the need to handle unexciting differences like active-low
    vs active-high signals, and allow other users to share and enjoy your
    application, instead of being frustrated by the fact that it doesn't
    work for them simply because their LEDs or relays are wired in a slightly
    different way.
    """
    def off(self) -> None:
        """
        Deactivate signal.
        """
        ...
    def on(self) -> None:
        """
        Activate signal.
        """
        ...

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

    @overload
    def __init__(self, pin_obj: _PinLike, invert: bool = False, /) -> None:
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
        id: _PinLike,
        /,
        mode: int = -1,
        pull: int = -1,
        *,
        value: Any = None,
        drive: int | None = None,
        alt: int | None = None,
        invert: bool = False,
    ) -> None:
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

class SPI:
    """
    SPI is a synchronous serial protocol that is driven by a controller. At the
    physical level, a bus consists of 3 lines: SCK, MOSI, MISO. Multiple devices
    can share the same bus. Each device should have a separate, 4th signal,
    CS (Chip Select), to select a particular device on a bus with which
    communication takes place. Management of a CS signal should happen in
    user code (via machine.Pin class).

    Both hardware and software SPI implementations exist via the
    :ref:`machine.SPI <machine.SPI>` and `machine.SoftSPI` classes.  Hardware SPI uses underlying
    hardware support of the system to perform the reads/writes and is usually
    efficient and fast but may have restrictions on which pins can be used.
    Software SPI is implemented by bit-banging and can be used on any pin but
    is not as efficient.  These classes have the same methods available and
    differ primarily in the way they are constructed.

    Example usage::

        from machine import SPI, Pin

        spi = SPI(0, baudrate=400000)           # Create SPI peripheral 0 at frequency of 400kHz.
                                                # Depending on the use case, extra parameters may be required
                                                # to select the bus characteristics and/or pins to use.
        cs = Pin(4, mode=Pin.OUT, value=1)      # Create chip-select on pin 4.

        try:
            cs(0)                               # Select peripheral.
            spi.write(b"12345678")              # Write 8 bytes, and don't care about received data.
        finally:
            cs(1)                               # Deselect peripheral.

        try:
            cs(0)                               # Select peripheral.
            rxdata = spi.read(8, 0x42)          # Read 8 bytes while writing 0x42 for each byte.
        finally:
            cs(1)                               # Deselect peripheral.

        rxdata = bytearray(8)
        try:
            cs(0)                               # Select peripheral.
            spi.readinto(rxdata, 0x42)          # Read 8 bytes inplace while writing 0x42 for each byte.
        finally:
            cs(1)                               # Deselect peripheral.

        txdata = b"12345678"
        rxdata = bytearray(len(txdata))
        try:
            cs(0)                               # Select peripheral.
            spi.write_readinto(txdata, rxdata)  # Simultaneously write and read bytes.
        finally:
            cs(1)                               # Deselect peripheral.
    """

    LSB: Final[int] = 1
    """set the first bit to be the least significant bit"""
    MSB: Final[int] = 0
    """set the first bit to be the most significant bit"""
    CONTROLLER: Incomplete
    def deinit(self) -> None:
        """
        Turn off the SPI bus.
        """
        ...

    @overload
    def init(
        self,
        baudrate: int = 1_000_000,
        *,
        polarity: int = 0,
        phase: int = 0,
        bits: int = 8,
        firstbit: int = MSB,
        sck: _PinLike | None = None,
        mosi: _PinLike | None = None,
        miso: _PinLike | None = None,
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
        pins: tuple[_PinLike, _PinLike, _PinLike] | None = None,
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
    def write_readinto(self, write_buf: AnyReadableBuf, read_buf: AnyWritableBuf, /) -> int | None:
        """
        Write the bytes from ``write_buf`` while reading into ``read_buf``.  The
        buffers can be the same or different, but both buffers must have the
        same length.
        Returns ``None``.

        Note: on WiPy this function returns the number of bytes written.
        """
        ...
    def read(self, nbytes: int, write: int = 0x00, /) -> bytes:
        """
        Read a number of bytes specified by ``nbytes`` while continuously writing
        the single byte given by ``write``.
        Returns a ``bytes`` object with the data that was read.
        """
        ...
    def write(self, buf: AnyReadableBuf, /) -> int | None:
        """
        Write the bytes contained in ``buf``.
        Returns ``None``.

        Note: on WiPy this function returns the number of bytes written.
        """
        ...
    def readinto(self, buf: AnyWritableBuf, write: int = 0x00, /) -> int | None:
        """
        Read into the buffer specified by ``buf`` while continuously writing the
        single byte given by ``write``.
        Returns ``None``.

        Note: on WiPy this function returns the number of bytes read.
        """
        ...
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
        sck: _PinLike | None = None,
        mosi: _PinLike | None = None,
        miso: _PinLike | None = None,
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
        pins: tuple[_PinLike, _PinLike, _PinLike] | None = None,
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

class ADCBlock:
    @overload
    def connect(self, channel: int, **kwargs) -> ADC: ...
    @overload
    def connect(self, source: _PinLike, **kwargs) -> ADC: ...
    @overload
    def connect(self, channel: int, source: _PinLike, **kwargs) -> ADC:
        """
        Connect up a channel on the ADC peripheral so it is ready for sampling,
        and return an :ref:`ADC <machine.ADC>` object that represents that connection.

        The *channel* argument must be an integer, and *source* must be an object
        (for example a :ref:`Pin <machine.Pin>`) which can be connected up for sampling.

        If only *channel* is given then it is configured for sampling.

        If only *source* is given then that object is connected to a default
        channel ready for sampling.

        If both *channel* and *source* are given then they are connected together
        and made ready for sampling.

        Any additional keyword arguments are used to configure the returned ADC object,
        via its :meth:`init <machine.ADC.init>` method.
        """
        ...

class ADCWiPy:
    @overload
    def channel(self, id: int, *, pin=None) -> adcchannel: ...
    @overload
    def channel(self, *, pin) -> adcchannel: ...
    @overload
    def channel(self, id: int, *, pin) -> adcchannel:
        """
        Create an analog pin. If only channel ID is given, the correct pin will
        be selected. Alternatively, only the pin can be passed and the correct
        channel will be selected. Examples::

           # all of these are equivalent and enable ADC channel 1 on GP3
           apin = adc.channel(1)
           apin = adc.channel(pin='GP3')
           apin = adc.channel(id=1, pin='GP3')
        """
        ...

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

    @overload
    def memory(self) -> bytes:
        """
        ``RTC.memory(data)`` will write *data* to the RTC memory, where *data* is any
        object which supports the buffer protocol (including `bytes`, `bytearray`,
        `memoryview` and `array.array`). ``RTC.memory()`` reads RTC memory and returns
        a `bytes` object.

        Data written to RTC user memory is persistent across restarts, including
        :ref:`soft_reset` and `machine.deepsleep()`.

        The maximum length of RTC user memory is 2048 bytes by default on esp32,
        and 492 bytes on esp8266.

        Availability: esp32, esp8266 ports.

        .. note::

           For cross-port persistent storage, see :func:`machine.mem_backup`
           which is available on more ports and provides direct memoryview access.
        """
        ...

    @overload
    def memory(self, data: AnyReadableBuf, /) -> None:
        """
        ``RTC.memory(data)`` will write *data* to the RTC memory, where *data* is any
        object which supports the buffer protocol (including `bytes`, `bytearray`,
        `memoryview` and `array.array`). ``RTC.memory()`` reads RTC memory and returns
        a `bytes` object.

        Data written to RTC user memory is persistent across restarts, including
        :ref:`soft_reset` and `machine.deepsleep()`.

        The maximum length of RTC user memory is 2048 bytes by default on esp32,
        and 492 bytes on esp8266.

        Availability: esp32, esp8266 ports.

        .. note::

           For cross-port persistent storage, see :func:`machine.mem_backup`
           which is available on more ports and provides direct memoryview access.
        """
        ...

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

class SDCard:
    @mp_available()  # force merge
    def __init__(
        self,
        slot: int = 1,
        width: int = 1,
        *,
        cd: _PinLike | None = None,
        wp: _PinLike | None = None,
        sck: _PinLike | None = None,
        cmd: _PinLike | None = None,
        data: tuple[_PinLike, _PinLike, _PinLike, _PinLike] | None = None,
        miso: _PinLike | None = None,
        mosi: _PinLike | None = None,
        cs: _PinLike | None = None,
        freq: int = 20000000,
    ) -> None:
        """
        This class provides access to SD or MMC storage cards using either
        a dedicated SD/MMC interface hardware or through an SPI channel.
        The class implements the block protocol defined by :class:`os.AbstractBlockDev`.
        This allows the mounting of an SD card to be as simple as::

          os.mount(machine.SDCard(), "/sd")

        The constructor takes the following parameters:

         - *slot* selects which of the available interfaces to use. Leaving this
           unset will select the default interface.

         - *width* selects the bus width for the SD/MMC interface.

         - *cd* can be used to specify a card-detect pin.

         - *wp* can be used to specify a write-protect pin.

         - *sck* can be used to specify an SPI clock pin.

         - *miso* can be used to specify an SPI miso pin.

         - *mosi* can be used to specify an SPI mosi pin.

         - *cs* can be used to specify an SPI chip select pin.

         - *freq* selects the SD/MMC interface frequency in Hz (only supported on the ESP32).
        """
