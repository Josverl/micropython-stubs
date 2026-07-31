"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.10.1/api/

This module provides filesystem operations for PyScript applications,
allowing mounting, syncing, and unmounting of virtual filesystems.

---
Module: 'pyscript.fs' on micropython-v1.28.0-webassembly-pyscript
"""

# MCU: {'family': 'micropython', 'version': '1.28.0', 'build': '', 'ver': '1.28.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.3
from __future__ import annotations

from typing import Any, AsyncGenerator, Final, Generator, Literal

from _typeshed import Incomplete

_B: Final[str] = "pyscript"
mounted: dict = {}
"""Dictionary mapping mount points to filesystem information"""
RUNNING_IN_WORKER: Final[bool] = False

def to_js(x0) -> Incomplete: ...

interpreter: Incomplete  ## <class 'JsProxy'> = <JsProxy nn>
_fs: Incomplete  ## <class 'JsProxy'> = <JsProxy nn>

async def unmount(path: str) -> None:
    """
    Unmount the filesystem at the specified path.

    Args:
        path: The path of the mounted filesystem to unmount

    Raises:
        ValueError: If no filesystem is mounted at the specified path
    """
    ...

async def revoke(path: str, id: str = "pyscript") -> bool: ...
async def _check_permission(x0) -> Incomplete: ...
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

_A: Incomplete  ## <class 'NoneType'> = None
