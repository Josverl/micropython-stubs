"""
Module: 'aioble.__init__' on micropython-v1.24.0-preview-rp2-RPI_PICO_W
"""

# MCU: {'build': 'preview.60.gcebc9b0ae', 'ver': '1.24.0-preview-preview.60.gcebc9b0ae', 'version': '1.24.0-preview', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.20.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

ADDR_PUBLIC: int = 0
ADDR_RANDOM: int = 1

def log_warn(*args, **kwargs) -> Incomplete: ...
def log_info(*args, **kwargs) -> Incomplete: ...
def log_error(*args, **kwargs) -> Incomplete: ...
def register_services(*args, **kwargs) -> Incomplete: ...
def stop(*args, **kwargs) -> Incomplete: ...
def config(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...

class Service:
    def _tuple(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class scan:
    cancel: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

advertise: Generator  ## = <generator>

class Characteristic:
    def _remote_write(self, *args, **kwargs) -> Incomplete: ...
    def _remote_read(self, *args, **kwargs) -> Incomplete: ...
    def notify(self, *args, **kwargs) -> Incomplete: ...
    def on_read(self, *args, **kwargs) -> Incomplete: ...
    def _tuple(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def _register(self, *args, **kwargs) -> Incomplete: ...
    def _indicate_done(self, *args, **kwargs) -> Incomplete: ...
    def _init_capture(self, *args, **kwargs) -> Incomplete: ...

    written: Generator  ## = <generator>
    indicate: Generator  ## = <generator>
    _run_capture_task: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class GattError(Exception): ...

class BufferedCharacteristic:
    def on_read(self, *args, **kwargs) -> Incomplete: ...
    def _remote_read(self, *args, **kwargs) -> Incomplete: ...
    def _remote_write(self, *args, **kwargs) -> Incomplete: ...
    def notify(self, *args, **kwargs) -> Incomplete: ...
    def _tuple(self, *args, **kwargs) -> Incomplete: ...
    def _init_capture(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def _indicate_done(self, *args, **kwargs) -> Incomplete: ...

    written: Generator  ## = <generator>
    def _register(self, *args, **kwargs) -> Incomplete: ...

    indicate: Generator  ## = <generator>
    _run_capture_task: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class DeviceDisconnectedError(Exception): ...

class Descriptor:
    def _tuple(self, *args, **kwargs) -> Incomplete: ...
    def _remote_read(self, *args, **kwargs) -> Incomplete: ...
    def _remote_write(self, *args, **kwargs) -> Incomplete: ...
    def on_read(self, *args, **kwargs) -> Incomplete: ...
    def _register(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def _init_capture(self, *args, **kwargs) -> Incomplete: ...

    written: Generator  ## = <generator>
    _run_capture_task: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class Device:
    def addr_hex(self, *args, **kwargs) -> Incomplete: ...

    connect: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
