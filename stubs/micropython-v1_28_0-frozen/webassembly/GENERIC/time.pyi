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
from typing import Literal, overload
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
@overload
def ticks_diff(ticks1: _Ticks, ticks2: _Ticks, /) -> int:
    """
    Measure ticks difference between values returned from `ticks_ms()`, `ticks_us()`,
    or `ticks_cpu()` functions, as a signed value which may wrap around.

    The argument order is the same as for subtraction
    operator, ``ticks_diff(ticks1, ticks2)`` has the same meaning as ``ticks1 - ticks2``.
    However, values returned by `ticks_ms()`, etc. functions may wrap around, so
    directly using subtraction on them will produce incorrect result. That is why
    `ticks_diff()` is needed, it implements modular (or more specifically, ring)
    arithmetic to produce correct result even for wrap-around values (as long as they not
    too distant in between, see below). The function returns **signed** value in the range
    [*-TICKS_PERIOD/2* .. *TICKS_PERIOD/2-1*] (that's a typical range definition for
    two's-complement signed binary integers). If the result is negative, it means that
    *ticks1* occurred earlier in time than *ticks2*. Otherwise, it means that
    *ticks1* occurred after *ticks2*. This holds **only** if *ticks1* and *ticks2*
    are apart from each other for no more than *TICKS_PERIOD/2-1* ticks. If that does
    not hold, incorrect result will be returned. Specifically, if two tick values are
    apart for *TICKS_PERIOD/2-1* ticks, that value will be returned by the function.
    However, if *TICKS_PERIOD/2* of real-time ticks has passed between them, the
    function will return *-TICKS_PERIOD/2* instead, i.e. result value will wrap around
    to the negative range of possible values.

    Informal rationale of the constraints above: Suppose you are locked in a room with no
    means to monitor passing of time except a standard 12-notch clock. Then if you look at
    dial-plate now, and don't look again for another 13 hours (e.g., if you fall for a
    long sleep), then once you finally look again, it may seem to you that only 1 hour
    has passed. To avoid this mistake, just look at the clock regularly. Your application
    should do the same. "Too long sleep" metaphor also maps directly to application
    behaviour: don't let your application run any single task for too long. Run tasks
    in steps, and do time-keeping in between.

    `ticks_diff()` is designed to accommodate various usage patterns, among them:

    * Polling with timeout. In this case, the order of events is known, and you will deal
      only with positive results of `ticks_diff()`::

         # Wait for GPIO pin to be asserted, but at most 500us
         start = time.ticks_us()
         while pin.value() == 0:
             if time.ticks_diff(time.ticks_us(), start) > 500:
                 raise TimeoutError

    * Scheduling events. In this case, `ticks_diff()` result may be negative
      if an event is overdue::

         # This code snippet is not optimized
         now = time.ticks_ms()
         scheduled_time = task.scheduled_time()
         if ticks_diff(scheduled_time, now) > 0:
             print("Too early, let's nap")
             sleep_ms(ticks_diff(scheduled_time, now))
             task.run()
         elif ticks_diff(scheduled_time, now) == 0:
             print("Right at time!")
             task.run()
         elif ticks_diff(scheduled_time, now) < 0:
             print("Oops, running late, tell task to run faster!")
             task.run(run_faster=true)

    Note: Do not pass `time()` values to `ticks_diff()`, you should use
    normal mathematical operations on them. But note that `time()` may (and will)
    also overflow. This is known as https://en.wikipedia.org/wiki/Year_2038_problem .
    """
    ...

@overload
# 2nd overload to satisfy mypy when using literal 0 as argument
def ticks_diff(ticks1: _Ticks | Literal[0] | int, ticks2: _Ticks | Literal[0] | int, /) -> int: ...

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
