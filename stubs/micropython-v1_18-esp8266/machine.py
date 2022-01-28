"""
Module: 'machine' on micropython-v1.18-esp8266
"""
# MCU: {'ver': 'v1.18', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.18', 'name': 'micropython', 'mpy': 9733, 'version': '1.18', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.3
from typing import Any


class ADC:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def read(self, *args) -> Any:
        ...

    def read_u16(self, *args) -> Any:
        ...


DEEPSLEEP = 4  # type: int
DEEPSLEEP_RESET = 5  # type: int
HARD_RESET = 6  # type: int


class I2C:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def readinto(self, *args) -> Any:
        ...

    def start(self, *args) -> Any:
        ...

    def stop(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def readfrom(self, *args) -> Any:
        ...

    def readfrom_into(self, *args) -> Any:
        ...

    def readfrom_mem(self, *args) -> Any:
        ...

    def readfrom_mem_into(self, *args) -> Any:
        ...

    def scan(self, *args) -> Any:
        ...

    def writeto(self, *args) -> Any:
        ...

    def writeto_mem(self, *args) -> Any:
        ...

    def writevto(self, *args) -> Any:
        ...


class PWM:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def deinit(self, *args) -> Any:
        ...

    def duty(self, *args) -> Any:
        ...

    def freq(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...


PWRON_RESET = 0  # type: int


class Pin:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def value(self, *args) -> Any:
        ...

    IN = 0  # type: int
    IRQ_FALLING = 2  # type: int
    IRQ_RISING = 1  # type: int
    OPEN_DRAIN = 2  # type: int
    OUT = 1  # type: int
    PULL_UP = 1  # type: int

    def init(self, *args) -> Any:
        ...

    def irq(self, *args) -> Any:
        ...

    def off(self, *args) -> Any:
        ...

    def on(self, *args) -> Any:
        ...


class RTC:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    ALARM0 = 0  # type: int

    def alarm(self, *args) -> Any:
        ...

    def alarm_left(self, *args) -> Any:
        ...

    def datetime(self, *args) -> Any:
        ...

    def irq(self, *args) -> Any:
        ...

    def memory(self, *args) -> Any:
        ...


SOFT_RESET = 4  # type: int


class SPI:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    LSB = 1  # type: int
    MSB = 0  # type: int

    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def write_readinto(self, *args) -> Any:
        ...


class Signal:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def value(self, *args) -> Any:
        ...

    def off(self, *args) -> Any:
        ...

    def on(self, *args) -> Any:
        ...


class SoftI2C:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def readinto(self, *args) -> Any:
        ...

    def start(self, *args) -> Any:
        ...

    def stop(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def readfrom(self, *args) -> Any:
        ...

    def readfrom_into(self, *args) -> Any:
        ...

    def readfrom_mem(self, *args) -> Any:
        ...

    def readfrom_mem_into(self, *args) -> Any:
        ...

    def scan(self, *args) -> Any:
        ...

    def writeto(self, *args) -> Any:
        ...

    def writeto_mem(self, *args) -> Any:
        ...

    def writevto(self, *args) -> Any:
        ...


class SoftSPI:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    LSB = 1  # type: int
    MSB = 0  # type: int

    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def write_readinto(self, *args) -> Any:
        ...


class Timer:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    ONE_SHOT = 0  # type: int
    PERIODIC = 1  # type: int

    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...


class UART:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def any(self, *args) -> Any:
        ...

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def readline(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...


class WDT:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def deinit(self, *args) -> Any:
        ...

    def feed(self, *args) -> Any:
        ...


WDT_RESET = 1  # type: int


def bitstream(*args) -> Any:
    ...


def deepsleep(*args) -> Any:
    ...


def disable_irq(*args) -> Any:
    ...


def enable_irq(*args) -> Any:
    ...


def freq(*args) -> Any:
    ...


def idle(*args) -> Any:
    ...


def lightsleep(*args) -> Any:
    ...


mem16: Any  ## <class 'mem'> = <16-bit memory>
mem32: Any  ## <class 'mem'> = <32-bit memory>
mem8: Any  ## <class 'mem'> = <8-bit memory>


def reset(*args) -> Any:
    ...


def reset_cause(*args) -> Any:
    ...


def sleep(*args) -> Any:
    ...


def soft_reset(*args) -> Any:
    ...


def time_pulse_us(*args) -> Any:
    ...


def unique_id(*args) -> Any:
    ...
