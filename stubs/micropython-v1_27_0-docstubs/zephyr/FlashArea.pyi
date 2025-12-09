""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing import overload
from typing_extensions import TypeVar, TypeAlias, Awaitable

class FlashArea:
    """
    Gets an object for accessing flash memory at partition specified by ``id`` and with block size of ``block_size``.

    ``id`` values are integers correlating to fixed flash partitions defined in the devicetree.
    A commonly used partition is the designated flash storage area defined as ``FlashArea.STORAGE`` if
    ``FLASH_AREA_LABEL_EXISTS(storage)`` returns true at boot.
    Zephyr devicetree fixed flash partitions are ``boot_partition``, ``slot0_partition``, ``slot1_partition``, and
    ``scratch_partition``. Because MCUBoot is not enabled by default for MicroPython, these fixed partitions can be accessed by
    ID integer values 1, 2, 3, and 4, respectively.
    """
    def __init__(self, id, block_size) -> None: ...
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
        These methods implement the simple and extended
        :ref:`block protocol <block-device-interface>` defined by
        :class:`vfs.AbstractBlockDev`.
        """
        ...
