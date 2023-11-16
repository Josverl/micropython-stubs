from _typeshed import Incomplete as Incomplete

LITTLE_ENDIAN: bytes
BIG_ENDIAN: Incomplete
NATIVE: Incomplete
UINT8: int
INT8: int
UINT16: int
INT16: int
UINT32: int
INT32: int
UINT64: int
INT64: int
FLOAT32: Incomplete
FLOAT64: Incomplete
VOID: Incomplete
PTR: Incomplete
ARRAY: Incomplete

class struct:
    """
    Instantiate a "foreign data structure" object based on structure address in
    memory, descriptor (encoded as a dictionary), and layout type (see below).
    """

    def __init__(self, addr, descriptor, layout_type=...) -> None: ...

def sizeof(struct, layout_type=...) -> int:
    """
    Return size of data structure in bytes. The *struct* argument can be
    either a structure class or a specific instantiated structure object
    (or its aggregate field).
    """

def addressof(obj) -> int:
    """
    Return address of an object. Argument should be bytes, bytearray or
    other object supporting buffer protocol (and address of this buffer
    is what actually returned).
    """

def bytes_at(addr, size) -> bytes:
    """
    Capture memory at the given address and size as bytes object. As bytes
    object is immutable, memory is actually duplicated and copied into
    bytes object, so if memory contents change later, created object
    retains original value.
    """

def bytearray_at(addr, size) -> bytearray:
    """
    Capture memory at the given address and size as bytearray object.
    Unlike bytes_at() function above, memory is captured by reference,
    so it can be both written too, and you will access current value
    at the given memory address.
    """
