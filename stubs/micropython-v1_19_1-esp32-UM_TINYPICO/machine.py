"""
Module: 'machine' on micropython-v1.19.1-esp32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Any


class ADC:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    ATTN_0DB = 0  # type: int
    ATTN_11DB = 3  # type: int
    ATTN_2_5DB = 1  # type: int
    ATTN_6DB = 2  # type: int
    WIDTH_10BIT = 10  # type: int
    WIDTH_11BIT = 11  # type: int
    WIDTH_12BIT = 12  # type: int
    WIDTH_9BIT = 9  # type: int

    def atten(self, *args, **kwargs) -> Any:
        ...

    def block(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def read_u16(self, *args, **kwargs) -> Any:
        ...

    def read_uv(self, *args, **kwargs) -> Any:
        ...

    def width(self, *args, **kwargs) -> Any:
        ...


class ADCBlock:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def connect(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...


class DAC:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def write(self, *args, **kwargs) -> Any:
        ...


DEEPSLEEP = 4  # type: int
DEEPSLEEP_RESET = 4  # type: int
EXT0_WAKE = 2  # type: int
EXT1_WAKE = 3  # type: int
HARD_RESET = 2  # type: int


class I2C:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def start(self, *args, **kwargs) -> Any:
        ...

    def stop(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def readfrom(self, *args, **kwargs) -> Any:
        ...

    def readfrom_into(self, *args, **kwargs) -> Any:
        ...

    def readfrom_mem(self, *args, **kwargs) -> Any:
        ...

    def readfrom_mem_into(self, *args, **kwargs) -> Any:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...

    def writeto(self, *args, **kwargs) -> Any:
        ...

    def writeto_mem(self, *args, **kwargs) -> Any:
        ...

    def writevto(self, *args, **kwargs) -> Any:
        ...


class I2S:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    MONO = 0  # type: int
    RX = 9  # type: int
    STEREO = 1  # type: int
    TX = 5  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def shift(self, *args, **kwargs) -> Any:
        ...


PIN_WAKE = 2  # type: int


class PWM:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def duty(self, *args, **kwargs) -> Any:
        ...

    def duty_ns(self, *args, **kwargs) -> Any:
        ...

    def duty_u16(self, *args, **kwargs) -> Any:
        ...

    def freq(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...


PWRON_RESET = 1  # type: int


class Pin:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def value(self, *args, **kwargs) -> Any:
        ...

    DRIVE_0 = 0  # type: int
    DRIVE_1 = 1  # type: int
    DRIVE_2 = 2  # type: int
    DRIVE_3 = 3  # type: int
    IN = 1  # type: int
    IRQ_FALLING = 2  # type: int
    IRQ_RISING = 1  # type: int
    OPEN_DRAIN = 7  # type: int
    OUT = 3  # type: int
    PULL_DOWN = 1  # type: int
    PULL_UP = 2  # type: int
    WAKE_HIGH = 5  # type: int
    WAKE_LOW = 4  # type: int

    def init(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def off(self, *args, **kwargs) -> Any:
        ...

    def on(self, *args, **kwargs) -> Any:
        ...


class RTC:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def datetime(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def memory(self, *args, **kwargs) -> Any:
        ...


class SDCard:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def info(self, *args, **kwargs) -> Any:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def readblocks(self, *args, **kwargs) -> Any:
        ...

    def writeblocks(self, *args, **kwargs) -> Any:
        ...


SLEEP = 2  # type: int
SOFT_RESET = 5  # type: int


class SPI:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    LSB = 1  # type: int
    MSB = 0  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def write_readinto(self, *args, **kwargs) -> Any:
        ...


class Signal:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def value(self, *args, **kwargs) -> Any:
        ...

    def off(self, *args, **kwargs) -> Any:
        ...

    def on(self, *args, **kwargs) -> Any:
        ...


class SoftI2C:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def start(self, *args, **kwargs) -> Any:
        ...

    def stop(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def readfrom(self, *args, **kwargs) -> Any:
        ...

    def readfrom_into(self, *args, **kwargs) -> Any:
        ...

    def readfrom_mem(self, *args, **kwargs) -> Any:
        ...

    def readfrom_mem_into(self, *args, **kwargs) -> Any:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...

    def writeto(self, *args, **kwargs) -> Any:
        ...

    def writeto_mem(self, *args, **kwargs) -> Any:
        ...

    def writevto(self, *args, **kwargs) -> Any:
        ...


class SoftSPI:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    LSB = 1  # type: int
    MSB = 0  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def write_readinto(self, *args, **kwargs) -> Any:
        ...


TIMER_WAKE = 4  # type: int
TOUCHPAD_WAKE = 5  # type: int


class Timer:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def value(self, *args, **kwargs) -> Any:
        ...

    ONE_SHOT = 0  # type: int
    PERIODIC = 1  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...


class TouchPad:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def config(self, *args, **kwargs) -> Any:
        ...


class UART:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def any(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    CTS = 2  # type: int
    INV_CTS = 8  # type: int
    INV_RTS = 64  # type: int
    INV_RX = 4  # type: int
    INV_TX = 32  # type: int
    RTS = 1  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def sendbreak(self, *args, **kwargs) -> Any:
        ...


ULP_WAKE = 6  # type: int


class WDT:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def feed(self, *args, **kwargs) -> Any:
        ...


WDT_RESET = 3  # type: int


def bitstream(*args, **kwargs) -> Any:
    ...


def deepsleep(*args, **kwargs) -> Any:
    ...


def disable_irq(*args, **kwargs) -> Any:
    ...


def enable_irq(*args, **kwargs) -> Any:
    ...


def freq(*args, **kwargs) -> Any:
    ...


def idle(*args, **kwargs) -> Any:
    ...


def lightsleep(*args, **kwargs) -> Any:
    ...


mem16: Any  ## <class 'mem'> = <16-bit memory>
mem32: Any  ## <class 'mem'> = <32-bit memory>
mem8: Any  ## <class 'mem'> = <8-bit memory>


def reset(*args, **kwargs) -> Any:
    ...


def reset_cause(*args, **kwargs) -> Any:
    ...


def sleep(*args, **kwargs) -> Any:
    ...


def soft_reset(*args, **kwargs) -> Any:
    ...


def time_pulse_us(*args, **kwargs) -> Any:
    ...


def unique_id(*args, **kwargs) -> Any:
    ...


def wake_reason(*args, **kwargs) -> Any:
    ...
