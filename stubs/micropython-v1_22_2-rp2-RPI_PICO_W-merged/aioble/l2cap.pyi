"""
Module: 'aioble.l2cap' on micropython-v1.22.2-rp2-RPI_PICO_W
"""

# MCU: {'build': '', 'ver': '1.22.2', 'version': '1.22.2', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.20.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

_listening: bool = False

def register_irq_handler(*args, **kwargs) -> Incomplete: ...
def _l2cap_irq(*args, **kwargs) -> Incomplete: ...
def _l2cap_shutdown(*args, **kwargs) -> Incomplete: ...
def log_error(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...

accept: Generator  ## = <generator>
ble: Incomplete  ## <class 'BLE'> = <BLE>

class L2CAPChannel:
    def available(self, *args, **kwargs) -> Incomplete: ...
    def _assert_connected(self, *args, **kwargs) -> Incomplete: ...

    disconnected: Generator  ## = <generator>
    recvinto: Generator  ## = <generator>
    send: Generator  ## = <generator>
    flush: Generator  ## = <generator>
    disconnect: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

connect: Generator  ## = <generator>

class L2CAPConnectionError(Exception): ...
class L2CAPDisconnectedError(Exception): ...

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
