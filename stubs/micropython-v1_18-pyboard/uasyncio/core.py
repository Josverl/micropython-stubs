"""
Module: 'uasyncio.core' on micropython-v1.18-pyboard
"""
# MCU: {'ver': 'v1.18', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.18.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.18.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.2
from typing import Any


class CancelledError(Exception):
    """"""


class Task:
    """"""

    def __init__(self, *argv) -> None:
        """"""
        ...


class TaskQueue:
    """"""

    def __init__(self, *argv) -> None:
        """"""
        ...

    def remove(self, *args) -> Any:
        ...

    def peek(self, *args) -> Any:
        ...

    def pop_head(self, *args) -> Any:
        ...

    def push_head(self, *args) -> Any:
        ...

    def push_sorted(self, *args) -> Any:
        ...


def sleep(*args) -> Any:
    ...


def sleep_ms(*args) -> Any:
    ...


def ticks_add(*args) -> Any:
    ...


def ticks_diff(*args) -> Any:
    ...


def ticks(*args) -> Any:
    ...


class TimeoutError(Exception):
    """"""


class SingletonGenerator:
    """"""

    def __init__(self, *argv) -> None:
        """"""
        ...

    def __init__(self, *args) -> None:
        ...


class IOQueue:
    """"""

    def __init__(self, *argv) -> None:
        """"""
        ...

    def __init__(self, *args) -> None:
        ...

    def remove(self, *args) -> Any:
        ...

    def queue_read(self, *args) -> Any:
        ...

    def queue_write(self, *args) -> Any:
        ...

    def wait_io_event(self, *args) -> Any:
        ...


def create_task(*args) -> Any:
    ...


def run_until_complete(*args) -> Any:
    ...


def run(*args) -> Any:
    ...


class Loop:
    """"""

    def __init__(self, *argv) -> None:
        """"""
        ...

    def close(self, *args) -> Any:
        ...

    def stop(self, *args) -> Any:
        ...

    def create_task(self, *args) -> Any:
        ...

    def run_until_complete(self, *args) -> Any:
        ...

    def call_exception_handler(self, *args) -> Any:
        ...

    def run_forever(self, *args) -> Any:
        ...

    def set_exception_handler(self, *args) -> Any:
        ...

    def get_exception_handler(self, *args) -> Any:
        ...

    def default_exception_handler(self, *args) -> Any:
        ...


def get_event_loop(*args) -> Any:
    ...


def current_task(*args) -> Any:
    ...


def new_event_loop(*args) -> Any:
    ...
