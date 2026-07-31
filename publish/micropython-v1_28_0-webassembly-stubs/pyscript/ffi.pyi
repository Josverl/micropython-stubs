"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.10.1/api/
"""
# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed

from typing import Any, Callable

def create_proxy(obj: Any) -> Any:
    """
    Create a JavaScript proxy for a Python object.

    This function wraps a Python object in a JavaScript Proxy, allowing
    JavaScript code to interact with Python objects more naturally. This is
    particularly useful for passing Python functions, objects, or collections
    to JavaScript APIs.

    Args:
        obj: The Python object to wrap in a proxy

    Returns:
        A JavaScript Proxy that wraps the Python object

    Example:
        def my_callback(event):
            print(f"Event: {event}")

        js_callback = create_proxy(my_callback)
        element.addEventListener("click", js_callback)
    """
    ...

def to_js(obj: Any, **kw: Any) -> Any:
    """
    Convert a Python object to its JavaScript equivalent.

    This function recursively converts Python objects to JavaScript objects,
    handling common types like dict, list, tuple, etc. It provides fine-grained
    control over the conversion process through various parameters.

    Args:
        obj: The Python object to convert
        depth: Maximum recursion depth for conversion. -1 means unlimited.
               Use 0 for shallow conversion, 1 for one level deep, etc.
        default_converter: Optional custom converter function for types not
                          handled by the default conversion logic
        dict_converter: Optional custom converter specifically for dict objects.
                       If not provided, dicts are converted to JS objects.
        create_proxies: If True, creates proxies for unconvertible objects.
                       If False, leaves them as Python objects.

    Returns:
        The JavaScript representation of the Python object

    Example:
        data = {"items": [1, 2, 3], "name": "test"}
        js_data = to_js(data)
        # Converts to JS: {items: [1, 2, 3], name: "test"}

        # Shallow conversion
        nested = {"outer": {"inner": "value"}}
        js_shallow = to_js(nested, depth=1)
    """
    ...

def is_none(value: Any) -> bool: ...
def assign(source: Any, *args: Any) -> Any: ...
def direct(source: Any) -> Any: ...

gather: Callable[..., Any]
query: Callable[..., Any]
