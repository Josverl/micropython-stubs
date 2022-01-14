"""
Module: 'flowlib.units._finger' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
from typing import Any

ACK_FAIL = 1
ACK_FULL = 4
ACK_NOUSER = 5
ACK_SUCCESS = 0
ACK_TIMEOUT = 8
ACK_USER_EXIST = 7
ACK_USER_OCCUPIED = 6


class Finger:
    """"""

    def _monitor(self, *argv) -> Any:
        pass

    def _write(self, *argv) -> Any:
        pass

    def addUser(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def getUnknownCb(self, *argv) -> Any:
        pass

    def readFingerCb(self, *argv) -> Any:
        pass

    def readUser(self, *argv) -> Any:
        pass

    def removeAllUser(self, *argv) -> Any:
        pass

    def removeUser(self, *argv) -> Any:
        pass


machine = None
timEx = None
time = None
unit = None
