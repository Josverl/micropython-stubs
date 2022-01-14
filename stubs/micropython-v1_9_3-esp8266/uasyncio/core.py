"""
Module: 'uasyncio.core' on esp8266 v1.9.3
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.0.0(5a875ba)', version='v1.9.3-8-g63826ac5c on 2017-11-01', machine='ESP module with ESP8266')
# Stubber: 1.1.2 - updated
from typing import Any

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


class IOReadDone:
    """"""


class IOWrite:
    """"""


class IOWriteDone:
    """"""


class PollEventLoop:
    """"""

    def add_reader(self, *argv) -> Any:
        pass

    def add_writer(self, *argv) -> Any:
        pass

    def remove_reader(self, *argv) -> Any:
        pass

    def remove_writer(self, *argv) -> Any:
        pass

    def wait(self, *argv) -> Any:
        pass


class SleepMs:
    """"""


class StopLoop:
    """"""


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

    def get_extra_info(self, *argv) -> Any:
        pass


class SysCall:
    """"""

    def handle(self, *argv) -> Any:
        pass


class SysCall1:
    """"""


def Task():
    pass


_socket = None
core = None


def coroutine():
    pass


def ensure_future():
    pass


def get_event_loop():
    pass


log = None
open_connection = None
select = None


def set_debug():
    pass


sleep = None
sleep_ms = None
start_server = None
time = None


class type_gen:
    """"""

    def close(self, *argv) -> Any:
        pass

    def send(self, *argv) -> Any:
        pass

    def throw(self, *argv) -> Any:
        pass


uasyncio = None
uerrno = None
utimeq = None
