from typing import Any

class LSM6DSOX:
    _CTRL3_C: Any
    _CTRL1_XL: Any
    _CTRL8_XL: Any
    _CTRL9_XL: Any
    _CTRL2_G: Any
    _CTRL7_G: Any
    _OUTX_L_G: Any
    _OUTX_L_XL: Any
    _MLC_STATUS: Any
    _DEFAULT_ADDR: Any
    _WHO_AM_I_REG: Any
    _FUNC_CFG_ACCESS: Any
    _FUNC_CFG_BANK_USER: Any
    _FUNC_CFG_BANK_HUB: Any
    _FUNC_CFG_BANK_EMBED: Any
    _MLC0_SRC: Any
    _MLC_INT1: Any
    _TAP_CFG0: Any
    _EMB_FUNC_EN_A: Any
    _EMB_FUNC_EN_B: Any
    i2c: Any
    address: Any
    scratch_int: Any
    gyro_scale: Any
    accel_scale: Any
    def __init__(self, i2c, address=..., gyro_odr: int = ..., accel_odr: int = ..., gyro_scale: int = ..., accel_scale: int = ..., ucf: Any | None = ...) -> None: ...
    def __read_reg(self, reg, size: int = ...): ...
    def __write_reg(self, reg, val) -> None: ...
    def reset(self) -> None: ...
    def set_mem_bank(self, bank) -> None: ...
    def set_embedded_functions(self, enable, emb_ab: Any | None = ...): ...
    def load_mlc(self, ucf) -> None: ...
    def read_mlc_output(self): ...
    def read_gyro(self): ...
    def read_accel(self): ...
