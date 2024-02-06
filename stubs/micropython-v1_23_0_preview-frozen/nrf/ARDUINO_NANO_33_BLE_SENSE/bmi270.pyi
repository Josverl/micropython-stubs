from _typeshed import Incomplete

_DEFAULT_ADDR: Incomplete
_CHIP_ID: Incomplete
_STATUS: Incomplete
_INIT_ADDR_0: Incomplete
_INIT_ADDR_1: Incomplete
_DATA_8: Incomplete
_DATA_14: Incomplete
_CMD: Incomplete
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
        cs: Incomplete | None = ...,
        address=...,
        gyro_odr: int = ...,
        gyro_scale: int = ...,
        accel_odr: int = ...,
        accel_scale: int = ...,
        bmm_magnet: Incomplete | None = ...,
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
    def _read_reg(self, reg, size: int = ...): ...
    def _read_reg_into(self, reg, buf) -> None: ...
    def _write_reg(self, reg, val) -> None: ...
    def _write_burst(self, reg, data, chunk: int = ...) -> None: ...
    def _poll_reg(self, reg, mask, retry: int = ..., delay: int = ...): ...
    def reset(self) -> None: ...
    def gyro(self):
        """Returns gyroscope vector in degrees/sec."""
    def accel(self):
        """Returns acceleration vector in gravity units (9.81m/s^2)."""
    def magnet(self):
        """Returns magnetometer vector."""
