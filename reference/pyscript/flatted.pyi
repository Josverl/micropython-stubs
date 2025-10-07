"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/
"""

from typing import Any, Callable

class _Known:
    """
    Internal class for tracking known objects during serialization.

    Used by the flatted algorithm to detect and handle circular references.
    """

    def __init__(self) -> None:
        """Initialize a _Known instance for tracking objects."""
        ...

class _String:
    """
    Internal wrapper class for string values during serialization.

    Used by the flatted algorithm to distinguish between regular strings
    and special marker strings.
    """

    def __init__(self, value: str) -> None:
        """
        Initialize a _String wrapper.

        Args:
            value: The string value to wrap
        """
        ...

def parse(
    value: str,
    reviver: Callable[[str, Any], Any] | None = None,
) -> Any:
    """
    Parse a flatted JSON string into a Python object.

    Reconstructs objects from flatted JSON format, which can handle
    circular references and repeated objects that standard JSON cannot.

    Args:
        value: The flatted JSON string to parse
        reviver: Optional function to transform values during parsing.
                Called for each key-value pair with (key, value) and
                should return the transformed value.

    Returns:
        The reconstructed Python object

    Example:
        json_str = '["[Circular]","hello",{"ref":"0"}]'
        obj = parse(json_str)
    """
    ...

def stringify(
    value: Any,
    replacer: Callable[[str, Any], Any] | list[str] | None = None,
    space: str | int = "",
) -> str:
    """
    Convert a Python object to flatted JSON string.

    Serializes objects to a JSON format that can handle circular references
    and repeated objects, which standard JSON cannot handle.

    Args:
        value: The Python object to serialize
        replacer: Optional function to transform values during serialization,
                 called with (key, value) and should return the transformed
                 value. Can also be a list of keys to include.
        space: Indentation for pretty-printing. Can be a string (used as-is)
              or an integer (number of spaces). Default is no indentation.

    Returns:
        A flatted JSON string representation of the object

    Example:
        obj = {"name": "Alice"}
        obj["self"] = obj  # Circular reference
        json_str = stringify(obj)  # Works with circular refs
        json_str = stringify(obj, space=2)  # Pretty print
    """
    ...
