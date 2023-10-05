"""
input/output streams. See: https://docs.micropython.org/en/v1.17/library/io.html

|see_cpython_module| :mod:`python:io` https://docs.python.org/3/library/io.html .

This module contains additional types of `stream` (file-like) objects
and helper functions.
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.17.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Raspberry Pi Pico with RP2040', 'nodename': 'rp2', 'ver': 'v1.17', 'release': '1.17.0'}
# Stubber: 1.5.2
from typing import IO, Optional, Any


def open(name, mode="r", **kwargs) -> Any:
    """
    Open a file. Builtin ``open()`` function is aliased to this function.
    All ports (which provide access to file system) are required to support
    *mode* parameter, but support for other arguments vary by port.
    """
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

    def close(self, *args) -> Any:
        ...

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def readline(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    def flush(self, *args) -> Any:
        ...

    def getvalue(self) -> Any:
        """
        Get the current contents of the underlying buffer which holds data.
        """
        ...

    def seek(self, *args) -> Any:
        ...

    def tell(self, *args) -> Any:
        ...


class FileIO(IO):
    """
    This is type of a file open in binary mode, e.g. using ``open(name, "rb")``.
    You should not instantiate this class directly.
    """

    def close(self, *args) -> Any:
        ...

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def readline(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    def flush(self, *args) -> Any:
        ...

    def readlines(self, *args) -> Any:
        ...

    def seek(self, *args) -> Any:
        ...

    def tell(self, *args) -> Any:
        ...


class IOBase:
    """"""


class StringIO(IO):
    """"""

    def close(self, *args) -> Any:
        ...

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def readline(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    def flush(self, *args) -> Any:
        ...

    def getvalue(self, *args) -> Any:
        ...

    def seek(self, *args) -> Any:
        ...

    def tell(self, *args) -> Any:
        ...


class TextIOWrapper(IO):
    """
    This is type of a file open in text mode, e.g. using ``open(name, "rt")``.
    You should not instantiate this class directly.
    """

    def close(self, *args) -> Any:
        ...

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def readline(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    def flush(self, *args) -> Any:
        ...

    def readlines(self, *args) -> Any:
        ...

    def seek(self, *args) -> Any:
        ...

    def tell(self, *args) -> Any:
        ...
