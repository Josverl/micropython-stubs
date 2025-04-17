"""
Module: 'onewire' on micropython-v1.25.0-esp8266-ESP8266_GENERIC
"""
# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensa', 'ver': '1.25.0', 'cpu': 'ESP8266'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete


class OneWireError(Exception):
    ...

class OneWire():
    SKIP_ROM: Final[int] = 204
    SEARCH_ROM: Final[int] = 240
    MATCH_ROM: Final[int] = 85
    def select_rom(self, *args, **kwargs) -> Incomplete:
        ...

    def writebit(self, *args, **kwargs) -> Incomplete:
        ...

    def writebyte(self, *args, **kwargs) -> Incomplete:
        ...

    def _search_rom(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def crc8(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def scan(self, *args, **kwargs) -> Incomplete:
        ...

    def reset(self, *args, **kwargs) -> Incomplete:
        ...

    def readbit(self, *args, **kwargs) -> Incomplete:
        ...

    def readbyte(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

