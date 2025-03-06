"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/
"""

class Event:
    """
    Represents something that may happen at some point in the future.
    """

    def __init__(self) -> None: ...
    def trigger(self, result) -> None:
        """
        Trigger the event with a result to pass into the handlers.
        """
        ...

    def add_listener(self, listener) -> None:
        """
        Add a callable/awaitable to listen to when this event is triggered.
        """
        ...

    def remove_listener(self, *args) -> None:
        """
        Clear the specified handler functions in *args. If no handlers
        provided, clear all handlers.
        """
        ...

def when(
    target, *args, **kwargs
):  #  -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], CoroutineType[Any, Any, Any]] | Callable[..., _Wrapped[Callable[..., Any], Any, Callable[..., Any], CoroutineType[Any, Any, Any]]]:
    """
    Add an event listener to the target element(s) for the specified event type.

    The target can be a string representing the event type, or an Event object.
    If the target is an Event object, the event listener will be added to that
    object. If the target is a string, the event listener will be added to the
    element(s) that match the (second) selector argument.

    If a (third) handler argument is provided, it will be called when the event
    is triggered; thus allowing this to be used as both a function and a
    decorator.
    """
    ...
