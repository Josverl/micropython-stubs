"""
Module: 'asyncio.core' on micropython-v1.27.0-preview-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.27.0-preview', 'build': '252', 'ver': '1.27.0-preview-252', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

_exc_context: dict = {}
def _promote_to_task(*args, **kwargs) -> Incomplete:
    ...

def _run_iter(*args, **kwargs) -> Incomplete:
    ...

def ticks_diff(*args, **kwargs) -> Incomplete:
    ...

def ticks_add(*args, **kwargs) -> Incomplete:
    ...

def sleep_ms(*args, **kwargs) -> Incomplete:
    ...

def get_event_loop(*args, **kwargs) -> Incomplete:
    ...

def new_event_loop(*args, **kwargs) -> Incomplete:
    ...

def _schedule_run_iter(*args, **kwargs) -> Incomplete:
    ...

def current_task(*args, **kwargs) -> Incomplete:
    ...

def create_task(*args, **kwargs) -> Incomplete:
    ...

def ticks(*args, **kwargs) -> Incomplete:
    ...

def sleep(*args, **kwargs) -> Incomplete:
    ...

asyncio_timer: Incomplete ## <class 'NoneType'> = None

class ThenableEvent():
    def set(self, *args, **kwargs) -> Incomplete:
        ...

    def cancel(self, *args, **kwargs) -> Incomplete:
        ...

    def remove(self, *args, **kwargs) -> Incomplete:
        ...

    def wait(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class TopLevelCoro():
    def set(self, *args, **kwargs) -> Incomplete:
        ...

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
    def default_exception_handler(self, *args, **kwargs) -> Incomplete:
        ...

    def create_task(self, *args, **kwargs) -> Incomplete:
        ...

    def get_exception_handler(self, *args, **kwargs) -> Incomplete:
        ...

    def set_exception_handler(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

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
