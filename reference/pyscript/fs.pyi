"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/

This module provides filesystem operations for PyScript applications,
allowing mounting, syncing, and unmounting of virtual filesystems.
"""

from typing import Any, Dict, Literal

mounted: Dict[str, Dict[str, Any]]
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
