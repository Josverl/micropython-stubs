"""
Module: 'flowlib.lib.easyIO' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
from typing import Any


class ADC:
    """"""

    ATTN_0DB = 0
    ATTN_11DB = 3
    ATTN_2_5DB = 1
    ATTN_6DB = 2
    HALL = 8
    WIDTH_10BIT = 1
    WIDTH_11BIT = 2
    WIDTH_12BIT = 3
    WIDTH_9BIT = 0

    def atten(self, *argv) -> Any:
        pass

    def collect(self, *argv) -> Any:
        pass

    def collected(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def progress(self, *argv) -> Any:
        pass

    def read(self, *argv) -> Any:
        pass

    def read_timed(self, *argv) -> Any:
        pass

    def readraw(self, *argv) -> Any:
        pass

    def stopcollect(self, *argv) -> Any:
        pass

    def vref(self, *argv) -> Any:
        pass

    def width(self, *argv) -> Any:
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

    def list(self, *argv) -> Any:
        pass

    def pause(self, *argv) -> Any:
        pass

    def resume(self, *argv) -> Any:
        pass


class Pin:
    """"""

    IN = 1
    INOUT = 3
    IRQ_FALLING = 2
    IRQ_RISING = 1
    OPEN_DRAIN = 7
    OUT = 3
    OUT_OD = 6
    PULL_DOWN = 1
    PULL_FLOAT = 3
    PULL_HOLD = 4
    PULL_UP = 2
    WAKE_HIGH = 5
    WAKE_LOW = 4

    def deinit(self, *argv) -> Any:
        pass

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


_adc_map = None


def _deinitIO():
    pass


_io_map = None
_pwm_map = None


def analogRead():
    pass


def analogWrite():
    pass


def digitalRead():
    pass


def digitalWrite():
    pass


def map_value():
    pass


def toggleIO():
    pass
