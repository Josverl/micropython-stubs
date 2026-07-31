"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.10.1/api/
"""
# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed

from __future__ import annotations

from typing import Any

from _typeshed import Incomplete

RUNNING_IN_WORKER: bool
"""True if code is running in a web worker, False if in main thread."""

config: dict[str, Any]
"""PyScript configuration object containing runtime settings."""

js_modules: Any

# generate N modules in the system that will proxy the real value
# for name in globalThis.Reflect.ownKeys(js_modules):
#     sys.modules[f"pyscript.js_modules.{name}"] = JSModule(name)
# sys.modules["pyscript.js_modules"] = js_modules

class JSModule:
    """
    Lazy loader for JavaScript modules.

    Provides a Python interface to dynamically import and access
    JavaScript modules and their exports.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a JSModule loader.

        Args:
            name: The name or path of the JavaScript module to load
        """
        ...

    def __getattr__(self, field: str) -> Any | None: ...

PyWorker: Any

window: Incomplete
"""
The browser's window object.

Provides access to the global window object and all its properties
and methods when running in the main thread.

Not available in worker context (None).
"""

document: Incomplete
"""
The browser's document object.

Provides access to the DOM (Document Object Model) for manipulating
HTML elements when running in the main thread.

Not available in worker context (None)."""

sync: Any
"""
A function used to pass serializable data from workers to the main thread.

Convert async operations to synchronous calls when running in a worker.

ref: https://docs.pyscript.net/latest/api/#pyscriptsync
"""

def js_import(name: str) -> Any: ...
def current_target() -> Any:
    """
    Get the current execution target in worker context.

    Returns:
        The worker's global scope object

    rRef: https://docs.pyscript.net/2025.10.1/api/#pyscriptcurrent_target
    """
    ...
