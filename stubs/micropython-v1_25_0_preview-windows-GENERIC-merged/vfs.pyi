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
Module: 'vfs' on micropython-v1.24.1-windows-GENERIC
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'windows', 'board': 'GENERIC', 'cpu': 'win32 [GCC 12.0.0] version', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.24.0
from __future__ import annotations
from typing import overload, Any, Generator
from _typeshed import Incomplete
from _mpy_shed import _BlockDeviceProtocol
from abc import ABC, abstractmethod
from typing_extensions import Awaitable, TypeAlias, TypeVar

def mount(fsobj, mount_point: str, *, readonly: bool = False) -> Incomplete:
    """
    Mount the filesystem object *fsobj* at the location in the VFS given by the
    *mount_point* string.  *fsobj* can be a a VFS object that has a ``mount()``
    method, or a block device.  If it's a block device then the filesystem type
    is automatically detected (an exception is raised if no filesystem was
    recognised).  *mount_point* may be ``'/'`` to mount *fsobj* at the root,
    or ``'/<name>'`` to mount it at a subdirectory under the root.

    If *readonly* is ``True`` then the filesystem is mounted read-only.

    During the mount process the method ``mount()`` is called on the filesystem
    object.

    Will raise ``OSError(EPERM)`` if *mount_point* is already mounted.
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
    def __init__(self, *argv, **kwargs) -> None: ...

class AbstractBlockDev:
    #
    @abstractmethod
    @overload  # force merge
    def readblocks(self, block_num: int, buf: Incomplete) -> Incomplete: ...
    @abstractmethod
    @overload  # force merge
    def readblocks(self, block_num: int, buf: Incomplete, offset: int) -> Incomplete:
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
    @overload  # force merge
    def writeblocks(self, block_num: int, buf: Incomplete) -> Incomplete: ...
    @abstractmethod
    @overload
    def writeblocks(self, block_num: int, buf, offset: int) -> Incomplete:
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
    def ioctl(self, op: int, arg) -> None: ...
    #
    @abstractmethod
    @overload
    def ioctl(self, op: int) -> int:
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
