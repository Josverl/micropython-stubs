"""
Zephyr sensor bindings.

MicroPython module: https://docs.micropython.org/en/v1.23.0/library/zsensor.html

The ``zsensor`` module contains a class for using sensors with Zephyr.
"""

# source version: v1.23.0
# origin module:: repos/micropython/docs/library/zephyr.zsensor.rst
from __future__ import annotations
from _typeshed import Incomplete

ACCEL_X: Incomplete
"""Acceleration on the X axis, in m/s^2."""
ACCEL_Y: Incomplete
"""Acceleration on the Y axis, in m/s^2."""
ACCEL_Z: Incomplete
"""Acceleration on the Z axis, in m/s^2."""
GYRO_X: Incomplete
"""Angular velocity around the X axis, in radians/s."""
GYRO_Y: Incomplete
"""Angular velocity around the Y axis, in radians/s."""
GYRO_Z: Incomplete
"""Angular velocity around the Z axis, in radians/s."""
MAGN_X: Incomplete
"""Magnetic field on the X axis, in Gauss."""
MAGN_Y: Incomplete
"""Magnetic field on the Y axis, in Gauss."""
MAGN_Z: Incomplete
"""Magnetic field on the Z axis, in Gauss."""
DIE_TEMP: Incomplete
"""Device die temperature in degrees Celsius."""
PRESS: Incomplete
"""Pressure in kilopascal."""
PROX: Incomplete
"""Proximity. Dimensionless. A value of 1 indicates that an object is close."""
HUMIDITY: Incomplete
"""Humidity, in percent."""
LIGHT: Incomplete
"""Illuminance in visible spectrum, in lux."""
ALTITUDE: Incomplete
"""Altitude, in meters."""

class Sensor:
    """
    Device names are defined in the devicetree for your board.
    For example, the device name for the accelerometer in the FRDM-k64f board is "FXOS8700".
    """

    def __init__(self, device_name) -> None: ...
    def measure(self) -> Incomplete:
        """
        Obtains a measurement sample from the sensor device using Zephyr sensor_sample_fetch and
        stores it in an internal driver buffer as a useful value, a pair of (integer part of value,
        fractional part of value in 1-millionths).
        Returns none if successful or OSError value if failure.
        """
        ...

    def get_float(self, sensor_channel) -> float:
        """
        Returns the value of the sensor measurement sample as a float.
        """
        ...

    def get_micros(self, sensor_channel) -> Incomplete:
        """
        Returns the value of the sensor measurement sample in millionths.
        (Ex. value of ``(1, 500000)`` returns as ``1500000``)
        """
        ...

    def get_millis(self, sensor_channel) -> Incomplete:
        """
        Returns the value of sensor measurement sample in thousandths.
        (Ex. value of ``(1, 500000)`` returns as ``1500``)
        """
        ...

    def get_int(self, sensor_channel) -> int:
        """
        Returns only the integer value of the measurement sample.
        (Ex. value of ``(1, 500000)`` returns as ``1``)
        """
        ...
