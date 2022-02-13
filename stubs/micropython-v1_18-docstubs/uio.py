"""
input/output streams. See: https://docs.micropython.org/en/v1.18/library/io.html

|see_cpython_module| :mod:`python:io` https://docs.python.org/3/library/io.html .

This module contains additional types of `stream` (file-like) objects
and helper functions.
"""

# source version: v1_18
# origin module:: micropython/docs/library/io.rst
from typing import Any, IO, Optional


class FileIO(IO):
    """
    This is type of a file open in binary mode, e.g. using ``open(name, "rb")``.
    You should not instantiate this class directly.
    """

    def __init__(self, *args) -> None:
        ...


class TextIOWrapper:
    """
    This is type of a file open in text mode, e.g. using ``open(name, "rt")``.
    You should not instantiate this class directly.
    """

    def __init__(self, *args) -> None:
        ...


class StringIO(IO):
    def __init__(self, string: Optional[Any]) -> None:
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

    def __init__(self, string: Optional[Any]) -> None:
        ...

    def getvalue(self) -> Any:
        """
        Get the current contents of the underlying buffer which holds data.
        """
        ...


def open(name, mode="r", **kwargs) -> Any:
    """
    Open a file. Builtin ``open()`` function is aliased to this function.
    All ports (which provide access to file system) are required to support
    *mode* parameter, but support for other arguments vary by port.
    """
    ...
