"""
Module: 'uasyncio.stream' on micropython-v1.25.0-preview-unix
"""
# MCU: {'family': 'micropython', 'version': '1.25.0-preview', 'build': '301', 'ver': '1.25.0-preview-301', 'port': 'unix', 'board': '', 'cpu': 'linux [GCC 12.4.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

stream_awrite: Generator ## = <generator>
open_connection: Generator ## = <generator>
start_server: Generator ## = <generator>

class StreamWriter():
    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def get_extra_info(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    awritestr: Generator ## = <generator>
    wait_closed: Generator ## = <generator>
    drain: Generator ## = <generator>
    readexactly: Generator ## = <generator>
    readinto: Generator ## = <generator>
    read: Generator ## = <generator>
    awrite: Generator ## = <generator>
    readline: Generator ## = <generator>
    aclose: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class Server():
    def close(self, *args, **kwargs) -> Incomplete:
        ...

    wait_closed: Generator ## = <generator>
    _serve: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class Stream():
    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def get_extra_info(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    awritestr: Generator ## = <generator>
    wait_closed: Generator ## = <generator>
    drain: Generator ## = <generator>
    readexactly: Generator ## = <generator>
    readinto: Generator ## = <generator>
    read: Generator ## = <generator>
    awrite: Generator ## = <generator>
    readline: Generator ## = <generator>
    aclose: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class StreamReader():
    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def get_extra_info(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    awritestr: Generator ## = <generator>
    wait_closed: Generator ## = <generator>
    drain: Generator ## = <generator>
    readexactly: Generator ## = <generator>
    readinto: Generator ## = <generator>
    read: Generator ## = <generator>
    awrite: Generator ## = <generator>
    readline: Generator ## = <generator>
    aclose: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...

