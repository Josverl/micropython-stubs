from _typeshed import Incomplete
from collections.abc import Generator
from micropython import const as const

_WHO_AM_I: int
_CTRL_REG1_G: int
_INT_GEN_SRC_G: int
_OUT_TEMP: int
_OUT_G: int
_CTRL_REG4_G: int
_STATUS_REG: int
_OUT_XL: int
_FIFO_CTRL_REG: int
_FIFO_SRC: int
_OFFSET_REG_X_M: int
_CTRL_REG1_M: int
_OUT_M: int
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
        address_imu: int = 107,
        address_magnet: int = 30,
        gyro_odr: int = 952,
        gyro_scale: int = 245,
        accel_odr: int = 952,
        accel_scale: int = 4,
        magnet_odr: int = 80,
        magnet_scale: int = 4,
    ) -> None:
        """Initializes Gyro, Accelerometer and Magnetometer.
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
    def iter_accel_gyro(self) -> Generator[Incomplete]:
        """A generator that returns tuples of (gyro,accelerometer) data from the fifo."""
