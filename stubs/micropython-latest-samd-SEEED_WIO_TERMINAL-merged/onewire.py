"""
Module: 'onewire' on micropython-v1.21.0-samd-SEEED_WIO_TERMINAL
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51P19A', 'arch': 'armv7emsp'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete


class OneWire:
    MATCH_ROM = 85  # type: int
    SKIP_ROM = 204  # type: int
    SEARCH_ROM = 240  # type: int

    def select_rom(self, *args, **kwargs) -> Incomplete:
        ...

    def writebyte(self, *args, **kwargs) -> Incomplete:
        ...

    def crc8(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def readbyte(self, *args, **kwargs) -> Incomplete:
        ...

    def readbit(self, *args, **kwargs) -> Incomplete:
        ...

    def writebit(self, *args, **kwargs) -> Incomplete:
        ...

    def reset(self, *args, **kwargs) -> Incomplete:
        ...

    def scan(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class OneWireError(Exception):
    ...
