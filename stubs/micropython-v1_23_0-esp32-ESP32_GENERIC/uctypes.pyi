"""
Module: 'uctypes' on micropython-v1.23.0-esp32-ESP32_GENERIC
"""

# MCU: {'version': '1.23.0', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.23.0', 'cpu': 'ESP32'}
# Stubber: v1.23.0
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

def sizeof(*args, **kwargs) -> Incomplete: ...
def bytes_at(*args, **kwargs) -> Incomplete: ...
def bytearray_at(*args, **kwargs) -> Incomplete: ...
def addressof(*args, **kwargs) -> Incomplete: ...

class struct:
    def __init__(self, *argv, **kwargs) -> None: ...
