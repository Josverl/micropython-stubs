"""
Virtual filesystem control.

MicroPython module: https://docs.micropython.org/en/v1.25.0/library/vfs.html

The ``vfs`` module contains functions for creating filesystem objects and
mounting/unmounting them in the Virtual Filesystem.

Filesystem mounting
-------------------

Some ports provide a Virtual Filesystem (VFS) and the ability to mount multiple
"real" filesystems within this VFS.  Filesystem objects can be mounted at either
the root of the VFS, or at a subdirectory that lives in the root.  This allows
dynamic and flexible configuration of the filesystem that is seen by Python
programs.  Ports that have this functionality provide the :func:`mount` and
:func:`umount` functions, and possibly various filesystem implementations
represented by VFS classes.

---
Module: 'vfs' on micropython-v1.25.0-windows-standard
"""

# MCU: {'family': 'micropython', 'version': '1.25.0', 'build': '', 'ver': '1.25.0', 'port': 'windows', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'win32 [GCC 12.0.0] version', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
from __future__ import annotations
from typing import List, overload, Any, Final, Generator
from _typeshed import Incomplete
from _mpy_shed import _BlockDeviceProtocol
from abc import ABC, abstractmethod
from typing_extensions import Awaitable, TypeAlias, TypeVar

@overload
def mount(fsobj, mount_point: str, *, readonly: bool = False) -> None:
    """
    :noindex:

    With no arguments to :func:`mount`, return a list of tuples representing
    all active mountpoints.

    The returned list has the form *[(fsobj, mount_point), ...]*.
    """
    ...

@overload
def mount() -> List[tuple[Incomplete, str]]:
    """
    :noindex:

    With no arguments to :func:`mount`, return a list of tuples representing
    all active mountpoints.

    The returned list has the form *[(fsobj, mount_point), ...]*.
    """
    ...

def umount(mount_point: Incomplete) -> Incomplete:
    """
    Unmount a filesystem. *mount_point* can be a string naming the mount location,
    or a previously-mounted filesystem object.  During the unmount process the
    method ``umount()`` is called on the filesystem object.

    Will raise ``OSError(EINVAL)`` if *mount_point* is not found.
    """
    ...

class VfsPosix:
    """
    Create a filesystem object that accesses the host POSIX filesystem.
    If *root* is specified then it should be a path in the host filesystem to use
    as the root of the ``VfsPosix`` object.  Otherwise the current directory of
    the host filesystem is used.
    """
    def rename(self, *args, **kwargs) -> Incomplete: ...
    def mount(self, *args, **kwargs) -> Incomplete: ...
    def mkdir(self, *args, **kwargs) -> Incomplete: ...
    def rmdir(self, *args, **kwargs) -> Incomplete: ...
    def stat(self, *args, **kwargs) -> Incomplete: ...
    def umount(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def open(self, *args, **kwargs) -> Incomplete: ...
    def ilistdir(self, *args, **kwargs) -> Incomplete: ...
    def chdir(self, *args, **kwargs) -> Incomplete: ...
    def getcwd(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, root: str | None = None) -> None: ...

class AbstractBlockDev:
    #
    @abstractmethod
    @overload
    def readblocks(self, block_num: int, buf: bytearray) -> bool: ...
    @abstractmethod
    @overload
    def readblocks(self, block_num: int, buf: bytearray, offset: int) -> bool:
        """
        The first form reads aligned, multiples of blocks.
        Starting at the block given by the index *block_num*, read blocks from
        the device into *buf* (an array of bytes).
        The number of blocks to read is given by the length of *buf*,
        which will be a multiple of the block size.

        The second form allows reading at arbitrary locations within a block,
        and arbitrary lengths.
        Starting at block index *block_num*, and byte offset within that block
        of *offset*, read bytes from the device into *buf* (an array of bytes).
        The number of bytes to read is given by the length of *buf*.
        """
        ...

    @abstractmethod
    @overload
    def writeblocks(self, block_num: int, buf: bytes | bytearray, /) -> None:
        """
        The first form writes aligned, multiples of blocks, and requires that the
        blocks that are written to be first erased (if necessary) by this method.
        Starting at the block given by the index *block_num*, write blocks from
        *buf* (an array of bytes) to the device.
        The number of blocks to write is given by the length of *buf*,
        which will be a multiple of the block size.

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

    @abstractmethod
    @overload
    def writeblocks(self, block_num: int, buf: bytes | bytearray, offset: int, /) -> None:
        """
        The first form writes aligned, multiples of blocks, and requires that the
        blocks that are written to be first erased (if necessary) by this method.
        Starting at the block given by the index *block_num*, write blocks from
        *buf* (an array of bytes) to the device.
        The number of blocks to write is given by the length of *buf*,
        which will be a multiple of the block size.

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
        ...

    @abstractmethod
    @overload
    def ioctl(self, op: int, arg) -> int | None: ...
    #
    @abstractmethod
    @overload
    def ioctl(self, op: int) -> int | None:
        """
         Control the block device and query its parameters.  The operation to
         perform is given by *op* which is one of the following integers:

           - 1 -- initialise the device (*arg* is unused)
           - 2 -- shutdown the device (*arg* is unused)
           - 3 -- sync the device (*arg* is unused)
           - 4 -- get a count of the number of blocks, should return an integer
             (*arg* is unused)
           - 5 -- get the number of bytes in a block, should return an integer,
             or ``None`` in which case the default value of 512 is used
             (*arg* is unused)
           - 6 -- erase a block, *arg* is the block number to erase

        As a minimum ``ioctl(4, ...)`` must be intercepted; for littlefs
        ``ioctl(6, ...)`` must also be intercepted. The need for others is
        hardware dependent.

        Prior to any call to ``writeblocks(block, ...)`` littlefs issues
        ``ioctl(6, block)``. This enables a device driver to erase the block
        prior to a write if the hardware requires it. Alternatively a driver
        might intercept ``ioctl(6, block)`` and return 0 (success). In this case
        the driver assumes responsibility for detecting the need for erasure.

        Unless otherwise stated ``ioctl(op, arg)`` can return ``None``.
        Consequently an implementation can ignore unused values of ``op``. Where
        ``op`` is intercepted, the return value for operations 4 and 5 are as
        detailed above. Other operations should return 0 on success and non-zero
        for failure, with the value returned being an ``OSError`` errno code.
        """
        ...
