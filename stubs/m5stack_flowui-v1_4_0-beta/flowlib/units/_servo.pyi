from typing import Any

class PWM:
    def deinit(self, *argv) -> Any: ...
    def duty(self, *argv) -> Any: ...
    def freq(self, *argv) -> Any: ...
    def init(self, *argv) -> Any: ...
    def list(self, *argv) -> Any: ...
    def pause(self, *argv) -> Any: ...
    def resume(self, *argv) -> Any: ...

class Servo:
    def deinit(self, *argv) -> Any: ...
    portMethod: int
    def write_angle(self, *argv) -> Any: ...
    def write_us(self, *argv) -> Any: ...

unit: Any
