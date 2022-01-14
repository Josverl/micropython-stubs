"""
Module: 'flowlib.power' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
from typing import Any


class IP5306:
    """"""

    def getBatteryLevel(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def isChargeFull(self, *argv) -> Any:
        pass

    def isCharging(self, *argv) -> Any:
        pass

    def setCharge(self, *argv) -> Any:
        pass

    def setChargeVolt(self, *argv) -> Any:
        pass

    def setVinMaxCurrent(self, *argv) -> Any:
        pass


i2c_bus = None
