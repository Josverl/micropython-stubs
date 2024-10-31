""" """

from __future__ import annotations
from _typeshed import Incomplete
from .Pin import Pin

class Switch(Pin):
    """
    Create and return a switch object.
    """

    def __init__(self) -> None: ...
    def __call__(self) -> Incomplete:
        """
        Call switch object directly to get its state: ``True`` if pressed down,
        ``False`` otherwise.
        """
        ...

    def value(self) -> bool:
        """
        Get the switch state.  Returns ``True`` if pressed down, otherwise ``False``.
        """
        ...

    def callback(self, fun) -> None:
        """
        Register the given function to be called when the switch is pressed down.
        If ``fun`` is ``None``, then it disables the callback.
        """
        ...
