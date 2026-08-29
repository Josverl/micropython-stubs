"""Event API documented by PyScript 2026.7.3."""
# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed

from typing import Callable, TypeVar

_F = TypeVar("_F", bound=Callable[..., object])

class Event:
    """
    Represents something that may happen at some point in the future.
    """

    def __init__(self) -> None: ...
    def trigger(self, result: object) -> None:
        """
        Trigger the event with a result to pass into the handlers.
        """
        ...

    def add_listener(self, listener: Callable[..., object]) -> None:
        """
        Add a callable/awaitable to listen to when this event is triggered.
        """
        ...

    def remove_listener(self, *listeners: Callable[..., object]) -> None:
        """
        Clear the specified handler functions in *args. If no handlers
        provided, clear all handlers.
        """
        ...

def when(
    event_type: str | Event | list[Event],
    selector: object = None,
    **options: object,
) -> Callable[[_F], _F]:
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
