from collections.abc import Generator
from typing import Any

_WHO_AM_I: Any
_CTRL_REG1_G: Any
_INT_GEN_SRC_G: Any
_OUT_TEMP: Any
_OUT_G: Any
_CTRL_REG4_G: Any
_STATUS_REG: Any
_OUT_XL: Any
_FIFO_CTRL_REG: Any
_FIFO_SRC: Any
_OFFSET_REG_X_M: Any
_CTRL_REG1_M: Any
_OUT_M: Any
_SCALE_GYRO: Any
_SCALE_ACCEL: Any

class LSM9DS1:
    i2c: Any
    address_gyro: Any
    address_magnet: Any
    scratch: Any
    scratch_int: Any
    def __init__(self, i2c, address_gyro: int = ..., address_magnet: int = ...) -> None: ...
    scale_gyro: Any
    scale_accel: Any
    def init_gyro_accel(self, sample_rate: int = ..., scale_gyro: int = ..., scale_accel: int = ...) -> None: ...
    scale_factor_magnet: Any
    def init_magnetometer(self, sample_rate: int = ..., scale_magnet: int = ...) -> None: ...
    def calibrate_magnet(self, offset) -> None: ...
    def gyro_id(self): ...
    def magent_id(self): ...
    def magnet(self): ...
    def gyro(self): ...
    def accel(self): ...
    def iter_accel_gyro(self) -> Generator[Any, None, None]: ...
