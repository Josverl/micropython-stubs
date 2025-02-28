"""
Asynchronous I/O scheduler for writing concurrent code.

Eventfunctions
"""

from __future__ import annotations

from collections.abc import Generator
from typing import Any, Coroutine

from _mpy_shed import AnyReadableBuf
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar  # noqa: UP035

from . import core as core

_T = TypeVar("_T")
_C: TypeAlias = Coroutine[Any, None, _T] | Awaitable[_T]

class Event:
    """
    class Event
    -----------
    """

    state: bool
    waiting: Incomplete
    def __init__(self) -> None:
        """
        Create a new event which can be used to synchronise tasks.  Events start
        in the cleared state.
        """

    def is_set(self) -> bool:
        """
        Returns ``True`` if the event is set, ``False`` otherwise.
        """
        ...

    def set(self) -> None:
        """
        Set the event.  Any tasks waiting on the event will be scheduled to run.

        Note: This must be called from within a task. It is not safe to call this
        from an IRQ, scheduler callback, or other thread. See `ThreadSafeFlag`.
        """
        ...

    def clear(self) -> None:
        """
        Clear the event.
        """
        ...

    def wait(self) -> Generator[None, None, Incomplete]:
        """
        Wait for the event to be set.  If the event is already set then it returns
        immediately.

        This is a coroutine.
        """
        ...

class ThreadSafeFlag:
    """
    class ThreadSafeFlag
    --------------------
    """

    state: int
    def __init__(self) -> None:
        """
        Create a new flag which can be used to synchronise a task with code running
        outside the asyncio loop, such as other threads, IRQs, or scheduler
        callbacks.  Flags start in the cleared state.
        """

    def ioctl(self, req, flags): ...
    def set(self) -> None:
        """
        Set the flag.  If there is a task waiting on the flag, it will be scheduled
        to run.
        """
        ...

    def clear(self) -> None:
        """
        Clear the flag. This may be used to ensure that a possibly previously-set
        flag is clear before waiting for it.
        """
        ...

    async def wait(self) -> Generator[Incomplete]:
        """
        Wait for the flag to be set.  If the flag is already set then it returns
        immediately.  The flag is automatically reset upon return from ``wait``.

        A flag may only be waited on by a single task at a time.

        This is a coroutine.
        """
        ...
