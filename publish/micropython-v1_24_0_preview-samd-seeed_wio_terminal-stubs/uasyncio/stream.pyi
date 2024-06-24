"""
Module: 'uasyncio.stream' on micropython-v1.24.0-preview-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'family': 'micropython', 'build': '62', 'arch': 'armv7emsp', 'ver': '1.24.0-preview-62', 'cpu': 'SAMD51P19A'}
# Stubber: v1.20.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

stream_awrite: Generator  ## = <generator>
open_connection: Generator  ## = <generator>
start_server: Generator  ## = <generator>

class StreamWriter:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awritestr: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    awrite: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class Server:
    def close(self, *args, **kwargs) -> Incomplete: ...

    wait_closed: Generator  ## = <generator>
    _serve: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class Stream:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awritestr: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    awrite: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class StreamReader:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awritestr: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    awrite: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
