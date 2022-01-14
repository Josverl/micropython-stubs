"""
Module: 'flowlib.timeSchedule' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
from typing import Any

ONE_SHOT = 1
PERIODIC = 0


class Timer:
    """"""

    ONE_SHOT = 1
    PERIODIC = 0

    def deinit(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def setCallback(self, *argv) -> Any:
        pass

    def start(self, *argv) -> Any:
        pass

    def stop(self, *argv) -> Any:
        pass

    def update(self, *argv) -> Any:
        pass


machine = None
time = None


class timeSch:
    """"""

    ONE_SHOT = 1
    PERIODIC = 0

    def checkInit(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def event(self, *argv) -> Any:
        pass

    def remove_all(self, *argv) -> Any:
        pass

    def run(self, *argv) -> Any:
        pass

    def setTimer(self, *argv) -> Any:
        pass

    def stop(self, *argv) -> Any:
        pass

    def timerCb(self, *argv) -> Any:
        pass
