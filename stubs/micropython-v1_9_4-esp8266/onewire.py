"""
Module: 'onewire' on esp8266 v1.9.4
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.9.4-8-ga9a3caad0 on 2018-05-11', machine='ESP module with ESP8266')
# Stubber: 1.1.2 - updated
from typing import Any


class OneWire:
    """"""

    MATCH_ROM = 85
    SEARCH_ROM = 240
    SKIP_ROM = 204

    def _search_rom(self, *argv) -> Any:
        pass

    def crc8(self, *argv) -> Any:
        pass

    def readbit(self, *argv) -> Any:
        pass

    def readbyte(self, *argv) -> Any:
        pass

    def readinto(self, *argv) -> Any:
        pass

    def reset(self, *argv) -> Any:
        pass

    def scan(self, *argv) -> Any:
        pass

    def select_rom(self, *argv) -> Any:
        pass

    def write(self, *argv) -> Any:
        pass

    def writebit(self, *argv) -> Any:
        pass

    def writebyte(self, *argv) -> Any:
        pass


class OneWireError(Exception):
    """"""


_ow = None


def const():
    pass
