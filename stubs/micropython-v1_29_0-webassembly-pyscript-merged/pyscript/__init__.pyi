"""
The public PyScript 2026.7.3 API available to MicroPython.

---
Module: 'pyscript.__init__' on micropython-v1.29.0-webassembly-pyscript
"""

# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete
from pyscript.context import (
    PyWorker as PyWorker,
    RUNNING_IN_WORKER as RUNNING_IN_WORKER,
    config as config,
    current_target as current_target,
    document as document,
    js_import as js_import,
    js_modules as js_modules,
    sync as sync,
    window as window,
)
from pyscript.display import HTML as HTML, display as display
from pyscript.events import Event as Event, when as when
from pyscript.fetch import fetch as fetch
from pyscript.storage import Storage as Storage, storage as storage
from pyscript.websocket import WebSocket as WebSocket
from pyscript.workers import create_named_worker as create_named_worker, workers as workers

config: dict = {}
RUNNING_IN_WORKER: Final[bool] = False

workers: Incomplete  ## <class '_ReadOnlyProxy'> = <_ReadOnlyProxy object at ...>

@classmethod
def py_import(*args, **kwargs) -> Incomplete: ...

sync: Incomplete  ## <class 'NotSupported'> = <NotSupported pyscript.sync [pyscript.sync works only when running in a worker]>

js_modules: Incomplete  ## <class 'JsProxy'> = <JsProxy nn>

document: Incomplete  ## <class 'JsProxy'> = <JsProxy nn>
