""" """

from __future__ import annotations

from typing import overload
from typing_extensions import deprecated

from vfs import AbstractBlockDev

class Flash(AbstractBlockDev):
    """
    The Flash class allows direct access to the primary flash device on the pyboard.

    In most cases, to store persistent data on the device, you'll want to use a
    higher-level abstraction, for example the filesystem via Python's standard file
    API, but this interface is useful to :ref:`customise the filesystem
    configuration <filesystem>` or implement a low-level storage system for your
    application.
    """
    @deprecated("This constructor is deprecated and will be removed in a future version of MicroPython")
    @overload
    def __init__(self):
        """
        Create and return a block device that represents the flash device presented
        to the USB mass storage interface.

        It includes a virtual partition table at the start, and the actual flash
        starts at block ``0x100``.

        This constructor is deprecated and will be removed in a future version of MicroPython.
        """

    @overload
    def __init__(self, *, start: int = -1, len: int = -1):
        """
        Create and return a block device that accesses the flash at the specified offset. The length defaults to the remaining size of the device.

        The *start* and *len* offsets are in bytes, and must be a multiple of the block size (typically 512 for internal flash).
        """

    @overload
    def readblocks(self, block_num: int, buf: bytearray) -> bool:
        """
        The first form reads aligned, multiples of blocks.
        Starting at the block given by the index *block_num*, read blocks from
        the device into *buf* (an array of bytes).
        The number of blocks to read is given by the length of *buf*,
        which will be a multiple of the block size.
        """

    @overload
    def readblocks(self, block_num: int, buf: bytearray, offset: int) -> bool:
        """
        The second form allows reading at arbitrary locations within a block,
        and arbitrary lengths.
        Starting at block index *block_num*, and byte offset within that block
        of *offset*, read bytes from the device into *buf* (an array of bytes).
        The number of bytes to read is given by the length of *buf*.
        """

    @overload
    def writeblocks(self, block_num: int, buf: bytes | bytearray, /) -> None:
        """
        The first form writes aligned, multiples of blocks, and requires that the
        blocks that are written to be first erased (if necessary) by this method.
        Starting at the block given by the index *block_num*, write blocks from
        *buf* (an array of bytes) to the device.
        The number of blocks to write is given by the length of *buf*,
        which will be a multiple of the block size.
        """

    @overload
    def writeblocks(self, block_num: int, buf: bytes | bytearray, offset: int, /) -> None:
        """
        The second form allows writing at arbitrary locations within a block,
        and arbitrary lengths.  Only the bytes being written should be changed,
        and the caller of this method must ensure that the relevant blocks are
        erased via a prior ``ioctl`` call.
        Starting at block index *block_num*, and byte offset within that block
        of *offset*, write bytes from *buf* (an array of bytes) to the device.
        The number of bytes to write is given by the length of *buf*.

        Note that implementations must never implicitly erase blocks if the offset
        argument is specified, even if it is zero.
        """


    def ioctl(self, op: int, arg: int) -> int | None:
        """
        These methods implement the simple and :ref:`extended
        <block-device-interface>` block protocol defined by
        :class:`vfs.AbstractBlockDev`.
        """

