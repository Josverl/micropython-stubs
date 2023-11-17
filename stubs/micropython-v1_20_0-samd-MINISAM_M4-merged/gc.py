"""
Module: 'gc' on micropython-v1.20.0-samd-MINISAM_M4
"""
# MCU: OrderedDict({'build': '', 'ver': 'v1.20.0', 'version': '1.20.0', 'port': 'samd', 'board': 'MINISAM_M4', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51G19A', 'arch': 'armv7emsp'})
# Stubber: v1.13.7
from typing import Optional, Any
from _typeshed import Incomplete as Incomplete


def isenabled(*args, **kwargs) -> Any:
    ...


def mem_free() -> int:
    """
    Return the number of bytes of available heap RAM, or -1 if this amount
    is not known.

    Difference to CPython

       This function is MicroPython extension.
    """
    ...


def mem_alloc() -> int:
    """
    Return the number of bytes of heap RAM that are allocated.

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
