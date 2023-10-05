"""
Module: 'uasyncio.stream' on micropython-v1.20.0-stm32-PYBV11
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': 'v1.20.0', 'cpu': 'STM32F405RG'})
# Stubber: v1.13.7
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
