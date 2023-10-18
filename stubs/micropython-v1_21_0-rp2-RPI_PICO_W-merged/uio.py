"""
Input/output streams.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/io.html

CPython module: :mod:`python:io` https://docs.python.org/3/library/io.html .

This module contains additional types of `stream` (file-like) objects
and helper functions.
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import IO, Optional, Any
from _typeshed import Incomplete
from stdlib.io import *


def open(name, mode="r", **kwargs) -> Incomplete:
    """
    Open a file. Builtin ``open()`` function is aliased to this function.
    All ports (which provide access to file system) are required to support
    *mode* parameter, but support for other arguments vary by port.
    """
    ...


class IOBase:
    def __init__(self, *argv, **kwargs) -> None:
        ...


class StringIO(IO):
    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def getvalue(self, *args, **kwargs) -> Incomplete:
        ...

    def seek(self, *args, **kwargs) -> Incomplete:
        ...

    def tell(self, *args, **kwargs) -> Incomplete:
        ...

    def readline(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, string: Optional[Any] = None) -> None:
        ...


class BytesIO(IO):
    """
    In-memory file-like objects for input/output. `StringIO` is used for
    text-mode I/O (similar to a normal file opened with "t" modifier).
    `BytesIO` is used for binary-mode I/O (similar to a normal file
    opened with "b" modifier). Initial contents of file-like objects
    can be specified with *string* parameter (should be normal string
    for `StringIO` or bytes object for `BytesIO`). All the usual file
    methods like ``read()``, ``write()``, ``seek()``, ``flush()``,
    ``close()`` are available on these objects, and additionally, a
    following method:
    """

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def getvalue(self) -> Incomplete:
        """
        Get the current contents of the underlying buffer which holds data.
        """
        ...

    def seek(self, *args, **kwargs) -> Incomplete:
        ...

    def tell(self, *args, **kwargs) -> Incomplete:
        ...

    def readline(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, string: Optional[Any] = None) -> None:
        ...
