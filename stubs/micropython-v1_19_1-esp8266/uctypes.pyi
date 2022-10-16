from typing import Any

VOID: int
NATIVE: int
PTR: int
SHORT: int
LONGLONG: int
INT8: int
LITTLE_ENDIAN: int
LONG: int
UINT: int
ULONG: int
ULONGLONG: int
USHORT: int
UINT8: int
UINT16: int
UINT32: int
UINT64: int
INT64: int
BFUINT16: int
BFUINT32: int
BFUINT8: int
BFINT8: int
ARRAY: int
BFINT16: int
BFINT32: int
BF_LEN: int
INT: int
INT16: int
INT32: int
FLOAT64: int
BF_POS: int
BIG_ENDIAN: int
FLOAT32: int

def sizeof(*args, **kwargs) -> Any: ...
def bytes_at(*args, **kwargs) -> Any: ...
def bytearray_at(*args, **kwargs) -> Any: ...
def addressof(*args, **kwargs) -> Any: ...

class struct:
    def __init__(self, *argv, **kwargs) -> None: ...
