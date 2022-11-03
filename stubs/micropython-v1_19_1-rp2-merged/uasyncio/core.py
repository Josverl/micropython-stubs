"""
Module: 'uasyncio.core' on micropython-v1.19.1-rp2
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico with RP2040', 'nodename': 'rp2'}
# Stubber: 1.9.11
from typing import Any


def ticks(*args, **kwargs) -> Any:
    ...


def run_until_complete(*args, **kwargs) -> Any:
    ...


def create_task(*args, **kwargs) -> Any:
    ...


def ticks_diff(*args, **kwargs) -> Any:
    ...


def run(*args, **kwargs) -> Any:
    ...


def new_event_loop(*args, **kwargs) -> Any:
    ...


def current_task(*args, **kwargs) -> Any:
    ...


def get_event_loop(*args, **kwargs) -> Any:
    ...


def sleep_ms(*args, **kwargs) -> Any:
    ...


def ticks_add(*args, **kwargs) -> Any:
    ...


def sleep(*args, **kwargs) -> Any:
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
