from _typeshed import Incomplete, structseq, AnyStr_co
from typing_extensions import TypeAlias, TypeVar, Protocol
from typing import overload
from array import array

# ------------------------------------------------------------------------------------
# TODO: need some to allow string to be passed in : uart_1.write("hello")
AnyReadableBuf: TypeAlias = bytearray | array | memoryview | bytes | Incomplete
AnyWritableBuf: TypeAlias = bytearray | array | memoryview | Incomplete


# ------------------------------------------------------------------------------------
# MicroPython Buffer Protocol
# See: https://github.com/micropython/micropython/pull/17938#discussion_r2329804709
# 
# This protocol defines the extended write method that supports:
# - write(buf) - basic write
# - write(buf, max_len) - write with maximum length
# - write(buf, off, max_len) - write with offset and maximum length


class _WriteStream(Protocol):
    """
    Protocol for MicroPython streams that support the extended write signature
    with optional offset and max_len parameters.
    
    This is commonly used in MicroPython's IO streams, sockets, and serial interfaces.
    """

    @overload
    def write(self, buf: AnyReadableBuf, /) -> int | None:
        """
        Write the buffer of bytes to the stream.
        
        Args:
            buf: Buffer to write
            
        Returns:
            Number of bytes written, or None if non-blocking and would block
        """
        ...

    @overload
    def write(self, buf: AnyReadableBuf, max_len: int, /) -> int | None:
        """
        Write up to max_len bytes from the buffer to the stream.
        
        Args:
            buf: Buffer to write
            max_len: Maximum number of bytes to write
            
        Returns:
            Number of bytes written, or None if non-blocking and would block
        """
        ...

    @overload
    def write(self, buf: AnyReadableBuf, off: int, max_len: int, /) -> int | None:
        """
        Write up to max_len bytes from the buffer starting at offset off to the stream.
        
        Args:
            buf: Buffer to write
            off: Offset into the buffer to start writing from
            max_len: Maximum number of bytes to write
            
        Returns:
            Number of bytes written, or None if non-blocking and would block
        """
        ...
