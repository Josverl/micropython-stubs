from typing import Any

MAKEY_I2C_ADDR: int

class Makey:
    def _available() -> None: ...
    def _updateValue() -> None: ...
    def deinit() -> None: ...
    value: Any
    valueAll: Any

i2c_bus: Any
unit: Any
