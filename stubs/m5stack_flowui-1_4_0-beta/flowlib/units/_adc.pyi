from typing import Any

ADDRESS: int

class Adc:
    def _available() -> None: ...
    def _read_u16() -> None: ...
    def _write_u8() -> None: ...
    def deinit() -> None: ...
    def measure_set() -> None: ...
    voltage: Any

GAIN_EIGHT: int
GAIN_FOUR: int
GAIN_ONE: int
GAIN_TWO: int
MODE_CONTIN: int
MODE_SINGLE: int
OSMODE_STATE: int
RATE_15: int
RATE_240: int
RATE_30: int
RATE_60: int

def const() -> None: ...

i2c_bus: Any
struct: Any
unit: Any
