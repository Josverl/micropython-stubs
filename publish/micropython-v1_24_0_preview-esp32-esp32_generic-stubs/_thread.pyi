"""
Multithreading support.

MicroPython module: https://docs.micropython.org/en/v1.24.0-preview/library/_thread.html

CPython module: :mod:`python:_thread` https://docs.python.org/3/library/_thread.html .

This module implements multithreading support.

This module is highly experimental and its API is not yet fully settled
and not yet described in this documentation.

---
Module: '_thread' on micropython-v1.24.0-preview-esp32-ESP32_GENERIC
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'family': 'micropython', 'build': 'preview.60.gcebc9b0ae', 'arch': 'xtensawin', 'ver': '1.24.0-preview-preview.60.gcebc9b0ae', 'cpu': 'ESP32'}
# Stubber: v1.20.0
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
