"""
Module: 'aioble.server' on micropython-v1.21.0-rp2-RPI_PICO_W
"""

# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete


def log_info(*args, **kwargs) -> Incomplete: ...


def register_irq_handler(*args, **kwargs) -> Incomplete: ...


def log_warn(*args, **kwargs) -> Incomplete: ...


def log_error(*args, **kwargs) -> Incomplete: ...


def const(*args, **kwargs) -> Incomplete: ...


def ensure_active(*args, **kwargs) -> Incomplete: ...


def register_services(*args, **kwargs) -> Incomplete: ...


class Descriptor:
    def write(self, *args, **kwargs) -> Incomplete: ...

    def on_read(self, *args, **kwargs) -> Incomplete: ...

    def read(self, *args, **kwargs) -> Incomplete: ...

    written: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class DeviceConnection:
    def services(self, *args, **kwargs) -> Incomplete: ...

    def is_connected(self, *args, **kwargs) -> Incomplete: ...

    def timeout(self, *args, **kwargs) -> Incomplete: ...

    l2cap_accept: Incomplete  ## <class 'generator'> = <generator>
    exchange_mtu: Incomplete  ## <class 'generator'> = <generator>
    pair: Incomplete  ## <class 'generator'> = <generator>
    l2cap_connect: Incomplete  ## <class 'generator'> = <generator>
    service: Incomplete  ## <class 'generator'> = <generator>
    disconnect: Incomplete  ## <class 'generator'> = <generator>
    device_task: Incomplete  ## <class 'generator'> = <generator>
    disconnected: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


ble: Incomplete  ## <class 'BLE'> = <BLE>


class DeviceTimeout:
    def __init__(self, *argv, **kwargs) -> None: ...


class BaseCharacteristic:
    def write(self, *args, **kwargs) -> Incomplete: ...

    def on_read(self, *args, **kwargs) -> Incomplete: ...

    def read(self, *args, **kwargs) -> Incomplete: ...

    written: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class deque:
    def popleft(self, *args, **kwargs) -> Incomplete: ...

    def append(self, *args, **kwargs) -> Incomplete: ...

    def __init__(self, *argv, **kwargs) -> None: ...


class BufferedCharacteristic:
    def on_read(self, *args, **kwargs) -> Incomplete: ...

    def notify(self, *args, **kwargs) -> Incomplete: ...

    def write(self, *args, **kwargs) -> Incomplete: ...

    def read(self, *args, **kwargs) -> Incomplete: ...

    indicate: Incomplete  ## <class 'generator'> = <generator>
    written: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class Characteristic:
    def on_read(self, *args, **kwargs) -> Incomplete: ...

    def notify(self, *args, **kwargs) -> Incomplete: ...

    def write(self, *args, **kwargs) -> Incomplete: ...

    def read(self, *args, **kwargs) -> Incomplete: ...

    indicate: Incomplete  ## <class 'generator'> = <generator>
    written: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class GattError(Exception): ...
