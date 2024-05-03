"""
Module: 'aioble.__init__' on micropython-v1.21.0-rp2-RPI_PICO_W
"""

# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

ADDR_RANDOM = 1  # type: int
ADDR_PUBLIC = 0  # type: int


def log_error(*args, **kwargs) -> Incomplete: ...


def log_warn(*args, **kwargs) -> Incomplete: ...


def stop(*args, **kwargs) -> Incomplete: ...


def register_services(*args, **kwargs) -> Incomplete: ...


def const(*args, **kwargs) -> Incomplete: ...


def log_info(*args, **kwargs) -> Incomplete: ...


def config(*args, **kwargs) -> Incomplete: ...


class BufferedCharacteristic:
    def on_read(self, *args, **kwargs) -> Incomplete: ...

    def notify(self, *args, **kwargs) -> Incomplete: ...

    def write(self, *args, **kwargs) -> Incomplete: ...

    def read(self, *args, **kwargs) -> Incomplete: ...

    indicate: Incomplete  ## <class 'generator'> = <generator>
    written: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class Descriptor:
    def write(self, *args, **kwargs) -> Incomplete: ...

    def on_read(self, *args, **kwargs) -> Incomplete: ...

    def read(self, *args, **kwargs) -> Incomplete: ...

    written: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class scan:
    cancel: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class DeviceDisconnectedError(Exception): ...
