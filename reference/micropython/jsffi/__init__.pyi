"""
Type stubs for the MicroPython WebAssembly jsffi module.

This module provides JavaScript Foreign Function Interface (FFI) capabilities
for MicroPython running in WebAssembly environments, enabling bidirectional
communication between Python and JavaScript code.
"""

from typing import Any, Iterator, TypeVar, Union, overload

__version__: str

T = TypeVar("T")

class JsProxy:
    """
    A proxy object that represents JavaScript objects in Python.

    JsProxy instances are created when JavaScript objects are passed to Python
    or when explicitly created using jsffi.create_proxy(). They provide
    transparent access to JavaScript object properties and methods.
    """

    def __init__(self, js_ref: int) -> None:
        """Initialize a JsProxy with a JavaScript object reference."""
        ...

    def __repr__(self) -> str:
        """Return a string representation of the JsProxy."""
        ...

    def __str__(self) -> str:
        """Return a string representation of the JsProxy."""
        ...

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """
        Call the JavaScript object as a function.

        Args:
            *args: Positional arguments to pass to the JavaScript function
            **kwargs: Keyword arguments to pass to the JavaScript function

        Returns:
            The result of calling the JavaScript function
        """
        ...

    def __getattr__(self, name: str) -> Any:
        """
        Get an attribute from the JavaScript object.

        Args:
            name: The attribute name

        Returns:
            The attribute value, which may be wrapped in a JsProxy if it's a JavaScript object
        """
        ...

    def __setattr__(self, name: str, value: Any) -> None:
        """
        Set an attribute on the JavaScript object.

        Args:
            name: The attribute name
            value: The value to set
        """
        ...

    def __delattr__(self, name: str) -> None:
        """
        Delete an attribute from the JavaScript object.

        Args:
            name: The attribute name to delete
        """
        ...

    def __getitem__(self, key: Any) -> Any:
        """
        Get an item from the JavaScript object using bracket notation.

        Args:
            key: The key to access

        Returns:
            The value at the specified key
        """
        ...

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Set an item on the JavaScript object using bracket notation.

        Args:
            key: The key to set
            value: The value to set
        """
        ...

    def __eq__(self, other: object) -> bool:
        """
        Check equality with another JsProxy.

        Args:
            other: The object to compare with

        Returns:
            True if both JsProxy objects reference the same JavaScript object
        """
        ...

    def __iter__(self) -> Iterator[Any]:
        """
        Return an iterator over the JavaScript object.

        For JavaScript objects that implement the iterable protocol (have a Symbol.iterator method),
        this returns an iterator that yields the values from the JavaScript iterator.
        For JavaScript objects that have a 'then' method (thenables/promises), this creates
        a generator that can be used with asyncio.

        Returns:
            An iterator over the object's values
        """
        ...

    def __del__(self) -> None:
        """Finalizer to clean up JavaScript object references."""
        ...

class JsException(Exception):
    """
    Exception raised when JavaScript code throws an error.

    This exception wraps JavaScript errors and provides access to the original
    JavaScript error object through its args.
    """

    def __init__(self, js_error: JsProxy, name: str, message: str) -> None:
        """
        Initialize a JsException.

        Args:
            js_error: The original JavaScript error object
            name: The error name (e.g., "TypeError", "ReferenceError")
            message: The error message
        """
        super().__init__(message)
        self.js_error = js_error
        self.name = name

def create_proxy(obj: Any) -> JsProxy:
    """
    Create a JsProxy that forces double-proxying of the given Python object.

    This function creates a JavaScript proxy of the Python object, then
    creates a Python JsProxy of that JavaScript proxy. This is useful
    for ensuring that Python objects behave consistently when passed
    through the JavaScript boundary.

    Args:
        obj: The Python object to create a proxy for

    Returns:
        A JsProxy wrapping the JavaScript proxy of the Python object
    """
    ...

def to_js(obj: Any) -> JsProxy:
    """
    Convert a Python object to its JavaScript representation.

    This function converts Python objects to JavaScript objects using
    PyProxy.toJs() semantics, then wraps the result in a JsProxy.

    Args:
        obj: The Python object to convert

    Returns:
        A JsProxy wrapping the JavaScript representation of the object
    """
    ...

def mem_info() -> tuple[int, int, int, int, int, int, int]:
    """
    Get memory information about the proxy system.

    Returns:
        A tuple containing:
        - GC heap total bytes
        - GC heap used bytes
        - GC heap free bytes
        - proxy_c_ref allocated size
        - proxy_c_ref used count
        - proxy_js_ref allocated size
        - proxy_js_ref used count
    """
    ...
