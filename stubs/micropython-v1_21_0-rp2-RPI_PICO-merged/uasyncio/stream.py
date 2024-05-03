"""
Module: 'uasyncio.stream' on micropython-v1.21.0-rp2-RPI_PICO
"""

# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

stream_awrite: Incomplete  ## <class 'generator'> = <generator>


class StreamWriter:
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...

    def write(self, *args, **kwargs) -> Incomplete: ...

    def close(self, *args, **kwargs) -> Incomplete: ...

    awrite: Incomplete  ## <class 'generator'> = <generator>
    readexactly: Incomplete  ## <class 'generator'> = <generator>
    awritestr: Incomplete  ## <class 'generator'> = <generator>
    drain: Incomplete  ## <class 'generator'> = <generator>
    readinto: Incomplete  ## <class 'generator'> = <generator>
    read: Incomplete  ## <class 'generator'> = <generator>
    aclose: Incomplete  ## <class 'generator'> = <generator>
    readline: Incomplete  ## <class 'generator'> = <generator>
    wait_closed: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class Stream:
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...

    def write(self, *args, **kwargs) -> Incomplete: ...

    def close(self, *args, **kwargs) -> Incomplete: ...

    awrite: Incomplete  ## <class 'generator'> = <generator>
    readexactly: Incomplete  ## <class 'generator'> = <generator>
    awritestr: Incomplete  ## <class 'generator'> = <generator>
    drain: Incomplete  ## <class 'generator'> = <generator>
    readinto: Incomplete  ## <class 'generator'> = <generator>
    read: Incomplete  ## <class 'generator'> = <generator>
    aclose: Incomplete  ## <class 'generator'> = <generator>
    readline: Incomplete  ## <class 'generator'> = <generator>
    wait_closed: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class Server:
    def close(self, *args, **kwargs) -> Incomplete: ...

    wait_closed: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class StreamReader:
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...

    def write(self, *args, **kwargs) -> Incomplete: ...

    def close(self, *args, **kwargs) -> Incomplete: ...

    awrite: Incomplete  ## <class 'generator'> = <generator>
    readexactly: Incomplete  ## <class 'generator'> = <generator>
    awritestr: Incomplete  ## <class 'generator'> = <generator>
    drain: Incomplete  ## <class 'generator'> = <generator>
    readinto: Incomplete  ## <class 'generator'> = <generator>
    read: Incomplete  ## <class 'generator'> = <generator>
    aclose: Incomplete  ## <class 'generator'> = <generator>
    readline: Incomplete  ## <class 'generator'> = <generator>
    wait_closed: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


open_connection: Incomplete  ## <class 'generator'> = <generator>
start_server: Incomplete  ## <class 'generator'> = <generator>
