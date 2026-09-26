"""
Module: 'asyncio.event' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete


class ThreadSafeFlag():
    # inspect: arity=1
    def set(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=3
    def ioctl(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def clear(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    async def wait(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Event():
    # inspect: arity=1
    def set(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def is_set(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def clear(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    async def wait(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

