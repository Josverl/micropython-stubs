# copied from:
# Module: '_asyncio' on micropython-v1.24.1-rp2-RPI_PICO_W
# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.3', 'arch': 'armv6m'}

from __future__ import annotations

from _typeshed import Incomplete

class TaskQueue:
    def __init__(self, *argv, **kwargs) -> None: ...
    def push(self, *args, **kwargs) -> Incomplete: ...
    def peek(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def pop(self, *args, **kwargs) -> Incomplete: ...

class Task:
    def __init__(self, *argv, **kwargs) -> None: ...
