"""
Module: 'uctypes' on micropython-v1.24.1-esp8266-ESP8266_GENERIC
"""

# MCU: {'variant': '', 'build': '', 'arch': 'xtensa', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'board_id': 'ESP8266_GENERIC', 'mpy': 'v6.3', 'ver': '1.24.1', 'family': 'micropython', 'cpu': 'ESP8266', 'version': '1.24.1'}
# Stubber: v1.25.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

VOID: Final[int] = 0
NATIVE: Final[int] = 2
PTR: Final[int] = 536870912
SHORT: Final[int] = 402653184
LONGLONG: Final[int] = 939524096
INT8: Final[int] = 134217728
LITTLE_ENDIAN: Final[int] = 0
LONG: Final[int] = 671088640
UINT: Final[int] = 536870912
ULONG: Final[int] = 536870912
ULONGLONG: Final[int] = 805306368
USHORT: Final[int] = 268435456
UINT8: Final[int] = 0
UINT16: Final[int] = 268435456
UINT32: Final[int] = 536870912
UINT64: Final[int] = 805306368
INT64: Final[int] = 939524096
BFUINT16: Final[int] = -805306368
BFUINT32: Final[int] = -536870912
BFUINT8: Final[int] = -1073741824
BFINT8: Final[int] = -939524096
ARRAY: Final[int] = -1073741824
BFINT16: Final[int] = -671088640
BFINT32: Final[int] = -402653184
BF_LEN: Final[int] = 22
INT: Final[int] = 671088640
INT16: Final[int] = 402653184
INT32: Final[int] = 671088640
FLOAT64: Final[int] = -134217728
BF_POS: Final[int] = 17
BIG_ENDIAN: Final[int] = 1
FLOAT32: Final[int] = -268435456

def sizeof(*args, **kwargs) -> Incomplete: ...
def bytes_at(*args, **kwargs) -> Incomplete: ...
def bytearray_at(*args, **kwargs) -> Incomplete: ...
def addressof(*args, **kwargs) -> Incomplete: ...

class struct:
    def __init__(self, *argv, **kwargs) -> None: ...
