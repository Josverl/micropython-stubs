"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/
"""
# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed

from typing import Any, Callable, Iterable, Mapping

def from_entries(iterable: Iterable[tuple[str, Any]]) -> Any:
    """
    Create a JavaScript object from an iterable of key-value pairs.

    This function converts a Python iterable of (key, value) tuples into
    a JavaScript object, similar to JavaScript's Object.fromEntries().

    Args:
        iterable: An iterable of (key, value) tuples where keys are strings

    Returns:
        A JavaScript object containing the key-value pairs

    Example:
        obj = from_entries([("name", "Alice"), ("age", 30)])
        # Creates JS object: {name: "Alice", age: 30}
    """
    ...

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

def to_js(
    obj: Any,
    *,
    depth: int = -1,
    default_converter: Callable[[Any], Any] | None = None,
    dict_converter: Callable[[Mapping[str, Any]], Any] | None = None,
    create_proxies: bool = True,
) -> Any:
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
