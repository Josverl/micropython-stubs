"""
Module: 'aioble.l2cap' on micropython-v1.21.0-rp2-RPI_PICO_W
"""

# MCU: {'build': '', 'ver': '1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.20.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

_listening: bool = False

def const(*args, **kwargs) -> Incomplete: ...
def register_irq_handler(*args, **kwargs) -> Incomplete: ...
def _l2cap_irq(*args, **kwargs) -> Incomplete: ...
def _l2cap_shutdown(*args, **kwargs) -> Incomplete: ...
def log_error(*args, **kwargs) -> Incomplete: ...

class L2CAPChannel:
    def available(self, *args, **kwargs) -> Incomplete: ...
    def _assert_connected(self, *args, **kwargs) -> Incomplete: ...

    send: Generator  ## = <generator>
    recvinto: Generator  ## = <generator>
    disconnect: Generator  ## = <generator>
    disconnected: Generator  ## = <generator>
    flush: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

connect: Generator  ## = <generator>
accept: Generator  ## = <generator>

class L2CAPConnectionError(Exception): ...

ble: Incomplete  ## <class 'BLE'> = <BLE>

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

class L2CAPDisconnectedError(Exception): ...
