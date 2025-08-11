"""
Module: 'asyncio.lock' on micropython-v1.26.0-rp2-PIMORONI_PICOLIPO-FLASH_16M
"""

# MCU: {'mpy': 'v6.3', 'build': '', 'ver': '1.26.0', 'arch': 'armv6m', 'version': '1.26.0', 'port': 'rp2', 'board': 'PIMORONI_PICOLIPO', 'family': 'micropython', 'board_id': 'PIMORONI_PICOLIPO-FLASH_16M', 'variant': 'FLASH_16M', 'cpu': 'RP2040'}
# Stubber: v1.25.1
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...
    def acquire(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None: ...
