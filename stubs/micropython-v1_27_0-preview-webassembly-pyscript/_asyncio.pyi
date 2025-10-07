"""
Module: '_asyncio' on micropython-v1.27.0-preview-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.27.0-preview', 'build': '252', 'ver': '1.27.0-preview-252', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete


class TaskQueue():
    def push(self, *args, **kwargs) -> Incomplete:
        ...

    def peek(self, *args, **kwargs) -> Incomplete:
        ...

    def remove(self, *args, **kwargs) -> Incomplete:
        ...

    def pop(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Task():
    def __init__(self, *argv, **kwargs) -> None:
        ...

