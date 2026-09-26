"""
Module: 'asyncio.core' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

_exc_context: dict = {}
# inspect: arity=1
def _promote_to_task(*args, **kwargs) -> Incomplete:
    ...

def _run_iter() -> Incomplete:
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

def get_event_loop() -> Incomplete:
    ...

def new_event_loop() -> Incomplete:
    ...

# inspect: arity=1
def _schedule_run_iter(*args, **kwargs) -> Incomplete:
    ...

def current_task() -> Incomplete:
    ...

# inspect: arity=1
def create_task(*args, **kwargs) -> Incomplete:
    ...

def ticks() -> Incomplete:
    ...

# inspect: arity=1
def sleep(*args, **kwargs) -> Incomplete:
    ...

asyncio_timer: Incomplete ## <class 'NoneType'> = None

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

_task_queue: Incomplete ## <class 'TaskQueue'> = <TaskQueue>

class CancelledError(Exception):
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


class Task():
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

_top_level_task: Incomplete ## <class 'Task'> = <Task>
cur_task: Incomplete ## <class 'Task'> = <Task>

class SingletonGenerator():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class TimeoutError(Exception):
    ...
