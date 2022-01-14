"""
Module: 'flowlib.units._ir' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
from typing import Any


class Ir:
    """"""

    def _irq_cb(self, *argv) -> Any:
        pass

    def _update(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    portMethod = 15

    def rxStatus(self, *argv) -> Any:
        pass

    def txOff(self, *argv) -> Any:
        pass

    def txOn(self, *argv) -> Any:
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


class Timer:
    """"""

    ONE_SHOT = 0
    PERIODIC = 1

    def deinit(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def value(self, *argv) -> Any:
        pass


peripheral = None
unit = None
