# ------------------
# from typeshed/stdlib/io.pyi

import abc
from _io import (
    BytesIO as BytesIO,
)
from _io import (
    FileIO as FileIO,
)
from _io import (
    IncrementalNewlineDecoder as IncrementalNewlineDecoder,
)
from _io import (
    StringIO as StringIO,
)
from _io import (
    TextIOWrapper as TextIOWrapper,
)
from _io import (
    _BufferedIOBase,
    _IOBase,
    _RawIOBase,
    _TextIOBase,
)
from _io import (
    open as open,
)
from types import TracebackType
from typing import Self, TypeVar

from .pathlike import PathLike
from .buffer_mp import AnyReadableBuf, AnyWritableBuf

# class IOBase_mp(_IOBase, metaclass=abc.ABCMeta): ...
class IOBase_mp(Stream, metaclass=abc.ABCMeta): ...

# Andy
class Stream(metaclass=abc.ABCMeta):
    """
    MicroPython stream "base class". Due to implementation mechanism
    not all methods are guaranteed to be available on all classes
    based on the stream type / protocol.
    """

    def __init__(self, *argv, **kwargs) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    def close(self) -> None: ...
    def flush(self) -> None: ...
    def read(self, __size: int | None = ...) -> bytes: ...
    def read1(self, __size: int = ...) -> bytes: ...
    def readinto(self, __buffer: AnyWritableBuf) -> int: ...
    def readline(self, __size: int | None = ...) -> bytes: ...
    def readlines(self, __hint: int = ...) -> list[bytes]: ...
    def seek(self, __offset: int, __whence: int = ...) -> int: ...
    def tell(self) -> int: ...
    def write(self, __buffer: AnyReadableBuf) -> int: ...
    def write1(self, __buffer: AnyReadableBuf) -> int: ...

# Howard
_OpenFile = TypeVar("_OpenFile", str, bytes, PathLike[str], PathLike[bytes], int)
