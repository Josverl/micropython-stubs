"""
Module: 'uasyncio.lock' on micropython-v1.25.0-preview-rp2-UNKNOWN_BOARD
"""

# MCU: {'family': 'micropython', 'version': '1.25.0-preview', 'build': 'preview.236.gbfb1bee6f', 'ver': '1.25.0-preview-preview.236.gbfb1bee6f', 'port': 'rp2', 'board': 'UNKNOWN_BOARD', 'cpu': 'RP2350', 'mpy': 'v6.3', 'arch': 'armv7emsp'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...

    acquire: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
