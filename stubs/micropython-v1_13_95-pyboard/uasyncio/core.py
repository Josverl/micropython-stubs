"""
Module: 'uasyncio.core' on pyboard 1.13.0-95
"""
# MCU: (sysname='pyboard', nodename='pyboard', release='1.13.0', version='v1.13-95-g0fff2e03f on 2020-10-03', machine='PYBv1.1 with STM32F405RG')
# Stubber: 1.3.4 - updated
from typing import Any


class CancelledError(Exception):
    """"""


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


class Task:
    """"""
