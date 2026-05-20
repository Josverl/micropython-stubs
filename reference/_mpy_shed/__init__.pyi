"""
MicroPython-stubs base types that are not present in typeshed.

This is a collection of types that are not present in typeshed, but are used in the micropython stubs.

Common cases are:
- MicroPython implementation is different from CPython, so the types are different.
- MicroPython has some types that are not present in CPython.

"""

from __future__ import annotations

import abc  # mypy: ignore # not collections.abc
import sys
from typing import Final, final

from _typeshed import AnyStr_co, Incomplete, structseq
from typing_extensions import TypeAlias, TypeVar

from .blockdevice import _BlockDeviceProtocol as _BlockDeviceProtocol
from .blockdevice import _OldAbstractBlockDev, _OldAbstractReadOnlyBlockDev
from .buffer_mp import AnyReadableBuf as AnyReadableBuf
from .buffer_mp import AnyWritableBuf as AnyWritableBuf
from .io_mp import BytesIO as BytesIO
from .io_mp import FileIO as FileIO
from .io_mp import IncrementalNewlineDecoder as IncrementalNewlineDecoder
from .io_mp import IOBase_mp as IOBase_mp
from .io_mp import StringIO as StringIO
from .io_mp import TextIOWrapper as TextIOWrapper
from .io_mp import _BufferedIOBase as _BufferedIOBase
from .io_mp import _IOBase as _IOBase
from .io_mp import _RawIOBase as _RawIOBase
from .io_mp import _TextIOBase as _TextIOBase
from .io_mp import open as open
from .IRQs import _IRQ
from .neopixelbase import _NeoPixelBase as _NeoPixelBase
from .blockdevice import (
    _BlockDeviceProtocol as _BlockDeviceProtocol,
    _OldAbstractBlockDev,
    _OldAbstractReadOnlyBlockDev,
)
from .buffer_mp import (
    AnyReadableBuf as AnyReadableBuf,
    AnyWritableBuf as AnyWritableBuf,
    _WriteStream as _WriteStream,
)

from .io_mp import (
    BytesIO as BytesIO,
    FileIO as FileIO,
    IncrementalNewlineDecoder as IncrementalNewlineDecoder,
    StringIO as StringIO,
    TextIOWrapper as TextIOWrapper,
    IOBase_mp as IOBase_mp,
    _BufferedIOBase,
    _IOBase,
    _RawIOBase,
    _TextIOBase,
    open as open,
)

from .time_mp import _TimeTuple as _TimeTuple
from .pathlike import PathLike as PathLike

from .mp_implementation import _mp_implementation as _mp_implementation
from .mp_available import mp_available as mp_available
from .mp_implementation import _mp_implementation as _mp_implementation
from .neopixelbase import _NeoPixelBase as _NeoPixelBase
from .pathlike import PathLike as PathLike
from .subscriptable import Subscriptable as Subscriptable
from .time_mp import _TimeTuple as _TimeTuple

# ------------------
# copied from _typeshed  os.pyi as os.pyi cannot import from a module with the same name
GenericAlias = type(list[int])

# ------------------------------------------------------------------------------------
StrOrBytesPath: TypeAlias = str | bytes | PathLike[str] | PathLike[bytes]
_StrOrBytesT = TypeVar("_StrOrBytesT", str, bytes)

# ------------------------------------------------------------------------------------
_AnyPath: TypeAlias = str | bytes | PathLike[str] | PathLike[bytes]
_FdOrAnyPath: TypeAlias = int | _AnyPath

# ------------------------------------------------------------------------------------
# HID_Tuple is used in multiple pyb.submodules
HID_Tuple: TypeAlias = tuple[int, int, int, int, bytes]

#  ------------------------------------------------------------------------------------
# copied from _typeshed  os.pyi as os.pyi cannot import from a module with the same nam@final
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
from .mp_mem import _MemoryObject as _MemoryObject

# ------------------------------------------------------------------------------------

###########################
# HashLib

# manual addition to hashlib.pyi

class _Hash(abc.ABC):
    """
    Abstract base class for hashing algorithms that defines methods available in all algorithms.
    """

    def update(self, data: AnyReadableBuf, /) -> None:
        """
        Feed more binary data into hash.
        """

    def digest(self) -> bytes:
        """
        Return hash for all data passed through hash, as a bytes object. After this
        method is called, more data cannot be fed into the hash any longer.
        """

    def hexdigest(self) -> str:
        """
        This method is NOT implemented. Use ``binascii.hexlify(hash.digest())``
        to achieve a similar effect.
        """


__all__ = [
    # defined in this module
    "GenericAlias",
    "StrOrBytesPath",
    "_StrOrBytesT",
    "_AnyPath",
    "_FdOrAnyPath",
    "HID_Tuple",
    "uname_result",
    "_Hash",
    # re-exported from .blockdevice
    "_BlockDeviceProtocol",
    "_OldAbstractBlockDev",
    "_OldAbstractReadOnlyBlockDev",
    # re-exported from .buffer_mp
    "AnyReadableBuf",
    "AnyWritableBuf",
    # re-exported from .io_mp
    "BytesIO",
    "FileIO",
    "IncrementalNewlineDecoder",
    "IOBase_mp",
    "StringIO",
    "TextIOWrapper",
    "_BufferedIOBase",
    "_IOBase",
    "_RawIOBase",
    "_TextIOBase",
    "open",
    # re-exported from .IRQs
    "_IRQ",
    # re-exported from .mp_available
    "mp_available",
    # re-exported from .mp_implementation
    "_mp_implementation",
    # re-exported from .neopixelbase
    "_NeoPixelBase",
    # re-exported from .pathlike
    "PathLike",
    # re-exported from .subscriptable
    "Subscriptable",
    # re-exported from .time_mp
    "_TimeTuple",
    # re-exported from .mp_mem
    "_MemoryObject",
]
