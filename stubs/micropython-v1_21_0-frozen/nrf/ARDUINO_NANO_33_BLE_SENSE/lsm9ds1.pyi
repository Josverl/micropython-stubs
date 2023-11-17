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
    ) -> None:
        """Initalizes Gyro, Accelerometer and Magnetometer.
        bus: IMU bus
        address_imu: IMU I2C address.
        address_magnet: Magnetometer I2C address.
        gyro_odr: (0, 14.9Hz, 59.5Hz, 119Hz, 238Hz, 476Hz, 952Hz)
        gyro_scale: (245dps, 500dps, 2000dps )
        accel_odr: (0, 14.9Hz, 59.5Hz, 119Hz, 238Hz, 476Hz, 952Hz)
        accel_scale: (+/-2g, +/-4g, +/-8g, +-16g)
        magnet_odr: (0.625Hz, 1.25Hz, 2.5Hz, 5Hz, 10Hz, 20Hz, 40Hz, 80Hz)
        magnet_scale: (+/-4, +/-8, +/-12, +/-16)
        """
    def calibrate_magnet(self, offset) -> None:
        """
        offset is a magnet vector that will be subtracted by the magnetometer
        for each measurement. It is written to the magnetometer's offset register
        """
    def gyro_id(self): ...
    def magent_id(self): ...
    def magnet(self):
        """Returns magnetometer vector in gauss.
        raw_values: if True, the non-scaled adc values are returned
        """
    def gyro(self):
        """Returns gyroscope vector in degrees/sec."""
    def accel(self):
        """Returns acceleration vector in gravity units (9.81m/s^2)."""
    def iter_accel_gyro(self) -> Generator[Incomplete, None, None]:
        """A generator that returns tuples of (gyro,accelerometer) data from the fifo."""
