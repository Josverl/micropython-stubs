"""
Zephyr sensor bindings.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/zsensor.html

The ``zsensor`` module contains a class for using sensors with Zephyr.
"""

# source version: v1.26.1
# origin module:: repos/micropython/docs/library/zephyr.zsensor.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import TypeVar, TypeAlias, Awaitable
from typing import overload

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
ACCEL_XYZ: int
"""Pseudo-channel representing all three accelerometer axes."""
GYRO_XYZ: int
"""Pseudo-channel representing all three gyroscope axes."""
MAGN_XYZ: int
"""Pseudo-channel representing all three magnetic axes."""
AMBIENT_TEMP: int
"""Ambient temperature in degrees Celsius."""
IR: int
"""Infrared channel."""
RED: int
"""Red channel."""
GREEN: int
"""Green channel."""
BLUE: int
"""Blue channel."""
PM_1_0: int
"""Particulate matter concentration for 1.0um."""
PM_2_5: int
"""Particulate matter concentration for 2.5um."""
PM_10: int
"""Particulate matter concentration for 10um."""
DISTANCE: int
"""Distance channel."""
CO2: int
"""CO2 concentration channel."""
VOC: int
"""Volatile organic compound channel."""
GAS_RES: int
"""Gas resistance channel."""
VOLTAGE: int
"""Voltage channel."""
VSHUNT: int
"""Shunt voltage channel."""
CURRENT: int
"""Current channel."""
POWER: int
"""Power channel."""
RESISTANCE: int
"""Resistance channel."""
ATTR_SAMPLING_FREQUENCY: int
ATTR_LOWER_THRESH: int
ATTR_UPPER_THRESH: int
ATTR_SLOPE_TH: int
ATTR_SLOPE_DUR: int
ATTR_HYSTERESIS: int
ATTR_OVERSAMPLING: int
ATTR_FULL_SCALE: int
ATTR_OFFSET: int
ATTR_CALIB_TARGET: int
ATTR_CONFIGURATION: int
ATTR_CALIBRATION: int
ATTR_FEATURE_MASK: int
ATTR_ALERT: int
ATTR_FF_DUR: int
ATTR_BATCH_DURATION: int
ATTR_GAIN: int
ATTR_RESOLUTION: int

class Sensor:
    """
    Device names are defined in the devicetree for your board.
    For example, the device name for the accelerometer in the FRDM-k64f board is "FXOS8700".
    """
    def __init__(self, device_name: str) -> None: ...
    def measure(self) -> None:
        """
        Obtains a measurement sample from the sensor device using Zephyr sensor_sample_fetch and
        stores it in an internal driver buffer as a useful value, a pair of (integer part of value,
        fractional part of value in 1-millionths).
        Returns none if successful or OSError value if failure.
        """
        ...
    def get_float(self, sensor_channel: int) -> float:
        """
        Returns the value of the sensor measurement sample as a float.
        """
        ...
    def get_micros(self, sensor_channel: int) -> int:
        """
        Returns the value of the sensor measurement sample in millionths.
        (Ex. value of ``(1, 500000)`` returns as ``1500000``)
        """
        ...
    def get_millis(self, sensor_channel: int) -> int:
        """
        Returns the value of sensor measurement sample in thousandths.
        (Ex. value of ``(1, 500000)`` returns as ``1500``)
        """
        ...
    def get_int(self, sensor_channel: int) -> int:
        """
        Returns only the integer value of the measurement sample.
        (Ex. value of ``(1, 500000)`` returns as ``1``)
        """
        ...

    @overload
    def attr_set(self, sensor_channel: int, channel_attribute: int, val1: float, /) -> None: ...
    @overload
    def attr_set(self, sensor_channel: int, channel_attribute: int, val1: int, val2: int, /) -> None: ...
