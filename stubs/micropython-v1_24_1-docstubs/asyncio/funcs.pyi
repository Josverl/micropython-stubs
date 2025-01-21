"""
Asynchronous I/O scheduler for writing concurrent code.

Common Functions
"""

from __future__ import annotations

from collections.abc import Generator
from typing import Any, Coroutine

from _typeshed import Incomplete
# from typing_extensions import Awaitable, TypeAlias, TypeVar

# from . import core as core

async def _run(waiter, aw) -> None: ...
async def wait_for(aw, timeout, sleep=...) -> Coroutine[Incomplete, Any, Any]:
    """
    Wait for the *awaitable* to complete, but cancel it if it takes longer
    than *timeout* seconds.  If *awaitable* is not a task then a task will be
    created from it.

    If a timeout occurs, it cancels the task and raises ``asyncio.TimeoutError``:
    this should be trapped by the caller.  The task receives
    ``asyncio.CancelledError`` which may be ignored or trapped using ``try...except``
    or ``try...finally`` to run cleanup code.

    Returns the return value of *awaitable*.

    This is a coroutine.
    """
    ...

def wait_for_ms(aw, timeout) -> Coroutine[Incomplete, Any, Any]:
    """
    Similar to `wait_for` but *timeout* is an integer in milliseconds.

    This is a coroutine, and a MicroPython extension.
    """
    ...

class _Remove:
    @staticmethod
    def remove(t) -> None: ...

def gather(*aws, return_exceptions: bool = False) -> Generator[None, None, Incomplete]:
    """
    Run all *awaitables* concurrently.  Any *awaitables* that are not tasks are
    promoted to tasks.

    Returns a list of return values of all *awaitables*.

    This is a coroutine.
    """
    ...
