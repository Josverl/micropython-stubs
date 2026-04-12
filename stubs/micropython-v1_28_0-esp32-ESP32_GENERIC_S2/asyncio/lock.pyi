"""
Module: 'asyncio.lock' on micropython-v1.28.0-esp32-ESP32_GENERIC_S2
"""

# MCU: {'variant': '', 'build': '', 'arch': 'xtensawin', 'port': 'esp32', 'board': 'ESP32_GENERIC_S2', 'board_id': 'ESP32_GENERIC_S2', 'mpy': 'v6.3', 'ver': '1.28.0', 'family': 'micropython', 'cpu': 'ESP32S2', 'version': '1.28.0'}
# Stubber: v1.28.1
from __future__ import annotations
from _typeshed import Incomplete

class Lock:
    def locked(self) -> Incomplete: ...
    def release(self) -> Incomplete: ...
    async def acquire(self) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
