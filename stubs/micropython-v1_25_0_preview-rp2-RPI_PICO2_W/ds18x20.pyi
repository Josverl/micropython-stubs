"""
Module: 'ds18x20' on micropython-v1.25.0-preview-rp2-UNKNOWN_BOARD
"""

# MCU: {'family': 'micropython', 'version': '1.25.0-preview', 'build': 'preview.236.gbfb1bee6f', 'ver': '1.25.0-preview-preview.236.gbfb1bee6f', 'port': 'rp2', 'board': 'UNKNOWN_BOARD', 'cpu': 'RP2350', 'mpy': 'v6.3', 'arch': 'armv7emsp'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

def const(*args, **kwargs) -> Incomplete: ...

class DS18X20:
    def read_scratch(self, *args, **kwargs) -> Incomplete: ...
    def read_temp(self, *args, **kwargs) -> Incomplete: ...
    def write_scratch(self, *args, **kwargs) -> Incomplete: ...
    def convert_temp(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
