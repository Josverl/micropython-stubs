"""
Module: 'onewire' on micropython-v1.10-esp32
"""
# MCU: {'ver': 'v1.10', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.10.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.10.0'}
# Stubber: 1.5.0
from typing import Any


def const(*args) -> Any:
    ...


class OneWireError(Exception):
    """"""


class OneWire:
    """"""

    def __init__(self, *args) -> None:
        ...

    def crc8(self, *args) -> Any:
        ...

    def readbit(self, *args) -> Any:
        ...

    def readbyte(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def reset(self, *args) -> Any:
        ...

    def scan(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
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
