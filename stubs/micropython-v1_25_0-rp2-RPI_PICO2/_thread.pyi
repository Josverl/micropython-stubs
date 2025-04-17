"""
Module: '_thread' on micropython-v1.25.0-rp2-RPI_PICO2
"""

# MCU: {'build': '', 'ver': '1.25.0', 'version': '1.25.0', 'port': 'rp2', 'board': 'RPI_PICO2', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2350', 'arch': 'armv7emsp'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

def get_ident(*args, **kwargs) -> Incomplete: ...
def start_new_thread(*args, **kwargs) -> Incomplete: ...
def stack_size(*args, **kwargs) -> Incomplete: ...
def exit(*args, **kwargs) -> Incomplete: ...
def allocate_lock(*args, **kwargs) -> Incomplete: ...

class LockType:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...
    def acquire(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
