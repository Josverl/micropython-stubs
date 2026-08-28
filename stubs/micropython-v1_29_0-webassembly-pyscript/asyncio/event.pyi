"""
Module: 'asyncio.event' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.6
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete


class ThreadSafeFlag():
    def set(self) -> Incomplete:
        ...

    def ioctl(self, x1, x2) -> Incomplete:
        ...

    def clear(self) -> Incomplete:
        ...

    async def wait(self) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Event():
    def set(self) -> Incomplete:
        ...

    def is_set(self) -> Incomplete:
        ...

    def clear(self) -> Incomplete:
        ...

    async def wait(self) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

