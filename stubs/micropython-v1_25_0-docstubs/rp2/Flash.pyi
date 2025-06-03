""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing import Optional
from typing_extensions import TypeVar, TypeAlias, Awaitable

class Flash:
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
