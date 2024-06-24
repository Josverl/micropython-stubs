"""
Control the garbage collector.

MicroPython module: https://docs.micropython.org/en/v1.22.2/library/gc.html

CPython module: :mod:`python:gc` https://docs.python.org/3/library/gc.html .

---
Module: 'gc' on micropython-v1.22.2-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'build': '', 'ver': '1.22.2', 'version': '1.22.2', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'SAMD51P19A', 'arch': 'armv7emsp'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, Optional

def isenabled(*args, **kwargs) -> Incomplete: ...
def mem_free() -> int:
    """
    Return the number of bytes of heap RAM that is available for Python
    code to allocate, or -1 if this amount is not known.

    Difference to CPython

       This function is MicroPython extension.
    """
    ...

def mem_alloc() -> int:
    """
    Return the number of bytes of heap RAM that are allocated by Python code.

    Difference to CPython

       This function is MicroPython extension.
    """
    ...

def collect() -> None:
    """
    Run a garbage collection.
    """
    ...

def enable() -> None:
    """
    Enable automatic garbage collection.
    """
    ...

def disable() -> None:
    """
    Disable automatic garbage collection.  Heap memory can still be allocated,
    and garbage collection can still be initiated manually using :meth:`gc.collect`.
    """
    ...
