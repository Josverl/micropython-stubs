"""
Module: 'uasyncio.core' on micropython-v1.21.0-rp2-RPI_PICO_W
"""

# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete


def ticks(*args, **kwargs) -> Incomplete: ...


def run_until_complete(*args, **kwargs) -> Incomplete: ...


def create_task(*args, **kwargs) -> Incomplete: ...


def ticks_diff(*args, **kwargs) -> Incomplete: ...


def run(*args, **kwargs) -> Incomplete: ...


def new_event_loop(*args, **kwargs) -> Incomplete: ...


def current_task(*args, **kwargs) -> Incomplete: ...


def get_event_loop(*args, **kwargs) -> Incomplete: ...


def sleep_ms(*args, **kwargs) -> Incomplete: ...


def ticks_add(*args, **kwargs) -> Incomplete: ...


def sleep(*args, **kwargs) -> Incomplete: ...


class TaskQueue:
    def push(self, *args, **kwargs) -> Incomplete: ...

    def peek(self, *args, **kwargs) -> Incomplete: ...

    def remove(self, *args, **kwargs) -> Incomplete: ...

    def pop(self, *args, **kwargs) -> Incomplete: ...

    def __init__(self, *argv, **kwargs) -> None: ...


class Task:
    def __init__(self, *argv, **kwargs) -> None: ...


class CancelledError(Exception): ...
