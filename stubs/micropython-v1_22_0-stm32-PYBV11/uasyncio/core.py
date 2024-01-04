"""
Module: 'uasyncio.core' on micropython-v1.22.0-stm32-PYBV11
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'stm32', 'board': 'PYBV11', 'cpu': 'STM32F405RG', 'mpy': 'v6.2', 'arch': 'armv7emsp'}
# Stubber: v1.16.2
from _typeshed import Incomplete


def ticks(*args, **kwargs) -> Incomplete:
    ...


def current_task(*args, **kwargs) -> Incomplete:
    ...


def create_task(*args, **kwargs) -> Incomplete:
    ...


def ticks_diff(*args, **kwargs) -> Incomplete:
    ...


def get_event_loop(*args, **kwargs) -> Incomplete:
    ...


def run_until_complete(*args, **kwargs) -> Incomplete:
    ...


def run(*args, **kwargs) -> Incomplete:
    ...


def new_event_loop(*args, **kwargs) -> Incomplete:
    ...


def sleep_ms(*args, **kwargs) -> Incomplete:
    ...


def ticks_add(*args, **kwargs) -> Incomplete:
    ...


def sleep(*args, **kwargs) -> Incomplete:
    ...


class TaskQueue:
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


class Task:
    def __init__(self, *argv, **kwargs) -> None:
        ...


class CancelledError(Exception):
    ...