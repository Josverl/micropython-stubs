"""
Module: 'asyncio.stream' on micropython-v1.26.1-unix-standard
"""
# MCU: {'family': 'micropython', 'version': '1.26.1', 'build': '', 'ver': '1.26.1', 'port': 'unix', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'linux [GCC 12.4.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

def stream_awrite(*args, **kwargs) -> Generator:  ## = <generator>
    ...

def open_connection(*args, **kwargs) -> Generator:  ## = <generator>
    ...

def start_server(*args, **kwargs) -> Generator:  ## = <generator>
    ...


class StreamWriter():
    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def get_extra_info(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def awritestr(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def wait_closed(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def drain(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readexactly(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readinto(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def read(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def awrite(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readline(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def aclose(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Server():
    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def wait_closed(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def _serve(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Stream():
    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def get_extra_info(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def awritestr(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def wait_closed(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def drain(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readexactly(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readinto(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def read(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def awrite(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readline(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def aclose(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class StreamReader():
    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def get_extra_info(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def awritestr(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def wait_closed(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def drain(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readexactly(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readinto(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def read(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def awrite(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readline(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def aclose(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

