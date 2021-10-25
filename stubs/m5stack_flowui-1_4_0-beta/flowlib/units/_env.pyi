from typing import Any

class Env:
    def _available() -> None: ...
    def deinit() -> None: ...
    humidity: Any
    pressure: Any
    temperature: Any
    values: Any

i2c_bus: Any
time: Any
unit: Any
