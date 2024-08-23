""" """

from __future__ import annotations
from typing import Optional
from _typeshed import Incomplete

class Flash:
    """
    Create and return a block device that represents the flash device presented
    to the USB mass storage interface.

    It includes a virtual partition table at the start, and the actual flash
    starts at block ``0x100``.

    This constructor is deprecated and will be removed in a future version of MicroPython.
    """

    def __init__(self) -> None: ...
    def readblocks(self, block_num, buf, offset: Optional[int] = 0) -> Incomplete: ...
    def writeblocks(self, block_num, buf, offset: Optional[int] = 0) -> Incomplete: ...
    def ioctl(self, cmd, arg) -> Incomplete:
        """
        These methods implement the simple and :ref:`extended
        <block-device-interface>` block protocol defined by
        :class:`vfs.AbstractBlockDev`.
        """
        ...
