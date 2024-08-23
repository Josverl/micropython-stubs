""" """

from __future__ import annotations
from typing import Any, Optional, Tuple
from _typeshed import Incomplete
from machine import IDLE

class RTC:
    """
    Create an RTC object. See init for parameters of initialization.
    """

    ALARM0: Incomplete
    """irq trigger source"""
    def __init__(self, id=0, *args, **kwargs) -> None: ...
    def datetime(self, datetimetuple: Optional[Any] = None) -> Tuple:
        """
        Get or set the date and time of the RTC.

        With no arguments, this method returns an 8-tuple with the current
        date and time.  With 1 argument (being an 8-tuple) it sets the date
        and time.

        The 8-tuple has the following format:

            (year, month, day, weekday, hours, minutes, seconds, subseconds)

        The meaning of the ``subseconds`` field is hardware dependent.
        """
        ...

    def init(self, datetime) -> None:
        """
        Initialise the RTC. Datetime is a tuple of the form:

           ``(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])``
        """
        ...

    def now(self) -> Tuple:
        """
        Get get the current datetime tuple.
        """
        ...

    def deinit(self) -> None:
        """
        Resets the RTC to the time of January 1, 2015 and starts running it again.
        """
        ...

    def alarm(self, id, time, *, repeat=False) -> None:
        """
        Set the RTC alarm. Time might be either a millisecond value to program the alarm to
        current time + time_in_ms in the future, or a datetimetuple. If the time passed is in
        milliseconds, repeat can be set to ``True`` to make the alarm periodic.
        """
        ...

    def alarm_left(self, alarm_id=0) -> int:
        """
        Get the number of milliseconds left before the alarm expires.
        """
        ...

    def cancel(self, alarm_id=0) -> None:
        """
        Cancel a running alarm.
        """
        ...

    def irq(self, *, trigger, handler=None, wake=IDLE) -> Incomplete:
        """
        Create an irq object triggered by a real time clock alarm.

           - ``trigger`` must be ``RTC.ALARM0``
           - ``handler`` is the function to be called when the callback is triggered.
           - ``wake`` specifies the sleep mode from where this interrupt can wake
             up the system.
        """
        ...

    def memory(self, data: Optional[Any] = None) -> bytes:
        """
        ``RTC.memory(data)`` will write *data* to the RTC memory, where *data* is any
        object which supports the buffer protocol (including `bytes`, `bytearray`,
        `memoryview` and `array.array`). ``RTC.memory()`` reads RTC memory and returns
        a `bytes` object.

        Data written to RTC user memory is persistent across restarts, including
        `machine.soft_reset()` and `machine.deepsleep()`.

        The maximum length of RTC user memory is 2048 bytes by default on esp32,
        and 492 bytes on esp8266.

        Availability: esp32, esp8266 ports.
        """
        ...
