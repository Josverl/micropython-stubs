"""
Module: 'aioble.device' on micropython-v1.25.0-preview-rp2-UNKNOWN_BOARD
"""

# MCU: {'family': 'micropython', 'version': '1.25.0-preview', 'build': 'preview.236.gbfb1bee6f', 'ver': '1.25.0-preview-preview.236.gbfb1bee6f', 'port': 'rp2', 'board': 'UNKNOWN_BOARD', 'cpu': 'RP2350', 'mpy': 'v6.3', 'arch': 'armv7emsp'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

def _device_irq(*args, **kwargs) -> Incomplete: ...
def register_irq_handler(*args, **kwargs) -> Incomplete: ...
def log_error(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...

class Device:
    def addr_hex(self, *args, **kwargs) -> Incomplete: ...

    connect: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

ble: Incomplete  ## <class 'BLE'> = <BLE>

class DeviceConnection:
    _connected: dict = {}
    def is_connected(self, *args, **kwargs) -> Incomplete: ...
    def _run_task(self, *args, **kwargs) -> Incomplete: ...
    def services(self, *args, **kwargs) -> Incomplete: ...
    def timeout(self, *args, **kwargs) -> Incomplete: ...

    device_task: Generator  ## = <generator>
    l2cap_connect: Generator  ## = <generator>
    pair: Generator  ## = <generator>
    service: Generator  ## = <generator>
    l2cap_accept: Generator  ## = <generator>
    disconnected: Generator  ## = <generator>
    exchange_mtu: Generator  ## = <generator>
    disconnect: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class DeviceDisconnectedError(Exception): ...

class DeviceTimeout:
    _timeout_sleep: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
