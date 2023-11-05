"""
Module: 'uctypes' on micropython-v1.20.0-esp32-GENERIC
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'esp32', 'board': 'GENERIC', 'cpu': 'ESP32', 'mpy': 'v6.1', 'arch': 'xtensawin'})
# Stubber: v1.13.4
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


def sizeof(*args, **kwargs) -> Any:
    ...


def bytes_at(*args, **kwargs) -> Any:
    ...


def bytearray_at(*args, **kwargs) -> Any:
    ...


def addressof(*args, **kwargs) -> Any:
    ...


class struct:
    def __init__(self, *argv, **kwargs) -> None:
        ...
