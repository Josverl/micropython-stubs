""" """

from __future__ import annotations

class DiskAccess:
    """
    Gets an object for accessing disk memory of the specific disk.
    For accessing an SD card on the mimxrt1050_evk, ``disk_name`` would be ``SDHC``. See board documentation and
    devicetree for usable disk names for your board (ex. RT boards use style USDHC#).
    """

    disks: tuple[str, ...]

    def __init__(self, disk_name: str) -> None: ...

    def readblocks(self, block_num: int, buf: bytearray) -> int:
        """
        The first form reads aligned, multiples of blocks.
        Starting at the block given by the index *block_num*, read blocks from
        the device into *buf* (an array of bytes).
        The number of blocks to read is given by the length of *buf*,
        which will be a multiple of the block size.
        """

    def writeblocks(self, block_num: int, buf: bytes | bytearray, /) -> int:
        """
        The first form writes aligned, multiples of blocks, and requires that the
        blocks that are written to be first erased (if necessary) by this method.
        Starting at the block given by the index *block_num*, write blocks from
        *buf* (an array of bytes) to the device.
        The number of blocks to write is given by the length of *buf*,
        which will be a multiple of the block size.
        """

    def ioctl(self, op: int, arg: int) -> int:
        """
        These methods implement the simple and :ref:`extended
        <block-device-interface>` block protocol defined by
        :class:`vfs.AbstractBlockDev`.
        """
