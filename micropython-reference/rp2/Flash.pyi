"""
Module: '_rp2.Flash'
"""

from typing import Optional

from _typeshed import Incomplete
from vfs import AbstractBlockDev  # type: ignore

class Flash(AbstractBlockDev):
    """
    Gets the singleton object for accessing the SPI flash memory.
    """

    def __init__(self) -> None: ...
    def readblocks(self, block_num, buf, offset: Optional[int] = 0) -> Incomplete: ...
    def writeblocks(self, block_num, buf, offset: Optional[int] = 0) -> Incomplete: ...
    def ioctl(self, cmd, arg) -> Incomplete:
        """
        These methods implement the simple and extended
        :ref:`block protocol <block-device-interface>` defined by
        :class:`vfs.AbstractBlockDev`.
        """
        ...
