"""
Module: 'uasyncio.__init__' on micropython-v1.19.1-rp2
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico with RP2040', 'nodename': 'rp2'}
# Stubber: 1.9.11
from typing import Any


def ticks_diff(*args, **kwargs) -> Any:
    ...


def run_until_complete(*args, **kwargs) -> Any:
    ...


def create_task(*args, **kwargs) -> Any:
    ...


def wait_for_ms(*args, **kwargs) -> Any:
    ...


def run(*args, **kwargs) -> Any:
    ...


def new_event_loop(*args, **kwargs) -> Any:
    ...


def current_task(*args, **kwargs) -> Any:
    ...


def get_event_loop(*args, **kwargs) -> Any:
    ...


def ticks(*args, **kwargs) -> Any:
    ...


def sleep_ms(*args, **kwargs) -> Any:
    ...


def ticks_add(*args, **kwargs) -> Any:
    ...


def sleep(*args, **kwargs) -> Any:
    ...


wait_for: Any  ## <class 'generator'> = <generator>
gather: Any  ## <class 'generator'> = <generator>


class Loop:
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

    def run_until_complete(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    def stop(self, *args, **kwargs) -> Any:
        ...

    def create_task(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class IOQueue:
    def queue_write(self, *args, **kwargs) -> Any:
        ...

    def queue_read(self, *args, **kwargs) -> Any:
        ...

    def wait_io_event(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Event:
    def set(self, *args, **kwargs) -> Any:
        ...

    def is_set(self, *args, **kwargs) -> Any:
        ...

    def clear(self, *args, **kwargs) -> Any:
        ...

    wait: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class CancelledError(Exception):
    ...
