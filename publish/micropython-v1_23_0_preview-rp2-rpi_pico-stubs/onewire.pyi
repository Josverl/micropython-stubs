"""
Module: 'onewire' on micropython-v1.23.0-preview-rp2-RPI_PICO
"""
# MCU: {'build': 'preview.205.g2b6f81f2b', 'ver': '1.23.0-preview-preview.205.g2b6f81f2b', 'version': '1.23.0-preview', 'port': 'rp2', 'board': 'RPI_PICO', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete

class OneWireError(Exception): ...

class OneWire:
    SKIP_ROM: int = 204
    SEARCH_ROM: int = 240
    MATCH_ROM: int = 85
    def select_rom(self, *args, **kwargs) -> Incomplete: ...
    def writebit(self, *args, **kwargs) -> Incomplete: ...
    def writebyte(self, *args, **kwargs) -> Incomplete: ...
    def _search_rom(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def crc8(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def reset(self, *args, **kwargs) -> Incomplete: ...
    def readbit(self, *args, **kwargs) -> Incomplete: ...
    def readbyte(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
