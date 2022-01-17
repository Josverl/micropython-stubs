"""
pack and unpack primitive data types. See: https://docs.micropython.org/en/v1.18/library/struct.html

|see_cpython_module| :mod:`python:struct` https://docs.python.org/3/library/struct.html .

Supported size/byte order prefixes: ``@``, ``<``, ``>``, ``!``.

Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
``L``, ``q``, ``Q``, ``s``, ``P``, ``f``, ``d`` (the latter 2 depending
on the floating-point support).
"""

# source version: v1_18
# origin module:: micropython/docs/library/struct.rst
from typing import Any, Tuple


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
