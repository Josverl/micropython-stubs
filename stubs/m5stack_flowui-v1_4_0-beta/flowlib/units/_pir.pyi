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
    def deinit() -> None: ...
    def init() -> None: ...
    def irq() -> None: ...
    def off() -> None: ...
    def on() -> None: ...
    def value() -> None: ...

class Pir:
    def deinit() -> None: ...
    state: Any

unit: Any
