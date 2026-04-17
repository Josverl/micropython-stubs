"""
The tuple to pass or receive from the time methods is unfortunately
defined differently on different ports, boards and versions of MicroPython.

The _Time8Tuple and _Time9Tuple are the most common ones, and are unified in the _TimeTuple.

As this still does not cover all cases, the _TimeTuple is a union of the two common cases and the generic Tuple.
"""

from typing import Tuple, TypeVar
from typing_extensions import TypeAlias

_Time8Tuple: TypeAlias = Tuple[int, int, int, int, int, int, int, int]
_Time9Tuple: TypeAlias = Tuple[int, int, int, int, int, int, int, int, int]
_TimeTuple: TypeAlias = _Time8Tuple | _Time9Tuple | Tuple[int, ...]

# Opaque types for tick values to prevent direct arithmetic operations.
# These are stub-only types that don't exist at runtime (values are actually int).
# They prevent operations like `ticks_ms() - ticks_ms()` which would be incorrect.
# Use ticks_diff() and ticks_add() instead.
class _TicksMs:
    """Opaque millisecond tick value. Use ticks_diff() and ticks_add() for operations."""
    def __init__(self, value: int, /) -> None: ...

class _TicksUs:
    """Opaque microsecond tick value. Use ticks_diff() and ticks_add() for operations."""
    def __init__(self, value: int, /) -> None: ...

class _TicksCPU:
    """Opaque CPU tick value. Use ticks_diff() and ticks_add() for operations."""
    def __init__(self, value: int, /) -> None: ...

_Ticks = TypeVar("_Ticks", _TicksMs, _TicksUs, _TicksCPU)

__all__ = [
    "_TimeTuple",
    "_Time8Tuple",
    "_Time9Tuple",
    "_TicksMs",
    "_TicksUs",
    "_TicksCPU",
    "_Ticks",
]
