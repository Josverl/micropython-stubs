"""
Module: 'pyscript.fs' on micropython-v1.28.0-webassembly-pyscript
"""

# MCU: {'family': 'micropython', 'version': '1.28.0', 'build': '', 'ver': '1.28.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.3
from __future__ import annotations

from typing import Any, AsyncGenerator, Final, Generator

from _typeshed import Incomplete

_B: Final[str] = "pyscript"
mounted: dict = {}
RUNNING_IN_WORKER: Final[bool] = False

def to_js(x0) -> Incomplete: ...

interpreter: Incomplete  ## <class 'JsProxy'> = <JsProxy nn>
_fs: Incomplete  ## <class 'JsProxy'> = <JsProxy nn>

async def unmount(x0) -> Incomplete: ...
async def revoke(x0, x1) -> Incomplete: ...
async def _check_permission(x0) -> Incomplete: ...
async def mount(x0, x1, x2, x3) -> Incomplete: ...
async def sync(x0) -> Incomplete: ...

_A: Incomplete  ## <class 'NoneType'> = None
