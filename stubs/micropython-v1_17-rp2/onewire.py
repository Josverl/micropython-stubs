"""
Module: 'onewire' on micropython-v1.17-rp2
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.17.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Raspberry Pi Pico with RP2040', 'nodename': 'rp2', 'ver': 'v1.17', 'release': '1.17.0'}
# Stubber: 1.5.2
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
