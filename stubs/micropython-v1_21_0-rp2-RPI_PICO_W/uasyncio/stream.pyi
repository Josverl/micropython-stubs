"""
Module: 'uasyncio.stream' on micropython-v1.21.0-rp2-RPI_PICO_W
"""

# MCU: {'build': '', 'ver': '1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.23.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

stream_awrite: Generator  ## = <generator>

class StreamWriter:
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awrite: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    awritestr: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class Stream:
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awrite: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    awritestr: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class Server:
    def close(self, *args, **kwargs) -> Incomplete: ...

    _serve: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class StreamReader:
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awrite: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    awritestr: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

open_connection: Generator  ## = <generator>
start_server: Generator  ## = <generator>
