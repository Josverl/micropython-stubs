"""
Module: 'aioble.client' on micropython-v1.19.1-rp2
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2'}
# Stubber: 1.9.11
from typing import Any


def register_irq_handler(*args, **kwargs) -> Any:
    ...


def const(*args, **kwargs) -> Any:
    ...


class ClientDiscover:
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ClientService:
    def characteristics(self, *args, **kwargs) -> Any:
        ...

    characteristic: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ClientCharacteristic:
    def descriptors(self, *args, **kwargs) -> Any:
        ...

    indicated: Any  ## <class 'generator'> = <generator>
    notified: Any  ## <class 'generator'> = <generator>
    subscribe: Any  ## <class 'generator'> = <generator>
    read: Any  ## <class 'generator'> = <generator>
    descriptor: Any  ## <class 'generator'> = <generator>
    write: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class BaseClientCharacteristic:
    write: Any  ## <class 'generator'> = <generator>
    read: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ClientDescriptor:
    write: Any  ## <class 'generator'> = <generator>
    read: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class GattError(Exception):
    ...
