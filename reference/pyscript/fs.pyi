"""Filesystem API documented by PyScript 2026.7.3."""
# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed

from typing import Any, Literal
from _mpy_shed import mp_available

mounted: dict[str, Any]
"""Dictionary mapping mount points to filesystem information"""

async def mount(
    path: str,
    mode: Literal["readwrite", "read"] = "readwrite",
    root: Literal["desktop", "documents", "downloads", "music", "pictures", "videos", ""] = "",
    id: str = "pyscript",
) -> None:
    """
    Mount a filesystem at the specified path.

    Args:
        path: The path where the filesystem should be mounted
        mode: Access mode, either "r" (read-only) or "rw" (read-write)
        root: The root directory to mount (local path or URL)
        id: Optional identifier for the mounted filesystem

    Raises:
        ValueError: If the path is already mounted or parameters are invalid
        PermissionError: If the browser denies filesystem access
    """
    ...

async def sync(path: str) -> None:
    """
    Synchronize changes to the filesystem mounted at the given path.

    This ensures any pending changes are written to the underlying storage.

    Args:
        path: The path to the mounted filesystem to synchronize

    Raises:
        ValueError: If no filesystem is mounted at the specified path
    """
    ...

async def unmount(path: str) -> None:
    """
    Unmount the filesystem at the specified path.

    Args:
        path: The path of the mounted filesystem to unmount

    Raises:
        ValueError: If no filesystem is mounted at the specified path
    """
    ...

@mp_available(port="webassembly")
async def revoke(path: str, id: str = "pyscript") -> bool: ...
