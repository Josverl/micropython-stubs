"""
Module: 'aioble.server' on micropython-v1.22.0-rp2-ARDUINO_NANO_RP2040_CONNECT
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.16.2
from _typeshed import Incomplete


def log_error(*args, **kwargs) -> Incomplete:
    ...


def register_services(*args, **kwargs) -> Incomplete:
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


class BaseCharacteristic:
    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def on_read(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    written: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class BufferedCharacteristic:
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


ble: Incomplete  ## <class 'BLE'> = <BLE>


class deque:
    def popleft(self, *args, **kwargs) -> Incomplete:
        ...

    def append(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


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


class Descriptor:
    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def on_read(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    written: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Service:
    def __init__(self, *argv, **kwargs) -> None:
        ...


class DeviceTimeout:
    def __init__(self, *argv, **kwargs) -> None:
        ...


class GattError(Exception):
    ...
