""" """

from __future__ import annotations
from typing import Optional
from _typeshed import Incomplete

class DiskAccess:
    """
    Gets an object for accessing disk memory of the specific disk.
    For accessing an SD card on the mimxrt1050_evk, ``disk_name`` would be ``SDHC``. See board documentation and
    devicetree for usable disk names for your board (ex. RT boards use style USDHC#).
    """

    def __init__(self, disk_name) -> None: ...
    def readblocks(self, block_num, buf, offset: Optional[int] = 0) -> Incomplete: ...
    def writeblocks(self, block_num, buf, offset: Optional[int] = 0) -> Incomplete: ...
    def ioctl(self, cmd, arg) -> Incomplete:
        """
        These methods implement the simple and extended
        :ref:`block protocol <block-device-interface>` defined by
        :class:`vfs.AbstractBlockDev`.
        """
        ...
