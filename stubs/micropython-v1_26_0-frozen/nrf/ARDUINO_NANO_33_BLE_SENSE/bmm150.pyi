from _typeshed import Incomplete
from micropython import const as const

_DEFAULT_ADDR: int
_CHIP_ID: int
_DATA: int
_POWER: int
_OPMODE: int
_INT_STATUS: int
_TRIM_X1: int
_TRIM_Y1: int
_TRIM_Z4_LSB: int
_TRIM_Z2_LSB: int
_XYAXES_FLIP: int
_ZHAXES_FLIP: int
_ODR: Incomplete

class BMM150:
    bus: Incomplete
    cs: Incomplete
    address: Incomplete
    _use_i2c: Incomplete
    trim_x1: Incomplete
    trim_y1: Incomplete
    trim_x2: Incomplete
    trim_y2: Incomplete
    trim_z1: Incomplete
    trim_z2: Incomplete
    trim_z3: Incomplete
    trim_z4: Incomplete
    trim_xy1: Incomplete
    trim_xy2: Incomplete
    trim_xyz1: Incomplete
    scratch: Incomplete
    def __init__(self, bus, cs=None, address=..., magnet_odr: int = 30) -> None:
        """Initalizes the Magnetometer.
        bus: IMU bus
        address: I2C address (in I2C mode).
        cs: SPI CS pin (in SPI mode).
        magnet_odr: (2, 6, 8, 10, 15, 20, 25, 30)
        """

    def _read_reg(self, reg, size: int = 1): ...
    def _read_reg_into(self, reg, buf) -> None: ...
    def _write_reg(self, reg, val) -> None: ...
    def _compensate_x(self, raw, hall):
        """Compensation equation ported from C driver"""

    def _compensate_y(self, raw, hall):
        """Compensation equation ported from C driver"""

    def _compensate_z(self, raw, hall):
        """Compensation equation ported from C driver"""

    def magnet_raw(self): ...
    def magnet(self):
        """Returns magnetometer vector."""
