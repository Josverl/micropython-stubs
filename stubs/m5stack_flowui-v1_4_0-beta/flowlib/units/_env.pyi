from typing import Any

class Env:
    def _available(self, *argv) -> Any: ...
    def deinit(self, *argv) -> Any: ...
    humidity: Any
    pressure: Any
    temperature: Any
    values: Any

i2c_bus: Any
time: Any
unit: Any
