from typing import Any, Callable, List, NoReturn, Optional, Tuple

IDLE: Any
SLEEP: Any
DEEPSLEEP: Any
PWRON_RESET: Any
HARD_RESET: Any
WDT_RESET: Any
DEEPSLEEP_RESET: Any
SOFT_RESET: Any
WLAN_WAKE: Any
PIN_WAKE: Any
RTC_WAKE: Any

class Pin:
    IN: Any
    OUT: Any
    OPEN_DRAIN: Any
    ALT: Any
    ALT_OPEN_DRAIN: Any
    PULL_UP: Any
    PULL_DOWN: Any
    PULL_HOLD: Any
    LOW_POWER: Any
    MED_POWER: Any
    HIGH_POWER: Any
    IRQ_FALLING: Any
    IRQ_RISING: Any
    IRQ_LOW_LEVEL: Any
    IRQ_HIGH_LEVEL: Any
    def __init__(self, id, mode: int = ..., pull: int = ..., value, drive, alt) -> None: ...
    def init(self, mode: int = ..., pull: int = ..., value, drive, alt) -> None: ...
    def value(self, x: Optional[Any]) -> int: ...
    def __call__(self, x: Optional[Any]) -> Any: ...
    def on(self) -> None: ...
    def off(self) -> None: ...
    def irq(self, handler: Any | None = ..., trigger=..., *, priority: int = ..., wake: Any | None = ..., hard: bool = ...) -> Callable[..., Any]: ...
    def low(self) -> None: ...
    def high(self) -> None: ...
    def mode(self, mode: Optional[Any]) -> Any: ...
    def pull(self, pull: Optional[Any]) -> Any: ...
    def drive(self, drive: Optional[Any]) -> Any: ...

class Signal:
    def __init__(self, pin_obj, invert: bool = ...) -> None: ...
    def value(self, x: Optional[Any]) -> int: ...
    def on(self) -> None: ...
    def off(self) -> None: ...

class ADC:
    def __init__(self, id) -> None: ...
    def read_u16(self) -> int: ...

class UART:
    RX_ANY: Any
    def __init__(self, id, *args) -> None: ...
    def init(self, baudrate: int = ..., bits: int = ..., parity: Any | None = ..., stop: int = ..., *args) -> None: ...
    def deinit(self) -> None: ...
    def any(self) -> int: ...
    def read(self, nbytes: Optional[Any]) -> bytes: ...
    def readinto(self, buf, nbytes: Optional[Any]) -> int: ...
    def readline(self) -> None: ...
    def write(self, buf) -> int: ...
    def sendbreak(self) -> None: ...
    def irq(self, trigger, priority: int = ..., handler: Any | None = ..., wake=...) -> Any: ...

class SPI:
    MASTER: Any
    MSB: Any
    LSB: Any
    def __init__(self, id, *args) -> None: ...
    def init(self, baudrate: int = ..., *, polarity: int = ..., phase: int = ..., bits: int = ..., firstbit=..., sck: Any | None = ..., mosi: Any | None = ..., miso: Any | None = ..., pins: Optional[Tuple]) -> None: ...
    def deinit(self) -> None: ...
    def read(self, nbytes, write: int = ...) -> bytes: ...
    def readinto(self, buf, write: int = ...) -> int: ...
    def write(self, buf) -> int: ...
    def write_readinto(self, write_buf, read_buf) -> int: ...

class SoftSPI(SPI):
    def __init__(self, baudrate: int = ..., *, polarity: int = ..., phase: int = ..., bits: int = ..., firstbit=..., sck: Any | None = ..., mosi: Any | None = ..., miso: Any | None = ...) -> None: ...

class I2C:
    def __init__(self, id, scl, sda, *, freq: int = ...) -> None: ...
    def init(self, scl, sda, *, freq: int = ...) -> None: ...
    def deinit(self) -> None: ...
    def scan(self) -> List: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def readinto(self, buf, nack: bool = ...) -> Any: ...
    def write(self, buf) -> int: ...
    def readfrom(self, addr, nbytes, stop: bool = ...) -> bytes: ...
    def readfrom_into(self, addr, buf, stop: bool = ...) -> None: ...
    def writeto(self, addr, buf, stop: bool = ...) -> int: ...
    def writevto(self, addr, vector, stop: bool = ...) -> int: ...
    def readfrom_mem(self, addr, memaddr, nbytes, *, addrsize: int = ...) -> bytes: ...
    def readfrom_mem_into(self, addr, memaddr, buf, *, addrsize: int = ...) -> None: ...
    def writeto_mem(self, addr, memaddr, buf, *, addrsize: int = ...) -> None: ...

class SoftI2C(I2C):
    def __init__(self, scl, sda, *, freq: int = ..., timeout: int = ...) -> None: ...

class RTC:
    ALARM0: Any
    def __init__(self, id: int = ..., *args) -> None: ...
    def init(self, datetime) -> None: ...
    def now(self) -> Tuple: ...
    def deinit(self) -> None: ...
    def alarm(self, id, time, *, repeat: bool = ...) -> None: ...
    def alarm_left(self, alarm_id: int = ...) -> int: ...
    def cancel(self, alarm_id: int = ...) -> None: ...
    def irq(self, trigger, *, handler: Any | None = ..., wake=...) -> Any: ...

class Timer:
    ONE_SHOT: Any
    PERIODIC: Any
    def __init__(self, id, *args) -> None: ...
    def init(self, *, mode=..., period: int = ..., callback: Any | None = ...) -> None: ...
    def deinit(self) -> None: ...

class WDT:
    def __init__(self, id: int = ..., timeout: int = ...) -> None: ...

class wdt:
    def feed(self) -> None: ...

class SD:
    def __init__(self, id, *args) -> None: ...
    def init(self, id: int = ..., pins=...) -> None: ...
    def deinit(self) -> None: ...

class SDCard:
    def __init__(self, slot: int = ..., width: int = ..., cd: Any | None = ..., wp: Any | None = ..., sck: Any | None = ..., miso: Any | None = ..., mosi: Any | None = ..., cs: Any | None = ..., freq: int = ...) -> None: ...

def reset() -> NoReturn: ...
def soft_reset() -> NoReturn: ...
def reset_cause() -> int: ...
def disable_irq() -> Any: ...
def enable_irq(state) -> Any: ...
def freq() -> Any: ...
def idle() -> Any: ...
def sleep() -> Any: ...
def lightsleep(time_ms: Optional[Any]) -> Any: ...
def deepsleep(time_ms: Optional[Any]) -> None: ...
def wake_reason() -> Any: ...
def unique_id() -> bytes: ...
def time_pulse_us(pin, pulse_level, timeout_us: int = ...) -> int: ...
def rng() -> int: ...
