# MCU: {'build': '', 'ver': '1.23.0', 'version': '1.23.0', 'port': 'rp2', 'board': 'RPI_PICO', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.23.0
# MCU: {'build': '', 'ver': '1.23.0', 'version': '1.23.0', 'port': 'rp2', 'board': 'RPI_PICO', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.23.0
""" """

from __future__ import annotations

from typing import Optional

from _mpy_shed import AbstractBlockDev
from _rp2.DMA import DMA
from _rp2.Flash import Flash
from _rp2.PIO import PIO
from _rp2.PIOASMEmit import PIOASMEmit
from _rp2.StateMachine import StateMachine
from _typeshed import Incomplete
from machine import Pin
from typing_extensions import TypeAlias

_PIO_ASM_Program: TypeAlias = Incomplete

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
