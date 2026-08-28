"""
Module: 'asyncio.__init__' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.6
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

def create_task(x0) -> Incomplete:
    ...

def ticks_diff(x0, x1) -> Incomplete:
    ...

def ticks_add(x0, x1) -> Incomplete:
    ...

def sleep_ms(x0, x1) -> Incomplete:
    ...

def wait_for_ms(x0, x1) -> Incomplete:
    ...

def current_task() -> Incomplete:
    ...

def ticks() -> Incomplete:
    ...

def new_event_loop() -> Incomplete:
    ...

def get_event_loop() -> Incomplete:
    ...

def sleep(x0) -> Incomplete:
    ...

asyncio_timer: Incomplete ## <class 'NoneType'> = None
async def gather(x0) -> Incomplete:
    ...


class ThenableEvent():
    def set(self, x1) -> Incomplete:
        ...

    def cancel(self, x1) -> Incomplete:
        ...

    def remove(self, x1) -> Incomplete:
        ...

    async def wait(self) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class TopLevelCoro():
    def set(self, x1) -> Incomplete:
        ...

    def send(self) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


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

async def wait_for(x0, x1, x2) -> Incomplete:
    ...


class CancelledError(Exception):
    ...

class Task():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class TimeoutError(Exception):
    ...
cur_task: Incomplete ## <class 'Task'> = <Task>

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


class SingletonGenerator():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class Loop():
    def default_exception_handler(self, x1) -> Incomplete:
        ...

    def create_task(self) -> Incomplete:
        ...

    def get_exception_handler(self) -> Incomplete:
        ...

    def set_exception_handler(self) -> Incomplete:
        ...

    def close(self) -> Incomplete:
        ...

    def call_exception_handler(self) -> Incomplete:
        ...

    _exc_handler: Incomplete ## <class 'NoneType'> = None
    def __init__(self, *argv, **kwargs) -> None:
        ...


class Lock():
    def locked(self) -> Incomplete:
        ...

    def release(self) -> Incomplete:
        ...

    async def acquire(self) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

