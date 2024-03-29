from typing import Any

PWRON_RESET: int
HARD_RESET: int
SOFT_RESET: int
WDT_RESET: int
DEEPSLEEP_RESET: int
DEEPSLEEP: int

def enable_irq(*args, **kwargs) -> Any: ...
def sleep(*args, **kwargs) -> Any: ...
def freq(*args, **kwargs) -> Any: ...
def bitstream(*args, **kwargs) -> Any: ...
def disable_irq(*args, **kwargs) -> Any: ...
def deepsleep(*args, **kwargs) -> Any: ...
def reset_cause(*args, **kwargs) -> Any: ...
def idle(*args, **kwargs) -> Any: ...
def soft_reset(*args, **kwargs) -> Any: ...
def lightsleep(*args, **kwargs) -> Any: ...
def reset(*args, **kwargs) -> Any: ...
def time_pulse_us(*args, **kwargs) -> Any: ...
def unique_id(*args, **kwargs) -> Any: ...

class RTC:
    ALARM0: int
    def datetime(self, *args, **kwargs) -> Any: ...
    def irq(self, *args, **kwargs) -> Any: ...
    def memory(self, *args, **kwargs) -> Any: ...
    def alarm_left(self, *args, **kwargs) -> Any: ...
    def alarm(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Pin:
    IRQ_RISING: int
    OUT: int
    OPEN_DRAIN: int
    PULL_UP: int
    IRQ_FALLING: int
    IN: int
    def irq(self, *args, **kwargs) -> Any: ...
    def off(self, *args, **kwargs) -> Any: ...
    def on(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def value(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

mem8: Any
mem32: Any

class ADC:
    def read_u16(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class PWM:
    def init(self, *args, **kwargs) -> Any: ...
    def freq(self, *args, **kwargs) -> Any: ...
    def duty(self, *args, **kwargs) -> Any: ...
    def deinit(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class I2C:
    def readfrom_mem_into(self, *args, **kwargs) -> Any: ...
    def readfrom_into(self, *args, **kwargs) -> Any: ...
    def readfrom_mem(self, *args, **kwargs) -> Any: ...
    def writeto_mem(self, *args, **kwargs) -> Any: ...
    def scan(self, *args, **kwargs) -> Any: ...
    def writeto(self, *args, **kwargs) -> Any: ...
    def writevto(self, *args, **kwargs) -> Any: ...
    def start(self, *args, **kwargs) -> Any: ...
    def readfrom(self, *args, **kwargs) -> Any: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def stop(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class WDT:
    def feed(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Timer:
    PERIODIC: int
    ONE_SHOT: int
    def init(self, *args, **kwargs) -> Any: ...
    def deinit(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class SoftSPI:
    LSB: int
    MSB: int
    def deinit(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def write_readinto(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class UART:
    def readline(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def any(self, *args, **kwargs) -> Any: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

mem16: Any

class SPI:
    LSB: int
    MSB: int
    def deinit(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def write_readinto(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class SoftI2C:
    def readfrom_mem_into(self, *args, **kwargs) -> Any: ...
    def readfrom_into(self, *args, **kwargs) -> Any: ...
    def readfrom_mem(self, *args, **kwargs) -> Any: ...
    def writeto_mem(self, *args, **kwargs) -> Any: ...
    def scan(self, *args, **kwargs) -> Any: ...
    def writeto(self, *args, **kwargs) -> Any: ...
    def writevto(self, *args, **kwargs) -> Any: ...
    def start(self, *args, **kwargs) -> Any: ...
    def readfrom(self, *args, **kwargs) -> Any: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def stop(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Signal:
    def off(self, *args, **kwargs) -> Any: ...
    def on(self, *args, **kwargs) -> Any: ...
    def value(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...
