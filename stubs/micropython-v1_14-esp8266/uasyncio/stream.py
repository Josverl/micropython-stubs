"""
Module: 'uasyncio.stream' on micropython-v1.14-esp8266
"""
# MCU: {'ver': 'v1.14', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.14', 'name': 'micropython', 'mpy': 9733, 'version': '1.14', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.3
from typing import Any


class Stream:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def close(self, *args) -> Any:
        ...

    read: Any  ## <class 'generator'> = <generator>
    readline: Any  ## <class 'generator'> = <generator>

    def write(self, *args) -> Any:
        ...

    wait_closed: Any  ## <class 'generator'> = <generator>
    aclose: Any  ## <class 'generator'> = <generator>
    awrite: Any  ## <class 'generator'> = <generator>
    awritestr: Any  ## <class 'generator'> = <generator>

    def get_extra_info(self, *args) -> Any:
        ...

    readexactly: Any  ## <class 'generator'> = <generator>
    drain: Any  ## <class 'generator'> = <generator>


class StreamReader:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def close(self, *args) -> Any:
        ...

    read: Any  ## <class 'generator'> = <generator>
    readline: Any  ## <class 'generator'> = <generator>

    def write(self, *args) -> Any:
        ...

    wait_closed: Any  ## <class 'generator'> = <generator>
    aclose: Any  ## <class 'generator'> = <generator>
    awrite: Any  ## <class 'generator'> = <generator>
    awritestr: Any  ## <class 'generator'> = <generator>

    def get_extra_info(self, *args) -> Any:
        ...

    readexactly: Any  ## <class 'generator'> = <generator>
    drain: Any  ## <class 'generator'> = <generator>


class StreamWriter:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def close(self, *args) -> Any:
        ...

    read: Any  ## <class 'generator'> = <generator>
    readline: Any  ## <class 'generator'> = <generator>

    def write(self, *args) -> Any:
        ...

    wait_closed: Any  ## <class 'generator'> = <generator>
    aclose: Any  ## <class 'generator'> = <generator>
    awrite: Any  ## <class 'generator'> = <generator>
    awritestr: Any  ## <class 'generator'> = <generator>

    def get_extra_info(self, *args) -> Any:
        ...

    readexactly: Any  ## <class 'generator'> = <generator>
    drain: Any  ## <class 'generator'> = <generator>


open_connection: Any  ## <class 'generator'> = <generator>


class Server:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def close(self, *args) -> Any:
        ...

    wait_closed: Any  ## <class 'generator'> = <generator>


start_server: Any  ## <class 'generator'> = <generator>
stream_awrite: Any  ## <class 'generator'> = <generator>
