"""
Type stub for the _asyncio module.

This module provides low-level C implementations of core asyncio components.

"""

from __future__ import annotations

from typing import Any, Callable, Coroutine, Generic, Iterator, Optional, TypeVar, Union

_T = TypeVar("_T")

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

class Task(Generic[_T]):
    """
    A C implementation of an asyncio Task.

    This represents a scheduled coroutine and provides the core functionality
    for asyncio task management.
    """

    # Attributes (accessible via attribute access)
    coro: Coroutine[Any, Any, _T]
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

    def __init__(self, coro: Coroutine[Any, Any, _T], context: Optional[Any] = None) -> None:
        """
        Create a new Task from a coroutine.

        Args:
            coro: The coroutine to wrap in a Task.
            context: Optional asyncio context dictionary.
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

    def __iter__(self) -> Iterator[Any]:
        """
        Make the task awaitable by implementing the iterator protocol.

        This allows the task to be used with 'await' syntax.
        """
        ...

    def __next__(self) -> Any:
        """
        Implementation of the iterator protocol for awaitable tasks.

        Raises:
            StopIteration: When the task completes, with the result as the value.
        """
        ...
