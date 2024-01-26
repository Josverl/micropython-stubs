"""
Time related functions.

MicroPython module: https://docs.micropython.org/en/v1.22.0/library/time.html

CPython module: :mod:`python:time` https://docs.python.org/3/library/time.html .

The ``time`` module provides functions for getting the current time and date,
measuring time intervals, and for delays.

**Time Epoch**: Unix port uses standard for POSIX systems epoch of
1970-01-01 00:00:00 UTC. However, some embedded ports use epoch of
2000-01-01 00:00:00 UTC. Epoch year may be determined with ``gmtime(0)[0]``.

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
from utime import *
from _typeshed import Incomplete

_TS_YEAR: Incomplete
_TS_MON: Incomplete
_TS_MDAY: Incomplete
_TS_HOUR: Incomplete
_TS_MIN: Incomplete
_TS_SEC: Incomplete
_TS_WDAY: Incomplete
_TS_YDAY: Incomplete
_TS_ISDST: Incomplete
_WDAY: Incomplete
_MDAY: Incomplete

def strftime(datefmt, ts): ...
