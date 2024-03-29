from typing import Any

TIMER_WAKE: int
EXT1_WAKE: int
HARD_RESET: int
SOFT_RESET: int
PIN_WAKE: int
PWRON_RESET: int
SLEEP: int
WDT_RESET: int
TOUCHPAD_WAKE: int
ULP_WAKE: int
EXT0_WAKE: int
DEEPSLEEP: int
DEEPSLEEP_RESET: int

def enable_irq(*args, **kwargs) -> Any: ...
def bitstream(*args, **kwargs) -> Any: ...
def disable_irq(*args, **kwargs) -> Any: ...
def deepsleep(*args, **kwargs) -> Any: ...
def wake_reason(*args, **kwargs) -> Any: ...
def sleep(*args, **kwargs) -> Any: ...
def soft_reset(*args, **kwargs) -> Any: ...
def time_pulse_us(*args, **kwargs) -> Any: ...
def unique_id(*args, **kwargs) -> Any: ...
def freq(*args, **kwargs) -> Any: ...
def reset_cause(*args, **kwargs) -> Any: ...
def idle(*args, **kwargs) -> Any: ...
def lightsleep(*args, **kwargs) -> Any: ...
def reset(*args, **kwargs) -> Any: ...

mem8: Any

class PWM:
    def duty_u16(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def freq(self, *args, **kwargs) -> Any: ...
    def deinit(self, *args, **kwargs) -> Any: ...
    def duty_ns(self, *args, **kwargs) -> Any: ...
    def duty(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class UART:
    INV_RTS: int
    INV_RX: int
    CTS: int
    INV_CTS: int
    INV_TX: int
    RTS: int
    def deinit(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def sendbreak(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def any(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def readline(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

mem32: Any
mem16: Any

class ADCBlock:
    def init(self, *args, **kwargs) -> Any: ...
    def connect(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class ADC:
    ATTN_6DB: int
    WIDTH_10BIT: int
    WIDTH_11BIT: int
    WIDTH_12BIT: int
    WIDTH_9BIT: int
    ATTN_0DB: int
    ATTN_2_5DB: int
    ATTN_11DB: int
    def read_u16(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def read_uv(self, *args, **kwargs) -> Any: ...
    def width(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def block(self, *args, **kwargs) -> Any: ...
    def atten(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class I2S:
    RX: int
    MONO: int
    STEREO: int
    TX: int
    def shift(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def irq(self, *args, **kwargs) -> Any: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def deinit(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class DAC:
    def write(self, *args, **kwargs) -> Any: ...
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

class Timer:
    ONE_SHOT: int
    PERIODIC: int
    def deinit(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def value(self, *args, **kwargs) -> Any: ...
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

class Pin:
    OPEN_DRAIN: int
    IRQ_FALLING: int
    IRQ_RISING: int
    PULL_UP: int
    OUT: int
    PULL_DOWN: int
    WAKE_HIGH: int
    DRIVE_0: int
    IN: int
    WAKE_LOW: int
    DRIVE_3: int
    DRIVE_1: int
    DRIVE_2: int
    def irq(self, *args, **kwargs) -> Any: ...
    def off(self, *args, **kwargs) -> Any: ...
    def on(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def value(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class WDT:
    def feed(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class TouchPad:
    def config(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class SDCard:
    def ioctl(self, *args, **kwargs) -> Any: ...
    def readblocks(self, *args, **kwargs) -> Any: ...
    def writeblocks(self, *args, **kwargs) -> Any: ...
    def info(self, *args, **kwargs) -> Any: ...
    def deinit(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class RTC:
    def init(self, *args, **kwargs) -> Any: ...
    def memory(self, *args, **kwargs) -> Any: ...
    def datetime(self, *args, **kwargs) -> Any: ...
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

class Signal:
    def off(self, *args, **kwargs) -> Any: ...
    def on(self, *args, **kwargs) -> Any: ...
    def value(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...
