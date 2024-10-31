""" """

from __future__ import annotations
from typing import Any, Optional, Tuple
from _typeshed import Incomplete

class Servo:
    """
    Create a servo object.  ``id`` is 1-4, and corresponds to pins X1 through X4.
    """

    def __init__(self, id) -> None: ...
    def angle(self, angle: Optional[Any] = None, time=0) -> Incomplete:
        """
        If no arguments are given, this function returns the current angle.

        If arguments are given, this function sets the angle of the servo:

          - ``angle`` is the angle to move to in degrees.
          - ``time`` is the number of milliseconds to take to get to the specified
            angle.  If omitted, then the servo moves as quickly as possible to its
            new position.
        """
        ...

    def speed(self, speed: Optional[Any] = None, time=0) -> Incomplete:
        """
        If no arguments are given, this function returns the current speed.

        If arguments are given, this function sets the speed of the servo:

          - ``speed`` is the speed to change to, between -100 and 100.
          - ``time`` is the number of milliseconds to take to get to the specified
            speed.  If omitted, then the servo accelerates as quickly as possible.
        """
        ...

    def pulse_width(self, value: Optional[Any] = None) -> Incomplete:
        """
        If no arguments are given, this function returns the current raw pulse-width
        value.

        If an argument is given, this function sets the raw pulse-width value.
        """
        ...

    def calibration(self, pulse_min, pulse_max, pulse_centre, pulse_angle_90, pulse_speed_100) -> Tuple:
        """
        If no arguments are given, this function returns the current calibration
        data, as a 5-tuple.

        If arguments are given, this function sets the timing calibration:

          - ``pulse_min`` is the minimum allowed pulse width.
          - ``pulse_max`` is the maximum allowed pulse width.
          - ``pulse_centre`` is the pulse width corresponding to the centre/zero position.
          - ``pulse_angle_90`` is the pulse width corresponding to 90 degrees.
          - ``pulse_speed_100`` is the pulse width corresponding to a speed of 100.
        """
        ...
