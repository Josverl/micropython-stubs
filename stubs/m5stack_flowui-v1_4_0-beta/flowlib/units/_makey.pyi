from typing import Any

MAKEY_I2C_ADDR: int

class Makey:
    def _available(self, *argv) -> Any: ...
    def _updateValue(self, *argv) -> Any: ...
    def deinit(self, *argv) -> Any: ...
    value: Any
    valueAll: Any

i2c_bus: Any
unit: Any
