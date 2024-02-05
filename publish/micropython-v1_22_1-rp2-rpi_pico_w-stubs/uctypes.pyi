"""
Access binary data in a structured way.

MicroPython module: https://docs.micropython.org/en/v1.22.1/library/uctypes.html

This module implements "foreign data interface" for MicroPython. The idea
behind it is similar to CPython's ``ctypes`` modules, but the actual API is
different, streamlined and optimized for small size. The basic idea of the
module is to define data structure layout with about the same power as the
C language allows, and then access it using familiar dot-syntax to reference
sub-fields.

---
Module: 'uctypes' on micropython-v1.22.1-rp2-RPI_PICO_W
"""
# MCU: {'family': 'micropython', 'version': '1.22.1', 'build': '', 'ver': '1.22.1', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.17.1
from __future__ import annotations
from _typeshed import Incomplete

VOID: int = 0
NATIVE: int = 2
PTR: int = 536870912
SHORT: int = 402653184
LONGLONG: int = 939524096
INT8: int = 134217728
LITTLE_ENDIAN: int = 0
LONG: int = 671088640
UINT: int = 536870912
ULONG: int = 536870912
ULONGLONG: int = 805306368
USHORT: int = 268435456
UINT8: int = 0
UINT16: int = 268435456
UINT32: int = 536870912
UINT64: int = 805306368
INT64: int = 939524096
BFUINT16: int = -805306368
BFUINT32: int = -536870912
BFUINT8: int = -1073741824
BFINT8: int = -939524096
ARRAY: int = -1073741824
BFINT16: int = -671088640
BFINT32: int = -402653184
BF_LEN: int = 22
INT: int = 671088640
INT16: int = 402653184
INT32: int = 671088640
FLOAT64: int = -134217728
BF_POS: int = 17
BIG_ENDIAN: int = 1
FLOAT32: int = -268435456

def sizeof(struct, layout_type=NATIVE, /) -> int:
    """
    Return size of data structure in bytes. The *struct* argument can be
    either a structure class or a specific instantiated structure object
    (or its aggregate field).
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

def addressof(obj) -> int:
    """
    Return address of an object. Argument should be bytes, bytearray or
    other object supporting buffer protocol (and address of this buffer
    is what actually returned).
    """
    ...

class struct:
    """
    Instantiate a "foreign data structure" object based on structure address in
    memory, descriptor (encoded as a dictionary), and layout type (see below).
    """

    def __init__(self, *argv, **kwargs) -> None: ...
