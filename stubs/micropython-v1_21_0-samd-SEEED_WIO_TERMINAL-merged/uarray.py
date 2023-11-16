"""
Module: 'uarray' on micropython-v1.21.0-samd-SEEED_WIO_TERMINAL
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51P19A', 'arch': 'armv7emsp'}
# Stubber: v1.13.8
from typing import List, Optional, Any
from _typeshed import Incomplete as Incomplete, Incomplete


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

    def __init__(self, typecode, iterable: Optional[Any] = ...) -> None:
        ...
