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
_ACCEL_SCALE: Incomplete
_GYRO_SCALE: Incomplete
_MAGNET_SCALE: Incomplete
_ODR_IMU: Incomplete
_ODR_MAGNET: Incomplete

class LSM9DS1:
    bus: Incomplete
    address_imu: Incomplete
    address_magnet: Incomplete
    gyro_scale: Incomplete
    accel_scale: Incomplete
    scale_factor_magnet: Incomplete
    scratch_int: Incomplete
    def __init__(
        self,
        bus,
        address_imu: int = ...,
        address_magnet: int = ...,
        gyro_odr: int = ...,
        gyro_scale: int = ...,
        accel_odr: int = ...,
        accel_scale: int = ...,
        magnet_odr: int = ...,
        magnet_scale: int = ...,
    ) -> None: ...
    def calibrate_magnet(self, offset) -> None: ...
    def gyro_id(self): ...
    def magent_id(self): ...
    def magnet(self): ...
    def gyro(self): ...
    def accel(self): ...
    def iter_accel_gyro(self) -> Generator[Incomplete, None, None]: ...
