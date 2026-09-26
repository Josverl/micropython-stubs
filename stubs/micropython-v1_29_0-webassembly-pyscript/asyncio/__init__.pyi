"""
Module: 'asyncio.__init__' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

# inspect: arity=1
def create_task(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def ticks_diff(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def ticks_add(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def sleep_ms(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def wait_for_ms(*args, **kwargs) -> Incomplete:
    ...

def current_task() -> Incomplete:
    ...

def ticks() -> Incomplete:
    ...

def new_event_loop() -> Incomplete:
    ...

def get_event_loop() -> Incomplete:
    ...

# inspect: arity=1
def sleep(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
async def gather(*args, **kwargs) -> Incomplete:
    ...


class ThenableEvent():
    # inspect: arity=2
    def set(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def cancel(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def remove(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    async def wait(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class TopLevelCoro():
    # inspect: arity=2
    def set(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def send(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

asyncio_timer: Incomplete ## <class 'NoneType'> = None

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

# inspect: arity=3
async def wait_for(*args, **kwargs) -> Incomplete:
    ...


class CancelledError(Exception):
    ...

class Task():
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

cur_task: Incomplete ## <class 'Task'> = <Task>

class TimeoutError(Exception):
    ...

class Future():
    # inspect: arity=2
    def remove_done_callback(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def exception(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def set_result(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def result(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def set_exception(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def cancel(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def send(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def cancelled(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def done(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def add_done_callback(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SingletonGenerator():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class Loop():
    # inspect: arity=1
    def set_exception_handler(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def create_task(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def default_exception_handler(self, *args, **kwargs) -> Incomplete:
        ...

    def get_exception_handler(self) -> Incomplete:
        ...

    def create_future(self) -> Incomplete:
        ...

    def close(self) -> Incomplete:
        ...

    # inspect: arity=1
    def call_exception_handler(self, *args, **kwargs) -> Incomplete:
        ...

    _exc_handler: Incomplete ## <class 'NoneType'> = None
    def __init__(self, *argv, **kwargs) -> None:
        ...


class Lock():
    # inspect: arity=1
    def locked(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def release(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    async def acquire(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

