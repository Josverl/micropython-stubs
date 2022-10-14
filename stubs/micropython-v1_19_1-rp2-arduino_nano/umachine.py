"""
Module: 'umachine' on micropython-v1.19.1-rp2
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2'}
# Stubber: 1.9.11
from typing import Any

WDT_RESET = 3  # type: int
PWRON_RESET = 1  # type: int


def disable_irq(*args, **kwargs) -> Any:
    ...


def soft_reset(*args, **kwargs) -> Any:
    ...


def enable_irq(*args, **kwargs) -> Any:
    ...


def bitstream(*args, **kwargs) -> Any:
    ...


def deepsleep(*args, **kwargs) -> Any:
    ...


def bootloader(*args, **kwargs) -> Any:
    ...


def reset(*args, **kwargs) -> Any:
    ...


def freq(*args, **kwargs) -> Any:
    ...


def reset_cause(*args, **kwargs) -> Any:
    ...


def idle(*args, **kwargs) -> Any:
    ...


def time_pulse_us(*args, **kwargs) -> Any:
    ...


def lightsleep(*args, **kwargs) -> Any:
    ...


def unique_id(*args, **kwargs) -> Any:
    ...


class WDT:
    def feed(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


mem8: Any  ## <class 'mem'> = <8-bit memory>
mem32: Any  ## <class 'mem'> = <32-bit memory>
mem16: Any  ## <class 'mem'> = <16-bit memory>


class PWM:
    def freq(self, *args, **kwargs) -> Any:
        ...

    def duty_u16(self, *args, **kwargs) -> Any:
        ...

    def duty_ns(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC:
    CORE_TEMP = 4  # type: int

    def read_u16(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2C:
    def readfrom_mem_into(self, *args, **kwargs) -> Any:
        ...

    def readfrom_into(self, *args, **kwargs) -> Any:
        ...

    def readfrom_mem(self, *args, **kwargs) -> Any:
        ...

    def writeto_mem(self, *args, **kwargs) -> Any:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...

    def writeto(self, *args, **kwargs) -> Any:
        ...

    def writevto(self, *args, **kwargs) -> Any:
        ...

    def start(self, *args, **kwargs) -> Any:
        ...

    def readfrom(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def stop(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S:
    RX = 0  # type: int
    MONO = 0  # type: int
    STEREO = 1  # type: int
    TX = 1  # type: int

    def shift(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Pin:
    PULL_DOWN = 2  # type: int
    IRQ_RISING = 8  # type: int
    OPEN_DRAIN = 2  # type: int
    OUT = 1  # type: int
    IRQ_FALLING = 4  # type: int
    PULL_UP = 1  # type: int
    ALT = 3  # type: int
    IN = 0  # type: int

    def toggle(self, *args, **kwargs) -> Any:
        ...

    def low(self, *args, **kwargs) -> Any:
        ...

    def off(self, *args, **kwargs) -> Any:
        ...

    def on(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def value(self, *args, **kwargs) -> Any:
        ...

    def high(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SoftSPI:
    LSB = 0  # type: int
    MSB = 1  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def write_readinto(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Timer:
    PERIODIC = 1  # type: int
    ONE_SHOT = 0  # type: int

    def init(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class UART:
    INV_TX = 1  # type: int
    CTS = 1  # type: int
    INV_RX = 2  # type: int
    RTS = 2  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def sendbreak(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def any(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SoftI2C:
    def readfrom_mem_into(self, *args, **kwargs) -> Any:
        ...

    def readfrom_into(self, *args, **kwargs) -> Any:
        ...

    def readfrom_mem(self, *args, **kwargs) -> Any:
        ...

    def writeto_mem(self, *args, **kwargs) -> Any:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...

    def writeto(self, *args, **kwargs) -> Any:
        ...

    def writevto(self, *args, **kwargs) -> Any:
        ...

    def start(self, *args, **kwargs) -> Any:
        ...

    def readfrom(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def stop(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class RTC:
    def datetime(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SPI:
    LSB = 0  # type: int
    MSB = 1  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def write_readinto(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Signal:
    def off(self, *args, **kwargs) -> Any:
        ...

    def on(self, *args, **kwargs) -> Any:
        ...

    def value(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
