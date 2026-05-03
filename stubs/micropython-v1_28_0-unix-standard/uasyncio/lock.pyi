"""
Module: 'uasyncio.lock' on micropython-v1.28.0-unix-standard
"""
# MCU: {'family': 'micropython', 'version': '1.28.0', 'build': '', 'ver': '1.28.0', 'port': 'unix', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'linux [GCC 12.5.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.28.3
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete


class Lock():
    def locked(self, *args, **kwargs) -> Incomplete:
        ...

    def release(self, *args, **kwargs) -> Incomplete:
        ...

    def acquire(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

