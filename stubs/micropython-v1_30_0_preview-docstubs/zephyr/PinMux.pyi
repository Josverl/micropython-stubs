""" """

from __future__ import annotations

from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

class PinMux:
    """
    Gets an object describing a pin function. The implementation is platform-specific.

    ``func`` may be a string or an integer corresponding to a function.
    """
    def __init__(self, func) -> None: ...
