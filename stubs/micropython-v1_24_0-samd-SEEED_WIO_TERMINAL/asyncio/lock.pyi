"""
Module: 'asyncio.lock' on micropython-v1.24.0-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'family': 'micropython', 'version': '1.24.0', 'build': '', 'ver': '1.24.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'cpu': 'SAMD51P19A', 'mpy': 'v6.3', 'arch': 'armv7emsp'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...

    acquire: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
