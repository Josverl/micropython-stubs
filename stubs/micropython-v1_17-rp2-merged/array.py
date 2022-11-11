"""
efficient arrays of numeric data. See: https://docs.micropython.org/en/v1.17/library/array.html

|see_cpython_module| :mod:`python:array` https://docs.python.org/3/library/array.html .

Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
``L``, ``q``, ``Q``, ``f``, ``d`` (the latter 2 depending on the
floating-point support).
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.17.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Raspberry Pi Pico with RP2040', 'nodename': 'rp2', 'ver': 'v1.17', 'release': '1.17.0'}
# Stubber: 1.5.2
from typing import Any


class array:
    """
    Create array with elements of given type. Initial contents of the
    array are given by *iterable*. If it is not provided, an empty
    array is created.
    """

    def append(self, val) -> Any:
        """
        Append new element *val* to the end of array, growing it.
        """
        ...

    def extend(self, iterable) -> Any:
        """
        Append new elements as contained in *iterable* to the end of
        array, growing it.
        """
        ...

    def decode(self, *args) -> Any:
        ...
