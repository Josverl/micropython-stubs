"""
Module: 'uasyncio.core' on micropython-v1.13-266-esp32
"""
# MCU: {'ver': 'v1.13-266', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.13.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.13.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '266', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.0
from typing import Any


class CancelledError(Exception):
    """"""


class Loop:
    """"""

    def close(self, *args) -> Any:
        ...

    def stop(self, *args) -> Any:
        ...

    def call_exception_handler(self, *args) -> Any:
        ...

    def create_task(self, *args) -> Any:
        ...

    def run_until_complete(self, *args) -> Any:
        ...

    def run_forever(self, *args) -> Any:
        ...

    def set_exception_handler(self, *args) -> Any:
        ...

    def get_exception_handler(self, *args) -> Any:
        ...

    def default_exception_handler(self, *args) -> Any:
        ...


class Task:
    """"""


class TaskQueue:
    """"""

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


def run(*args) -> Any:
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

    def __init__(self, *args) -> None:
        ...


class IOQueue:
    """"""

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


def get_event_loop(*args) -> Any:
    ...


def new_event_loop(*args) -> Any:
    ...
