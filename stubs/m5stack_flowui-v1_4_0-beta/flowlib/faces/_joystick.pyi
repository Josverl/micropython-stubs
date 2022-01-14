from typing import Any

class Joystick:
    InvertX: Any
    InvertY: Any
    Press: Any
    X: Any
    Y: Any
    def _available(self, *argv) -> Any: ...
    def _update(self, *argv) -> Any: ...
    def deinit(self, *argv) -> Any: ...
    def setLed(self, *argv) -> Any: ...

i2c_bus: Any
time: Any
