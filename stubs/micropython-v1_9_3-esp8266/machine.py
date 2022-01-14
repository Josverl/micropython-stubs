"""
Module: 'machine' on esp8266 v1.9.3
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.0.0(5a875ba)', version='v1.9.3-8-g63826ac5c on 2017-11-01', machine='ESP module with ESP8266')
# Stubber: 1.1.2 - updated
from typing import Any


class ADC:
    """"""

    def read(self, *argv) -> Any:
        pass


DEEPSLEEP = 4
DEEPSLEEP_RESET = 5
HARD_RESET = 6


class I2C:
    """"""

    def init(self, *argv) -> Any:
        pass

    def readfrom(self, *argv) -> Any:
        pass

    def readfrom_into(self, *argv) -> Any:
        pass

    def readfrom_mem(self, *argv) -> Any:
        pass

    def readfrom_mem_into(self, *argv) -> Any:
        pass

    def readinto(self, *argv) -> Any:
        pass

    def scan(self, *argv) -> Any:
        pass

    def start(self, *argv) -> Any:
        pass

    def stop(self, *argv) -> Any:
        pass

    def write(self, *argv) -> Any:
        pass

    def writeto(self, *argv) -> Any:
        pass

    def writeto_mem(self, *argv) -> Any:
        pass


class PWM:
    """"""

    def deinit(self, *argv) -> Any:
        pass

    def duty(self, *argv) -> Any:
        pass

    def freq(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
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

    def init(self, *argv) -> Any:
        pass

    def irq(self, *argv) -> Any:
        pass

    def off(self, *argv) -> Any:
        pass

    def on(self, *argv) -> Any:
        pass

    def value(self, *argv) -> Any:
        pass


class RTC:
    """"""

    ALARM0 = 0

    def alarm(self, *argv) -> Any:
        pass

    def alarm_left(self, *argv) -> Any:
        pass

    def datetime(self, *argv) -> Any:
        pass

    def irq(self, *argv) -> Any:
        pass

    def memory(self, *argv) -> Any:
        pass


SOFT_RESET = 4


class SPI:
    """"""

    LSB = 1
    MSB = 0

    def deinit(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def read(self, *argv) -> Any:
        pass

    def readinto(self, *argv) -> Any:
        pass

    def write(self, *argv) -> Any:
        pass

    def write_readinto(self, *argv) -> Any:
        pass


class Signal:
    """"""

    def off(self, *argv) -> Any:
        pass

    def on(self, *argv) -> Any:
        pass

    def value(self, *argv) -> Any:
        pass


class Timer:
    """"""

    ONE_SHOT = 0
    PERIODIC = 1

    def deinit(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass


class UART:
    """"""

    def any(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def read(self, *argv) -> Any:
        pass

    def readinto(self, *argv) -> Any:
        pass

    def readline(self, *argv) -> Any:
        pass

    def write(self, *argv) -> Any:
        pass


class WDT:
    """"""

    def deinit(self, *argv) -> Any:
        pass

    def feed(self, *argv) -> Any:
        pass


WDT_RESET = 1


def deepsleep():
    pass


def disable_irq():
    pass


def enable_irq():
    pass


def freq():
    pass


def idle():
    pass


mem16 = None
mem32 = None
mem8 = None


def reset():
    pass


def reset_cause():
    pass


def sleep():
    pass


def time_pulse_us():
    pass


def unique_id():
    pass
