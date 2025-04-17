"""
Module: 'asyncio.__init__' on micropython-v1.25.0-rp2-RPI_PICO2_W
"""

# MCU: {'build': '', 'ver': '1.25.0', 'version': '1.25.0', 'port': 'rp2', 'board': 'RPI_PICO2_W', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2350', 'arch': 'armv7emsp'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

_attrs: dict = {}

def current_task(*args, **kwargs) -> Incomplete: ...
def get_event_loop(*args, **kwargs) -> Incomplete: ...
def create_task(*args, **kwargs) -> Incomplete: ...
def ticks_diff(*args, **kwargs) -> Incomplete: ...
def new_event_loop(*args, **kwargs) -> Incomplete: ...
def ticks(*args, **kwargs) -> Incomplete: ...
def run_until_complete(*args, **kwargs) -> Incomplete: ...
def run(*args, **kwargs) -> Incomplete: ...
def wait_for_ms(*args, **kwargs) -> Incomplete: ...
def sleep_ms(*args, **kwargs) -> Incomplete: ...
def ticks_add(*args, **kwargs) -> Incomplete: ...
def sleep(*args, **kwargs) -> Incomplete: ...

class TaskQueue:
    def push(self, *args, **kwargs) -> Incomplete: ...
    def peek(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def pop(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

def open_connection(*args, **kwargs) -> Generator:  ## = <generator>
    ...

cur_task: Incomplete  ## <class 'NoneType'> = None

def gather(*args, **kwargs) -> Generator:  ## = <generator>
    ...

class Task:
    def __init__(self, *argv, **kwargs) -> None: ...

def wait_for(*args, **kwargs) -> Generator:  ## = <generator>
    ...

class CancelledError(Exception): ...

def start_server(*args, **kwargs) -> Generator:  ## = <generator>
    ...

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...
    def acquire(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None: ...

class StreamWriter:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def awritestr(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def wait_closed(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def drain(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readexactly(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readinto(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def read(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def awrite(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readline(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def aclose(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None: ...

class StreamReader:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def awritestr(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def wait_closed(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def drain(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readexactly(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readinto(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def read(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def awrite(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readline(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def aclose(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None: ...

class SingletonGenerator:
    def __init__(self, *argv, **kwargs) -> None: ...

class Loop:
    def get_exception_handler(self, *args, **kwargs) -> Incomplete: ...
    def default_exception_handler(self, *args, **kwargs) -> Incomplete: ...
    def set_exception_handler(self, *args, **kwargs) -> Incomplete: ...
    def run_forever(self, *args, **kwargs) -> Incomplete: ...
    def run_until_complete(self, *args, **kwargs) -> Incomplete: ...
    def stop(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def create_task(self, *args, **kwargs) -> Incomplete: ...
    def call_exception_handler(self, *args, **kwargs) -> Incomplete: ...

    _exc_handler: Incomplete  ## <class 'NoneType'> = None
    def __init__(self, *argv, **kwargs) -> None: ...

class Event:
    def set(self, *args, **kwargs) -> Incomplete: ...
    def is_set(self, *args, **kwargs) -> Incomplete: ...
    def clear(self, *args, **kwargs) -> Incomplete: ...
    def wait(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None: ...

class ThreadSafeFlag:
    def set(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def clear(self, *args, **kwargs) -> Incomplete: ...
    def wait(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None: ...

class IOQueue:
    def queue_read(self, *args, **kwargs) -> Incomplete: ...
    def wait_io_event(self, *args, **kwargs) -> Incomplete: ...
    def queue_write(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def _enqueue(self, *args, **kwargs) -> Incomplete: ...
    def _dequeue(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class TimeoutError(Exception): ...
