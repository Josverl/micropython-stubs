"""
Efficient arrays of numeric data.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/array.html

CPython module: :mod:`python:array` https://docs.python.org/3/library/array.html .

Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
``L``, ``q``, ``Q``, ``f``, ``d`` (the latter 2 depending on the
floating-point support).

---
Module: 'array' on micropython-v1.21.0-esp8266-ESP8266_GENERIC
"""

# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensa', 'ver': '1.21.0', 'cpu': 'ESP8266'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, List, Optional

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

    def __init__(self, *argv, **kwargs) -> None: ...
