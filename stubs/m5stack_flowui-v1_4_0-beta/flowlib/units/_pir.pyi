from typing import Any

class Pin:
    IN: int
    INOUT: int
    IRQ_FALLING: int
    IRQ_RISING: int
    OPEN_DRAIN: int
    OUT: int
    OUT_OD: int
    PULL_DOWN: int
    PULL_FLOAT: int
    PULL_HOLD: int
    PULL_UP: int
    WAKE_HIGH: int
    WAKE_LOW: int
    def deinit(self, *argv) -> Any: ...
    def init(self, *argv) -> Any: ...
    def irq(self, *argv) -> Any: ...
    def off(self, *argv) -> Any: ...
    def on(self, *argv) -> Any: ...
    def value(self, *argv) -> Any: ...

class Pir:
    def deinit(self, *argv) -> Any: ...
    state: Any

unit: Any
