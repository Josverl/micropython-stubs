""" """

from __future__ import annotations
from typing import Tuple
from _typeshed import Incomplete

class Accel:
    """
    Create and return an accelerometer object.
    """

    def __init__(self) -> None: ...
    def filtered_xyz(self) -> Tuple:
        """
        Get a 3-tuple of filtered x, y and z values.

        Implementation note: this method is currently implemented as taking the
        sum of 4 samples, sampled from the 3 previous calls to this function along
        with the sample from the current call.  Returned values are therefore 4
        times the size of what they would be from the raw x(), y() and z() calls.
        """
        ...

    def tilt(self) -> Incomplete:
        """
        Get the tilt register.
        """
        ...

    def x(self) -> Incomplete:
        """
        Get the x-axis value.
        """
        ...

    def y(self) -> Incomplete:
        """
        Get the y-axis value.
        """
        ...

    def z(self) -> Incomplete:
        """
        Get the z-axis value.
        """
        ...
