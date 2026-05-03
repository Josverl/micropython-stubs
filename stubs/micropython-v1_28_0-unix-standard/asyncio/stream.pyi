"""
Module: 'asyncio.stream' on micropython-v1.28.0-unix-standard
"""
# MCU: {'family': 'micropython', 'version': '1.28.0', 'build': '', 'ver': '1.28.0', 'port': 'unix', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'linux [GCC 12.5.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.28.3
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
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

    def awritestr(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def wait_closed(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def drain(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readexactly(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readinto(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def read(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def awrite(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readline(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def aclose(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Server():
    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def wait_closed(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def _serve(self, *args, **kwargs) -> Generator:  ## = <generator>
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

    def awritestr(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def wait_closed(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def drain(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readexactly(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readinto(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def read(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def awrite(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readline(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def aclose(self, *args, **kwargs) -> Generator:  ## = <generator>
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

    def awritestr(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def wait_closed(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def drain(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readexactly(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readinto(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def read(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def awrite(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def readline(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def aclose(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

