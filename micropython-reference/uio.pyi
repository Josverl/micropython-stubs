# io module
# Allow the use of micro-module notation

from array import array
from io import *  # type: ignore
from typing import TypeVar

from _mpy_shed import PathLike

_T = TypeVar("_T")
AnyStr_co = TypeVar("AnyStr_co", str, bytes, covariant=True)
StrOrBytesPath = TypeVar("StrOrBytesPath", str, bytes, PathLike[str], PathLike[bytes])
_OpenFile = TypeVar("_OpenFile", str, bytes, PathLike[str], PathLike[bytes], int)
AnyReadableBuf = TypeVar("AnyReadableBuf", bytearray, array, memoryview, bytes)
AnyWritableBuf = TypeVar("AnyWritableBuf", bytearray, array, memoryview)
_Self = TypeVar("_Self")
