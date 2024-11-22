"""
MicroPython-stubs base types that are not present in typeshed.

This is a collection of types that are not present in typeshed, but are used in the micropython stubs.

Common cases are:
- MicroPython implementation is different from CPython, so the types are different.
- MicroPython has some types that are not present in CPython.

"""

from __future__ import annotations

import sys
from array import array
from typing import Any, AnyStr, Final, Literal, Protocol, final, overload, runtime_checkable
from typing_extensions import Self

from _typeshed import structseq
from typing_extensions import TypeAlias, TypeVar

# from _collections_abc import _check_methods
import abc

# ------------------
import _io
from .io_modes import (
    _OpenTextModeUpdating,
    _OpenTextModeWriting,
    _OpenTextModeReading,
    _OpenTextMode,
)

class IOBase(_io._IOBase, metaclass=abc.ABCMeta):
    __doc__ = _io._IOBase.__doc__

class RawIOBase(_io._RawIOBase, IOBase):
    __doc__ = _io._RawIOBase.__doc__

class BufferedIOBase(_io._BufferedIOBase, IOBase):
    __doc__ = _io._BufferedIOBase.__doc__

class TextIOBase(_io._TextIOBase, IOBase):
    __doc__ = _io._TextIOBase.__doc__

# Howard
_OpenFile = TypeVar("_OpenFile", str, bytes, PathLike[str], PathLike[bytes], int)

class TextIOWrapper(IOBase):
    """
    Str stream from a file.
    """

    def __init__(self, name: _OpenFile, mode: str = ..., /, **kwargs):
        """
        This is type of a file open in text mode, e.g. using ``open(name, "rt")``.
        You should not instantiate this class directly.
        """

# IO Base alternative from Howard

# @runtime_checkable
# class IOBase_2(Protocol[AnyStr]):
#     """A `Protocol` (structurally typed) for an IOStream."""

#     __slots__ = ()
#     def __enter__(self) -> Self:
#         """
#         Called on entry to a `with` block.
#         The `with` statement will bind this method’s return value to the target(s) specified in the `as` clause
#         of the statement, if any.
#         """

#     def __exit__(
#         self,
#         exc_type: type[BaseException] | None,
#         exc_value: BaseException | None,
#         # traceback: TracebackType | None,
#     ) -> bool | None:
#         """
#         Called on exit of a `with` block.
#         The parameters describe the exception that caused the context to be exited.
#         If the context was exited without an exception, all three arguments will be `None`.

#         If an exception is supplied, and the method wishes to suppress the exception
#         (i.e., prevent it from being propagated), it should return a true value.
#         Otherwise, the exception will be processed normally upon exit from this method.

#         *Note* that `__exit__()` methods should not re-raise the passed-in exception;
#         this is the caller’s responsibility.
#         """

#     def __next__(self) -> AnyStr:
#         """
#         Next string.
#         """

#     def __iter__(self) -> Self:
#         """
#         Start new iteration.
#         """

#     def close(self) -> None:
#         """
#         Flushes the write buffers and closes the IO stream; best not called directly, use a `with` block instead.
#         Calling `f.close()` without using a `with` block might result in content not being completely written to the
#         disk, even if the program exits successfully.
#         A closed file cannot be read or written any more.
#         Any operation which requires that the file be open will raise a `ValueError` after the file has been closed.
#         Calling `f.close()` more than once is allowed.
#         """

#     def flush(self) -> None:
#         """
#         Flushes the write buffers of the IO stream.
#         `flush()` does not necessarily write the file’s data to disk.
#         Use `f.flush()` followed by `os.sync()` to ensure this behavior.

#         This method does nothing for read-only and non-blocking streams.
#         """

#     def read(self, size: int | None = -1) -> AnyStr | None:
#         """
#         Read up to `size` bytes from the object and return them as a `str` (text file) or `bytes` (binary file).
#         As a convenience, if `size` is unspecified or -1, all bytes until EOF are returned.
#         Otherwise, only one system call is ever made.
#         Fewer than `size` bytes may be returned if the operating system call returns fewer than `size` bytes.

#         If 0 bytes are returned, and `size` was not 0, this indicates end of file.
#         If `self` is in non-blocking mode and no bytes are available, `None` is returned.
#         """

#     def readinto(self, b: AnyWritableBuf) -> int | None:
#         """
#         Read bytes into a pre-allocated, writable bytes-like object b, and return the number of bytes read.
#         For example, b might be a bytearray.

#         If `self` is in non-blocking mode and no bytes are available, `None` is returned.
#         """

#     def readline(self, size: int = -1) -> AnyStr:
#         """
#         Read and return, as a `str` (text file) or `bytes` (binary file), one line from the stream.
#         If size is specified, at most size bytes will be read.

#         The line terminator is always ``b''`` for binary files;
#         for text files, the newline argument to `open()` can be used to select the line terminator(s) recognized.
#         """

#     def readlines(self, hint: int | None = -1) -> list[AnyStr]:
#         """
#         Read and return a list of lines, as a `list[str]` (text file) or `list[bytes]` (binary file), from the stream.
#         `hint` can be specified to control the number of lines read:
#         no more lines will be read if the total size (in bytes/characters) of all lines so far exceeds `hint`.

#         `hint` values of 0 or less, as well as `None`, are treated as no hint.
#         The line terminator is always ``b''`` for binary files;
#         for text files, the newline argument to `open()` can be used to select the line terminator(s) recognized.

#         *Note* that it’s already possible to iterate on file objects using `for line in file: ...`
#         without calling `file.readlines()`.
#         """

#     def write(self, b: AnyReadableBuf) -> int | None:
#         """
#         Write the given bytes-like object, `b`, to the underlying raw stream, and return the number of bytes written.
#         This can be less than the length of `b` in bytes, depending on specifics of the underlying raw stream,
#         and especially if it is in non-blocking mode.
#         `None` is returned if the raw stream is set not to block and no single byte could be readily written to it.

#         The caller may release or mutate `b` after this method returns,
#         so the implementation only access `b` during the method call.
#         """

#     def seek(self, offset: int, whence: int = 0) -> int:
#         """
#         Change the stream position to the given byte `offset`.
#         `offset` is interpreted relative to the position indicated by `whence`.
#         The default value for whence is 0.

#         Values for whence are:

#           * 0 – start of the stream (the default); offset should be zero or positive.
#           * 1 – current stream position; offset may be negative.
#           * 2 – end of the stream; offset is usually negative.

#         Returns the new absolute position.
#         """

#     def tell(self) -> int:
#         """
#         Return the current stream position.
#         """

# ------------------
# copied from _typeshed  os.pyi as os.pyi cannot import from a module with the same name
GenericAlias = type(list[int])

class PathLike(abc.ABC):
    """Abstract base class for implementing the file system path protocol."""

    @abc.abstractmethod
    def __fspath__(self):
        """Return the file system path representation of the object."""
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, subclass):
        ...
        # if cls is PathLike:
        #     return _check_methods(subclass, "__fspath__")
        # return NotImplemented
    __class_getitem__ = classmethod(...)

# ------------------------------------------------------------------------------------
AnyReadableBuf: TypeAlias = bytearray | array | memoryview | bytes
AnyWritableBuf: TypeAlias = bytearray | array | memoryview

StrOrBytesPath: TypeAlias = str | bytes | PathLike[str] | PathLike[bytes]

# ------------------------------------------------------------------------------------
_StrOrBytesT = TypeVar("_StrOrBytesT", str, bytes)

# ------------------------------------------------------------------------------------
_AnyPath: TypeAlias = str | bytes | PathLike[str] | PathLike[bytes]
_FdOrAnyPath: TypeAlias = int | _AnyPath

# ------------------------------------------------------------------------------------

# copied from _typeshed  os.pyi as os.pyi cannot import from a module with the same name
@final
class uname_result(structseq[str], tuple[str, str, str, str, str]):
    if sys.version_info >= (3, 8):
        __match_args__: Final = ("sysname", "nodename", "release", "version", "machine")

    @property
    def sysname(self) -> str: ...
    @property
    def nodename(self) -> str: ...
    @property
    def release(self) -> str: ...
    @property
    def version(self) -> str: ...
    @property
    def machine(self) -> str: ...

# ------------------------------------------------------------------------------------

# TODO: improve the typechecking implementation if possible
_OldAbstractReadOnlyBlockDev: TypeAlias = Any
_OldAbstractBlockDev: TypeAlias = Any

@runtime_checkable
class AbstractBlockDev(Protocol):
    """
    Block devices
    -------------

    A block device is an object which implements the block protocol. This enables a
    device to support MicroPython filesystems. The physical hardware is represented
    by a user defined class. The :class:`AbstractBlockDev` class is a template for
    the design of such a class: MicroPython does not actually provide that class,
    but an actual block device class must implement the methods described below.

    A concrete implementation of this class will usually allow access to the
    memory-like functionality of a piece of hardware (like flash memory). A block
    device can be formatted to any supported filesystem and mounted using ``os``
    methods.

    See :ref:`filesystem` for example implementations of block devices using the
    two variants of the block protocol described below.

    .. _block-device-interface:

    Simple and extended interface
    .............................

    There are two compatible signatures for the ``readblocks`` and ``writeblocks``
    methods (see below), in order to support a variety of use cases.  A given block
    device may implement one form or the other, or both at the same time. The second
    form (with the offset parameter) is referred to as the "extended interface".

    Some filesystems (such as littlefs) that require more control over write
    operations, for example writing to sub-block regions without erasing, may require
    that the block device supports the extended interface.
    """

    def __init__(self) -> None:
        """
        Construct a block device object.  The parameters to the constructor are
        dependent on the specific block device.
        """

    @overload
    def readblocks(self, block_num: int, buf: bytearray, /) -> None:
        """
        The first form reads aligned, multiples of blocks.
        Starting at the block given by the index *block_num*, read blocks from
        the device into *buf* (an array of bytes).
        The number of blocks to read is given by the length of *buf*,
        which will be a multiple of the block size.

        The second form allows reading at arbitrary locations within a block,
        and arbitrary lengths.
        Starting at block index *block_num*, and byte offset within that block
        of *offset*, read bytes from the device into *buf* (an array of bytes).
        The number of bytes to read is given by the length of *buf*.
        """

    @overload
    def readblocks(self, block_num: int, buf: bytearray, offset: int, /) -> None:
        """
        The first form reads aligned, multiples of blocks.
        Starting at the block given by the index *block_num*, read blocks from
        the device into *buf* (an array of bytes).
        The number of blocks to read is given by the length of *buf*,
        which will be a multiple of the block size.

        The second form allows reading at arbitrary locations within a block,
        and arbitrary lengths.
        Starting at block index *block_num*, and byte offset within that block
        of *offset*, read bytes from the device into *buf* (an array of bytes).
        The number of bytes to read is given by the length of *buf*.
        """

    @overload
    def writeblocks(self, block_num: int, buf: bytes | bytearray, /) -> None:
        """
        The first form writes aligned, multiples of blocks, and requires that the
        blocks that are written to be first erased (if necessary) by this method.
        Starting at the block given by the index *block_num*, write blocks from
        *buf* (an array of bytes) to the device.
        The number of blocks to write is given by the length of *buf*,
        which will be a multiple of the block size.

        The second form allows writing at arbitrary locations within a block,
        and arbitrary lengths.  Only the bytes being written should be changed,
        and the caller of this method must ensure that the relevant blocks are
        erased via a prior ``ioctl`` call.
        Starting at block index *block_num*, and byte offset within that block
        of *offset*, write bytes from *buf* (an array of bytes) to the device.
        The number of bytes to write is given by the length of *buf*.

        Note that implementations must never implicitly erase blocks if the offset
        argument is specified, even if it is zero.
        """

    @overload
    def writeblocks(self, block_num: int, buf: bytes | bytearray, offset: int, /) -> None:
        """
        The first form writes aligned, multiples of blocks, and requires that the
        blocks that are written to be first erased (if necessary) by this method.
        Starting at the block given by the index *block_num*, write blocks from
        *buf* (an array of bytes) to the device.
        The number of blocks to write is given by the length of *buf*,
        which will be a multiple of the block size.

        The second form allows writing at arbitrary locations within a block,
        and arbitrary lengths.  Only the bytes being written should be changed,
        and the caller of this method must ensure that the relevant blocks are
        erased via a prior ``ioctl`` call.
        Starting at block index *block_num*, and byte offset within that block
        of *offset*, write bytes from *buf* (an array of bytes) to the device.
        The number of bytes to write is given by the length of *buf*.

        Note that implementations must never implicitly erase blocks if the offset
        argument is specified, even if it is zero.
        """

    @overload
    def ioctl(self, op: Literal[4, 5], arg: int) -> int:
        """
        Control the block device and query its parameters.  The operation to
        perform is given by *op* which is one of the following integers:

          - 1 -- initialise the device (*arg* is unused)
          - 2 -- shutdown the device (*arg* is unused)
          - 3 -- sync the device (*arg* is unused)
          - 4 -- get a count of the number of blocks, should return an integer
            (*arg* is unused)
          - 5 -- get the number of bytes in a block, should return an integer,
            or ``None`` in which case the default value of 512 is used
            (*arg* is unused)
          - 6 -- erase a block, *arg* is the block number to erase

        As a minimum ``ioctl(4, ...)`` must be intercepted; for littlefs
        ``ioctl(6, ...)`` must also be intercepted. The need for others is
        hardware dependent.

        Prior to any call to ``writeblocks(block, ...)`` littlefs issues
        ``ioctl(6, block)``. This enables a device driver to erase the block
        prior to a write if the hardware requires it. Alternatively a driver
        might intercept ``ioctl(6, block)`` and return 0 (success). In this case
        the driver assumes responsibility for detecting the need for erasure.

        Unless otherwise stated ``ioctl(op, arg)`` can return ``None``.
        Consequently an implementation can ignore unused values of ``op``. Where
        ``op`` is intercepted, the return value for operations 4 and 5 are as
        detailed above. Other operations should return 0 on success and non-zero
        for failure, with the value returned being an ``OSError`` errno code.
        """

    @overload
    def ioctl(self, op: Literal[1, 2, 3, 6], arg: int) -> int | None:
        """
        Control the block device and query its parameters.  The operation to
        perform is given by *op* which is one of the following integers:

          - 1 -- initialise the device (*arg* is unused)
          - 2 -- shutdown the device (*arg* is unused)
          - 3 -- sync the device (*arg* is unused)
          - 4 -- get a count of the number of blocks, should return an integer
            (*arg* is unused)
          - 5 -- get the number of bytes in a block, should return an integer,
            or ``None`` in which case the default value of 512 is used
            (*arg* is unused)
          - 6 -- erase a block, *arg* is the block number to erase

        As a minimum ``ioctl(4, ...)`` must be intercepted; for littlefs
        ``ioctl(6, ...)`` must also be intercepted. The need for others is
        hardware dependent.

        Prior to any call to ``writeblocks(block, ...)`` littlefs issues
        ``ioctl(6, block)``. This enables a device driver to erase the block
        prior to a write if the hardware requires it. Alternatively a driver
        might intercept ``ioctl(6, block)`` and return 0 (success). In this case
        the driver assumes responsibility for detecting the need for erasure.

        Unless otherwise stated ``ioctl(op, arg)`` can return ``None``.
        Consequently an implementation can ignore unused values of ``op``. Where
        ``op`` is intercepted, the return value for operations 4 and 5 are as
        detailed above. Other operations should return 0 on success and non-zero
        for failure, with the value returned being an ``OSError`` errno code.
        """
