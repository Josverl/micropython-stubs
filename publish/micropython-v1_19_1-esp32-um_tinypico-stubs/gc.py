"""
control the garbage collector. See: https://docs.micropython.org/en/v1.19.1/library/gc.html

|see_cpython_module| :mod:`python:gc` https://docs.python.org/3/library/gc.html .
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Callable, Coroutine, Dict, Generator, IO, Iterator, List, NoReturn, Optional, Tuple, Union, Any


def collect() -> None:
    """
    Run a garbage collection.
    """
    ...


def disable() -> None:
    """
    Disable automatic garbage collection.  Heap memory can still be allocated,
    and garbage collection can still be initiated manually using :meth:`gc.collect`.
    """
    ...


def enable() -> None:
    """
    Enable automatic garbage collection.
    """
    ...


def isenabled(*args, **kwargs) -> Any:
    ...


def mem_alloc() -> int:
    """
    Return the number of bytes of heap RAM that are allocated.
    """
    ...


def mem_free() -> int:
    """
    Return the number of bytes of available heap RAM, or -1 if this amount
    is not known.
    """
    ...


def threshold(amount: Optional[Any] = None) -> Any:
    """
    Set or query the additional GC allocation threshold. Normally, a collection
    is triggered only when a new allocation cannot be satisfied, i.e. on an
    out-of-memory (OOM) condition. If this function is called, in addition to
    OOM, a collection will be triggered each time after *amount* bytes have been
    allocated (in total, since the previous time such an amount of bytes
    have been allocated). *amount* is usually specified as less than the
    full heap size, with the intention to trigger a collection earlier than when the
    heap becomes exhausted, and in the hope that an early collection will prevent
    excessive memory fragmentation. This is a heuristic measure, the effect
    of which will vary from application to application, as well as
    the optimal value of the *amount* parameter.

    Calling the function without argument will return the current value of
    the threshold. A value of -1 means a disabled allocation threshold.
    """
    ...
