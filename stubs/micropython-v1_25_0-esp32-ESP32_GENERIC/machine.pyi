"""
Module: 'machine' on micropython-v1.25.0-esp32-ESP32_GENERIC
"""

# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.25.0', 'cpu': 'ESP32'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

ULP_WAKE: Final[int] = 6
SLEEP: Final[int] = 2
PWRON_RESET: Final[int] = 1
PIN_WAKE: Final[int] = 2
SOFT_RESET: Final[int] = 5
WDT_RESET: Final[int] = 3
TOUCHPAD_WAKE: Final[int] = 5
TIMER_WAKE: Final[int] = 4
HARD_RESET: Final[int] = 2
EXT0_WAKE: Final[int] = 2
DEEPSLEEP_RESET: Final[int] = 4
DEEPSLEEP: Final[int] = 4
EXT1_WAKE: Final[int] = 3

def deepsleep(*args, **kwargs) -> Incomplete: ...
def soft_reset(*args, **kwargs) -> Incomplete: ...
def dht_readinto(*args, **kwargs) -> Incomplete: ...
def reset(*args, **kwargs) -> Incomplete: ...
def unique_id(*args, **kwargs) -> Incomplete: ...
def time_pulse_us(*args, **kwargs) -> Incomplete: ...
def bitstream(*args, **kwargs) -> Incomplete: ...
def idle(*args, **kwargs) -> Incomplete: ...
def freq(*args, **kwargs) -> Incomplete: ...
def lightsleep(*args, **kwargs) -> Incomplete: ...
def disable_irq(*args, **kwargs) -> Incomplete: ...
def enable_irq(*args, **kwargs) -> Incomplete: ...
def reset_cause(*args, **kwargs) -> Incomplete: ...
def sleep(*args, **kwargs) -> Incomplete: ...
def wake_reason(*args, **kwargs) -> Incomplete: ...

mem8: Incomplete  ## <class 'mem'> = <8-bit memory>

class PWM:
    def duty_u16(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def freq(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def duty_ns(self, *args, **kwargs) -> Incomplete: ...
    def duty(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class UART:
    INV_RX: Final[int] = 4
    INV_TX: Final[int] = 32
    INV_RTS: Final[int] = 64
    RTS: Final[int] = 1
    IRQ_RXIDLE: Final[int] = 4096
    IRQ_BREAK: Final[int] = 2
    IRQ_RX: Final[int] = 1
    INV_CTS: Final[int] = 8
    CTS: Final[int] = 2
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def sendbreak(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def flush(self, *args, **kwargs) -> Incomplete: ...
    def txdone(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def any(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

mem32: Incomplete  ## <class 'mem'> = <32-bit memory>
mem16: Incomplete  ## <class 'mem'> = <16-bit memory>

class ADCBlock:
    def init(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class ADC:
    ATTN_6DB: Final[int] = 2
    WIDTH_10BIT: Final[int] = 10
    WIDTH_11BIT: Final[int] = 11
    WIDTH_12BIT: Final[int] = 12
    WIDTH_9BIT: Final[int] = 9
    ATTN_0DB: Final[int] = 0
    ATTN_2_5DB: Final[int] = 1
    ATTN_11DB: Final[int] = 3
    def read_u16(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def read_uv(self, *args, **kwargs) -> Incomplete: ...
    def width(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def block(self, *args, **kwargs) -> Incomplete: ...
    def atten(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class I2S:
    RX: Final[int] = 1
    MONO: Final[int] = 0
    STEREO: Final[int] = 1
    TX: Final[int] = 2
    def shift(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class DAC:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class I2C:
    def readfrom_mem_into(self, *args, **kwargs) -> Incomplete: ...
    def readfrom_into(self, *args, **kwargs) -> Incomplete: ...
    def readfrom_mem(self, *args, **kwargs) -> Incomplete: ...
    def writeto_mem(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def writeto(self, *args, **kwargs) -> Incomplete: ...
    def writevto(self, *args, **kwargs) -> Incomplete: ...
    def start(self, *args, **kwargs) -> Incomplete: ...
    def readfrom(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def stop(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Timer:
    ONE_SHOT: Final[int] = 0
    PERIODIC: Final[int] = 1
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def value(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class SoftSPI:
    LSB: Final[int] = 1
    MSB: Final[int] = 0
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def write_readinto(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Pin:
    OPEN_DRAIN: Final[int] = 7
    OUT: Final[int] = 3
    IRQ_RISING: Final[int] = 1
    WAKE_LOW: Final[int] = 4
    WAKE_HIGH: Final[int] = 5
    PULL_DOWN: Final[int] = 1
    PULL_UP: Final[int] = 2
    DRIVE_1: Final[int] = 1
    IRQ_FALLING: Final[int] = 2
    DRIVE_0: Final[int] = 0
    IN: Final[int] = 1
    DRIVE_2: Final[int] = 2
    DRIVE_3: Final[int] = 3
    def off(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def on(self, *args, **kwargs) -> Incomplete: ...
    def toggle(self, *args, **kwargs) -> Incomplete: ...
    def value(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...

    class board:
        def __init__(self, *argv, **kwargs) -> None: ...

    def __init__(self, *argv, **kwargs) -> None: ...

class TouchPad:
    def config(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class WDT:
    def feed(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class SDCard:
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def readblocks(self, *args, **kwargs) -> Incomplete: ...
    def writeblocks(self, *args, **kwargs) -> Incomplete: ...
    def info(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class RTC:
    def init(self, *args, **kwargs) -> Incomplete: ...
    def memory(self, *args, **kwargs) -> Incomplete: ...
    def datetime(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class SoftI2C:
    def readfrom_mem_into(self, *args, **kwargs) -> Incomplete: ...
    def readfrom_into(self, *args, **kwargs) -> Incomplete: ...
    def readfrom_mem(self, *args, **kwargs) -> Incomplete: ...
    def writeto_mem(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def writeto(self, *args, **kwargs) -> Incomplete: ...
    def writevto(self, *args, **kwargs) -> Incomplete: ...
    def start(self, *args, **kwargs) -> Incomplete: ...
    def readfrom(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def stop(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class SPI:
    LSB: Final[int] = 1
    MSB: Final[int] = 0
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def write_readinto(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Signal:
    def off(self, *args, **kwargs) -> Incomplete: ...
    def on(self, *args, **kwargs) -> Incomplete: ...
    def value(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
