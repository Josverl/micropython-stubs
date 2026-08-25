"""
Functions related to the hardware.

MicroPython module: https://docs.micropython.org/en/v1.30.0/library/machine.html

The ``machine`` module contains specific functions related to the hardware
on a particular board. Most functions in this module allow to achieve direct
and unrestricted access to and control of hardware blocks on a system
(like CPU, timers, buses, etc.). Used incorrectly, this can lead to
malfunction, lockups, crashes of your board, and in extreme cases, hardware
damage.
"""

# source version: v1.30.0-preview
# origin module:: repos/micropython/docs/library/machine.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing import overload, Any, NoReturn, Optional, Tuple
from typing_extensions import deprecated, TypeVar, TypeAlias, Awaitable
from machine.Pin import Pin
from machine.Signal import Signal
from machine.ADC import ADC
from machine.ADCBlock import ADCBlock
from machine.DAC import DAC
from machine.PWM import PWM
from machine.UART import UART
from machine.SPI import SoftSPI, SPI
from machine.I2C import SoftI2C, I2C
from machine.I2CTarget import I2CTarget
from machine.I2S import I2S
from machine.CAN import CAN
from machine.RTC import RTC
from machine.Timer import Timer
from machine.Counter import Counter
from machine.Encoder import Encoder
from machine.WDT import WDT
from machine.SD import SD
from machine.SDCard import SDCard
from machine.USBDevice import USBDevice
from _mpy_shed.mp_mem import _MemoryObject as _MemoryObject

mem8: Incomplete
"""Read/write 8 bits of memory."""
mem16: Incomplete
"""Read/write 16 bits of memory."""
mem32: int
"""\
Read/write 32 bits of memory.

Use subscript notation ``[...]`` to index these objects with the address of
interest. Note that the address is the byte address, regardless of the size of
memory being accessed.

Example use (registers are specific to an stm32 microcontroller):
"""
IDLE: Incomplete
"""IRQ wake values."""
SLEEP: Incomplete
"""IRQ wake values."""
DEEPSLEEP: Incomplete
"""IRQ wake values."""
PWRON_RESET: Incomplete
"""Reset causes."""
HARD_RESET: Incomplete
"""Reset causes."""
WDT_RESET: Incomplete
"""Reset causes."""
DEEPSLEEP_RESET: Incomplete
"""Reset causes."""
SOFT_RESET: Incomplete
"""Reset causes."""
WLAN_WAKE: Incomplete
"""Wake-up reasons."""
PIN_WAKE: Incomplete
"""Wake-up reasons."""
RTC_WAKE: Incomplete
"""Wake-up reasons."""
_IRQ_STATE: TypeAlias = int

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

def reset() -> NoReturn:
    """
    :ref:`Hard resets <hard_reset>` the device in a manner similar to pushing the
    external RESET button.
    """
    ...

def soft_reset() -> NoReturn:
    """
    Performs a :ref:`soft reset <soft_reset>` of the interpreter, deleting all
    Python objects and resetting the Python heap.
    """
    ...

def reset_cause() -> int:
    """
    Get the reset cause. See :ref:`constants <machine_constants>` for the possible return values.
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

def disable_irq() -> _IRQ_STATE:
    """
    Disable interrupt requests.
    Returns the previous IRQ state which should be considered an opaque value.
    This return value should be passed to the `enable_irq()` function to restore
    interrupts to their original state, before `disable_irq()` was called.
    """
    ...

def enable_irq(state: _IRQ_STATE, /) -> None:
    """
    Re-enable interrupt requests.
    The *state* parameter should be the value that was returned from the most
    recent call to the `disable_irq()` function.
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

def wake_reason() -> int:
    """
    Get the wake reason. See :ref:`constants <machine_constants>` for the possible return values.

    Availability: ESP32, WiPy.
    """
    ...

def wake_pins() -> Tuple:
    """
    Returns the GPIO pin numbers of those pins which caused wakeup from deep sleep as a
    tuple of integers.

    Availability: ESP32.
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

def time_pulse_us(pin: Pin, pulse_level: int, timeout_us: int = 1_000_000, /) -> int:
    """
    Time a pulse on the given *pin*, and return the duration of the pulse in
    microseconds.  The *pulse_level* argument should be 0 to time a low pulse
    or 1 to time a high pulse.

    If the current input value of the pin is different to *pulse_level*,
    the function first (*) waits until the pin input becomes equal to *pulse_level*,
    then (**) times the duration that the pin is equal to *pulse_level*.
    If the pin is already equal to *pulse_level* then timing starts straight away.

    The function will return -2 if there was timeout waiting for condition marked
    (*) above, and -1 if there was timeout during the main measurement, marked (**)
    above. The timeout is the same for both cases and given by *timeout_us* (which
    is in microseconds).
    """
    ...

def bitstream(pin, encoding, timing, data, /) -> Incomplete:
    """
    Transmits *data* by bit-banging the specified *pin*. The *encoding* argument
    specifies how the bits are encoded, and *timing* is an encoding-specific timing
    specification.

    The supported encodings are:

      - ``0`` for "high low" pulse duration modulation. This will transmit 0 and
        1 bits as timed pulses, starting with the most significant bit.
        The *timing* must be a four-tuple of nanoseconds in the format
        ``(high_time_0, low_time_0, high_time_1, low_time_1)``. For example,
        ``(400, 850, 800, 450)`` is the timing specification for WS2812 RGB LEDs
        at 800kHz.

    The accuracy of the timing varies between ports. On Cortex M0 at 48MHz, it is
    at best +/- 120ns, however on faster MCUs (ESP8266, ESP32, STM32, Pyboard), it
    will be closer to +/-30ns.

    ``Note:`` For controlling WS2812 / NeoPixel strips, see the :mod:`neopixel`
       module for a higher-level API.
    """
    ...

def rng() -> int:
    """
    Return a 24-bit software generated random number.

    Availability: WiPy.
    """
    ...
