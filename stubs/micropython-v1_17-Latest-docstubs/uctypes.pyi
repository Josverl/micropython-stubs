from typing import Any

LITTLE_ENDIAN: bytes
BIG_ENDIAN: Any
NATIVE: Any
UINT8: int
INT8: int
UINT16: int
INT16: int
UINT32: int
INT32: int
UINT64: int
INT64: int
FLOAT32: Any
FLOAT64: Any
VOID: Any
PTR: Any
ARRAY: Any

class struct:
    def __init__(self, addr, descriptor, layout_type=...) -> None: ...

def sizeof(struct, layout_type=...) -> int: ...
def addressof(obj) -> int: ...
def bytes_at(addr, size) -> bytes: ...
def bytearray_at(addr, size) -> bytearray: ...
