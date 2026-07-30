"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.10.1/api/

---
Module: '_pyscript' on micropython-v1.28.0-webassembly-pyscript
"""

# MCU: {'family': 'micropython', 'version': '1.28.0', 'build': '', 'ver': '1.28.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.3
from __future__ import annotations

import sys
from typing import Any, AsyncGenerator, Awaitable, Callable, Final, Generator, Iterable, List, Literal, Mapping, Tuple, Type

import storage as _storage
from _typeshed import Incomplete
from libcst import Not
from pyscript import Event, document
from pyscript import when as when
from pyscript.ffi import create_proxy
from typing_extensions import Self

_MIME_METHODS = ...
_MIME_RENDERERS = ...
RUNNING_IN_WORKER: bool
ELEMENT_CLASSES: ElementCollection = ...

target: str = "mpy-0"

@classmethod
def js_import(name: str) -> JSModule:
    """Module level __getattr__ that returns an JSModule object for any requested attribute."""
    ...

fs: Incomplete  ## <class 'JsProxy'> = <JsProxy nn>
interpreter: Incomplete  ## <class 'JsProxy'> = <JsProxy nn>

class PyWorker(XWorker):
    def __init__(self, name) -> None: ...

@classmethod
def new(*args, **kwargs) -> Incomplete: ...
