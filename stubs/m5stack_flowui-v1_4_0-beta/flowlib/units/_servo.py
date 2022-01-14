"""
Module: 'flowlib.units._servo' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
from typing import Any


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


class Servo:
    """"""

    def deinit(self, *argv) -> Any:
        pass

    portMethod = 3

    def write_angle(self, *argv) -> Any:
        pass

    def write_us(self, *argv) -> Any:
        pass


unit = None
