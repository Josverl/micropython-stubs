"""
Module: 'uasyncio.__init__' on pyboard 1.13.0-95
"""
# MCU: (sysname='pyboard', nodename='pyboard', release='1.13.0', version='v1.13-95-g0fff2e03f on 2020-10-03', machine='PYBv1.1 with STM32F405RG')
# Stubber: 1.3.4 - updated
from typing import Any


class CancelledError(Exception):
    """"""


class Event:
    """"""

    def clear(self, *args) -> Any:
        pass

    def is_set(self, *args) -> Any:
        pass

    def set(self, *args) -> Any:
        pass

    wait = None


class IOQueue:
    """"""

    def _dequeue(self, *args) -> Any:
        pass

    def _enqueue(self, *args) -> Any:
        pass

    def queue_read(self, *args) -> Any:
        pass

    def queue_write(self, *args) -> Any:
        pass

    def remove(self, *args) -> Any:
        pass

    def wait_io_event(self, *args) -> Any:
        pass


class Lock:
    """"""

    acquire = None

    def locked(self, *args) -> Any:
        pass

    def release(self, *args) -> Any:
        pass


class Loop:
    """"""

    _exc_handler = None

    def call_exception_handler(self, *args) -> Any:
        pass

    def close(self, *args) -> Any:
        pass

    def create_task(self, *args) -> Any:
        pass

    def default_exception_handler(self, *args) -> Any:
        pass

    def get_exception_handler(self, *args) -> Any:
        pass

    def run_forever(self, *args) -> Any:
        pass

    def run_until_complete(self, *args) -> Any:
        pass

    def set_exception_handler(self, *args) -> Any:
        pass

    def stop(self, *args) -> Any:
        pass


class SingletonGenerator:
    """"""


class StreamReader:
    """"""

    aclose = None
    awrite = None
    awritestr = None

    def close(self, *args) -> Any:
        pass

    drain = None

    def get_extra_info(self, *args) -> Any:
        pass

    read = None
    readexactly = None
    readline = None
    wait_closed = None

    def write(self, *args) -> Any:
        pass


class StreamWriter:
    """"""

    aclose = None
    awrite = None
    awritestr = None

    def close(self, *args) -> Any:
        pass

    drain = None

    def get_extra_info(self, *args) -> Any:
        pass

    read = None
    readexactly = None
    readline = None
    wait_closed = None

    def write(self, *args) -> Any:
        pass


class Task:
    """"""
