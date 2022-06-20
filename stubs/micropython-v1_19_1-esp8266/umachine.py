"""
Module: 'umachine' on micropython-v1.19.1-esp8266
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp8266', 'port': 'esp8266', 'machine': 'ESP module (1M) with ESP8266', 'release': '1.19.1', 'nodename': 'esp8266', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp8266', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Any


class ADC:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def read_u16(self, *args, **kwargs) -> Any:
        ...


DEEPSLEEP = 4  # type: int
DEEPSLEEP_RESET = 5  # type: int
HARD_RESET = 6  # type: int


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


class PWM:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def duty(self, *args, **kwargs) -> Any:
        ...

    def freq(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...


PWRON_RESET = 0  # type: int


class Pin:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def value(self, *args, **kwargs) -> Any:
        ...

    IN = 0  # type: int
    IRQ_FALLING = 2  # type: int
    IRQ_RISING = 1  # type: int
    OPEN_DRAIN = 2  # type: int
    OUT = 1  # type: int
    PULL_UP = 1  # type: int

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

    ALARM0 = 0  # type: int

    def alarm(self, *args, **kwargs) -> Any:
        ...

    def alarm_left(self, *args, **kwargs) -> Any:
        ...

    def datetime(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def memory(self, *args, **kwargs) -> Any:
        ...


SOFT_RESET = 4  # type: int


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


class Timer:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    ONE_SHOT = 0  # type: int
    PERIODIC = 1  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
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

    def init(self, *args, **kwargs) -> Any:
        ...


class WDT:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def feed(self, *args, **kwargs) -> Any:
        ...


WDT_RESET = 1  # type: int


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
