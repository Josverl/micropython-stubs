"""
Input/output streams.

MicroPython module: https://docs.micropython.org/en/v1.22.0/library/io.html

CPython module: :mod:`python:io` https://docs.python.org/3/library/io.html .

This module contains additional types of `stream` (file-like) objects
and helper functions.

Conceptual hierarchy
--------------------

Difference to CPython

   Conceptual hierarchy of stream base classes is simplified in MicroPython,
   as described in this section.

(Abstract) base stream classes, which serve as a foundation for behaviour
of all the concrete classes, adhere to few dichotomies (pair-wise
classifications) in CPython. In MicroPython, they are somewhat simplified
and made implicit to achieve higher efficiencies and save resources.

An important dichotomy in CPython is unbuffered vs buffered streams. In
MicroPython, all streams are currently unbuffered. This is because all
modern OSes, and even many RTOSes and filesystem drivers already perform
buffering on their side. Adding another layer of buffering is counter-
productive (an issue known as "bufferbloat") and takes precious memory.
Note that there still cases where buffering may be useful, so we may
introduce optional buffering support at a later time.

But in CPython, another important dichotomy is tied with "bufferedness" -
it's whether a stream may incur short read/writes or not. A short read
is when a user asks e.g. 10 bytes from a stream, but gets less, similarly
for writes. In CPython, unbuffered streams are automatically short
operation susceptible, while buffered are guarantee against them. The
no short read/writes is an important trait, as it allows to develop
more concise and efficient programs - something which is highly desirable
for MicroPython. So, while MicroPython doesn't support buffered streams,
it still provides for no-short-operations streams. Whether there will
be short operations or not depends on each particular class' needs, but
developers are strongly advised to favour no-short-operations behaviour
for the reasons stated above. For example, MicroPython sockets are
guaranteed to avoid short read/writes. Actually, at this time, there is
no example of a short-operations stream class in the core, and one would
be a port-specific class, where such a need is governed by hardware
peculiarities.

The no-short-operations behaviour gets tricky in case of non-blocking
streams, blocking vs non-blocking behaviour being another CPython dichotomy,
fully supported by MicroPython. Non-blocking streams never wait for
data either to arrive or be written - they read/write whatever possible,
or signal lack of data (or ability to write data). Clearly, this conflicts
with "no-short-operations" policy, and indeed, a case of non-blocking
buffered (and this no-short-ops) streams is convoluted in CPython - in
some places, such combination is prohibited, in some it's undefined or
just not documented, in some cases it raises verbose exceptions. The
matter is much simpler in MicroPython: non-blocking stream are important
for efficient asynchronous operations, so this property prevails on
the "no-short-ops" one. So, while blocking streams will avoid short
reads/writes whenever possible (the only case to get a short read is
if end of file is reached, or in case of error (but errors don't
return short data, but raise exceptions)), non-blocking streams may
produce short data to avoid blocking the operation.

The final dichotomy is binary vs text streams. MicroPython of course
supports these, but while in CPython text streams are inherently
buffered, they aren't in MicroPython. (Indeed, that's one of the cases
for which we may introduce buffering support.)

Note that for efficiency, MicroPython doesn't provide abstract base
classes corresponding to the hierarchy above, and it's not possible
to implement, or subclass, a stream class in pure Python.
"""
import abc
import builtins
import codecs
import sys
from _typeshed import Incomplete, FileDescriptorOrPath, ReadableBuffer, WriteableBuffer
from collections.abc import Callable, Iterable, Iterator
from os import _Opener
from types import TracebackType
from typing import IO, Any, BinaryIO, TextIO, TypeVar, overload
from typing_extensions import Literal, Self
from stdlib.io import *

__all__ = [
    "BlockingIOError",
    "open",
    "IOBase",
    "RawIOBase",
    "FileIO",
    "BytesIO",
    "StringIO",
    "BufferedIOBase",
    "BufferedReader",
    "BufferedWriter",
    "BufferedRWPair",
    "BufferedRandom",
    "TextIOBase",
    "TextIOWrapper",
    "UnsupportedOperation",
    "SEEK_SET",
    "SEEK_CUR",
    "SEEK_END",
]

if sys.version_info >= (3, 8):
    __all__ += ["open_code"]

if sys.version_info >= (3, 11):
    __all__ += ["DEFAULT_BUFFER_SIZE", "IncrementalNewlineDecoder", "text_encoding"]

_T = TypeVar("_T")

# DEFAULT_BUFFER_SIZE: Literal[8192]

# SEEK_SET: Literal[0]
# SEEK_CUR: Literal[1]
# SEEK_END: Literal[2]

open = builtins.open

if sys.version_info >= (3, 8):
    def open_code(path: str) -> IO[bytes]: ...

# BlockingIOError = builtins.BlockingIOError

class UnsupportedOperation(OSError, ValueError): ...

class IOBase(metaclass=abc.ABCMeta):
    def __iter__(self) -> Iterator[bytes]: ...
    def __next__(self) -> bytes: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def readable(self) -> bool: ...
    read: Callable[..., Any]
    def readlines(self, __hint: int = -1) -> list[bytes]: ...
    def seek(self, __offset: int, __whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, __size: int | None = ...) -> int: ...
    def writable(self) -> bool: ...
    write: Callable[..., Any]
    def writelines(self, __lines: Iterable[ReadableBuffer]) -> None: ...
    def readline(self, __size: int | None = -1) -> bytes: ...
    def __del__(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    def _checkClosed(self, msg: str | None = ...) -> None: ...  # undocumented

class RawIOBase(IOBase):
    def readall(self) -> bytes: ...
    def readinto(self, __buffer: WriteableBuffer) -> int | None: ...
    def write(self, __b: ReadableBuffer) -> int | None: ...
    def read(self, __size: int = -1) -> bytes | None: ...

class BufferedIOBase(IOBase):
    raw: RawIOBase  # This is not part of the BufferedIOBase API and may not exist on some implementations.
    def detach(self) -> RawIOBase: ...
    def readinto(self, __buffer: WriteableBuffer) -> int: ...
    def write(self, __buffer: ReadableBuffer) -> int: ...
    def readinto1(self, __buffer: WriteableBuffer) -> int: ...
    def read(self, __size: int | None = ...) -> bytes: ...
    def read1(self, __size: int = ...) -> bytes: ...

class FileIO(RawIOBase, BinaryIO):  # type: ignore[misc]  # incompatible definitions of writelines in the base classes
    mode: str
    name: FileDescriptorOrPath
    def __init__(self, file: FileDescriptorOrPath, mode: str = ..., closefd: bool = ..., opener: _Opener | None = ...) -> None: ...
    @property
    def closefd(self) -> bool: ...
    def write(self, __b: ReadableBuffer) -> int: ...
    def read(self, __size: int = -1) -> bytes: ...
    def __enter__(self) -> Self: ...

class BytesIO(IO):  # type: ignore[misc]  # incompatible definitions of methods in the base classes
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

    def __init__(self, initial_bytes: ReadableBuffer = ...) -> None: ...
    # BytesIO does not contain a "name" field. This workaround is necessary
    # to allow BytesIO sub-classes to add this field, as it is defined
    # as a read-only property on IO[].
    name: Any
    def __enter__(self) -> Self: ...
    def getvalue(self) -> bytes:
        """
        Get the current contents of the underlying buffer which holds data.
        """
        ...
    def getbuffer(self) -> memoryview: ...
    def read1(self, __size: int | None = -1) -> bytes: ...

class BufferedReader(BufferedIOBase, BinaryIO):  # type: ignore[misc]  # incompatible definitions of methods in the base classes
    def __enter__(self) -> Self: ...
    def __init__(self, raw: RawIOBase, buffer_size: int = ...) -> None: ...
    def peek(self, __size: int = 0) -> bytes: ...

class BufferedWriter(BufferedIOBase, BinaryIO):  # type: ignore[misc]  # incompatible definitions of writelines in the base classes
    def __enter__(self) -> Self: ...
    def __init__(self, raw: RawIOBase, buffer_size: int = ...) -> None: ...
    def write(self, __buffer: ReadableBuffer) -> int: ...

class BufferedRandom(BufferedReader, BufferedWriter):  # type: ignore[misc]  # incompatible definitions of methods in the base classes
    def __enter__(self) -> Self: ...
    def seek(self, __target: int, __whence: int = 0) -> int: ...  # stubtest needs this

class BufferedRWPair(BufferedIOBase):
    def __init__(self, reader: RawIOBase, writer: RawIOBase, buffer_size: int = ...) -> None: ...
    def peek(self, __size: int = ...) -> bytes: ...

class TextIOBase(IOBase):
    encoding: str
    errors: str | None
    newlines: str | tuple[str, ...] | None
    def __iter__(self) -> Iterator[str]: ...  # type: ignore[override]
    def __next__(self) -> str: ...  # type: ignore[override]
    def detach(self) -> BinaryIO: ...
    def write(self, __s: str) -> int: ...
    def writelines(self, __lines: Iterable[str]) -> None: ...  # type: ignore[override]
    def readline(self, __size: int = ...) -> str: ...  # type: ignore[override]
    def readlines(self, __hint: int = -1) -> list[str]: ...  # type: ignore[override]
    def read(self, __size: int | None = ...) -> str: ...

class TextIOWrapper(TextIOBase, TextIO):  # type: ignore[misc]  # incompatible definitions of write in the base classes
    def __init__(
        self,
        buffer: IO[bytes],
        encoding: str | None = ...,
        errors: str | None = ...,
        newline: str | None = ...,
        line_buffering: bool = ...,
        write_through: bool = ...,
    ) -> None: ...
    @property
    def buffer(self) -> BinaryIO: ...
    @property
    def closed(self) -> bool: ...
    @property
    def line_buffering(self) -> bool: ...
    @property
    def write_through(self) -> bool: ...
    def reconfigure(
        self,
        *,
        encoding: str | None = None,
        errors: str | None = None,
        newline: str | None = None,
        line_buffering: bool | None = None,
        write_through: bool | None = None,
    ) -> None: ...
    # These are inherited from TextIOBase, but must exist in the stub to satisfy mypy.
    def __enter__(self) -> Self: ...
    def __iter__(self) -> Iterator[str]: ...  # type: ignore[override]
    def __next__(self) -> str: ...  # type: ignore[override]
    def writelines(self, __lines: Iterable[str]) -> None: ...  # type: ignore[override]
    def readline(self, __size: int = -1) -> str: ...  # type: ignore[override]
    def readlines(self, __hint: int = -1) -> list[str]: ...  # type: ignore[override]
    def seek(self, __cookie: int, __whence: int = 0) -> int: ...  # stubtest needs this

class StringIO(IO):
    def __init__(self, initial_value: str | None = ..., newline: str | None = ...) -> None: ...
    # StringIO does not contain a "name" field. This workaround is necessary
    # to allow StringIO sub-classes to add this field, as it is defined
    # as a read-only property on IO[].
    name: Any
    def getvalue(self) -> str: ...

class IncrementalNewlineDecoder(codecs.IncrementalDecoder):
    def __init__(self, decoder: codecs.IncrementalDecoder | None, translate: bool, errors: str = ...) -> None: ...
    def decode(self, input: ReadableBuffer | str, final: bool = False) -> str: ...
    @property
    def newlines(self) -> str | tuple[str, ...] | None: ...
    def setstate(self, __state: tuple[bytes, int]) -> None: ...

if sys.version_info >= (3, 10):
    @overload
    def text_encoding(__encoding: None, __stacklevel: int = 2) -> Literal["locale", "utf-8"]: ...
    @overload
    def text_encoding(__encoding: _T, __stacklevel: int = 2) -> _T: ...
