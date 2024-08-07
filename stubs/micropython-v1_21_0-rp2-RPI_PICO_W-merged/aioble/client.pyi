"""
Module: 'aioble.client' on micropython-v1.21.0-rp2-RPI_PICO_W
"""

# MCU: {'build': '', 'ver': '1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.23.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

def _client_irq(*args, **kwargs) -> Incomplete: ...
def register_irq_handler(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...

class ClientService:
    def _start_discovery(self, *args, **kwargs) -> Incomplete: ...
    def characteristics(self, *args, **kwargs) -> Incomplete: ...

    characteristic: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class ClientDiscover:
    def _discover_done(self, *args, **kwargs) -> Incomplete: ...
    def _discover_result(self, *args, **kwargs) -> Incomplete: ...

    _start: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class ClientDescriptor:
    def _start_discovery(self, *args, **kwargs) -> Incomplete: ...
    def _write_done(self, *args, **kwargs) -> Incomplete: ...
    def _check(self, *args, **kwargs) -> Incomplete: ...
    def _register_with_connection(self, *args, **kwargs) -> Incomplete: ...
    def _find(self, *args, **kwargs) -> Incomplete: ...
    def _connection(self, *args, **kwargs) -> Incomplete: ...
    def _read_done(self, *args, **kwargs) -> Incomplete: ...
    def _read_result(self, *args, **kwargs) -> Incomplete: ...

    write: Generator  ## = <generator>
    read: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class BaseClientCharacteristic:
    def _check(self, *args, **kwargs) -> Incomplete: ...
    def _write_done(self, *args, **kwargs) -> Incomplete: ...
    def _register_with_connection(self, *args, **kwargs) -> Incomplete: ...
    def _find(self, *args, **kwargs) -> Incomplete: ...
    def _read_done(self, *args, **kwargs) -> Incomplete: ...
    def _read_result(self, *args, **kwargs) -> Incomplete: ...

    write: Generator  ## = <generator>
    read: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class ClientCharacteristic:
    def _on_indicate(self, *args, **kwargs) -> Incomplete: ...
    def _write_done(self, *args, **kwargs) -> Incomplete: ...
    def _on_notify(self, *args, **kwargs) -> Incomplete: ...
    def _find(self, *args, **kwargs) -> Incomplete: ...
    def _start_discovery(self, *args, **kwargs) -> Incomplete: ...
    def _register_with_connection(self, *args, **kwargs) -> Incomplete: ...
    def _check(self, *args, **kwargs) -> Incomplete: ...
    def _connection(self, *args, **kwargs) -> Incomplete: ...
    def _on_notify_indicate(self, *args, **kwargs) -> Incomplete: ...
    def _read_done(self, *args, **kwargs) -> Incomplete: ...
    def descriptors(self, *args, **kwargs) -> Incomplete: ...
    def _read_result(self, *args, **kwargs) -> Incomplete: ...

    notified: Generator  ## = <generator>
    subscribe: Generator  ## = <generator>
    indicated: Generator  ## = <generator>
    _notified_indicated: Generator  ## = <generator>
    read: Generator  ## = <generator>
    write: Generator  ## = <generator>
    descriptor: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class DeviceConnection:
    _connected: dict = {}
    def is_connected(self, *args, **kwargs) -> Incomplete: ...
    def _run_task(self, *args, **kwargs) -> Incomplete: ...
    def services(self, *args, **kwargs) -> Incomplete: ...
    def timeout(self, *args, **kwargs) -> Incomplete: ...

    l2cap_accept: Generator  ## = <generator>
    exchange_mtu: Generator  ## = <generator>
    pair: Generator  ## = <generator>
    l2cap_connect: Generator  ## = <generator>
    service: Generator  ## = <generator>
    disconnect: Generator  ## = <generator>
    device_task: Generator  ## = <generator>
    disconnected: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class deque:
    def popleft(self, *args, **kwargs) -> Incomplete: ...
    def append(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

ble: Incomplete  ## <class 'BLE'> = <BLE>

class GattError(Exception): ...
