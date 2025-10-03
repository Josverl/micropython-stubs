"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/
"""

from __future__ import annotations

import sys
from typing import Any, Callable

from _pyscript import PyWorker as PyWorker
from _pyscript import js_import as js_import

RUNNING_IN_WORKER: bool
"""True if code is running in a web worker, False if in main thread."""

config: dict[str, Any]
"""PyScript configuration object containing runtime settings."""

if "MicroPython" in sys.version:
    ...
else:
    ...

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

if RUNNING_IN_WORKER:
    PyWorker: None
    """Not available in worker context (None)."""

    window: None
    """Not available in worker context (None)."""

    document: None
    """Not available in worker context (None)."""

    js_import: None
    """Not available in worker context (None)."""

    sync: Callable[[Any], Any]
    """
    Synchronize with main thread (worker context).

    Convert async operations to synchronous calls when running in a worker.
    """

    def current_target() -> Any:
        """
        Get the current execution target in worker context.

        Returns:
            The worker's global scope object
        """
        ...

else:
    window: Any
    """
    The browser's window object.

    Provides access to the global window object and all its properties
    and methods when running in the main thread.
    """

    document: Any
    """
    The browser's document object.

    Provides access to the DOM (Document Object Model) for manipulating
    HTML elements when running in the main thread.
    """

    sync: Callable[[Any], Any]
    """
    Synchronize async operations (main thread context).

    Convert async operations to synchronous calls when running in main thread.
    """

    def current_target() -> Any:
        """
        Get the current execution target in main thread context.

        Returns:
            The current script element or execution context
        """
        ...
    """
    Synchronize async operations (main thread context).

    Convert async operations to synchronous calls when running in main thread.
    """

    def current_target() -> Any:
        """
        Get the current execution target in main thread context.

        Returns:
            The current script element or execution context
        """
        ...
