""" """

from __future__ import annotations

from typing import Callable, overload

class Switch:
    """
    A Switch object is used to control a push-button switch.

    Usage::

         sw = pyb.Switch()       # create a switch object
         sw.value()              # get state (True if pressed, False otherwise)
         sw()                    # shorthand notation to get the switch state
         sw.callback(f)          # register a callback to be called when the
                                 #   switch is pressed down
         sw.callback(None)       # remove the callback

    Example::

         pyb.Switch().callback(lambda: pyb.LED(1).toggle())
    """

    def __init__(self) -> None:
        """
        Create and return a switch object.
        """

    @overload
    def __call__(self) -> bool:
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

    def callback(self, fun: Callable[[], None] | None) -> None:
        """
        Register the given function to be called when the switch is pressed down.
        If ``fun`` is ``None``, then it disables the callback.
        """
        ...
