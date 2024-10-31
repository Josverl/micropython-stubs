""" """

from __future__ import annotations
from typing import Optional
from _typeshed import Incomplete

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
    def readblocks(self, block_num, buf, offset: Optional[int] = 0) -> Incomplete: ...
    def writeblocks(self, block_num, buf, offset: Optional[int] = 0) -> Incomplete: ...
    def ioctl(self, cmd, arg) -> Incomplete:
        """
        These methods implement the simple and extended
        :ref:`block protocol <block-device-interface>` defined by
        :class:`vfs.AbstractBlockDev`.
        """
        ...
