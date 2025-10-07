"""
Module: 'asyncio.__init__' on micropython-v1.25.0-preview-webassembly
"""
# MCU: {'family': 'micropython', 'version': '1.25.0-preview', 'build': '301', 'ver': '1.25.0-preview-301', 'port': 'webassembly', 'board': '', 'board_id': '', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

asyncio_timer: int = 6
def create_task(*args, **kwargs) -> Incomplete:
    ...

def ticks_diff(*args, **kwargs) -> Incomplete:
    ...

def ticks_add(*args, **kwargs) -> Incomplete:
    ...

def sleep_ms(*args, **kwargs) -> Incomplete:
    ...

def current_task(*args, **kwargs) -> Incomplete:
    ...

def ticks(*args, **kwargs) -> Incomplete:
    ...

def new_event_loop(*args, **kwargs) -> Incomplete:
    ...

def get_event_loop(*args, **kwargs) -> Incomplete:
    ...

def wait_for_ms(*args, **kwargs) -> Incomplete:
    ...

def sleep(*args, **kwargs) -> Incomplete:
    ...

def gather(*args, **kwargs) -> Generator:  ## = <generator>
    ...


class ThenableEvent():
    def set(self, *args, **kwargs) -> Incomplete:
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

    resolve: Incomplete ## <class 'JsProxy'> = <JsProxy 54>
    reject: Incomplete ## <class 'JsProxy'> = <JsProxy 55>
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

def wait_for(*args, **kwargs) -> Generator:  ## = <generator>
    ...


class CancelledError(Exception):
    ...

class Task():
    def __init__(self, *argv, **kwargs) -> None:
        ...

cur_task: Incomplete ## <class 'Task'> = <Task>

class Event():
    def set(self, *args, **kwargs) -> Incomplete:
        ...

    def is_set(self, *args, **kwargs) -> Incomplete:
        ...

    def clear(self, *args, **kwargs) -> Incomplete:
        ...

    def wait(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Lock():
    def locked(self, *args, **kwargs) -> Incomplete:
        ...

    def release(self, *args, **kwargs) -> Incomplete:
        ...

    def acquire(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class TimeoutError(Exception):
    ...

class SingletonGenerator():
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

