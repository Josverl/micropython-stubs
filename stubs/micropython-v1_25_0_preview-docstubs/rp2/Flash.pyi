""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing import Optional
from typing_extensions import TypeVar, TypeAlias, Awaitable
from vfs import AbstractBlockDev
from rp2 import bootsel_button
from rp2.DMA import DMA
from rp2.PIO import PIO
from rp2.PIOASMEmit import PIOASMEmit
from rp2.StateMachine import StateMachine

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
