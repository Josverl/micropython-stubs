"""
MicroPython's `_asyncio` C module.

Mirrors the C module in `extmod/modasyncio.c`, whose module globals table
exports exactly `Task` and `TaskQueue` (plus `__name__`). `Future` is kept as a
minimal generic base so the typeshed-derived `asyncio.futures` stub can still
re-export `asyncio.Future` and so `Task` stays awaitable and typed.

Types follow typeshed (so `asyncio.create_task(coro)` still infers
`Task[<coro return type>]`), but the interface is trimmed to MicroPython's
actual surface: no `result()` / `add_done_callback()` / `get_stack()`, no
`contextvars`, and no CPython `sys.version_info` guards.

The loop/task helper functions (`get_event_loop`, `current_task`,
`_register_task`, ...) are NOT part of MicroPython's `_asyncio`: the real ones
live in the `asyncio` package (`asyncio/core.py`) and the CPython-only internals
do not exist in MicroPython at all. They are therefore defined in the `asyncio`
package stubs (or omitted), not here.

MicroPython docs: https://docs.micropython.org/en/latest/library/asyncio.html
"""
from __future__ import annotations

from collections.abc import Awaitable, Coroutine, Generator

from typing import Any, Callable, Coroutine, Generator, Generic, Iterator, Optional, TypeVar, Union

from _typeshed import Incomplete

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)


class TaskQueue:
    """
    A priority queue implementation for managing asyncio tasks.

    This is a C implementation of a heap-based priority queue optimized for
    asyncio task scheduling.
    """

    def __init__(self) -> None:
        """Create a new empty task queue."""
        ...

    def peek(self) -> Optional[Task[Any]]:
        """
        Return the highest priority task without removing it.

        Returns:
            The task with the earliest scheduled time, or None if queue is empty.
        """
        ...

    def push(self, task: Task[Any], key: Optional[int] = None) -> None:
        """
        Add a task to the queue with optional priority key.

        Args:
            task: The Task object to add to the queue.
            key: Optional priority key (typically a timestamp).
                If not provided, uses the task's ph_key attribute.
        """
        ...

    def pop(self) -> Task[Any]:
        """
        Remove and return the highest priority task.

        Returns:
            The task with the earliest scheduled time.

        Raises:
            IndexError: If the queue is empty.
        """
        ...

    def remove(self, task: Task[Any]) -> None:
        """
        Remove a specific task from the queue.

        Args:
            task: The Task object to remove.

        Raises:
            ValueError: If the task is not in the queue.
        """
        ...


# Micropython's `_asyncio` C module does not expose a `Future` class, 
# but we define a minimal generic base so that `Task` can be awaitable and typed, 

class _Future(Awaitable[_T]):
    def __await__(self) -> Generator[Any, None, _T]: ...
    def __iter__(self) -> Generator[Any, None, _T]: ...

# `Task` is a covariant subclass of the (invariant) `Future`, mirroring typeshed.
# That is sound here because MicroPython's `Task` has no `set_result()` (the only
# reason `Future` would otherwise need to stay invariant).

class Task(_Future[_T_co]):  # type: ignore[type-var]
    """
    A C implementation of an asyncio Task.

    This represents a scheduled coroutine and provides the core functionality
    for asyncio task management.
    """

    # Attributes (accessible via attribute access)
    coro: Coroutine[Any, Any, _T_co]
    """The underlying coroutine"""
    data: Any
    """Task-specific data (used for queuing, cancellation, etc.)"""
    state: Union[
        bool,  # True=running not waited on, False=done was waited on
        None,  # done not waited on
        TaskQueue,  # other tasks waiting on this task
        Callable[[Task[Any], Any], None],  # completion callback
    ]
    """Task state indicator
     True=running not waited on, False=done was waited on 
     None=done not waited on
     TaskQueue=other tasks waiting on this task
     Callable[[Task[Any], Any], None]=completion callback
    """

    ph_key: int
    """Priority heap key (typically a timestamp)"""

    def __init__(self, coro: Coroutine[Any, Any, _T_co] | Generator[Any, None, _T_co], globals=None, /) -> None:
        """
        Create a new Task from a coroutine.

        Args:
            coro: The coroutine to wrap in a Task.
            globals: Optional asyncio context dictionary (ignored).
        """
        ...

    def done(self) -> bool:
        """
        Check if the task has completed (either successfully or with an exception).

        Returns:
            True if the task is done, False otherwise.
        """
        ...

    def cancel(self) -> bool:
        """
        Request cancellation of the task.

        Returns:
            True if the task was successfully cancelled, False if it was already done.

        Raises:
            RuntimeError: If attempting to cancel the currently running task.
        """
        ...

    def __next__(self) -> Any:
        """
        Implementation of the iterator protocol for awaitable tasks.

        Raises:
            StopIteration: When the task completes, with the result as the value.
        """
        ...

