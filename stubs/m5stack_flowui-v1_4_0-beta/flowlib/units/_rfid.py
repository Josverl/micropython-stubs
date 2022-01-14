"""
Module: 'flowlib.units._rfid' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
from typing import Any

AUTHENT1A = 96
AUTHENT1B = 97
ERR = 2
NOTAGERR = 1
OK = 0
REQALL = 82
REQIDL = 38


class Rfid:
    """"""

    def _antenna_on(self, *argv) -> Any:
        pass

    def _anticoll(self, *argv) -> Any:
        pass

    def _auth(self, *argv) -> Any:
        pass

    def _available(self, *argv) -> Any:
        pass

    def _cflags(self, *argv) -> Any:
        pass

    def _crc(self, *argv) -> Any:
        pass

    def _get_access(self, *argv) -> Any:
        pass

    def _read(self, *argv) -> Any:
        pass

    def _request(self, *argv) -> Any:
        pass

    def _reset(self, *argv) -> Any:
        pass

    def _rreg(self, *argv) -> Any:
        pass

    def _selectTag(self, *argv) -> Any:
        pass

    def _sflags(self, *argv) -> Any:
        pass

    def _stop_crypto1(self, *argv) -> Any:
        pass

    def _tocard(self, *argv) -> Any:
        pass

    def _wreg(self, *argv) -> Any:
        pass

    def _write(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def isCardOn(self, *argv) -> Any:
        pass

    def readBlock(self, *argv) -> Any:
        pass

    def readBlockStr(self, *argv) -> Any:
        pass

    def readUid(self, *argv) -> Any:
        pass

    def writeBlock(self, *argv) -> Any:
        pass


def const():
    pass


i2c_bus = None
time = None
unit = None
