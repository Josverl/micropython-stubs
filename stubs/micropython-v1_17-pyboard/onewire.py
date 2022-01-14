"""
Module: 'onewire' on micropython-v1.17-pyboard
"""
# MCU: {'ver': 'v1.17', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.17.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.17.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
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
