from _typeshed import Incomplete

_DEFAULT_ADDR: int
_CHIP_ID: int
_STATUS: int
_INIT_ADDR_0: int
_INIT_ADDR_1: int
_DATA_8: int
_DATA_14: int
_CMD: int
_CONFIG_DATA: Incomplete

class BMI270:
    bus: Incomplete
    bmm_magnet: Incomplete
    cs: Incomplete
    address: Incomplete
    _use_i2c: Incomplete
    accel_scale: Incomplete
    gyro_scale: Incomplete
    scratch: Incomplete
    def __init__(
        self,
        bus,
        cs=None,
        address=...,
        gyro_odr: int = 100,
        gyro_scale: int = 2000,
        accel_odr: int = 100,
        accel_scale: int = 4,
        bmm_magnet=None,
    ) -> None:
        """Initalizes Gyro and Accelerometer.
        bus: IMU bus
        address: I2C address (in I2C mode).
        cs: SPI CS pin (in SPI mode).
        gyro_odr:  (0.78, 1.5Hz, 3.1Hz, 6.25Hz, 12.5Hz, 25Hz, 50Hz, 100Hz, 200Hz, 400Hz, 800Hz, 1600Hz)
        gyro_scale:  (125dps, 250dps, 500dps, 1000dps, 2000dps)
        accel_odr: (0.78, 1.5Hz, 3.1Hz, 6.25Hz, 12.5Hz, 25Hz, 50Hz, 100Hz, 200Hz, 400Hz, 800Hz, 1600Hz)
        accel_scale: (+/-2g, +/-4g, +/-8g, +-16g)
        """

    def _read_reg(self, reg, size: int = 1): ...
    def _read_reg_into(self, reg, buf) -> None: ...
    def _write_reg(self, reg, val) -> None: ...
    def _write_burst(self, reg, data, chunk: int = 16) -> None: ...
    def _poll_reg(self, reg, mask, retry: int = 10, delay: int = 100): ...
    def reset(self) -> None: ...
    def gyro(self):
        """Returns gyroscope vector in degrees/sec."""

    def accel(self):
        """Returns acceleration vector in gravity units (9.81m/s^2)."""

    def magnet(self):
        """Returns magnetometer vector."""
