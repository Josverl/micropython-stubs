"""
Module: 'uasyncio.stream' on micropython-v1.20.0-esp32-GENERIC
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'esp32', 'board': 'GENERIC', 'cpu': 'ESP32', 'mpy': 'v6.1', 'arch': 'xtensawin'})
# Stubber: v1.13.4
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
