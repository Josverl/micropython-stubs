from typing import Any

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
INT16: int
INT32: int
INT64: int
INT8: int
LITTLE_ENDIAN: int
NATIVE: int
PTR: int
UINT16: int
UINT32: int
UINT64: int
UINT8: int
VOID: int

def addressof(*args) -> Any: ...
def bytearray_at(*args) -> Any: ...
def bytes_at(*args) -> Any: ...
def sizeof(*args) -> Any: ...

class struct: ...
