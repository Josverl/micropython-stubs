"""
Module: 'flowlib.units._ext_io' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
from typing import Any


class Ext_io:
    """"""

    ALL_INPUT = 255
    ALL_OUTPUT = 0
    INPUT = 1
    OUTPUT = 0

    def _available(self, *argv) -> Any:
        pass

    def _get_mode(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def digitRead(self, *argv) -> Any:
        pass

    def digitReadPort(self, *argv) -> Any:
        pass

    def digitWrite(self, *argv) -> Any:
        pass

    def digitWritePort(self, *argv) -> Any:
        pass

    def setPinMode(self, *argv) -> Any:
        pass

    def setPortMode(self, *argv) -> Any:
        pass


def const():
    pass


i2c_bus = None
unit = None
ustruct = None
