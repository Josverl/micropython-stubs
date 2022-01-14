"""
Module: 'onewire' on micropython-v1.17-esp32
"""
# MCU: {'ver': 'v1.17', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.17.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.17.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.0
from typing import Any


class OneWireError(Exception):
    """"""


class OneWire:
    """"""

    def __init__(self, *args) -> None:
        ...

    def readinto(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    def crc8(self, *args) -> Any:
        ...

    def readbit(self, *args) -> Any:
        ...

    def readbyte(self, *args) -> Any:
        ...

    def reset(self, *args) -> Any:
        ...

    def scan(self, *args) -> Any:
        ...

    def writebit(self, *args) -> Any:
        ...

    def writebyte(self, *args) -> Any:
        ...

    SEARCH_ROM = 240  # type: int
    MATCH_ROM = 85  # type: int
    SKIP_ROM = 204  # type: int

    def select_rom(self, *args) -> Any:
        ...
