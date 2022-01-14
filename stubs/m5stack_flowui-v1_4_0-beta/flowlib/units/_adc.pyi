from typing import Any

ADDRESS: int

class Adc:
    def _available(self, *argv) -> Any: ...
    def _read_u16(self, *argv) -> Any: ...
    def _write_u8(self, *argv) -> Any: ...
    def deinit(self, *argv) -> Any: ...
    def measure_set(self, *argv) -> Any: ...
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
