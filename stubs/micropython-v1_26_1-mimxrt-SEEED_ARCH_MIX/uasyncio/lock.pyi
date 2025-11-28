"""
Module: 'uasyncio.lock' on micropython-v1.26.1-mimxrt-SEEED_ARCH_MIX
"""

# MCU: {'variant': '', 'build': '', 'arch': 'armv7emdp', 'port': 'mimxrt', 'board': 'SEEED_ARCH_MIX', 'board_id': 'SEEED_ARCH_MIX', 'mpy': 'v6.3', 'ver': '1.26.1', 'family': 'micropython', 'cpu': 'MIMXRT1052DVL5B', 'version': '1.26.1'}
# Stubber: v1.26.3
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...
    def acquire(*args, **kwargs) -> Generator:  ## = <generator>
        ...
    def __init__(self, *argv, **kwargs) -> None: ...
