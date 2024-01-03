"""
Module: 'aioble.__init__' on micropython-v1.22.0-rp2-RPI_PICO_W
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.16.2
from _typeshed import Incomplete

ADDR_PUBLIC = 0  # type: int
ADDR_RANDOM = 1  # type: int


def log_warn(*args, **kwargs) -> Incomplete:
    ...


def log_info(*args, **kwargs) -> Incomplete:
    ...


def log_error(*args, **kwargs) -> Incomplete:
    ...


def register_services(*args, **kwargs) -> Incomplete:
    ...


def stop(*args, **kwargs) -> Incomplete:
    ...


def config(*args, **kwargs) -> Incomplete:
    ...


def const(*args, **kwargs) -> Incomplete:
    ...


class Service:
    def __init__(self, *argv, **kwargs) -> None:
        ...


class scan:
    cancel: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


advertise: Incomplete  ## <class 'generator'> = <generator>


class Characteristic:
    def notify(self, *args, **kwargs) -> Incomplete:
        ...

    def on_read(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    written: Incomplete  ## <class 'generator'> = <generator>
    indicate: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class GattError(Exception):
    ...
