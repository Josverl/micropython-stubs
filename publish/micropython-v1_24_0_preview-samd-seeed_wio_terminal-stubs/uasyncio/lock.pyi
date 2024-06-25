"""
Module: 'uasyncio.lock' on micropython-v1.24.0-preview-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'family': 'micropython', 'build': '63', 'arch': 'armv7emsp', 'ver': '1.24.0-preview-63', 'cpu': 'SAMD51P19A'}
# Stubber: v1.20.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...

    acquire: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
