"""
Zephyr sensor bindings.

MicroPython module: https://docs.micropython.org/en/v1.28.0/library/zsensor.html

The ``zsensor`` module contains a class for using sensors with Zephyr.
"""

# source version: v1.28.0-preview
# origin module:: repos/micropython/docs/library/zephyr.zsensor.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, Optional
from typing_extensions import TypeVar, TypeAlias, Awaitable

ACCEL_X: Incomplete
"""Acceleration on the X axis, in m/s^2."""
ACCEL_Y: Incomplete
"""Acceleration on the Y axis, in m/s^2."""
ACCEL_Z: Incomplete
"""Acceleration on the Z axis, in m/s^2."""
ACCEL_XYZ: Incomplete
"""\
Pseudo-channel representing all three accelerometer axes.
Used for :meth:`Sensor.attr_set` and the ``Sensor.attr_get_xxx()`` methods.
"""
GYRO_X: Incomplete
"""Angular velocity around the X axis, in radians/s."""
GYRO_Y: Incomplete
"""Angular velocity around the Y axis, in radians/s."""
GYRO_Z: Incomplete
"""Angular velocity around the Z axis, in radians/s."""
GYRO_XYZ: Incomplete
"""\
Pseudo-channel representing all three gyroscope axes.
Used for :meth:`Sensor.attr_set` and the ``Sensor.attr_get_xxx()`` methods.
"""
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
"""\
Altitude, in meters.

Channel Attributes
~~~~~~~~~~~~~~~~~~~
"""
ATTR_SAMPLING_FREQUENCY: Incomplete
"""Sensor sampling frequency, i.e. how many times a second the sensor takes a measurement."""
ATTR_LOWER_THRESH: Incomplete
"""Lower threshold for trigger."""
ATTR_UPPER_THRESH: Incomplete
"""Upper threshold for trigger."""
ATTR_SLOPE_TH: Incomplete
"""Threshold for any-motion (slope) trigger."""
ATTR_SLOPE_DUR: Incomplete
"""Duration for which the slope values needs to be outside the threshold for the trigger to fire."""
ATTR_HYSTERESIS: Incomplete
ATTR_OVERSAMPLING: Incomplete
"""Oversampling factor."""
ATTR_FULL_SCALE: Incomplete
"""Sensor range, in SI units."""
ATTR_OFFSET: int
"""The sensor value returned will be altered by the amount indicated by offset: final_value = sensor_value + offset."""
ATTR_CALIB_TARGET: Incomplete
"""Calibration target. This will be used by the internal chip's algorithms to calibrate itself on a certain axis, or all of them."""
ATTR_CONFIGURATION: Incomplete
"""Configure the operating modes of a sensor."""
ATTR_CALIBRATION: Incomplete
"""Set a calibration value needed by a sensor."""
ATTR_FEATURE_MASK: Incomplete
"""Enable/disable sensor features."""
ATTR_ALERT: Incomplete
"""Alert threshold or alert enable/disable."""
ATTR_FF_DUR: Incomplete
"""\
Free-fall duration represented in milliseconds.
If the sampling frequency is changed during runtime, this attribute should be set to adjust freefall duration to the new sampling frequency.
"""
ATTR_BATCH_DURATION: Incomplete
"""Hardware batch duration in ticks."""
ATTR_GAIN: Incomplete
ATTR_RESOLUTION: Incomplete

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
    def attr_set(self, sensor_channel, channel_attribute, val1, val2: Optional[Any] = None) -> None:
        """
        Set the given channel's attribute to the given value.
        ``val1`` may be a float, in which case ``val2`` is not given, or
        ``val1`` can be used for the value's
        integer part and ``val2`` for the value's fractional part in millionths.

        Returns ``None`` if successful, or raises ``OSError``.
        """
        ...
    def attr_get_float(self, sensor_channel, channel_attribute) -> float:
        """
        Returns the value of the sensor channel's attribute as a float.

        Many sensors do not support this or any other of the ``attr_get`` methods.
        """
        ...
    def attr_get_micros(self, sensor_channel, channel_attribute) -> Incomplete:
        """
        Returns the value of the sensor channel's attribute in millionths.
        (Ex. value of ``(1, 500000)`` returns as ``1500000``)
        """
        ...
    def attr_get_millis(self, sensor_channel, channel_attribute) -> Incomplete:
        """
        Returns the value of the sensor channel's attribute in thousandths.
        (Ex. value of ``(1, 500000)`` returns as ``1500``)
        """
        ...
    def attr_get_int(self, sensor_channel, channel_attribute) -> int:
        """
        Returns only the integer value of the channel's attribute.
        (Ex. value of ``(1, 500000)`` returns as ``1``)
        """
        ...
