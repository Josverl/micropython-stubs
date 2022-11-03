"""
Module: 'aioble.__init__' on micropython-v1.19.1-rp2
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2'}
# Stubber: 1.9.11
from typing import Any

ADDR_RANDOM = 1  # type: int
ADDR_PUBLIC = 0  # type: int


def log_error(*args, **kwargs) -> Any:
    ...


def log_warn(*args, **kwargs) -> Any:
    ...


def stop(*args, **kwargs) -> Any:
    ...


def register_services(*args, **kwargs) -> Any:
    ...


def const(*args, **kwargs) -> Any:
    ...


def log_info(*args, **kwargs) -> Any:
    ...


def config(*args, **kwargs) -> Any:
    ...


class BufferedCharacteristic:
    def on_read(self, *args, **kwargs) -> Any:
        ...

    def notify(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    indicate: Any  ## <class 'generator'> = <generator>
    written: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Descriptor:
    def write(self, *args, **kwargs) -> Any:
        ...

    def on_read(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    written: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class scan:
    cancel: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class DeviceDisconnectedError(Exception):
    ...
