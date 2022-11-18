"""
access binary data in a structured way. See: https://docs.micropython.org/en/v1.19.1/library/uctypes.html

This module implements "foreign data interface" for MicroPython. The idea
behind it is similar to CPython's ``ctypes`` modules, but the actual API is
different, streamlined and optimized for small size. The basic idea of the
module is to define data structure layout with about the same power as the
C language allows, and then access it using familiar dot-syntax to reference
sub-fields.
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp8266', 'port': 'esp8266', 'machine': 'ESP module (1M) with ESP8266', 'release': '1.19.1', 'nodename': 'esp8266', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp8266', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Any

VOID = 0  # type: int
NATIVE = 2  # type: int
PTR = 536870912  # type: int
SHORT = 402653184  # type: int
LONGLONG = 939524096  # type: int
INT8 = 134217728  # type: int
LITTLE_ENDIAN = 0  # type: int
LONG = 671088640  # type: int
UINT = 536870912  # type: int
ULONG = 536870912  # type: int
ULONGLONG = 805306368  # type: int
USHORT = 268435456  # type: int
UINT8 = 0  # type: int
UINT16 = 268435456  # type: int
UINT32 = 536870912  # type: int
UINT64 = 805306368  # type: int
INT64 = 939524096  # type: int
BFUINT16 = -805306368  # type: int
BFUINT32 = -536870912  # type: int
BFUINT8 = -1073741824  # type: int
BFINT8 = -939524096  # type: int
ARRAY = -1073741824  # type: int
BFINT16 = -671088640  # type: int
BFINT32 = -402653184  # type: int
BF_LEN = 22  # type: int
INT = 671088640  # type: int
INT16 = 402653184  # type: int
INT32 = 671088640  # type: int
FLOAT64 = -134217728  # type: int
BF_POS = 17  # type: int
BIG_ENDIAN = 1  # type: int
FLOAT32 = -268435456  # type: int


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

    def __init__(self, addr, descriptor, layout_type=NATIVE, /) -> None:
        ...
