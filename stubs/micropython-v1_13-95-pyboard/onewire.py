"""
Module: 'onewire' on pyboard 1.13.0-95
"""
# MCU: (sysname='pyboard', nodename='pyboard', release='1.13.0', version='v1.13-95-g0fff2e03f on 2020-10-03', machine='PYBv1.1 with STM32F405RG')
# Stubber: 1.3.4 - updated
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
