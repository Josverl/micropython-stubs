"""
Module: 'aioble.central' on micropython-v1.21.0-rp2-RPI_PICO_W
"""

# MCU: {'build': '', 'ver': '1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.20.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

def _central_irq(*args, **kwargs) -> Incomplete: ...
def ensure_active(*args, **kwargs) -> Incomplete: ...
def log_info(*args, **kwargs) -> Incomplete: ...
def log_warn(*args, **kwargs) -> Incomplete: ...
def log_error(*args, **kwargs) -> Incomplete: ...
def _central_shutdown(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...
def register_irq_handler(*args, **kwargs) -> Incomplete: ...

_connect: Generator  ## = <generator>

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

_active_scanner: Incomplete  ## <class 'NoneType'> = None

class ScanResult:
    def _update(self, *args, **kwargs) -> Incomplete: ...
    def name(self, *args, **kwargs) -> Incomplete: ...

    _decode_field: Generator  ## = <generator>
    manufacturer: Generator  ## = <generator>
    services: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

_cancel_pending: Generator  ## = <generator>
_connecting: set  ## = set()

class scan:
    cancel: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class DeviceTimeout:
    _timeout_sleep: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

ble: Incomplete  ## <class 'BLE'> = <BLE>

class Device:
    def addr_hex(self, *args, **kwargs) -> Incomplete: ...

    connect: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
