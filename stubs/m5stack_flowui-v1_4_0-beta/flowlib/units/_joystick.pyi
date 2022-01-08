from typing import Any

class Joystick:
    InvertX: Any
    InvertY: Any
    Press: Any
    X: Any
    Y: Any
    def _available() -> None: ...
    def _update() -> None: ...
    def deinit() -> None: ...
    portMethod: int

i2c_bus: Any
time: Any
unit: Any
