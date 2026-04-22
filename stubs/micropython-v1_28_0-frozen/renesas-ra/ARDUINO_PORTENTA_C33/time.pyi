# Micropython v1.28.0 frozen stubs
"""
Time related functions.

MicroPython module: https://docs.micropython.org/en/v1.28.0/library/time.html

CPython module: :mod:`python:time` https://docs.python.org/3/library/time.html .

The ``time`` module provides functions for getting the current time and date,
measuring time intervals, and for delays.

**Time Epoch**: The unix, windows, webassembly, alif, mimxrt and rp2 ports
use the standard for POSIX systems epoch of 1970-01-01 00:00:00 UTC.
The other embedded ports use an epoch of 2000-01-01 00:00:00 UTC.
Epoch year may be determined with ``gmtime(0)[0]``.

**Maintaining actual calendar date/time**: This requires a
Real Time Clock (RTC). On systems with underlying OS (including some
RTOS), an RTC may be implicit. Setting and maintaining actual calendar
time is responsibility of OS/RTOS and is done outside of MicroPython,
it just uses OS API to query date/time. On baremetal ports however
system time depends on ``machine.RTC()`` object. The current calendar time
may be set using ``machine.RTC().datetime(tuple)`` function, and maintained
by following means:

* By a backup battery (which may be an additional, optional component for
  a particular board).
* Using networked time protocol (requires setup by a port/user).
* Set manually by a user on each power-up (many boards then maintain
  RTC time across hard resets, though some may require setting it again
  in such case).

If actual calendar time is not maintained with a system/MicroPython RTC,
functions below which require reference to current absolute time may
behave not as expected.
"""

from __future__ import annotations
from utime import *
from _typeshed import Incomplete
from _mpy_shed import _TimeTuple, mp_available
from _mpy_shed.time_mp import _Ticks, _TicksCPU, _TicksMs, _TicksUs
from typing_extensions import Awaitable, TypeAlias, TypeVar

_TS_YEAR: int
_TS_MON: int
_TS_MDAY: int
_TS_HOUR: int
_TS_MIN: int
_TS_SEC: int
_TS_WDAY: int
_TS_YDAY: int
_TS_ISDST: int
_WDAY: Incomplete
_MDAY: Incomplete

def strftime(datefmt, ts): ...

# override the type of ticks_ms()  as it is discovered as `int` in docstubs.
@mp_available
def ticks_ms() -> _TicksMs:
    """
    Returns an increasing millisecond counter with an arbitrary reference point, that
    wraps around after some value.

    The wrap-around value is not explicitly exposed, but we will
    refer to it as *TICKS_MAX* to simplify discussion. Period of the values is
    *TICKS_PERIOD = TICKS_MAX + 1*. *TICKS_PERIOD* is guaranteed to be a power of
    two, but otherwise may differ from port to port. The same period value is used
    for all of `ticks_ms()`, `ticks_us()`, `ticks_cpu()` functions (for
    simplicity). Thus, these functions will return a value in range [*0* ..
    *TICKS_MAX*], inclusive, total *TICKS_PERIOD* values. Note that only
    non-negative values are used. For the most part, you should treat values returned
    by these functions as opaque. The only operations available for them are
    `ticks_diff()` and `ticks_add()` functions described below.

    Note: Performing standard mathematical operations (+, -) or relational
    operators (<, <=, >, >=) directly on these value will lead to invalid
    result. Performing mathematical operations and then passing their results
    as arguments to `ticks_diff()` or `ticks_add()` will also lead to
    invalid results from the latter functions.
    """
    ...
