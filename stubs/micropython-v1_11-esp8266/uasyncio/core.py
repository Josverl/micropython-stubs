"""
Module: 'uasyncio.core' on esp8266 v1.11
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.11-8-g48dcbbe60 on 2019-05-29', machine='ESP module with ESP8266')
# Stubber: 1.1.0 - updated
from typing import Any


class CancelledError(Exception):
    """"""


DEBUG = 0


class EventLoop:
    """"""

    def call_at_(self, *args) -> Any:
        pass

    def call_later(self, *args) -> Any:
        pass

    def call_later_ms(self, *args) -> Any:
        pass

    def call_soon(self, *args) -> Any:
        pass

    def close(self, *args) -> Any:
        pass

    def create_task(self, *args) -> Any:
        pass

    def run_forever(self, *args) -> Any:
        pass

    def run_until_complete(self, *args) -> Any:
        pass

    def stop(self, *args) -> Any:
        pass

    def time(self, *args) -> Any:
        pass

    def wait(self, *args) -> Any:
        pass


class IORead:
    """"""

    def handle(self, *args) -> Any:
        pass


class IOReadDone:
    """"""

    def handle(self, *args) -> Any:
        pass


class IOWrite:
    """"""

    def handle(self, *args) -> Any:
        pass


class IOWriteDone:
    """"""

    def handle(self, *args) -> Any:
        pass


class PollEventLoop:
    """"""

    def add_reader(self, *args) -> Any:
        pass

    def add_writer(self, *args) -> Any:
        pass

    def call_at_(self, *args) -> Any:
        pass

    def call_later(self, *args) -> Any:
        pass

    def call_later_ms(self, *args) -> Any:
        pass

    def call_soon(self, *args) -> Any:
        pass

    def close(self, *args) -> Any:
        pass

    def create_task(self, *args) -> Any:
        pass

    def remove_reader(self, *args) -> Any:
        pass

    def remove_writer(self, *args) -> Any:
        pass

    def run_forever(self, *args) -> Any:
        pass

    def run_until_complete(self, *args) -> Any:
        pass

    def stop(self, *args) -> Any:
        pass

    def time(self, *args) -> Any:
        pass

    def wait(self, *args) -> Any:
        pass


class SleepMs:
    """"""

    def handle(self, *args) -> Any:
        pass


class StopLoop:
    """"""

    def handle(self, *args) -> Any:
        pass


class StreamReader:
    """"""

    aclose = None
    read = None
    readexactly = None
    readline = None


class StreamWriter:
    """"""

    aclose = None
    awrite = None
    awriteiter = None

    def get_extra_info(self, *args) -> Any:
        pass


class SysCall:
    """"""

    def handle(self, *args) -> Any:
        pass


class SysCall1:
    """"""

    def handle(self, *args) -> Any:
        pass


def Task(*args) -> Any:
    pass


class TimeoutError(Exception):
    """"""


class TimeoutObj:
    """"""


_socket = None


def cancel(*args) -> Any:
    pass


core = None


def coroutine(*args) -> Any:
    pass


def ensure_future(*args) -> Any:
    pass


def get_event_loop(*args) -> Any:
    pass


log = None
open_connection = None
select = None


def set_debug(*args) -> Any:
    pass


sleep = None
sleep_ms = None
start_server = None
time = None


class type_gen:
    """"""

    def close(self, *args) -> Any:
        pass

    def pend_throw(self, *args) -> Any:
        pass

    def send(self, *args) -> Any:
        pass

    def throw(self, *args) -> Any:
        pass


uasyncio = None
ucollections = None
uerrno = None
utimeq = None


def wait_for(*args) -> Any:
    pass


wait_for_ms = None
