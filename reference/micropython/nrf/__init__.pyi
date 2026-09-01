"""nRF-specific functions and access to internal flash storage."""

# MCU: {'variant': '', 'build': '', 'arch': 'armv7emsp', 'port': 'nrf', 'board': 'SEEED_XIAO_NRF52', 'board_id': 'SEEED_XIAO_NRF52', 'mpy': 'v6.3', 'ver': '1.29.0', 'family': 'micropython', 'cpu': 'NRF52840', 'version': '1.29.0'}
# Stubber: v1.28.6
from __future__ import annotations

from typing import overload

from _mpy_shed import AnyReadableBuf, AnyWritableBuf

def unused_flash_start() -> int:
    """Return the first page-aligned address in the unused flash region."""
    ...

def unused_flash_length() -> int:
    """Return the page-aligned size, in bytes, of the unused flash region."""
    ...

@overload
def dcdc() -> bool:
    """Return whether the on-chip DC/DC converter is enabled."""
    ...

@overload
def dcdc(state: object, /) -> bool:
    """Enable or disable the on-chip DC/DC converter and return its resulting state."""
    ...

class Flash:
    """Access a page-aligned region of internal flash using the block-device protocol."""

    def __init__(self, *, start: int = -1, len: int = -1) -> None:
        """
        Return the default internal-flash block device, or create one for the
        page-aligned region described by *start* and *len*.
        """
        ...

    @overload
    def readblocks(self, block_num: int, buf: AnyWritableBuf, /) -> int:
        """Read one or more whole flash blocks into *buf* and return zero."""
        ...

    @overload
    def readblocks(self, block_num: int, buf: AnyWritableBuf, offset: int, /) -> int:
        """Read bytes starting at *offset* within *block_num* into *buf* and return zero."""
        ...

    @overload
    def writeblocks(self, block_num: int, buf: AnyReadableBuf, /) -> int:
        """Erase and write one or more whole flash blocks from *buf*, returning zero."""
        ...

    @overload
    def writeblocks(self, block_num: int, buf: AnyReadableBuf, offset: int, /) -> int:
        """Write *buf* at *offset* within *block_num* without implicitly erasing it."""
        ...

    def ioctl(self, op: int, arg: int, /) -> int | None:
        """
        Perform a block-device control operation.

        Operations 1, 2 and 3 return zero; 4 and 5 return the block count and
        block size; 6 erases the block given by *arg*. Unsupported operations
        return ``None``.
        """
        ...