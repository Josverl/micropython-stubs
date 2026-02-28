"""
Module: 'uasyncio.lock' on micropython-v1.27.0-rp2-RPI_PICO_W
"""

# MCU: {'mpy': 'v6.3', 'build': '', 'ver': '1.27.0', 'arch': 'armv6m', 'version': '1.27.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'family': 'micropython', 'board_id': 'RPI_PICO_W', 'variant': '', 'cpu': 'RP2040'}
# Stubber: v1.26.5
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...
    def acquire(*args, **kwargs) -> Generator:  ## = <generator>
        ...
    def __init__(self, *argv, **kwargs) -> None: ...
