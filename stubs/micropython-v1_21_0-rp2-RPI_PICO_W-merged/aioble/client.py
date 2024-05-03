"""
Module: 'aioble.client' on micropython-v1.21.0-rp2-RPI_PICO_W
"""

# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete


def register_irq_handler(*args, **kwargs) -> Incomplete: ...


def const(*args, **kwargs) -> Incomplete: ...


class ClientDiscover:
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


class ClientDescriptor:
    write: Incomplete  ## <class 'generator'> = <generator>
    read: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class ClientCharacteristic:
    def descriptors(self, *args, **kwargs) -> Incomplete: ...

    subscribe: Incomplete  ## <class 'generator'> = <generator>
    notified: Incomplete  ## <class 'generator'> = <generator>
    indicated: Incomplete  ## <class 'generator'> = <generator>
    read: Incomplete  ## <class 'generator'> = <generator>
    descriptor: Incomplete  ## <class 'generator'> = <generator>
    write: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class ClientService:
    def characteristics(self, *args, **kwargs) -> Incomplete: ...

    characteristic: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class BaseClientCharacteristic:
    write: Incomplete  ## <class 'generator'> = <generator>
    read: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class deque:
    def popleft(self, *args, **kwargs) -> Incomplete: ...

    def append(self, *args, **kwargs) -> Incomplete: ...

    def __init__(self, *argv, **kwargs) -> None: ...


ble: Incomplete  ## <class 'BLE'> = <BLE>


class GattError(Exception): ...
