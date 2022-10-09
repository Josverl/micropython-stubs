"""
Module: 'uasyncio.stream' on micropython-v1.19.1-esp32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Any

stream_awrite: Any  ## <class 'generator'> = <generator>


class StreamWriter:
    def get_extra_info(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    awrite: Any  ## <class 'generator'> = <generator>
    readexactly: Any  ## <class 'generator'> = <generator>
    awritestr: Any  ## <class 'generator'> = <generator>
    drain: Any  ## <class 'generator'> = <generator>
    readinto: Any  ## <class 'generator'> = <generator>
    read: Any  ## <class 'generator'> = <generator>
    aclose: Any  ## <class 'generator'> = <generator>
    readline: Any  ## <class 'generator'> = <generator>
    wait_closed: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Stream:
    def get_extra_info(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    awrite: Any  ## <class 'generator'> = <generator>
    readexactly: Any  ## <class 'generator'> = <generator>
    awritestr: Any  ## <class 'generator'> = <generator>
    drain: Any  ## <class 'generator'> = <generator>
    readinto: Any  ## <class 'generator'> = <generator>
    read: Any  ## <class 'generator'> = <generator>
    aclose: Any  ## <class 'generator'> = <generator>
    readline: Any  ## <class 'generator'> = <generator>
    wait_closed: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Server:
    def close(self, *args, **kwargs) -> Any:
        ...

    wait_closed: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class StreamReader:
    def get_extra_info(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    awrite: Any  ## <class 'generator'> = <generator>
    readexactly: Any  ## <class 'generator'> = <generator>
    awritestr: Any  ## <class 'generator'> = <generator>
    drain: Any  ## <class 'generator'> = <generator>
    readinto: Any  ## <class 'generator'> = <generator>
    read: Any  ## <class 'generator'> = <generator>
    aclose: Any  ## <class 'generator'> = <generator>
    readline: Any  ## <class 'generator'> = <generator>
    wait_closed: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


open_connection: Any  ## <class 'generator'> = <generator>
start_server: Any  ## <class 'generator'> = <generator>
