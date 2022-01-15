"""
Module: 'machine' on micropython-v1.17-rp2
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.17.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Raspberry Pi Pico with RP2040', 'nodename': 'rp2', 'ver': 'v1.17', 'release': '1.17.0'}
# Stubber: 1.5.2
from typing import Any


class ADC:
    """"""

    CORE_TEMP = 4  # type: int

    def read_u16(self, *args) -> Any:
        ...


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


class PWM:
    """"""

    def deinit(self, *args) -> Any:
        ...

    def duty_ns(self, *args) -> Any:
        ...

    def duty_u16(self, *args) -> Any:
        ...

    def freq(self, *args) -> Any:
        ...


PWRON_RESET = 1  # type: int


class Pin:
    """"""

    def value(self, *args) -> Any:
        ...

    ALT = 3  # type: int
    IN = 0  # type: int
    IRQ_FALLING = 4  # type: int
    IRQ_RISING = 8  # type: int
    OPEN_DRAIN = 2  # type: int
    OUT = 1  # type: int
    PULL_DOWN = 2  # type: int
    PULL_UP = 1  # type: int

    def high(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def irq(self, *args) -> Any:
        ...

    def low(self, *args) -> Any:
        ...

    def off(self, *args) -> Any:
        ...

    def on(self, *args) -> Any:
        ...

    def toggle(self, *args) -> Any:
        ...


class RTC:
    """"""

    def datetime(self, *args) -> Any:
        ...


class SPI:
    """"""

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    LSB = 0  # type: int
    MSB = 1  # type: int

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


class SoftI2C:
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


class SoftSPI:
    """"""

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    LSB = 0  # type: int
    MSB = 1  # type: int

    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def write_readinto(self, *args) -> Any:
        ...


class Timer:
    """"""

    ONE_SHOT = 0  # type: int
    PERIODIC = 1  # type: int

    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
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

    CTS = 1  # type: int
    INV_RX = 2  # type: int
    INV_TX = 1  # type: int
    RTS = 2  # type: int

    def sendbreak(self, *args) -> Any:
        ...


class WDT:
    """"""

    def feed(self, *args) -> Any:
        ...


WDT_RESET = 3  # type: int


def bootloader(*args) -> Any:
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


def soft_reset(*args) -> Any:
    ...


def time_pulse_us(*args) -> Any:
    ...


def unique_id(*args) -> Any:
    ...
