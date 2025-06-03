"""
Virtual filesystem control.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/vfs.html

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
Module: 'vfs' on micropython-v1.25.0-stm32-PYBV11
"""

# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': '1.25.0', 'cpu': 'STM32F405RG'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete
from typing import List, Optional, Tuple
from typing_extensions import Awaitable, TypeAlias, TypeVar

def umount(mount_point) -> Incomplete:
    """
    Unmount a filesystem. *mount_point* can be a string naming the mount location,
    or a previously-mounted filesystem object.  During the unmount process the
    method ``umount()`` is called on the filesystem object.

    Will raise ``OSError(EINVAL)`` if *mount_point* is not found.
    """
    ...

def mount() -> List[Tuple]:
    """
    :noindex:

    With no arguments to :func:`mount`, return a list of tuples representing
    all active mountpoints.

    The returned list has the form *[(fsobj, mount_point), ...]*.
    """
    ...

class VfsLfs2:
    """
    Create a filesystem object that uses the `littlefs v2 filesystem format`_.
    Storage of the littlefs filesystem is provided by *block_dev*, which must
    support the :ref:`extended interface <block-device-interface>`.
    Objects created by this constructor can be mounted using :func:`mount`.

    The *mtime* argument enables modification timestamps for files, stored using
    littlefs attributes.  This option can be disabled or enabled differently each
    mount time and timestamps will only be added or updated if *mtime* is enabled,
    otherwise the timestamps will remain untouched.  Littlefs v2 filesystems without
    timestamps will work without reformatting and timestamps will be added
    transparently to existing files once they are opened for writing.  When *mtime*
    is enabled `os.stat` on files without timestamps will return 0 for the timestamp.

    See :ref:`filesystem` for more information.
    """

    def rename(self, *args, **kwargs) -> Incomplete: ...
    @staticmethod
    def mkfs(block_dev, readsize=32, progsize=32, lookahead=32) -> None:
        """
            Build a Lfs2 filesystem on *block_dev*.

        ``Note:`` There are reports of littlefs v2 failing in certain situations,
                  for details see `littlefs issue 295`_.
        """
        ...

    def mount(self, *args, **kwargs) -> Incomplete: ...
    def statvfs(self, *args, **kwargs) -> Incomplete: ...
    def rmdir(self, *args, **kwargs) -> Incomplete: ...
    def stat(self, *args, **kwargs) -> Incomplete: ...
    def umount(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def mkdir(self, *args, **kwargs) -> Incomplete: ...
    def open(self, *args, **kwargs) -> Incomplete: ...
    def ilistdir(self, *args, **kwargs) -> Incomplete: ...
    def chdir(self, *args, **kwargs) -> Incomplete: ...
    def getcwd(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, block_dev, readsize=32, progsize=32, lookahead=32, mtime=True) -> None: ...

class VfsFat:
    """
    Create a filesystem object that uses the FAT filesystem format.  Storage of
    the FAT filesystem is provided by *block_dev*.
    Objects created by this constructor can be mounted using :func:`mount`.
    """

    def rename(self, *args, **kwargs) -> Incomplete: ...
    @staticmethod
    def mkfs(block_dev) -> None:
        """
        Build a FAT filesystem on *block_dev*.
        """
        ...

    def mount(self, *args, **kwargs) -> Incomplete: ...
    def statvfs(self, *args, **kwargs) -> Incomplete: ...
    def rmdir(self, *args, **kwargs) -> Incomplete: ...
    def stat(self, *args, **kwargs) -> Incomplete: ...
    def umount(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def mkdir(self, *args, **kwargs) -> Incomplete: ...
    def open(self, *args, **kwargs) -> Incomplete: ...
    def ilistdir(self, *args, **kwargs) -> Incomplete: ...
    def chdir(self, *args, **kwargs) -> Incomplete: ...
    def getcwd(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, block_dev) -> None: ...
