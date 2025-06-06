"""
Module: 'aioble.__init__' on micropython-v1.25.0-rp2-RPI_PICO2_W
"""

# MCU: {'build': '', 'ver': '1.25.0', 'version': '1.25.0', 'port': 'rp2', 'board': 'RPI_PICO2_W', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2350', 'arch': 'armv7emsp'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Final, Generator
from _typeshed import Incomplete

ADDR_PUBLIC: Final[int] = 0
ADDR_RANDOM: Final[int] = 1

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
    def cancel(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None: ...

def advertise(*args, **kwargs) -> Generator:  ## = <generator>
    ...

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
    def written(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def indicate(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def _run_capture_task(*args, **kwargs) -> Generator:  ## = <generator>
        ...

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
    def written(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def _register(self, *args, **kwargs) -> Incomplete: ...
    def indicate(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def _run_capture_task(*args, **kwargs) -> Generator:  ## = <generator>
        ...

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
    def written(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def _run_capture_task(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None: ...

class Device:
    def addr_hex(self, *args, **kwargs) -> Incomplete: ...
    def connect(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None: ...
