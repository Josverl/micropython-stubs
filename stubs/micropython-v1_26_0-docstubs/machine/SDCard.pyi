""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import TypeVar, TypeAlias, Awaitable
from .Pin import Pin
from machine.Pin import Pin, PinLike
from typing import overload
from vfs import AbstractBlockDev

class SDCard(AbstractBlockDev):
    """
    SD cards are one of the most common small form factor removable storage media.
    SD cards come in a variety of sizes and physical form factors. MMC cards are
    similar removable storage devices while eMMC devices are electrically similar
    storage devices designed to be embedded into other systems. All three form
    share a common protocol for communication with their host system and high-level
    support looks the same for them all. As such in MicroPython they are implemented
    in a single class called :class:`machine.SDCard` .

    Both SD and MMC interfaces support being accessed with a variety of bus widths.
    When being accessed with a 1-bit wide interface they can be accessed using the
    SPI protocol. Different MicroPython hardware platforms support different widths
    and pin configurations but for most platforms there is a standard configuration
    for any given hardware. In general constructing an ``SDCard`` object with without
    passing any parameters will initialise the interface to the default card slot
    for the current hardware. The arguments listed below represent the common
    arguments that might need to be set in order to use either a non-standard slot
    or a non-standard pin assignment. The exact subset of arguments supported will
    vary from platform to platform.


    Implementation-specific details
    -------------------------------

    Different implementations of the ``SDCard`` class on different hardware support
    varying subsets of the options above.

    PyBoard
    ```````

    The standard PyBoard has just one slot. No arguments are necessary or supported.

    ESP32
    `````

    The ESP32 provides two channels of SD/MMC hardware and also supports
    access to SD Cards through either of the two SPI ports that are
    generally available to the user. As a result the *slot* argument can
    take a value between 0 and 3, inclusive. Slots 0 and 1 use the
    built-in SD/MMC hardware while slots 2 and 3 use the SPI ports. Slot 0
    supports 1, 4 or 8-bit wide access while slot 1 supports 1 or 4-bit
    access; the SPI slots only support 1-bit access.

      .. note:: Slot 0 is used to communicate with on-board flash memory
                on most ESP32 modules and so will be unavailable to the
                user.

      .. note:: Most ESP32 modules that provide an SD card slot using the
                dedicated hardware only wire up 1 data pin, so the default
                value for *width* is 1.

    The pins used by the dedicated SD/MMC hardware are fixed. The pins
    used by the SPI hardware can be reassigned.

      .. note:: If any of the SPI signals are remapped then all of the SPI
                signals will pass through a GPIO multiplexer unit which
                can limit the performance of high frequency signals. Since
                the normal operating speed for SD cards is 40MHz this can
                cause problems on some cards.

    The default (and preferred) pin assignment are as follows:

        ====== ====== ====== ====== ======
        Slot   0      1      2      3
        ------ ------ ------ ------ ------
        Signal   Pin    Pin    Pin    Pin
        ====== ====== ====== ====== ======
        sck       6     14     18     14
        cmd      11     15
        cs                      5     15
        miso                   19     12
        mosi                   23     13
        D0        7      2
        D1        8      4
        D2        9     12
        D3       10     13
        D4       16
        D5       17
        D6        5
        D7       18
        ====== ====== ====== ====== ======

    cc3200
    ``````

    You can set the pins used for SPI access by passing a tuple as the
    *pins* argument.

    *Note:* The current cc3200 SD card implementation names the this class
    :class:`machine.SD` rather than :class:`machine.SDCard` .
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
