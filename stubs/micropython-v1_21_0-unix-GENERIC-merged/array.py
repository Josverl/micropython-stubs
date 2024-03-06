"""
Efficient arrays of numeric data.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/array.html

CPython module: :mod:`python:array` https://docs.python.org/3/library/array.html .

Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
``L``, ``q``, ``Q``, ``f``, ``d`` (the latter 2 depending on the
floating-point support).

---
Module: 'array' on micropython-v1.21.0-unix-linux_[GCC_9.4.0]_version
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'unix', 'board': 'linux_[GCC_9.4.0]_version', 'cpu': '', 'mpy': '', 'arch': ''}
# Stubber: v1.15.1
from typing import List, Optional, Any
from _typeshed import Incomplete


class array(List):
    """
    Create array with elements of given type. Initial contents of the
    array are given by *iterable*. If it is not provided, an empty
    array is created.
    """

    def extend(self, iterable) -> Incomplete:
        """
        Append new elements as contained in *iterable* to the end of
        array, growing it.
        """
        ...

    def append(self, val) -> Incomplete:
        """
        Append new element *val* to the end of array, growing it.
        """
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
