"""
Functions related to the ESP8266 and ESP32.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/esp.html

The ``esp`` module contains specific functions related to both the ESP8266 and
ESP32 modules.  Some functions are only available on one or the other of these
ports.

---
Module: 'esp' on micropython-v1.25.0-esp8266-ESP8266_GENERIC-FLASH_2M_ROMFS
"""

# MCU: {'variant': 'FLASH_2M_ROMFS', 'build': '', 'arch': 'xtensa', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'board_id': 'ESP8266_GENERIC-FLASH_2M_ROMFS', 'mpy': 'v6.3', 'ver': '1.25.0', 'family': 'micropython', 'cpu': 'ESP8266', 'version': '1.25.0'}
# Stubber: v1.25.0
from __future__ import annotations
from typing import Any, Optional, Final
from _typeshed import Incomplete
from _mpy_shed import AnyReadableBuf, AnyWritableBuf
from typing_extensions import Awaitable, TypeAlias, TypeVar

SLEEP_MODEM: Final[int] = 2
SLEEP_NONE: Final[int] = 0
SLEEP_LIGHT: Final[int] = 1

def flash_user_start() -> Incomplete:
    """
    Read the memory offset at which the user flash space begins.
    """
    ...

def freemem(*args, **kwargs) -> Incomplete: ...
def free(*args, **kwargs) -> Incomplete: ...
def flash_write(byte_offset, bytes) -> Incomplete: ...
def malloc(*args, **kwargs) -> Incomplete: ...
def set_native_code_location(start, length) -> Incomplete:
    """
    **Note**: ESP8266 only

    Set the location that native code will be placed for execution after it is
    compiled.  Native code is emitted when the ``@micropython.native``,
    ``@micropython.viper`` and ``@micropython.asm_xtensa`` decorators are applied
    to a function.  The ESP8266 must execute code from either iRAM or the lower
    1MByte of flash (which is memory mapped), and this function controls the
    location.

    If *start* and *length* are both ``None`` then the native code location is
    set to the unused portion of memory at the end of the iRAM1 region.  The
    size of this unused portion depends on the firmware and is typically quite
    small (around 500 bytes), and is enough to store a few very small
    functions.  The advantage of using this iRAM1 region is that it does not
    get worn out by writing to it.

    If neither *start* nor *length* are ``None`` then they should be integers.
    *start* should specify the byte offset from the beginning of the flash at
    which native code should be stored.  *length* specifies how many bytes of
    flash from *start* can be used to store native code.  *start* and *length*
    should be multiples of the sector size (being 4096 bytes).  The flash will
    be automatically erased before writing to it so be sure to use a region of
    flash that is not otherwise used, for example by the firmware or the
    filesystem.

    When using the flash to store native code *start+length* must be less
    than or equal to 1MByte.  Note that the flash can be worn out if repeated
    erasures (and writes) are made so use this feature sparingly.
    In particular, native code needs to be recompiled and rewritten to flash
    on each boot (including wake from deepsleep).

    In both cases above, using iRAM1 or flash, if there is no more room left
    in the specified region then the use of a native decorator on a function
    will lead to `MemoryError` exception being raised during compilation of
    that function.
    """
    ...

def osdebug(uart_no, level: Optional[Any] = None) -> Incomplete:
    """
    :no-index:

    ``Note:`` This is the ESP32 form of this function.

    Change the level of OS serial debug log messages. On boot, OS
    serial debug log messages are limited to Error output only.

    The behaviour of this function depends on the arguments passed to it. The
    following combinations are supported:

    ``osdebug(None)`` restores the default OS debug log message level
    (``LOG_ERROR``).

    ``osdebug(0)`` enables all available OS debug log messages (in the
    default build configuration this is ``LOG_INFO``).

    ``osdebug(0, level)`` sets the OS debug log message level to the
     specified value. The log levels are defined as constants:

        * ``LOG_NONE`` -- No log output
        * ``LOG_ERROR`` -- Critical errors, software module can not recover on its own
        * ``LOG_WARN`` -- Error conditions from which recovery measures have been taken
        * ``LOG_INFO`` -- Information messages which describe normal flow of events
        * ``LOG_DEBUG`` -- Extra information which is not necessary for normal use (values, pointers, sizes, etc)
        * ``LOG_VERBOSE`` -- Bigger chunks of debugging information, or frequent messages
          which can potentially flood the output

    ``Note:`` ``LOG_DEBUG`` and ``LOG_VERBOSE`` are not compiled into the
              MicroPython binary by default, to save size. A custom build with a
              modified "``sdkconfig``" source file is needed to see any output
              at these log levels.

    ``Note:`` Log output on ESP32 is automatically suspended in "Raw REPL" mode,
              to prevent communications issues. This means OS level logging is never
              seen when using ``mpremote run`` and similar tools.
    """
    ...

def meminfo(*args, **kwargs) -> Incomplete: ...
def sleep_type(sleep_type: Optional[Any] = None) -> Incomplete:
    """
    **Note**: ESP8266 only

    Get or set the sleep type.

    If the *sleep_type* parameter is provided, sets the sleep type to its
    value. If the function is called without parameters, returns the current
    sleep type.

    The possible sleep types are defined as constants:

        * ``SLEEP_NONE`` -- all functions enabled,
        * ``SLEEP_MODEM`` -- modem sleep, shuts down the WiFi Modem circuit.
        * ``SLEEP_LIGHT`` -- light sleep, shuts down the WiFi Modem circuit
          and suspends the processor periodically.

    The system enters the set sleep mode automatically when possible.
    """
    ...

def flash_size() -> Incomplete:
    """
    Read the total size of the flash memory.
    """
    ...

def deepsleep(time_us=0, /) -> Incomplete:
    """
    **Note**: ESP8266 only - use `machine.deepsleep()` on ESP32

    Enter deep sleep.

    The whole module powers down, except for the RTC clock circuit, which can
    be used to restart the module after the specified time if the pin 16 is
    connected to the reset pin. Otherwise the module will sleep until manually
    reset.
    """
    ...

def check_fw(*args, **kwargs) -> Incomplete: ...
def apa102_write(*args, **kwargs) -> Incomplete: ...
def esf_free_bufs(*args, **kwargs) -> Incomplete: ...
def flash_read(byte_offset, length_or_buffer) -> Incomplete: ...
def flash_id() -> Incomplete:
    """
    **Note**: ESP8266 only

    Read the device ID of the flash memory.
    """
    ...

def flash_erase(sector_no) -> Incomplete: ...
