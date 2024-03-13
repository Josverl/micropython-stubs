"""
Efficient arrays of numeric data.

MicroPython module: https://docs.micropython.org/en/v1.23.0-preview/library/array.html

CPython module: :mod:`python:array` https://docs.python.org/3/library/array.html .

Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
``L``, ``q``, ``Q``, ``f``, ``d`` (the latter 2 depending on the
floating-point support).

---
Module: 'uarray' on micropython-v1.23.0-preview-stm32-PYBV11
"""
# MCU: {'version': '1.23.0-preview', 'mpy': 'v6.2', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': 'preview.203.gd712feb68', 'arch': 'armv7emsp', 'ver': '1.23.0-preview-preview.203.gd712feb68', 'cpu': 'STM32F405RG'}
# Stubber: v1.17.3
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
