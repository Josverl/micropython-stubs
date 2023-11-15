"""
Module: 'uasyncio.core' on micropython-v1.19.1-esp32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Any


def ticks(*args, **kwargs) -> Any:
    ...


def create_task(*args, **kwargs) -> Any:
    ...


def ticks_diff(*args, **kwargs) -> Any:
    ...


def ticks_add(*args, **kwargs) -> Any:
    ...


def run_until_complete(*args, **kwargs) -> Any:
    ...


def new_event_loop(*args, **kwargs) -> Any:
    ...


def current_task(*args, **kwargs) -> Any:
    ...


def get_event_loop(*args, **kwargs) -> Any:
    ...


def sleep(*args, **kwargs) -> Any:
    ...


def run(*args, **kwargs) -> Any:
    ...


def sleep_ms(*args, **kwargs) -> Any:
    ...


class TaskQueue:
    def push(self, *args, **kwargs) -> Any:
        ...

    def peek(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def pop(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Task:
    def __init__(self, *argv, **kwargs) -> None:
        ...


class CancelledError(Exception):
    ...
