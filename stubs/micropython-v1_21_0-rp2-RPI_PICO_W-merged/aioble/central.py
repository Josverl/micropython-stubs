"""
Module: 'aioble.central' on micropython-v1.21.0-rp2-RPI_PICO_W
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete


def register_irq_handler(*args, **kwargs) -> Incomplete:
    ...


def ensure_active(*args, **kwargs) -> Incomplete:
    ...


def log_info(*args, **kwargs) -> Incomplete:
    ...


def log_warn(*args, **kwargs) -> Incomplete:
    ...


def log_error(*args, **kwargs) -> Incomplete:
    ...


def const(*args, **kwargs) -> Incomplete:
    ...


ble: Incomplete  ## <class 'BLE'> = <BLE>


class DeviceConnection:
    def services(self, *args, **kwargs) -> Incomplete:
        ...

    def is_connected(self, *args, **kwargs) -> Incomplete:
        ...

    def timeout(self, *args, **kwargs) -> Incomplete:
        ...

    l2cap_accept: Incomplete  ## <class 'generator'> = <generator>
    exchange_mtu: Incomplete  ## <class 'generator'> = <generator>
    pair: Incomplete  ## <class 'generator'> = <generator>
    l2cap_connect: Incomplete  ## <class 'generator'> = <generator>
    service: Incomplete  ## <class 'generator'> = <generator>
    disconnect: Incomplete  ## <class 'generator'> = <generator>
    device_task: Incomplete  ## <class 'generator'> = <generator>
    disconnected: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class DeviceTimeout:
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ScanResult:
    def name(self, *args, **kwargs) -> Incomplete:
        ...

    manufacturer: Incomplete  ## <class 'generator'> = <generator>
    services: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class scan:
    cancel: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Device:
    def addr_hex(self, *args, **kwargs) -> Incomplete:
        ...

    connect: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...
