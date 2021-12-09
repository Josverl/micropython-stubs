from machine import I2C as I2C, Pin as Pin
from typing import Any

__version__: str
_GYRO_CONFIG: Any
_ACCEL_CONFIG: Any
_ACCEL_CONFIG2: Any
_INT_PIN_CFG: Any
_ACCEL_XOUT_H: Any
_ACCEL_XOUT_L: Any
_ACCEL_YOUT_H: Any
_ACCEL_YOUT_L: Any
_ACCEL_ZOUT_H: Any
_ACCEL_ZOUT_L: Any
_TEMP_OUT_H: Any
_TEMP_OUT_L: Any
_GYRO_XOUT_H: Any
_GYRO_XOUT_L: Any
_GYRO_YOUT_H: Any
_GYRO_YOUT_L: Any
_GYRO_ZOUT_H: Any
_GYRO_ZOUT_L: Any
_WHO_AM_I: Any
ACCEL_FS_SEL_2G: Any
ACCEL_FS_SEL_4G: Any
ACCEL_FS_SEL_8G: Any
ACCEL_FS_SEL_16G: Any
_ACCEL_SO_2G: int
_ACCEL_SO_4G: int
_ACCEL_SO_8G: int
_ACCEL_SO_16G: int
GYRO_FS_SEL_250DPS: Any
GYRO_FS_SEL_500DPS: Any
GYRO_FS_SEL_1000DPS: Any
GYRO_FS_SEL_2000DPS: Any
_GYRO_SO_250DPS: int
_GYRO_SO_500DPS: float
_GYRO_SO_1000DPS: float
_GYRO_SO_2000DPS: float
_I2C_BYPASS_MASK: Any
_I2C_BYPASS_EN: Any
_I2C_BYPASS_DIS: Any
SF_G: int
SF_M_S2: float
SF_DEG_S: int
SF_RAD_S: float

class MPU6500:
    i2c: Any
    address: Any
    _accel_so: Any
    _gyro_so: Any
    _accel_sf: Any
    _gyro_sf: Any
    def __init__(self, i2c, address: int = ..., accel_fs=..., gyro_fs=..., accel_sf=..., gyro_sf=...) -> None: ...
    @property
    def acceleration(self): ...
    @property
    def gyro(self): ...
    @property
    def whoami(self): ...
    def _register_short(self, register, value: Any | None = ..., buf=...): ...
    def _register_three_shorts(self, register, buf=...): ...
    def _register_char(self, register, value: Any | None = ..., buf=...): ...
    def _accel_fs(self, value): ...
    def _gyro_fs(self, value): ...
    def __enter__(self): ...
    def __exit__(self, exception_type, exception_value, traceback) -> None: ...
