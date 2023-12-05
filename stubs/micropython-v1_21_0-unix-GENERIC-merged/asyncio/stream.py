"""
Module: 'asyncio.stream' on micropython-v1.21.0-unix-linux_[GCC_9.4.0]_version
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'unix', 'board': 'linux_[GCC_9.4.0]_version', 'cpu': '', 'mpy': '', 'arch': ''}
# Stubber: v1.15.1
from typing import Any
from _typeshed import Incomplete

stream_awrite: Incomplete  ## <class 'generator'> = <generator>


class StreamWriter:
    def get_extra_info(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    awrite: Incomplete  ## <class 'generator'> = <generator>
    readexactly: Incomplete  ## <class 'generator'> = <generator>
    awritestr: Incomplete  ## <class 'generator'> = <generator>
    drain: Incomplete  ## <class 'generator'> = <generator>
    readinto: Incomplete  ## <class 'generator'> = <generator>
    read: Incomplete  ## <class 'generator'> = <generator>
    aclose: Incomplete  ## <class 'generator'> = <generator>
    readline: Incomplete  ## <class 'generator'> = <generator>
    wait_closed: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Stream:
    def get_extra_info(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    awrite: Incomplete  ## <class 'generator'> = <generator>
    readexactly: Incomplete  ## <class 'generator'> = <generator>
    awritestr: Incomplete  ## <class 'generator'> = <generator>
    drain: Incomplete  ## <class 'generator'> = <generator>
    readinto: Incomplete  ## <class 'generator'> = <generator>
    read: Incomplete  ## <class 'generator'> = <generator>
    aclose: Incomplete  ## <class 'generator'> = <generator>
    readline: Incomplete  ## <class 'generator'> = <generator>
    wait_closed: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Server:
    def close(self, *args, **kwargs) -> Incomplete:
        ...

    wait_closed: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class StreamReader:
    def get_extra_info(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    awrite: Incomplete  ## <class 'generator'> = <generator>
    readexactly: Incomplete  ## <class 'generator'> = <generator>
    awritestr: Incomplete  ## <class 'generator'> = <generator>
    drain: Incomplete  ## <class 'generator'> = <generator>
    readinto: Incomplete  ## <class 'generator'> = <generator>
    read: Incomplete  ## <class 'generator'> = <generator>
    aclose: Incomplete  ## <class 'generator'> = <generator>
    readline: Incomplete  ## <class 'generator'> = <generator>
    wait_closed: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


open_connection: Incomplete  ## <class 'generator'> = <generator>
start_server: Incomplete  ## <class 'generator'> = <generator>
