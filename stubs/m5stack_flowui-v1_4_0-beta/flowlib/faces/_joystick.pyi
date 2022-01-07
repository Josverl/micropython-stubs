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
    def setLed() -> None: ...

i2c_bus: Any
time: Any
