""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing import overload
from typing_extensions import TypeVar, TypeAlias, Awaitable

class Servo:
    """
    Create a servo object.  ``id`` is 1-4, and corresponds to pins X1 through X4.
    """
    def __init__(self, id: int, /) -> None: ...
    @overload
    def angle(self) -> int:
        """
        If no arguments are given, this function returns the current angle.

        If arguments are given, this function sets the angle of the servo:

          - ``angle`` is the angle to move to in degrees.
          - ``time`` is the number of milliseconds to take to get to the specified
            angle.  If omitted, then the servo moves as quickly as possible to its
            new position.
        """
        ...

    @overload
    def angle(self, angle: int | float, time: int = 0, /) -> None:
        """
        If no arguments are given, this function returns the current angle.

        If arguments are given, this function sets the angle of the servo:

          - ``angle`` is the angle to move to in degrees.
          - ``time`` is the number of milliseconds to take to get to the specified
            angle.  If omitted, then the servo moves as quickly as possible to its
            new position.
        """
        ...

    @overload
    def speed(self) -> int:
        """
        If no arguments are given, this function returns the current speed.

        If arguments are given, this function sets the speed of the servo:

          - ``speed`` is the speed to change to, between -100 and 100.
          - ``time`` is the number of milliseconds to take to get to the specified
            speed.  If omitted, then the servo accelerates as quickly as possible.
        """
        ...

    @overload
    def speed(self, speed: int | float, time: int = 0, /) -> None:
        """
        If no arguments are given, this function returns the current speed.

        If arguments are given, this function sets the speed of the servo:

          - ``speed`` is the speed to change to, between -100 and 100.
          - ``time`` is the number of milliseconds to take to get to the specified
            speed.  If omitted, then the servo accelerates as quickly as possible.
        """
        ...

    @overload
    def pulse_width(self) -> int:
        """
        If no arguments are given, this function returns the current raw pulse-width
        value.

        If an argument is given, this function sets the raw pulse-width value.
        """
        ...

    @overload
    def pulse_width(self, value: int, /) -> None:
        """
        If no arguments are given, this function returns the current raw pulse-width
        value.

        If an argument is given, this function sets the raw pulse-width value.
        """
        ...

    @overload
    def calibration(self) -> tuple[int, int, int, int, int]:
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

    @overload
    def calibration(self, pulse_min: int, pulse_max: int, pulse_centre: int, /) -> None:
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

    @overload
    def calibration(
        self,
        pulse_min: int,
        pulse_max: int,
        pulse_centre: int,
        pulse_angle_90: int,
        pulse_speed_100: int,
        /,
    ) -> None:
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
