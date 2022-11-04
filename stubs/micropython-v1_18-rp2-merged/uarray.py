"""
efficient arrays of numeric data. See: https://docs.micropython.org/en/v1.18/library/array.html

|see_cpython_module| :mod:`python:array` https://docs.python.org/3/library/array.html .

Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
``L``, ``q``, ``Q``, ``f``, ``d`` (the latter 2 depending on the
floating-point support).
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.18.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2', 'ver': 'v1.18', 'release': '1.18.0'}
# Stubber: 1.5.3
from typing import Optional, Any


class array:
    """
    Create array with elements of given type. Initial contents of the
    array are given by *iterable*. If it is not provided, an empty
    array is created.
    """

    def __init__(self, typecode, iterable: Optional[Any] = None) -> None:
        """"""
        ...

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

    def decode(self, *args, **kwargs) -> Any:
        ...
