"""
Module: 'machine' on esp8266 v1.10
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.10-8-g8b7039d7d on 2019-01-26', machine='ESP module with ESP8266')
# Stubber: 1.1.0 - updated
from typing import Any


class ADC:
    """"""

    def read(self, *args) -> Any:
        pass


DEEPSLEEP = 4
DEEPSLEEP_RESET = 5
HARD_RESET = 6


class I2C:
    """"""

    def init(self, *args) -> Any:
        pass

    def readfrom(self, *args) -> Any:
        pass

    def readfrom_into(self, *args) -> Any:
        pass

    def readfrom_mem(self, *args) -> Any:
        pass

    def readfrom_mem_into(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def scan(self, *args) -> Any:
        pass

    def start(self, *args) -> Any:
        pass

    def stop(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass

    def writeto(self, *args) -> Any:
        pass

    def writeto_mem(self, *args) -> Any:
        pass


class PWM:
    """"""

    def deinit(self, *args) -> Any:
        pass

    def duty(self, *args) -> Any:
        pass

    def freq(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass


PWRON_RESET = 0


class Pin:
    """"""

    IN = 0
    IRQ_FALLING = 2
    IRQ_RISING = 1
    OPEN_DRAIN = 2
    OUT = 1
    PULL_UP = 1

    def init(self, *args) -> Any:
        pass

    def irq(self, *args) -> Any:
        pass

    def off(self, *args) -> Any:
        pass

    def on(self, *args) -> Any:
        pass

    def value(self, *args) -> Any:
        pass


class RTC:
    """"""

    ALARM0 = 0

    def alarm(self, *args) -> Any:
        pass

    def alarm_left(self, *args) -> Any:
        pass

    def datetime(self, *args) -> Any:
        pass

    def irq(self, *args) -> Any:
        pass

    def memory(self, *args) -> Any:
        pass


SOFT_RESET = 4


class SPI:
    """"""

    LSB = 1
    MSB = 0

    def deinit(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass

    def write_readinto(self, *args) -> Any:
        pass


class Signal:
    """"""

    def off(self, *args) -> Any:
        pass

    def on(self, *args) -> Any:
        pass

    def value(self, *args) -> Any:
        pass


class Timer:
    """"""

    ONE_SHOT = 0
    PERIODIC = 1

    def deinit(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass


class UART:
    """"""

    def any(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def readline(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass


class WDT:
    """"""

    def deinit(self, *args) -> Any:
        pass

    def feed(self, *args) -> Any:
        pass


WDT_RESET = 1


def deepsleep(*args) -> Any:
    pass


def disable_irq(*args) -> Any:
    pass


def enable_irq(*args) -> Any:
    pass


def freq(*args) -> Any:
    pass


def idle(*args) -> Any:
    pass


mem16 = None
mem32 = None
mem8 = None


def reset(*args) -> Any:
    pass


def reset_cause(*args) -> Any:
    pass


def sleep(*args) -> Any:
    pass


def time_pulse_us(*args) -> Any:
    pass


def unique_id(*args) -> Any:
    pass
