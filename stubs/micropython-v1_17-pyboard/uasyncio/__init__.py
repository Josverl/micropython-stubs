"""
Module: 'uasyncio.__init__' on micropython-v1.17-pyboard
"""
# MCU: {'ver': 'v1.17', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.17.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.17.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any


class CancelledError(Exception):
    """"""


class Task:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class TaskQueue:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def peek(self, *args, **kwargs) -> Any:
        ...

    def pop_head(self, *args, **kwargs) -> Any:
        ...

    def push_head(self, *args, **kwargs) -> Any:
        ...

    def push_sorted(self, *args, **kwargs) -> Any:
        ...


def sleep(*args, **kwargs) -> Any:
    ...


def sleep_ms(*args, **kwargs) -> Any:
    ...


def ticks_add(*args, **kwargs) -> Any:
    ...


def ticks_diff(*args, **kwargs) -> Any:
    ...


wait_for: Any  ## <class 'generator'> = <generator>
gather: Any  ## <class 'generator'> = <generator>


class Event:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def clear(self, *args, **kwargs) -> Any:
        ...

    def set(self, *args, **kwargs) -> Any:
        ...

    def is_set(self, *args, **kwargs) -> Any:
        ...

    wait: Any  ## <class 'generator'> = <generator>


class Lock:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    acquire: Any  ## <class 'generator'> = <generator>

    def locked(self, *args, **kwargs) -> Any:
        ...

    def release(self, *args, **kwargs) -> Any:
        ...


def ticks(*args, **kwargs) -> Any:
    ...


class TimeoutError(Exception):
    """"""


class SingletonGenerator:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class IOQueue:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def queue_read(self, *args, **kwargs) -> Any:
        ...

    def queue_write(self, *args, **kwargs) -> Any:
        ...

    def wait_io_event(self, *args, **kwargs) -> Any:
        ...


def create_task(*args, **kwargs) -> Any:
    ...


def run_until_complete(*args, **kwargs) -> Any:
    ...


def run(*args, **kwargs) -> Any:
    ...


class Loop:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    def stop(self, *args, **kwargs) -> Any:
        ...

    def create_task(self, *args, **kwargs) -> Any:
        ...

    def run_until_complete(self, *args, **kwargs) -> Any:
        ...

    def call_exception_handler(self, *args, **kwargs) -> Any:
        ...

    def run_forever(self, *args, **kwargs) -> Any:
        ...

    def set_exception_handler(self, *args, **kwargs) -> Any:
        ...

    def get_exception_handler(self, *args, **kwargs) -> Any:
        ...

    def default_exception_handler(self, *args, **kwargs) -> Any:
        ...


def get_event_loop(*args, **kwargs) -> Any:
    ...


def current_task(*args, **kwargs) -> Any:
    ...


def new_event_loop(*args, **kwargs) -> Any:
    ...


class ThreadSafeFlag:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def set(self, *args, **kwargs) -> Any:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    wait: Any  ## <class 'generator'> = <generator>


def wait_for_ms(*args, **kwargs) -> Any:
    ...


class StreamReader:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    read: Any  ## <class 'generator'> = <generator>
    readinto: Any  ## <class 'generator'> = <generator>
    readline: Any  ## <class 'generator'> = <generator>

    def write(self, *args, **kwargs) -> Any:
        ...

    wait_closed: Any  ## <class 'generator'> = <generator>
    aclose: Any  ## <class 'generator'> = <generator>
    awrite: Any  ## <class 'generator'> = <generator>
    awritestr: Any  ## <class 'generator'> = <generator>

    def get_extra_info(self, *args, **kwargs) -> Any:
        ...

    readexactly: Any  ## <class 'generator'> = <generator>
    drain: Any  ## <class 'generator'> = <generator>


class StreamWriter:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    read: Any  ## <class 'generator'> = <generator>
    readinto: Any  ## <class 'generator'> = <generator>
    readline: Any  ## <class 'generator'> = <generator>

    def write(self, *args, **kwargs) -> Any:
        ...

    wait_closed: Any  ## <class 'generator'> = <generator>
    aclose: Any  ## <class 'generator'> = <generator>
    awrite: Any  ## <class 'generator'> = <generator>
    awritestr: Any  ## <class 'generator'> = <generator>

    def get_extra_info(self, *args, **kwargs) -> Any:
        ...

    readexactly: Any  ## <class 'generator'> = <generator>
    drain: Any  ## <class 'generator'> = <generator>


open_connection: Any  ## <class 'generator'> = <generator>
start_server: Any  ## <class 'generator'> = <generator>
