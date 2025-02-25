"""
Module: 'pyscript.fs' on micropython-v1.24.1-webassembly
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'webassembly', 'board': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator, Awaitable
from _typeshed import Incomplete

mounted: dict = {}

async def unmount(*args, **kwargs) -> Awaitable:  ## = <generator>
    ...

async def mount(*,path:str, mode:str = "readwrite", id:str="pyscript", root:str = "",) -> Awaitable[None]:  ## = <generator>
    """Mount a directory on the user's local filesystem into the browser's virtual filesystem. 
    If no previous transient user activation has taken place, this function will result in a minimalist 
    dialog to provide the required transient user activation.
    """
    ...

async def sync(*args, **kwargs) -> Awaitable:  ## = <generator>
    ...
