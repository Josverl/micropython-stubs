"""
Module: 'uasyncio.core' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any


class CancelledError(Exception):
    """"""


DEBUG = 0


class EventLoop:
    """"""

    def call_at_(self, *argv) -> Any:
        pass

    def call_later(self, *argv) -> Any:
        pass

    def call_later_ms(self, *argv) -> Any:
        pass

    def call_soon(self, *argv) -> Any:
        pass

    def close(self, *argv) -> Any:
        pass

    def create_task(self, *argv) -> Any:
        pass

    def run_forever(self, *argv) -> Any:
        pass

    def run_until_complete(self, *argv) -> Any:
        pass

    def stop(self, *argv) -> Any:
        pass

    def time(self, *argv) -> Any:
        pass

    def wait(self, *argv) -> Any:
        pass


class IORead:
    """"""

    def handle(self, *argv) -> Any:
        pass


class IOReadDone:
    """"""

    def handle(self, *argv) -> Any:
        pass


class IOWrite:
    """"""

    def handle(self, *argv) -> Any:
        pass


class IOWriteDone:
    """"""

    def handle(self, *argv) -> Any:
        pass


class SleepMs:
    """"""

    def handle(self, *argv) -> Any:
        pass


class StopLoop:
    """"""

    def handle(self, *argv) -> Any:
        pass


class SysCall:
    """"""

    def handle(self, *argv) -> Any:
        pass


class SysCall1:
    """"""

    def handle(self, *argv) -> Any:
        pass


def Task():
    pass


class TimeoutError(Exception):
    """"""


class TimeoutObj:
    """"""


_event_loop = None


class _event_loop_class:
    """"""

    def add_reader(self, *argv) -> Any:
        pass

    def add_writer(self, *argv) -> Any:
        pass

    def call_at_(self, *argv) -> Any:
        pass

    def call_later(self, *argv) -> Any:
        pass

    def call_later_ms(self, *argv) -> Any:
        pass

    def call_soon(self, *argv) -> Any:
        pass

    def close(self, *argv) -> Any:
        pass

    def create_task(self, *argv) -> Any:
        pass

    def remove_reader(self, *argv) -> Any:
        pass

    def remove_writer(self, *argv) -> Any:
        pass

    def run_forever(self, *argv) -> Any:
        pass

    def run_until_complete(self, *argv) -> Any:
        pass

    def stop(self, *argv) -> Any:
        pass

    def time(self, *argv) -> Any:
        pass

    def wait(self, *argv) -> Any:
        pass


_stop_iter = None


def cancel():
    pass


def coroutine():
    pass


def ensure_future():
    pass


def get_event_loop():
    pass


log = None


def set_debug():
    pass


sleep = None
sleep_ms = None
time = None


class type_gen:
    """"""

    def close(self, *argv) -> Any:
        pass

    def pend_throw(self, *argv) -> Any:
        pass

    def send(self, *argv) -> Any:
        pass

    def throw(self, *argv) -> Any:
        pass


ucollections = None
utimeq = None


def wait_for():
    pass


wait_for_ms = None
