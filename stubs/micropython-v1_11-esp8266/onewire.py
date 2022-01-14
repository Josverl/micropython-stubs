"""
Module: 'onewire' on esp8266 v1.11
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.11-8-g48dcbbe60 on 2019-05-29', machine='ESP module with ESP8266')
# Stubber: 1.1.0 - updated
from typing import Any


class OneWire:
    """"""

    MATCH_ROM = 85
    SEARCH_ROM = 240
    SKIP_ROM = 204

    def _search_rom(self, *args) -> Any:
        pass

    def crc8(self, *args) -> Any:
        pass

    def readbit(self, *args) -> Any:
        pass

    def readbyte(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def reset(self, *args) -> Any:
        pass

    def scan(self, *args) -> Any:
        pass

    def select_rom(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass

    def writebit(self, *args) -> Any:
        pass

    def writebyte(self, *args) -> Any:
        pass


class OneWireError(Exception):
    """"""


_ow = None


def const(*args) -> Any:
    pass
