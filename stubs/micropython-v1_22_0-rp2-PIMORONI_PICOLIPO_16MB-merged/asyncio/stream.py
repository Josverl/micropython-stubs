"""
Module: 'asyncio.stream' on micropython-v1.22.0-rp2-PIMORONI_PICOLIPO_16MB
"""

# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'rp2', 'board': 'PIMORONI_PICOLIPO_16MB', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.16.2
from _typeshed import Incomplete

stream_awrite: Incomplete  ## <class 'generator'> = <generator>
open_connection: Incomplete  ## <class 'generator'> = <generator>
start_server: Incomplete  ## <class 'generator'> = <generator>


class StreamWriter:
    def write(self, *args, **kwargs) -> Incomplete: ...

    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...

    def close(self, *args, **kwargs) -> Incomplete: ...

    awritestr: Incomplete  ## <class 'generator'> = <generator>
    wait_closed: Incomplete  ## <class 'generator'> = <generator>
    drain: Incomplete  ## <class 'generator'> = <generator>
    readexactly: Incomplete  ## <class 'generator'> = <generator>
    readinto: Incomplete  ## <class 'generator'> = <generator>
    read: Incomplete  ## <class 'generator'> = <generator>
    awrite: Incomplete  ## <class 'generator'> = <generator>
    readline: Incomplete  ## <class 'generator'> = <generator>
    aclose: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class Server:
    def close(self, *args, **kwargs) -> Incomplete: ...

    wait_closed: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class Stream:
    def write(self, *args, **kwargs) -> Incomplete: ...

    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...

    def close(self, *args, **kwargs) -> Incomplete: ...

    awritestr: Incomplete  ## <class 'generator'> = <generator>
    wait_closed: Incomplete  ## <class 'generator'> = <generator>
    drain: Incomplete  ## <class 'generator'> = <generator>
    readexactly: Incomplete  ## <class 'generator'> = <generator>
    readinto: Incomplete  ## <class 'generator'> = <generator>
    read: Incomplete  ## <class 'generator'> = <generator>
    awrite: Incomplete  ## <class 'generator'> = <generator>
    readline: Incomplete  ## <class 'generator'> = <generator>
    aclose: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class StreamReader:
    def write(self, *args, **kwargs) -> Incomplete: ...

    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...

    def close(self, *args, **kwargs) -> Incomplete: ...

    awritestr: Incomplete  ## <class 'generator'> = <generator>
    wait_closed: Incomplete  ## <class 'generator'> = <generator>
    drain: Incomplete  ## <class 'generator'> = <generator>
    readexactly: Incomplete  ## <class 'generator'> = <generator>
    readinto: Incomplete  ## <class 'generator'> = <generator>
    read: Incomplete  ## <class 'generator'> = <generator>
    awrite: Incomplete  ## <class 'generator'> = <generator>
    readline: Incomplete  ## <class 'generator'> = <generator>
    aclose: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...
