from _typeshed import Incomplete
from collections.abc import Generator

_WHO_AM_I: Incomplete
_CTRL_REG1_G: Incomplete
_INT_GEN_SRC_G: Incomplete
_OUT_TEMP: Incomplete
_OUT_G: Incomplete
_CTRL_REG4_G: Incomplete
_STATUS_REG: Incomplete
_OUT_XL: Incomplete
_FIFO_CTRL_REG: Incomplete
_FIFO_SRC: Incomplete
_OFFSET_REG_X_M: Incomplete
_CTRL_REG1_M: Incomplete
_OUT_M: Incomplete
_SCALE_GYRO: Incomplete
_SCALE_ACCEL: Incomplete

class LSM9DS1:
    i2c: Incomplete
    address_gyro: Incomplete
    address_magnet: Incomplete
    scratch: Incomplete
    scratch_int: Incomplete
    def __init__(self, i2c, address_gyro: int = ..., address_magnet: int = ...) -> None: ...
    scale_gyro: Incomplete
    scale_accel: Incomplete
    def init_gyro_accel(self, sample_rate: int = ..., scale_gyro: int = ..., scale_accel: int = ...) -> None: ...
    scale_factor_magnet: Incomplete
    def init_magnetometer(self, sample_rate: int = ..., scale_magnet: int = ...) -> None: ...
    def calibrate_magnet(self, offset) -> None: ...
    def gyro_id(self): ...
    def magent_id(self): ...
    def magnet(self): ...
    def gyro(self): ...
    def accel(self): ...
    def iter_accel_gyro(self) -> Generator[Incomplete, None, None]: ...
