""" """

from __future__ import annotations

from typing import Tuple

class Accel:
    """
    Accel is an object that controls the accelerometer.  Example usage::

        accel = pyb.Accel()
        for i in range(10):
            print(accel.x(), accel.y(), accel.z())

    Raw values are between -32 and 31.
    """

    def __init__(self) -> None:
        """
        Create and return an accelerometer object.
        """

    def filtered_xyz(self) -> Tuple:
        """
        Get a 3-tuple of filtered x, y and z values.

        Implementation note: this method is currently implemented as taking the
        sum of 4 samples, sampled from the 3 previous calls to this function along
        with the sample from the current call.  Returned values are therefore 4
        times the size of what they would be from the raw x(), y() and z() calls.
        """
        ...

    def tilt(self) -> int:
        """
        Get the tilt register.
        """
        ...

    def x(self) -> int:
        """
        Get the x-axis value.
        """
        ...

    def y(self) -> int:
        """
        Get the y-axis value.
        """
        ...

    def z(self) -> int:
        """
        Get the z-axis value.
        """
        ...
