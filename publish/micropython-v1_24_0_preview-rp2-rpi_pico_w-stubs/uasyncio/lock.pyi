"""
Module: 'uasyncio.lock' on micropython-v1.24.0-preview-rp2-RPI_PICO_W
"""

# MCU: {'build': 'preview.136.gd1bf0eeb0', 'ver': '1.24.0-preview-preview.136.gd1bf0eeb0', 'version': '1.24.0-preview', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.23.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...

    acquire: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
