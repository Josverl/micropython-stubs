"""
Module: 'aioble.__init__' on micropython-v1.21.0-rp2-RPI_PICO_W
"""

# MCU: {'build': '', 'ver': '1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.23.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

ADDR_RANDOM: int = 1
ADDR_PUBLIC: int = 0

def log_error(*args, **kwargs) -> Incomplete: ...
def log_warn(*args, **kwargs) -> Incomplete: ...
def stop(*args, **kwargs) -> Incomplete: ...
def register_services(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...
def log_info(*args, **kwargs) -> Incomplete: ...
def config(*args, **kwargs) -> Incomplete: ...

class BufferedCharacteristic:
    def _indicate_done(self, *args, **kwargs) -> Incomplete: ...
    def notify(self, *args, **kwargs) -> Incomplete: ...
    def _tuple(self, *args, **kwargs) -> Incomplete: ...
    def _init_capture(self, *args, **kwargs) -> Incomplete: ...
    def on_read(self, *args, **kwargs) -> Incomplete: ...
    def _remote_read(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def _remote_write(self, *args, **kwargs) -> Incomplete: ...

    indicate: Generator  ## = <generator>
    def _register(self, *args, **kwargs) -> Incomplete: ...

    written: Generator  ## = <generator>
    _run_capture_task: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class Descriptor:
    def on_read(self, *args, **kwargs) -> Incomplete: ...
    def _register(self, *args, **kwargs) -> Incomplete: ...
    def _tuple(self, *args, **kwargs) -> Incomplete: ...
    def _init_capture(self, *args, **kwargs) -> Incomplete: ...
    def _remote_read(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def _remote_write(self, *args, **kwargs) -> Incomplete: ...

    _run_capture_task: Generator  ## = <generator>
    written: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class scan:
    cancel: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class DeviceDisconnectedError(Exception): ...

class Device:
    def addr_hex(self, *args, **kwargs) -> Incomplete: ...

    connect: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class Characteristic:
    def _tuple(self, *args, **kwargs) -> Incomplete: ...
    def _register(self, *args, **kwargs) -> Incomplete: ...
    def on_read(self, *args, **kwargs) -> Incomplete: ...
    def _init_capture(self, *args, **kwargs) -> Incomplete: ...
    def notify(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def _indicate_done(self, *args, **kwargs) -> Incomplete: ...
    def _remote_write(self, *args, **kwargs) -> Incomplete: ...
    def _remote_read(self, *args, **kwargs) -> Incomplete: ...

    indicate: Generator  ## = <generator>
    written: Generator  ## = <generator>
    _run_capture_task: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class GattError(Exception): ...

advertise: Generator  ## = <generator>

class Service:
    def _tuple(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
