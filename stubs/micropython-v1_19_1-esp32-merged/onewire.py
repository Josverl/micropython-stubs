"""
Module: 'onewire' on micropython-v1.19.1-esp32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Any


class OneWire:
    MATCH_ROM = 85  # type: int
    SKIP_ROM = 204  # type: int
    SEARCH_ROM = 240  # type: int

    def select_rom(self, *args, **kwargs) -> Any:
        ...

    def writebyte(self, *args, **kwargs) -> Any:
        ...

    def crc8(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def readbyte(self, *args, **kwargs) -> Any:
        ...

    def readbit(self, *args, **kwargs) -> Any:
        ...

    def writebit(self, *args, **kwargs) -> Any:
        ...

    def reset(self, *args, **kwargs) -> Any:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class OneWireError(Exception):
    ...
