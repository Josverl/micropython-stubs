"""
Module: 'aioble.server' on micropython-v1.19.1-rp2
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2'}
# Stubber: 1.9.11
from typing import Any


def register_services(*args, **kwargs) -> Any:
    ...


def log_error(*args, **kwargs) -> Any:
    ...


def register_irq_handler(*args, **kwargs) -> Any:
    ...


def ensure_active(*args, **kwargs) -> Any:
    ...


def log_info(*args, **kwargs) -> Any:
    ...


def log_warn(*args, **kwargs) -> Any:
    ...


def const(*args, **kwargs) -> Any:
    ...


class DeviceTimeout:
    def __init__(self, *argv, **kwargs) -> None:
        ...


class DeviceConnection:
    def timeout(self, *args, **kwargs) -> Any:
        ...

    def services(self, *args, **kwargs) -> Any:
        ...

    def is_connected(self, *args, **kwargs) -> Any:
        ...

    service: Any  ## <class 'generator'> = <generator>
    pair: Any  ## <class 'generator'> = <generator>
    exchange_mtu: Any  ## <class 'generator'> = <generator>
    l2cap_accept: Any  ## <class 'generator'> = <generator>
    disconnected: Any  ## <class 'generator'> = <generator>
    disconnect: Any  ## <class 'generator'> = <generator>
    l2cap_connect: Any  ## <class 'generator'> = <generator>
    device_task: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


ble: Any  ## <class 'BLE'> = <BLE>


class BaseCharacteristic:
    def write(self, *args, **kwargs) -> Any:
        ...

    def on_read(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    written: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Characteristic:
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


class Service:
    def __init__(self, *argv, **kwargs) -> None:
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
