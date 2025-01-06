""" """

from __future__ import annotations

from array import array
from typing import overload

from _mpy_shed import AbstractBlockDev
from Accel import *
from ADC import *
from CAN import *
from DAC import *
from ExtInt import *
from Flash import *
from I2C import *
from LCD import *
from LED import *
from Pin import *
from RTC import *
from Servo import *
from SPI import *
from Switch import *
from Timer import *
from UART import *
from USB_HID import *
from USB_VCP import *

class Flash(AbstractBlockDev):
    """
    The Flash class allows direct access to the primary flash device on the pyboard.

    In most cases, to store persistent data on the device, you'll want to use a
    higher-level abstraction, for example the filesystem via Python's standard file
    API, but this interface is useful to :ref:`customise the filesystem
    configuration <filesystem>` or implement a low-level storage system for your
    application.
    """

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

    def readblocks(self, blocknum: int, buf: bytes, offset: int = 0, /) -> None:
        """
        These methods implement the simple and :ref:`extended
        <block-device-interface>` block protocol defined by
        :class:`os.AbstractBlockDev`.
        """

    def writeblocks(self, blocknum: int, buf: bytes, offset: int = 0, /) -> None:
        """
        These methods implement the simple and :ref:`extended
        <block-device-interface>` block protocol defined by
        :class:`os.AbstractBlockDev`.
        """

    def ioctl(self, op: int, arg: int) -> int | None:
        """
        These methods implement the simple and :ref:`extended
        <block-device-interface>` block protocol defined by
        :class:`vfs.AbstractBlockDev`.
        """
        ...
