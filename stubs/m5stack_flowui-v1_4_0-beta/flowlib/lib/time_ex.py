"""
Module: 'flowlib.lib.time_ex' on M5 FlowUI v1.4.0-beta
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

    def update(self, *argv) -> Any:
        pass


class TimerEx:
    """"""

    ONE_SHOT = 1
    PERIODIC = 0

    def addTimer(self, *argv) -> Any:
        pass

    def checkInit(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def timeCb(self, *argv) -> Any:
        pass


_thread = None
delete_num = None
time = None
