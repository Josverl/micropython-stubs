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
    "create_named_worker"
]


from polyscript import lazy_py_modules as py_import  # type: ignore
from pyscript.display import HTML as HTML, display as display
from pyscript.events import Event as Event, when as when
from pyscript.fetch import fetch as fetch
from pyscript.magic_js import (
    RUNNING_IN_WORKER as RUNNING_IN_WORKER,
    PyWorker as PyWorker,
    config as config,
    current_target as current_target,
    document as document,
    js_import as js_import,
    sync as sync,
    window as window,
    js_modules as js_modules
)

from pyscript.storage import Storage as Storage, storage as storage
from pyscript.websocket import WebSocket as WebSocket
from pyscript.workers import create_named_worker as create_named_worker, workers as workers

if not RUNNING_IN_WORKER:
    ...
