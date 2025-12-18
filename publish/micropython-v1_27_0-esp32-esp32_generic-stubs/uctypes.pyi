"""
Access binary data in a structured way.

MicroPython module: https://docs.micropython.org/en/v1.27.0/library/uctypes.html

This module implements "foreign data interface" for MicroPython. The idea
behind it is similar to CPython's ``ctypes`` modules, but the actual API is
different, streamlined and optimized for small size. The basic idea of the
module is to define data structure layout with about the same power as the
C language allows, and then access it using familiar dot-syntax to reference
sub-fields.

---
Module: 'uctypes' on micropython-v1.27.0-esp32-ESP32_GENERIC
"""

# MCU: {'variant': '', 'build': '', 'arch': 'xtensawin', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'board_id': 'ESP32_GENERIC', 'mpy': 'v6.3', 'ver': '1.27.0', 'family': 'micropython', 'cpu': 'ESP32', 'version': '1.27.0'}
# Stubber: v1.26.4
from __future__ import annotations
from typing import Dict, Tuple, Any, Final, Generator
from _typeshed import Incomplete
from _mpy_shed import AnyReadableBuf, AnyWritableBuf, mp_available
from typing_extensions import Awaitable, TypeAlias, TypeVar

VOID: Final[int] = 0
"""\
``VOID`` is an alias for ``UINT8``, and is provided to conveniently define
C's void pointers: ``(uctypes.PTR, uctypes.VOID)``.
"""
NATIVE: Final[int] = 2
"""\
Layout type for a native structure - with data endianness and alignment
conforming to the ABI of the system on which MicroPython runs.
"""
PTR: Final[int] = 536870912
"""\
Type constants for pointers and arrays. Note that there is no explicit
constant for structures, it's implicit: an aggregate type without ``PTR``
or ``ARRAY`` flags is a structure.
"""
SHORT: Final[int] = 402653184
LONGLONG: Final[int] = 939524096
INT8: Final[int] = 134217728
"""\
Integer types for structure descriptors. Constants for 8, 16, 32,
and 64 bit types are provided, both signed and unsigned.
"""
LITTLE_ENDIAN: Final[int] = 0
"""\
Layout type for a little-endian packed structure. (Packed means that every
field occupies exactly as many bytes as defined in the descriptor, i.e.
the alignment is 1).
"""
LONG: Final[int] = 671088640
UINT: Final[int] = 536870912
ULONG: Final[int] = 536870912
ULONGLONG: Final[int] = 805306368
USHORT: Final[int] = 268435456
UINT8: Final[int] = 0
"""\
Integer types for structure descriptors. Constants for 8, 16, 32,
and 64 bit types are provided, both signed and unsigned.
"""
UINT16: Final[int] = 268435456
"""\
Integer types for structure descriptors. Constants for 8, 16, 32,
and 64 bit types are provided, both signed and unsigned.
"""
UINT32: Final[int] = 536870912
"""\
Integer types for structure descriptors. Constants for 8, 16, 32,
and 64 bit types are provided, both signed and unsigned.
"""
UINT64: Final[int] = 805306368
"""\
Integer types for structure descriptors. Constants for 8, 16, 32,
and 64 bit types are provided, both signed and unsigned.
"""
INT64: Final[int] = 939524096
"""\
Integer types for structure descriptors. Constants for 8, 16, 32,
and 64 bit types are provided, both signed and unsigned.
"""
BFUINT16: Final[int] = -805306368
BFUINT32: Final[int] = -536870912
BFUINT8: Final[int] = -1073741824
BFINT8: Final[int] = -939524096
ARRAY: Final[int] = -1073741824
"""\
Type constants for pointers and arrays. Note that there is no explicit
constant for structures, it's implicit: an aggregate type without ``PTR``
or ``ARRAY`` flags is a structure.
"""
BFINT16: Final[int] = -671088640
BFINT32: Final[int] = -402653184
BF_LEN: Final[int] = 22
INT: Final[int] = 671088640
INT16: Final[int] = 402653184
"""\
Integer types for structure descriptors. Constants for 8, 16, 32,
and 64 bit types are provided, both signed and unsigned.
"""
INT32: Final[int] = 671088640
"""\
Integer types for structure descriptors. Constants for 8, 16, 32,
and 64 bit types are provided, both signed and unsigned.
"""
FLOAT64: Final[int] = -134217728
"""Floating-point types for structure descriptors."""
BF_POS: Final[int] = 17
BIG_ENDIAN: Final[int] = 1
"""Layout type for a big-endian packed structure."""
FLOAT32: Final[int] = -268435456
"""Floating-point types for structure descriptors."""
_property: TypeAlias = Incomplete
_descriptor: TypeAlias = Tuple | Dict

def sizeof(struct: struct | _descriptor | dict, layout_type: int = NATIVE, /) -> int:
    """
    Return size of data structure in bytes. The *struct* argument can be
    either a structure class or a specific instantiated structure object
    (or its aggregate field).
    """
    ...

def bytes_at(addr: int, size: int, /) -> bytes:
    """
    Capture memory at the given address and size as bytes object. As bytes
    object is immutable, memory is actually duplicated and copied into
    bytes object, so if memory contents change later, created object
    retains original value.
    """
    ...

def bytearray_at(addr: int, size: int, /) -> bytearray:
    """
    Capture memory at the given address and size as bytearray object.
    Unlike bytes_at() function above, memory is captured by reference,
    so it can be both written too, and you will access current value
    at the given memory address.
    """
    ...

def addressof(obj: AnyReadableBuf, /) -> int:
    """
    Return address of an object. Argument should be bytes, bytearray or
    other object supporting buffer protocol (and address of this buffer
    is what actually returned).
    """
    ...

class struct:
    """
    Module contents
    ---------------
    """
    def __init__(self, addr: int | struct, descriptor: _descriptor, layout_type: int = NATIVE, /) -> None:
        """
        Instantiate a "foreign data structure" object based on structure address in
        memory, descriptor (encoded as a dictionary), and layout type (see below).
        """
        ...
    @mp_available()  # force push
    def __getattr__(self, a): ...
