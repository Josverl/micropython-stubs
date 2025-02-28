"""
Efficient arrays of numeric data.

MicroPython module: https://docs.micropython.org/en/v1.24.0/library/array.html

CPython module: :mod:`python:array` https://docs.python.org/3/library/array.html .

Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
``L``, ``q``, ``Q``, ``f``, ``d`` (the latter 2 depending on the
floating-point support).
"""

# source version: v1.24.0
# origin module:: repos/micropython/docs/library/array.rst
from __future__ import annotations

from collections.abc import MutableSequence, Sequence
from typing import Any, Generic, TypeVar, overload

from typing_extensions import TypeVar

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

    def __init__(self, typecode: str, iterable: Sequence[Any] = ..., /) -> None:
        """
        Create array with elements of given type. Initial contents of the
        array are given by *iterable*. If it is not provided, an empty
        array is created.
        """

    def append(self, val: Any, /) -> None:
        """
        Append new element *val* to the end of array, growing it.
        """
        ...

    def extend(self, iterable: Sequence[Any], /) -> None:
        """
        Append new elements as contained in *iterable* to the end of
        array, growing it.
        """
        ...

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

    def __len__(self) -> int:
        """
        Returns the number of items in the array, called as ``len(a)`` (where ``a`` is an ``array``).

        **Note:** ``__len__`` cannot be called directly (``a.__len__()`` fails) and the
        method is not present in ``__dict__``, however ``len(a)`` does work.
        """
        ...

    def __add__(self, other: array[_T]) -> array[_T]:
        """
        Return a new ``array`` that is the concatenation of the array with *other*, called as
        ``a + other`` (where ``a`` and *other* are both ``arrays``).

        **Note:** ``__add__`` cannot be called directly (``a.__add__(other)`` fails) and
        is not present in ``__dict__``, however ``a + other`` does work.
        """
        ...

    def __iadd__(self, other: array[_T]) -> None:
        """
        Concatenates the array with *other* in-place, called as ``a += other`` (where ``a`` and *other*
        are both ``arrays``).  Equivalent to ``extend(other)``.

        **Note:** ``__iadd__`` cannot be called directly (``a.__iadd__(other)`` fails) and
        is not present in ``__dict__``, however ``a += other`` does work.
        """
        ...

    def __repr__(self) -> str:
        """
        Returns the string representation of the array, called as ``str(a)`` or ``repr(a)```
        (where ``a`` is an ``array``).  Returns the string ``"array(<type>, [<elements>])"``,
        where ``<type>`` is the type code letter for the array and ``<elements>`` is a comma
        separated list of the elements of the array.

        **Note:** ``__repr__`` cannot be called directly (``a.__repr__()`` fails) and
        is not present in ``__dict__``, however ``str(a)`` and ``repr(a)`` both work.
        """
        ...
