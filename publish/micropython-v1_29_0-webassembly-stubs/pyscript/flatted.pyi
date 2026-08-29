"""Circular JSON API documented by PyScript 2026.7.3."""

# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed
from typing import Any

def parse(value: str, *args: Any, **kwargs: Any) -> Any:
    """
    Parse a flatted JSON string into a Python object.

    Reconstructs objects from flatted JSON format, which can handle
    circular references and repeated objects that standard JSON cannot.

    Args:
        value: The flatted JSON string to parse
        Additional arguments are passed to ``json.loads``.

    Returns:
        The reconstructed Python object

    Example:
        json_str = '["[Circular]","hello",{"ref":"0"}]'
        obj = parse(json_str)
    """
    ...

def stringify(value: Any, *args: Any, **kwargs: Any) -> str:
    """
    Convert a Python object to flatted JSON string.

    Serializes objects to a JSON format that can handle circular references
    and repeated objects, which standard JSON cannot handle.

    Args:
        value: The Python object to serialize
          Additional arguments are passed to ``json.dumps``.

    Returns:
        A flatted JSON string representation of the object

    Example:
        obj = {"name": "Alice"}
        obj["self"] = obj  # Circular reference
        json_str = stringify(obj)  # Works with circular refs
        json_str = stringify(obj, indent=2)  # Pretty print
    """
    ...
