from _typeshed import Incomplete

class LSM6DSOX:
    _CTRL3_C: Incomplete
    _CTRL1_XL: Incomplete
    _CTRL8_XL: Incomplete
    _CTRL9_XL: Incomplete
    _CTRL2_G: Incomplete
    _CTRL7_G: Incomplete
    _OUTX_L_G: Incomplete
    _OUTX_L_XL: Incomplete
    _MLC_STATUS: Incomplete
    _DEFAULT_ADDR: Incomplete
    _WHO_AM_I_REG: Incomplete
    _FUNC_CFG_ACCESS: Incomplete
    _FUNC_CFG_BANK_USER: Incomplete
    _FUNC_CFG_BANK_HUB: Incomplete
    _FUNC_CFG_BANK_EMBED: Incomplete
    _MLC0_SRC: Incomplete
    _MLC_INT1: Incomplete
    _TAP_CFG0: Incomplete
    _EMB_FUNC_EN_A: Incomplete
    _EMB_FUNC_EN_B: Incomplete
    bus: Incomplete
    cs_pin: Incomplete
    address: Incomplete
    _use_i2c: Incomplete
    scratch_int: Incomplete
    gyro_scale: Incomplete
    accel_scale: Incomplete
    def __init__(
        self,
        bus,
        cs_pin: Incomplete | None = ...,
        address=...,
        gyro_odr: int = ...,
        accel_odr: int = ...,
        gyro_scale: int = ...,
        accel_scale: int = ...,
        ucf: Incomplete | None = ...,
    ) -> None: ...
    def __read_reg(self, reg, size: int = ...): ...
    def __write_reg(self, reg, val) -> None: ...
    def __read_reg_into(self, reg, buf) -> None: ...
    def reset(self) -> None: ...
    def set_mem_bank(self, bank) -> None: ...
    def set_embedded_functions(self, enable, emb_ab: Incomplete | None = ...): ...
    def load_mlc(self, ucf) -> None: ...
    def read_mlc_output(self): ...
    def read_gyro(self): ...
    def read_accel(self): ...
