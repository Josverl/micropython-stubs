"""
Module: 'machine' on micropython-v1.11-esp32
"""
# MCU: {'ver': 'v1.11', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.11.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.11.0'}
# Stubber: 1.5.0
from typing import Any


class ADC:
    """"""

    def read(self, *args) -> Any:
        ...

    ATTN_0DB = 0  # type: int
    ATTN_11DB = 3  # type: int
    ATTN_2_5DB = 1  # type: int
    ATTN_6DB = 2  # type: int
    WIDTH_10BIT = 1  # type: int
    WIDTH_11BIT = 2  # type: int
    WIDTH_12BIT = 3  # type: int
    WIDTH_9BIT = 0  # type: int

    def atten(self, *args) -> Any:
        ...

    @classmethod
    def width(cls, *args) -> Any:
        ...


class DAC:
    """"""

    def write(self, *args) -> Any:
        ...


DEEPSLEEP = 4  # type: int
DEEPSLEEP_RESET = 4  # type: int
EXT0_WAKE = 2  # type: int
EXT1_WAKE = 3  # type: int
HARD_RESET = 2  # type: int


class I2C:
    """"""

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


PIN_WAKE = 2  # type: int


class PWM:
    """"""

    def deinit(self, *args) -> Any:
        ...

    def duty(self, *args) -> Any:
        ...

    def freq(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...


PWRON_RESET = 1  # type: int


class Pin:
    """"""

    def value(self, *args) -> Any:
        ...

    IN = 1  # type: int
    IRQ_FALLING = 2  # type: int
    IRQ_RISING = 1  # type: int
    OPEN_DRAIN = 7  # type: int
    OUT = 3  # type: int
    PULL_DOWN = 1  # type: int
    PULL_HOLD = 4  # type: int
    PULL_UP = 2  # type: int
    WAKE_HIGH = 5  # type: int
    WAKE_LOW = 4  # type: int

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

    def datetime(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def memory(self, *args) -> Any:
        ...


SLEEP = 2  # type: int
SOFT_RESET = 5  # type: int


class SPI:
    """"""

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

    def value(self, *args) -> Any:
        ...

    def off(self, *args) -> Any:
        ...

    def on(self, *args) -> Any:
        ...


TIMER_WAKE = 4  # type: int
TOUCHPAD_WAKE = 5  # type: int


class Timer:
    """"""

    def value(self, *args) -> Any:
        ...

    ONE_SHOT = 0  # type: int
    PERIODIC = 1  # type: int

    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...


class TouchPad:
    """"""

    def read(self, *args) -> Any:
        ...

    def config(self, *args) -> Any:
        ...


class UART:
    """"""

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

    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def sendbreak(self, *args) -> Any:
        ...


ULP_WAKE = 6  # type: int


class WDT:
    """"""

    def feed(self, *args) -> Any:
        ...


WDT_RESET = 3  # type: int


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


def time_pulse_us(*args) -> Any:
    ...


def unique_id(*args) -> Any:
    ...


def wake_reason(*args) -> Any:
    ...
