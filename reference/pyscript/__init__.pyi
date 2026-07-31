"""
PyScript makes available convenience objects, functions and attributes.

These APIs will work with both Pyodide and MicroPython in exactly the same way.

PyScript can run in two contexts: the main browser thread, or on a web worker. T
he following three categories of API functionality explain features that are common for:
 - both main thread and worker,
 - main thread only,
 - and worker only.

 Most features work in both contexts in exactly the same manner, but please be aware that some are specific to either the main thread
 or a worker context.

"""
# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed

from typing import Any

__all__ = [
    "PyWorker",
    "config",
    "current_target",
    "display",
    "document",
    "fetch",
    "js_import",
    "js_modules",
    "py_import",
    "storage",
    "sync",
    "window",
    "workers",
    "HTML",
    "Event",
    "WebSocket",
    "create_named_worker",
]

async def py_import(*args: str) -> tuple[Any, ...]: ...

class HTML:
    def __init__(self, html: Any) -> None: ...

def display(*values: Any, target: Any = None, append: bool = True) -> None: ...

from pyscript.events import Event as Event

def when(target: Any, *args: Any, **kwargs: Any) -> Any: ...

from pyscript.fetch import _DirectResponse

def fetch(url: str, **kw: Any) -> _DirectResponse: ...

from pyscript.magic_js import (
    RUNNING_IN_WORKER as RUNNING_IN_WORKER,
    config as config,
    current_target as current_target,
    document as document,
    sync as sync,
    window as window,
    js_modules as js_modules,
)

def PyWorker(
    file: str,
    a_sync: bool = True,
    config: str = "",
    type: str = "pyodide",
    version: str = ...,
    serviceWorker: str = ...,
) -> Any: ...
def js_import(name: str) -> Any: ...

from pyscript.storage import Storage as Storage, storage as storage
from pyscript.websocket import WebSocket as _WebSocket

class WebSocket(_WebSocket):
    onopen: Any
    onmessage: Any
    onerror: Any
    onclose: Any
    def __init__(self, url: str | None = None, protocols: str | list[str] | None = None, **kw: Any) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...
    def __setattr__(self, attr: str, value: Any) -> None: ...
    def close(self, code: int = 1000, reason: str = "") -> None: ...
    def send(self, data: str | bytes | bytearray | memoryview) -> None: ...

from pyscript.workers import create_named_worker as create_named_worker, workers as workers

if not RUNNING_IN_WORKER: ...
