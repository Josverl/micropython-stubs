"""
Basic typing for polyscript

https://pyscript.github.io/polyscript/#the-polyscript-module

---
Module: '_pyscript' on micropython-v1.28.0-webassembly-pyscript
"""

# MCU: {'family': 'micropython', 'version': '1.28.0', 'build': '', 'ver': '1.28.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.3
from __future__ import annotations

from typing import Any, AsyncGenerator, Callable, Final, Generator, Tuple

import storage as _storage
from _typeshed import Incomplete

target: str = "mpy-0"

def js_import(name: str) -> JSModule:
    """Module level __getattr__ that returns an JSModule object for any requested attribute."""
    ...

fs: Incomplete  ## <class 'JsProxy'> = <JsProxy nn>
interpreter: Incomplete  ## <class 'JsProxy'> = <JsProxy nn>

class PyWorker(XWorker):
    pass

@classmethod
def new(*args, **kwargs) -> Incomplete: ...
