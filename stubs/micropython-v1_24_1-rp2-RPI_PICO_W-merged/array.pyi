"""
Efficient arrays of numeric data.

MicroPython module: https://docs.micropython.org/en/v1.24.0/library/array.html

CPython module: :mod:`python:array` https://docs.python.org/3/library/array.html .

Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
``L``, ``q``, ``Q``, ``f``, ``d`` (the latter 2 depending on the
floating-point support).

---
Module: 'array' on micropython-v1.24.1-rp2-RPI_PICO_W
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.3', 'arch': 'armv6m'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete
from collections.abc import MutableSequence, Sequence
from typing import Any, Generic, overload
from typing_extensions import Awaitable, TypeAlias, TypeVar

_T = TypeVar("_T", int, float, str)

class array(MutableSequence[_T], Generic[_T]):
    """
    |see_cpython_module| :mod:`python:array`.

    Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
    ``L``, ``q``, ``Q``, ``f``, ``d`` (the latter 2 depending on the
    floating-point support).

     +-----------+--------------------+-------------------+-----------------------+
     | Type code | C Type             | Python Type       | Minimum size in bytes |
     +===========+====================+===================+=======================+
     | ``'b'``   | signed char        | int               | 1                     |
     +-----------+--------------------+-------------------+-----------------------+
     | ``'B'``   | unsigned char      | int               | 1                     |
     +-----------+--------------------+-------------------+-----------------------+
     | ``'h'``   | signed short       | int               | 2                     |
     +-----------+--------------------+-------------------+-----------------------+
     | ``'H'``   | unsigned short     | int               | 2                     |
     +-----------+--------------------+-------------------+-----------------------+
     | ``'i'``   | signed int         | int               | 2                     |
     +-----------+--------------------+-------------------+-----------------------+
     | ``'I'``   | unsigned int       | int               | 2                     |
     +-----------+--------------------+-------------------+-----------------------+
     | ``'l'``   | signed long        | int               | 4                     |
     +-----------+--------------------+-------------------+-----------------------+
     | ``'L'``   | unsigned long      | int               | 4                     |
     +-----------+--------------------+-------------------+-----------------------+
     | ``'q'``   | signed long long   | int               | 8                     |
     +-----------+--------------------+-------------------+-----------------------+
     | ``'Q'``   | unsigned long long | int               | 8                     |
     +-----------+--------------------+-------------------+-----------------------+
     | ``'f'``   | float              | float             | 4                     |
     +-----------+--------------------+-------------------+-----------------------+
     | ``'d'``   | double             | float             | 8                     |
     +-----------+--------------------+-------------------+-----------------------+
    """

    def extend(self, iterable: Sequence[Any], /) -> None:
        """
        Append new elements as contained in *iterable* to the end of
        array, growing it.
        """
        ...

    def append(self, val: Any, /) -> None:
        """
        Append new element *val* to the end of array, growing it.
        """
        ...

    def __init__(self, *argv, **kwargs) -> None:
        """
        Create array with elements of given type. Initial contents of the
        array are given by *iterable*. If it is not provided, an empty
        array is created.
        """

    @overload
    def __getitem__(self, index: int) -> _T:
        """
        Indexed read of the array, called as ``a[index]`` (where ``a`` is an ``array``).
        Returns a value if *index* is an ``int`` and an ``array`` if *index* is a slice.
        Negative indices count from the end and ``IndexError`` is thrown if the index is
        out of range.

        **Note:** ``__getitem__`` cannot be called directly (``a.__getitem__(index)`` fails) and
        is not present in ``__dict__``, however ``a[index]`` does work.
        """

    @overload
    def __getitem__(self, sl: slice) -> array[_T]:
        """
        Indexed read of the array, called as ``a[index]`` (where ``a`` is an ``array``).
        Returns a value if *index* is an ``int`` and an ``array`` if *index* is a slice.
        Negative indices count from the end and ``IndexError`` is thrown if the index is
        out of range.

        **Note:** ``__getitem__`` cannot be called directly (``a.__getitem__(index)`` fails) and
        is not present in ``__dict__``, however ``a[index]`` does work.
        """

    @overload
    def __setitem__(self, index: int, value: _T) -> None:
        """
        Indexed write into the array, called as ``a[index] = value`` (where ``a`` is an ``array``).
        ``value`` is a single value if *index* is an ``int`` and an ``array`` if *index* is a slice.
        Negative indices count from the end and ``IndexError`` is thrown if the index is out of range.

        **Note:** ``__setitem__`` cannot be called directly (``a.__setitem__(index, value)`` fails) and
        is not present in ``__dict__``, however ``a[index] = value`` does work.
        """

    @overload
    def __setitem__(self, sl: slice, values: array[_T]) -> None:
        """
        Indexed write into the array, called as ``a[index] = value`` (where ``a`` is an ``array``).
        ``value`` is a single value if *index* is an ``int`` and an ``array`` if *index* is a slice.
        Negative indices count from the end and ``IndexError`` is thrown if the index is out of range.

        **Note:** ``__setitem__`` cannot be called directly (``a.__setitem__(index, value)`` fails) and
        is not present in ``__dict__``, however ``a[index] = value`` does work.
        """
