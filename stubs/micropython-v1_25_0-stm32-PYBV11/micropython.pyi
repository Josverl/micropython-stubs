"""
Module: 'micropython' on micropython-v1.25.0-stm32-PYBV11
"""

# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': '1.25.0', 'cpu': 'STM32F405RG'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

def opt_level(*args, **kwargs) -> Incomplete: ...
def mem_info(*args, **kwargs) -> Incomplete: ...
def kbd_intr(*args, **kwargs) -> Incomplete: ...
def qstr_info(*args, **kwargs) -> Incomplete: ...
def schedule(*args, **kwargs) -> Incomplete: ...
def stack_use(*args, **kwargs) -> Incomplete: ...
def heap_unlock(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...
def heap_lock(*args, **kwargs) -> Incomplete: ...
def alloc_emergency_exception_buf(*args, **kwargs) -> Incomplete: ...

class RingIO:
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def any(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
