""" """

from __future__ import annotations
from typing import Any, Optional, Tuple
from _typeshed import Incomplete

class RTC:
    """
    Create an RTC object.
    """

    def __init__(self) -> None: ...
    def datetime(self, datetimetuple: Optional[Any] = None) -> Tuple:
        """
        Get or set the date and time of the RTC.

        With no arguments, this method returns an 8-tuple with the current
        date and time.  With 1 argument (being an 8-tuple) it sets the date
        and time (and ``subseconds`` is reset to 255).

        The 8-tuple has the following format:

            (year, month, day, weekday, hours, minutes, seconds, subseconds)

        ``weekday`` is 1-7 for Monday through Sunday.

        ``subseconds`` counts down from 255 to 0
        """
        ...

    def wakeup(self, timeout, callback=None) -> None:
        """
        Set the RTC wakeup timer to trigger repeatedly at every ``timeout``
        milliseconds.  This trigger can wake the pyboard from both the sleep
        states: :meth:`pyb.stop` and :meth:`pyb.standby`.

        If ``timeout`` is ``None`` then the wakeup timer is disabled.

        If ``callback`` is given then it is executed at every trigger of the
        wakeup timer.  ``callback`` must take exactly one argument.
        """
        ...

    def info(self) -> Incomplete:
        """
        Get information about the startup time and reset source.

         - The lower 0xffff are the number of milliseconds the RTC took to
           start up.
         - Bit 0x10000 is set if a power-on reset occurred.
         - Bit 0x20000 is set if an external reset occurred
        """
        ...

    def calibration(self, cal) -> int:
        """
        Get or set RTC calibration.

        With no arguments, ``calibration()`` returns the current calibration
        value, which is an integer in the range [-511 : 512].  With one
        argument it sets the RTC calibration.

        The RTC Smooth Calibration mechanism adjusts the RTC clock rate by
        adding or subtracting the given number of ticks from the 32768 Hz
        clock over a 32 second period (corresponding to 2^20 clock ticks.)
        Each tick added will speed up the clock by 1 part in 2^20, or 0.954
        ppm; likewise the RTC clock it slowed by negative values. The
        usable calibration range is:
        (-511 * 0.954) ~= -487.5 ppm up to (512 * 0.954) ~= 488.5 ppm
        """
        ...
