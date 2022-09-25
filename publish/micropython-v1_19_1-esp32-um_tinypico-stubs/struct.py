"""
pack and unpack primitive data types. See: https://docs.micropython.org/en/v1.19.1/library/struct.html

|see_cpython_module| :mod:`python:struct` https://docs.python.org/3/library/struct.html .

Supported size/byte order prefixes: ``@``, ``<``, ``>``, ``!``.

Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
``L``, ``q``, ``Q``, ``s``, ``P``, ``f``, ``d`` (the latter 2 depending
on the floating-point support).
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Callable, Coroutine, Dict, Generator, IO, Iterator, List, NoReturn, Optional, Tuple, Union, Any


def calcsize(fmt) -> int:
    """
    Return the number of bytes needed to store the given *fmt*.
    """
    ...


def pack(fmt, v1, v2, *args) -> bytes:
    """
    Pack the values *v1*, *v2*, ... according to the format string *fmt*.
    The return value is a bytes object encoding the values.
    """
    ...


def pack_into(fmt, buffer, offset, v1, v2, *args) -> Any:
    """
    Pack the values *v1*, *v2*, ... according to the format string *fmt*
    into a *buffer* starting at *offset*. *offset* may be negative to count
    from the end of *buffer*.
    """
    ...


def unpack(fmt, data) -> Tuple:
    """
    Unpack from the *data* according to the format string *fmt*.
    The return value is a tuple of the unpacked values.
    """
    ...


def unpack_from(fmt, data, offset=0, /) -> Tuple:
    """
    Unpack from the *data* starting at *offset* according to the format string
    *fmt*. *offset* may be negative to count from the end of *buffer*. The return
    value is a tuple of the unpacked values.
    """
    ...
