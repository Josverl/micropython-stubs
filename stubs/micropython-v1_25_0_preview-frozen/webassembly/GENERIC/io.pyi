from __future__ import annotations
from uio import *
from _mpy_shed import AnyReadableBuf, AnyWritableBuf, FileIO, IOBase_mp, PathLike, TextIOWrapper
from _mpy_shed.io_modes import _OpenBinaryMode, _OpenTextModeWriting
from _typeshed import Incomplete
from array import array
from typing import overload
from typing_extensions import Awaitable, TypeAlias, TypeVar

_T = TypeVar("_T")
AnyStr_co = TypeVar("AnyStr_co", str, bytes, covariant=True)
StrOrBytesPath = TypeVar("StrOrBytesPath", str, bytes, PathLike[str], PathLike[bytes])
_OpenFile = TypeVar("_OpenFile", str, bytes, PathLike[str], PathLike[bytes], int)
AnyReadableBuf = TypeVar("AnyReadableBuf", bytearray, array, memoryview, bytes)
AnyWritableBuf = TypeVar("AnyWritableBuf", bytearray, array, memoryview)
_Self = TypeVar("_Self")

SEEK_SET: int
SEEK_CUR: int
SEEK_END: int

class StringIO:
    @overload
    def __init__(self, string: str = "", /):
        """

        In-memory file-like object for input/output.
        `StringIO` is used for text-mode I/O (similar to a normal file opened with "t" modifier).
        Initial contents can be specified with `string` parameter.

        `alloc_size` constructor creates an empty `StringIO` object,
        pre-allocated to hold up to `alloc_size` number of bytes.
        That means that writing that amount of bytes won't lead to reallocation of the buffer,
        and thus won't hit out-of-memory situation or lead to memory fragmentation.
        This constructor is a MicroPython extension and is recommended for usage only in special
        cases and in system-level libraries, not for end-user applications.

          .. admonition:: Difference to CPython
             :class: attention

             This constructor is a MicroPython extension.
        """

    @overload
    def __init__(self, alloc_size: int, /):
        """

        In-memory file-like object for input/output.
        `StringIO` is used for text-mode I/O (similar to a normal file opened with "t" modifier).
        Initial contents can be specified with `string` parameter.

        `alloc_size` constructor creates an empty `StringIO` object,
        pre-allocated to hold up to `alloc_size` number of bytes.
        That means that writing that amount of bytes won't lead to reallocation of the buffer,
        and thus won't hit out-of-memory situation or lead to memory fragmentation.
        This constructor is a MicroPython extension and is recommended for usage only in special
        cases and in system-level libraries, not for end-user applications.

          .. admonition:: Difference to CPython
             :class: attention

             This constructor is a MicroPython extension.
        """

class BytesIO:
    @overload
    def __init__(self, string: bytes = b"", /):
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


        `alloc_size` constructor creates an empty `BytesIO` object,
        pre-allocated to hold up to `alloc_size` number of bytes.
        That means that writing that amount of bytes won't lead to reallocation of the buffer,
        and thus won't hit out-of-memory situation or lead to memory fragmentation.
        This constructor is a MicroPython extension and is recommended for usage only in special
        cases and in system-level libraries, not for end-user applications.

          .. admonition:: Difference to CPython
             :class: attention

             This constructor is a MicroPython extension.
        """

    @overload
    def __init__(self, alloc_size: int, /):
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


        `alloc_size` constructor creates an empty `BytesIO` object,
        pre-allocated to hold up to `alloc_size` number of bytes.
        That means that writing that amount of bytes won't lead to reallocation of the buffer,
        and thus won't hit out-of-memory situation or lead to memory fragmentation.
        This constructor is a MicroPython extension and is recommended for usage only in special
        cases and in system-level libraries, not for end-user applications.

          .. admonition:: Difference to CPython
             :class: attention

             This constructor is a MicroPython extension.
        """

@overload
def open(name: _OpenFile, /, **kwargs) -> TextIOWrapper:
    """
    Open a file. Builtin ``open()`` function is aliased to this function.
    All ports (which provide access to file system) are required to support
    *mode* parameter, but support for other arguments vary by port.
    """

@overload
def open(name: _OpenFile, mode: _OpenTextModeWriting = ..., /, **kwargs) -> TextIOWrapper:
    """
    Open a file. Builtin ``open()`` function is aliased to this function.
    All ports (which provide access to file system) are required to support
    *mode* parameter, but support for other arguments vary by port.
    """

@overload
def open(name: _OpenFile, mode: _OpenBinaryMode = ..., /, **kwargs) -> FileIO:
    """
    Open a file. Builtin ``open()`` function is aliased to this function.
    All ports (which provide access to file system) are required to support
    *mode* parameter, but support for other arguments vary by port.
    """
