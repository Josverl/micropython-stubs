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

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/

---
Lightweight interface to the DOM and HTML elements.

As a convenience, and to ensure backwards compatibility, PyScript allows the use of inline event handlers via custom HTML attributes.

Warning: 
    This classic pattern of coding (inline event handlers) is no longer considered good practice in web development circles.

We include this behaviour for historic reasons, but the folks at Mozilla have a good explanation of why this is currently considered bad practice.

These attributes, expressed as py-* or mpy-* attributes of an HTML element, reference the name of a Python function to run when the event is fired. 
You should replace the * with the actual name of an event (e.g. py-click or mpy-click). This is similar to how all event handlers on elements start 
with on in standard HTML (e.g. onclick). The rule of thumb is to simply replace on with py- or mpy- and then reference the name of a Python function.

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/

---
Basic typing for polyscript

https://pyscript.github.io/polyscript/#the-polyscript-module

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/

---
Module: 'pyscript.__init__' on micropython-v1.26.0-preview-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.26.0-preview', 'build': '293', 'ver': '1.26.0-preview-293', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
from __future__ import annotations
from typing import List, Type, Tuple, Literal, Callable, Iterable, Mapping, Awaitable, Any, Final, Generator
from _typeshed import Incomplete
import sys
from _pyscript import PyWorker as PyWorker, js_import as js_import
from libcst import Not
from typing_extensions import Self, Incomplete
import storage as _storage
from pyscript import Event, document, when as when
from pyscript.ffi import create_proxy
from polyscript import lazy_py_modules as py_import
from pyscript.display import HTML as HTML, display as display
from pyscript.events import Event as Event, when as when
from pyscript.fetch import fetch as fetch
from pyscript.magic_js import PyWorker as PyWorker, RUNNING_IN_WORKER as RUNNING_IN_WORKER, config as config, current_target as current_target, document as document, js_import as js_import, js_modules as js_modules, sync as sync, window as window
from pyscript.storage import Storage as Storage, storage as storage
from pyscript.websocket import WebSocket as WebSocket
from pyscript.workers import create_named_worker as create_named_worker, workers as workers

config: dict = {}
"""PyScript configuration object containing runtime settings."""
RUNNING_IN_WORKER: Final[bool] = False
"""True if code is running in a web worker, False if in main thread."""
_MIME_METHODS = ...
_MIME_RENDERERS = ...
def display(*values, target=None, append:bool=True) -> None:
    """
    A function used to display content. The function is intelligent enough to introspect the object[s] it is passed and work out how to correctly 
    display the object[s] in the web page based on the following mime types::
        - text/plain to show the content as text
        - text/html to show the content as HTML
        - image/png to show the content as <img>
        - image/jpeg to show the content as <img>
        - image/svg+xml to show the content as <svg>
        - application/json to show the content as JSON
        - application/javascript to put the content in <script> (discouraged)

        
    The display function takes a list of *values as its first argument, and has two optional named arguments::
        - target=None - the DOM element into which the content should be placed. If not specified, the target will use the current_script() returned id and populate the related dedicated node to show the content.
        - append=True - a flag to indicate if the output is going to be appended to the target.
    """
    ...

def current_target() -> Any:
    """
    Get the current execution target in worker context.

    Returns:
        The worker's global scope object

    rRef: https://docs.pyscript.net/2025.8.1/api/#pyscriptcurrent_target
    """
    ...

def fetch(url: str, **kw: Any) -> Awaitable[_Response]:
    """
    Fetch a resource from the network.

    This is a Python wrapper around the JavaScript Fetch API, providing
    an async interface for making HTTP requests.

    Args:
        url: The URL to fetch
        **kw: Additional keyword arguments passed to the fetch request
              (e.g., method, headers, body, mode, credentials, etc.)

    Returns:
        An awaitable that resolves to a _Response object

    Example:
        response = await fetch("https://api.example.com/data")
        data = await response.json()
    """
    ...

def when(target, *args, **kwargs
):
    """
    Add an event listener to the target element(s) for the specified event type.

    The target can be a string representing the event type, or an Event object.
    If the target is an Event object, the event listener will be added to that
    object. If the target is a string, the event listener will be added to the
    element(s) that match the (second) selector argument.

    If a (third) handler argument is provided, it will be called when the event
    is triggered; thus allowing this to be used as both a function and a
    decorator.
    """
    ...

workers: Incomplete ## <class '_ReadOnlyProxy'> = <_ReadOnlyProxy object at ...>
"""
Read-only proxy to access named workers.

Provides access to workers created with create_named_worker() by their names.
"""

class HTML():
    """
    Wrap a string so that display() can render it as plain HTML
    """
    def _repr_html_(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, html) -> None:
        ...


class Storage(dict[str, Any]):
    """
    Persistent storage interface backed by IndexedDB.

    Extends dict to provide a dictionary-like interface for storing
    and retrieving data that persists across browser sessions.
    Data is stored in the browser's IndexedDB.
    """
    def popitem(self, *args, **kwargs) -> Incomplete:
        ...

    def pop(self, *args, **kwargs) -> Incomplete:
        ...

    def values(self, *args, **kwargs) -> Incomplete:
        ...

    def setdefault(self, *args, **kwargs) -> Incomplete:
        ...

    def update(self, *args, **kwargs) -> Incomplete:
        ...

    def keys(self, *args, **kwargs) -> Incomplete:
        ...

    def copy(self, *args, **kwargs) -> Incomplete:
        ...

    def get(self, *args, **kwargs) -> Incomplete:
        ...

    def items(self, *args, **kwargs) -> Incomplete:
        ...

    @classmethod
    def fromkeys(cls, *args, **kwargs) -> Incomplete:
        ...

    def sync(self) -> Generator:  ## = <generator>
        """
        Synchronize storage with IndexedDB.

        Ensures all pending writes are committed to the underlying
        IndexedDB store. Call this after making changes to persist them.

        Example:
            store = await storage("my_data")
            store["key"] = "value"
            await store.sync()  # Persist changes
        """
        ...

    def clear(self) -> None:
        """
        Remove all items from storage.

        Clears all key-value pairs from the storage instance.
        """
        ...

    def __init__(self, store: Any) -> None:
        """
        Initialize a Storage instance.

        Args:
            store: The underlying IndexedDB store object
        """
        ...

def storage(name: str = "pyscript",
    storage_class: Type[Storage] = Storage,
) -> Generator:  ## = <generator>
    """
    Create or access a named storage instance.

    A utility to instantiate a named idb-map (IndexedDB-backed storage)
    that can be consumed synchronously after initial async setup.

    Args:
        name: The name of the storage instance. Different names create
              separate storage namespaces. Default is "pyscript".
        storage_class: The Storage class to instantiate. Default is Storage.
                      Can be a custom subclass for specialized behavior.

    Returns:
        A Storage instance that acts like a dict but persists data
        to IndexedDB

    Example:
        # Create/access storage
        store = await storage("my_app_data")

        # Use like a dict
        store["username"] = "alice"
        store["settings"] = {"theme": "dark"}

        # Persist changes
        await store.sync()

        # Later, access the same data
        store = await storage("my_app_data")
        print(store["username"])  # "alice"
    """
    ...


class WebSocket():
    """
    PyScript WebSocket client for bidirectional communication.

    Provides a Python interface to the browser's WebSocket API for
    establishing persistent connections to WebSocket servers.
    """
    OPEN: Final[int] = 1
    """WebSocket connection is open (readyState = 1)."""
    CLOSED: Final[int] = 3
    """WebSocket is closed (readyState = 3)."""
    CLOSING: Final[int] = 2
    """WebSocket is closing (readyState = 2)."""
    CONNECTING: Final[int] = 0
    """WebSocket is connecting (readyState = 0)."""
    def send(self, data: str | bytes | bytearray | memoryview) -> None:
        """
        Send data through the WebSocket connection.

        Args:
            data: The data to send. Can be text (str) or binary data
                  (bytes, bytearray, memoryview)

        Example:
            ws.send("Hello, server!")
            ws.send(b"Binary data")
        """
        ...

    def close(self, code: int = 1000, reason: str = "") -> None:
        """
        Close the WebSocket connection.

        Args:
            code: The close status code (default: 1000 for normal closure)
            reason: Optional human-readable reason string

        Example:
            ws.close(1000, "Client closing connection")
        """
        ...

    def __init__(self,
        url: str | None = None,
        protocols: str | list[str] | None = None,
        **kw: Any,
    ) -> None:
        """
        Create a new WebSocket connection.

        Args:
            url: The WebSocket URL to connect to (ws:// or wss://)
            protocols: Optional sub-protocol(s) to use
            **kw: Additional keyword arguments for event handlers
                  (e.g., onopen, onmessage, onerror, onclose)

        Example:
            ws = WebSocket(
                url="wss://example.com/socket",
                onmessage=lambda msg: print(msg.data)
            )
        """
        ...

def create_named_worker(src: str = "",
    name: str = "",
    config: dict[str, Any] | None = None,
    type: str = "micropython",
) -> Generator:  ## = <generator>
    """
    Create a named web worker for parallel execution.

    Creates a PyScript worker that runs in a separate thread, allowing
    for parallel execution of Python code. Workers can be accessed later
    via the workers proxy.

    Args:
        src: The Python source code or URL to run in the worker.
             If empty, creates a worker with no initial code.
        name: The name to assign to the worker. Used to access it via
              the workers proxy.
        config: Optional configuration dictionary for the worker.
                Can include interpreter settings and other options.
        type: The worker type/interpreter. Default is "micropython".
              Other options include "pyodide" or "python".

    Returns:
        A worker object that can be used to communicate with the worker

    Example:
        worker = await create_named_worker(
            src="print('Hello from worker')",
            name="my_worker",
            type="micropython"
        )
        # Access later via: workers.my_worker
    """
    ...

py_import: Incomplete ## <class 'JsProxy'> = <JsProxy 135>

class Event():
    """
    Represents something that may happen at some point in the future.
    """
    def add_listener(self, listener) -> None:
        """
        Add a callable/awaitable to listen to when this event is triggered.
        """
        ...

    def remove_listener(self, *args) -> None:
        """
        Clear the specified handler functions in *args. If no handlers
        provided, clear all handlers.
        """
        ...

    def trigger(self, result) -> None:
        """
        Trigger the event with a result to pass into the handlers.
        """
        ...

    def __init__(self) -> None:
        ...

sync: Incomplete ## <class 'NotSupported'> = <NotSupported pyscript.sync [pyscript.sync works only when running in a worker]>
"""
A function used to pass serializable data from workers to the main thread.

Convert async operations to synchronous calls when running in a worker.

ref: https://docs.pyscript.net/latest/api/#pyscriptsync
"""
PyWorker: Incomplete ## <class 'JsProxy'> = <JsProxy 12>
"""Not available in worker context (None)."""
js_modules: Incomplete ## <class 'JsProxy'> = <JsProxy 4>
js_import: Incomplete ## <class 'JsProxy'> = <JsProxy 13>
document: Incomplete ## <class 'JsProxy'> = <JsProxy 14>
"""
The browser's document object.

Provides access to the DOM (Document Object Model) for manipulating
HTML elements when running in the main thread.

Not available in worker context (None)."""
ELEMENT_CLASSES :ElementCollection = ...
