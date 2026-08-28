"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.10.1/api/

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
see: https://docs.pyscript.net/2025.10.1/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.10.1/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.10.1/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.10.1/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.10.1/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.10.1/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.10.1/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.10.1/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.10.1/api/

---
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.10.1/api/

---
Basic typing for polyscript

https://pyscript.github.io/polyscript/#the-polyscript-module

---
Module: '_pyscript' on micropython-v1.29.0-webassembly-pyscript
"""

# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.6
from __future__ import annotations
from typing import List, overload, Type, Callable, Awaitable, Literal, Tuple, Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete
import storage as _storage
from pyscript import Event, document, when as when
from pyscript.ffi import create_proxy
from typing_extensions import Self

_MIME_METHODS = ...
_MIME_RENDERERS = ...
RUNNING_IN_WORKER: bool
"""True if code is running in a web worker, False if in main thread."""
ELEMENT_CLASSES: ElementCollection = ...

target: str = "mpy-0"

@classmethod
def js_import(name: str) -> JSModule:
    """Module level __getattr__ that returns an JSModule object for any requested attribute."""
    ...

fs: Incomplete  ## <class 'JsProxy'> = <JsProxy nn>
interpreter: Incomplete  ## <class 'JsProxy'> = <JsProxy nn>

class PyWorker(XWorker):
    pass

@classmethod
def new(*args, **kwargs) -> Incomplete: ...

class Element:
    @overload
    def __getitem__(self, key: int) -> Element: ...
    @overload
    def __getitem__(self, key: slice) -> ElementCollection: ...
    @overload
    def __getitem__(self, key: str) -> Element | None:
        """Get an item within the element's children.

        If `key` is an integer or a slice we use it to index/slice the element's
        children. Otherwise, we use `key` as a query selector.
        """
        ...

class ElementCollection:
    @overload
    def __getitem__(self, key: int) -> Element: ...
    @overload
    def __getitem__(self, key: slice) -> ElementCollection: ...
    @overload
    def __getitem__(self, key: str) -> Element | None:
        """Get an item in the collection.

        If `key` is an integer or a slice we use it to index/slice the collection.
        Otherwise, we use `key` as a query selector.
        """
        ...
