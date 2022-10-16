"""
access binary data in a structured way. See: https://docs.micropython.org/en/v1.19.1/library/uctypes.html

This module implements "foreign data interface" for MicroPython. The idea
behind it is similar to CPython's ``ctypes`` modules, but the actual API is
different, streamlined and optimized for small size. The basic idea of the
module is to define data structure layout with about the same power as the
C language allows, and then access it using familiar dot-syntax to reference
sub-fields.
"""
from typing import Callable, Coroutine, Dict, Generator, IO, Iterator, List, NoReturn, Optional, Tuple, Union, Any

ARRAY: int
BFINT16: int
BFINT32: int
BFINT8: int
BFUINT16: int
BFUINT32: int
BFUINT8: int
BF_LEN: int
BF_POS: int
BIG_ENDIAN: int
FLOAT32: int
FLOAT64: int
INT: int
INT16: int
INT32: int
INT64: int
INT8: int
LITTLE_ENDIAN: int
LONG: int
LONGLONG: int
NATIVE: int
PTR: int
SHORT: int
UINT: int
UINT16: int
UINT32: int
UINT64: int
UINT8: int
ULONG: int
ULONGLONG: int
USHORT: int
VOID: int

def addressof(obj) -> int:
    """
    Return address of an object. Argument should be bytes, bytearray or
    other object supporting buffer protocol (and address of this buffer
    is what actually returned).
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

def bytes_at(addr, size) -> bytes:
    """
    Capture memory at the given address and size as bytes object. As bytes
    object is immutable, memory is actually duplicated and copied into
    bytes object, so if memory contents change later, created object
    retains original value.
    """
    ...

def sizeof(struct, layout_type=NATIVE, /) -> int:
    """
    Return size of data structure in bytes. The *struct* argument can be
    either a structure class or a specific instantiated structure object
    (or its aggregate field).
    """
    ...

class struct:
    """
    Instantiate a "foreign data structure" object based on structure address in
    memory, descriptor (encoded as a dictionary), and layout type (see below).
    """

    def __init__(self, addr, descriptor, layout_type=NATIVE, /) -> None: ...
