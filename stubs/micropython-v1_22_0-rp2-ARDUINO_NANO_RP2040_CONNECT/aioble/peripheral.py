"""
Module: 'aioble.peripheral' on micropython-v1.22.0-rp2-ARDUINO_NANO_RP2040_CONNECT
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.16.2
from _typeshed import Incomplete


def log_error(*args, **kwargs) -> Incomplete:
    ...


def ensure_active(*args, **kwargs) -> Incomplete:
    ...


def register_irq_handler(*args, **kwargs) -> Incomplete:
    ...


def log_info(*args, **kwargs) -> Incomplete:
    ...


def log_warn(*args, **kwargs) -> Incomplete:
    ...


def const(*args, **kwargs) -> Incomplete:
    ...


class Device:
    def addr_hex(self, *args, **kwargs) -> Incomplete:
        ...

    connect: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class DeviceConnection:
    def timeout(self, *args, **kwargs) -> Incomplete:
        ...

    def is_connected(self, *args, **kwargs) -> Incomplete:
        ...

    def services(self, *args, **kwargs) -> Incomplete:
        ...

    l2cap_connect: Incomplete  ## <class 'generator'> = <generator>
    l2cap_accept: Incomplete  ## <class 'generator'> = <generator>
    pair: Incomplete  ## <class 'generator'> = <generator>
    service: Incomplete  ## <class 'generator'> = <generator>
    disconnect: Incomplete  ## <class 'generator'> = <generator>
    device_task: Incomplete  ## <class 'generator'> = <generator>
    disconnected: Incomplete  ## <class 'generator'> = <generator>
    exchange_mtu: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


ble: Incomplete  ## <class 'BLE'> = <BLE>


class DeviceTimeout:
    def __init__(self, *argv, **kwargs) -> None:
        ...


advertise: Incomplete  ## <class 'generator'> = <generator>
