from _typeshed import Incomplete
from micropython import const as const

_CTRL3_C: int
_CTRL1_XL: int
_CTRL8_XL: int
_CTRL9_XL: int
_CTRL2_G: int
_CTRL7_G: int
_OUTX_L_G: int
_OUTX_L_XL: int
_MLC_STATUS: int
_DEFAULT_ADDR: int
_WHO_AM_I_REG: int
_FUNC_CFG_ACCESS: int
_FUNC_CFG_BANK_USER: int
_FUNC_CFG_BANK_HUB: int
_FUNC_CFG_BANK_EMBED: int
_MLC0_SRC: int
_MLC_INT1: int
_TAP_CFG0: int
_EMB_FUNC_EN_A: int
_EMB_FUNC_EN_B: int

class LSM6DSOX:
    bus: Incomplete
    cs: Incomplete
    address: Incomplete
    _use_i2c: Incomplete
    scratch_int: Incomplete
    gyro_scale: Incomplete
    accel_scale: Incomplete
    def __init__(
        self, bus, cs=None, address=..., gyro_odr: int = 104, accel_odr: int = 104, gyro_scale: int = 2000, accel_scale: int = 4, ucf=None
    ) -> None:
        """Initalizes Gyro and Accelerator.
        accel_odr: (0, 1.6Hz, 3.33Hz, 6.66Hz, 12.5Hz, 26Hz, 52Hz, 104Hz, 208Hz, 416Hz, 888Hz)
        gyro_odr:  (0, 1.6Hz, 3.33Hz, 6.66Hz, 12.5Hz, 26Hz, 52Hz, 104Hz, 208Hz, 416Hz, 888Hz)
        gyro_scale:  (245dps, 500dps, 1000dps, 2000dps)
        accel_scale: (+/-2g, +/-4g, +/-8g, +-16g)
        ucf: MLC program to load.
        """

    def _read_reg(self, reg, size: int = 1): ...
    def _write_reg(self, reg, val) -> None: ...
    def _read_reg_into(self, reg, buf) -> None: ...
    def reset(self) -> None: ...
    def set_mem_bank(self, bank) -> None: ...
    def set_embedded_functions(self, enable, emb_ab=None): ...
    def load_mlc(self, ucf) -> None: ...
    def mlc_output(self): ...
    def gyro(self):
        """Returns gyroscope vector in degrees/sec."""

    def accel(self):
        """Returns acceleration vector in gravity units (9.81m/s^2)."""
