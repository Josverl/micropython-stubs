from machine import I2C as I2C, Pin as Pin
from typing import Any

__version__: str
_WIA: Any
_HXL: Any
_HXH: Any
_HYL: Any
_HYH: Any
_HZL: Any
_HZH: Any
_ST2: Any
_CNTL1: Any
_ASAX: Any
_ASAY: Any
_ASAZ: Any
_MODE_POWER_DOWN: int
MODE_SINGLE_MEASURE: int
MODE_CONTINOUS_MEASURE_1: int
MODE_CONTINOUS_MEASURE_2: int
MODE_EXTERNAL_TRIGGER_MEASURE: int
_MODE_SELF_TEST: int
_MODE_FUSE_ROM_ACCESS: int
OUTPUT_14_BIT: int
OUTPUT_16_BIT: int
_SO_14BIT: float
_SO_16BIT: float

class AK8963:
    i2c: Any
    address: Any
    _offset: Any
    _scale: Any
    _adjustement: Any
    _so: Any
    def __init__(self, i2c, address: int = ..., mode=..., output=..., offset=..., scale=...) -> None: ...
    @property
    def magnetic(self): ...
    @property
    def adjustement(self): ...
    @property
    def whoami(self): ...
    def _register_short(self, register, value: Any | None = ..., buf=...): ...
    def _register_three_shorts(self, register, buf=...): ...
    def _register_char(self, register, value: Any | None = ..., buf=...): ...
    def __enter__(self): ...
    def __exit__(self, exception_type, exception_value, traceback) -> None: ...
