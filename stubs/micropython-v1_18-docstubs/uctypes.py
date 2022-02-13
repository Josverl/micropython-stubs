"""
access binary data in a structured way. See: https://docs.micropython.org/en/v1.18/library/uctypes.html

This module implements "foreign data interface" for MicroPython. The idea
behind it is similar to CPython's ``ctypes`` modules, but the actual API is
different, streamlined and optimized for small size. The basic idea of the
module is to define data structure layout with about the same power as the
C language allows, and then access it using familiar dot-syntax to reference
sub-fields.
"""

# source version: v1_18
# origin module:: micropython/docs/library/uctypes.rst
from typing import Any

#    Layout type for a little-endian packed structure. (Packed means that every
#    field occupies exactly as many bytes as defined in the descriptor, i.e.
#    the alignment is 1).
LITTLE_ENDIAN: bytes
#    Layout type for a big-endian packed structure.
BIG_ENDIAN: Any = ...
#    Layout type for a native structure - with data endianness and alignment
#    conforming to the ABI of the system on which MicroPython runs.
NATIVE: Any = ...
#    Integer types for structure descriptors. Constants for 8, 16, 32,
#    and 64 bit types are provided, both signed and unsigned.
UINT8: int = 1
#    Integer types for structure descriptors. Constants for 8, 16, 32,
#    and 64 bit types are provided, both signed and unsigned.
INT8: int = 1
#    Integer types for structure descriptors. Constants for 8, 16, 32,
#    and 64 bit types are provided, both signed and unsigned.
UINT16: int = 1
#    Integer types for structure descriptors. Constants for 8, 16, 32,
#    and 64 bit types are provided, both signed and unsigned.
INT16: int = 1
#    Integer types for structure descriptors. Constants for 8, 16, 32,
#    and 64 bit types are provided, both signed and unsigned.
UINT32: int = 1
#    Integer types for structure descriptors. Constants for 8, 16, 32,
#    and 64 bit types are provided, both signed and unsigned.
INT32: int = 1
#    Integer types for structure descriptors. Constants for 8, 16, 32,
#    and 64 bit types are provided, both signed and unsigned.
UINT64: int = 1
#    Integer types for structure descriptors. Constants for 8, 16, 32,
#    and 64 bit types are provided, both signed and unsigned.
INT64: int = 1
#    Floating-point types for structure descriptors.
FLOAT32: Any = ...
#    Floating-point types for structure descriptors.
FLOAT64: Any = ...
#    ``VOID`` is an alias for ``UINT8``, and is provided to conveniently define
#    C's void pointers: ``(uctypes.PTR, uctypes.VOID)``.
VOID: Any = ...
#    Type constants for pointers and arrays. Note that there is no explicit
#    constant for structures, it's implicit: an aggregate type without ``PTR``
#    or ``ARRAY`` flags is a structure.
PTR: Any = ...
#    Type constants for pointers and arrays. Note that there is no explicit
#    constant for structures, it's implicit: an aggregate type without ``PTR``
#    or ``ARRAY`` flags is a structure.
ARRAY: Any = ...


class struct:
    """
    Instantiate a "foreign data structure" object based on structure address in
    memory, descriptor (encoded as a dictionary), and layout type (see below).
    """

    def __init__(self, addr, descriptor, layout_type=NATIVE, /) -> None:
        ...


def sizeof(struct, layout_type=NATIVE, /) -> int:
    """
    Return size of data structure in bytes. The *struct* argument can be
    either a structure class or a specific instantiated structure object
    (or its aggregate field).
    """
    ...


def addressof(obj) -> int:
    """
    Return address of an object. Argument should be bytes, bytearray or
    other object supporting buffer protocol (and address of this buffer
    is what actually returned).
    """
    ...


def bytes_at(addr, size) -> bytes:
    """
    Capture memory at the given address and size as bytes object. As bytes
    object is immutable, memory is actually duplicated and copied into
    bytes object, so if memory contents change later, created object
    retains original value.
    """
    ...


def bytearray_at(addr, size) -> bytearray:
    """
    Capture memory at the given address and size as bytearray object.
    Unlike bytes_at() function above, memory is captured by reference,
    so it can be both written too, and you will access current value
    at the given memory address.
    """
    ...
