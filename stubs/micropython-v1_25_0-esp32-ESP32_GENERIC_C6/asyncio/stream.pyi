"""
Module: 'asyncio.stream' on micropython-v1.25.0-esp32-ESP32_GENERIC_C6
"""

# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC_C6', 'family': 'micropython', 'build': '', 'arch': 'rv32imc', 'ver': '1.25.0', 'cpu': 'ESP32C6'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

def stream_awrite(*args, **kwargs) -> Generator:  ## = <generator>
    ...

def open_connection(*args, **kwargs) -> Generator:  ## = <generator>
    ...

def start_server(*args, **kwargs) -> Generator:  ## = <generator>
    ...

class StreamWriter:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
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

    def __init__(self, *argv, **kwargs) -> None: ...

class Server:
    def close(self, *args, **kwargs) -> Incomplete: ...
    def wait_closed(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def _serve(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None: ...

class Stream:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
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

    def __init__(self, *argv, **kwargs) -> None: ...

class StreamReader:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
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

    def __init__(self, *argv, **kwargs) -> None: ...
