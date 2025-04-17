"""
Module: 'asyncio.lock' on micropython-v1.25.0-esp32-ESP32_GENERIC_S2
"""

# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC_S2', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.25.0', 'cpu': 'ESP32S2'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...
    def acquire(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None: ...
