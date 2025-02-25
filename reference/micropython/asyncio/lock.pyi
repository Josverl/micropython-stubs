"""
Asynchronous I/O scheduler for writing concurrent code.

Lock functions
"""

from __future__ import annotations

from abc import ABC
from collections.abc import Generator

from _typeshed import Incomplete
from typing_extensions import Awaitable  # noqa: UP035

# from . import core as core

# _T = TypeVar("_T")
# _C: TypeAlias = Coroutine[Any, None, _T] | Awaitable[_T]

class Lock(Awaitable[None], ABC):
    """
    class Lock
    ----------
    """

    state: int
    waiting: Incomplete
    def __init__(self) -> None:
        """
        Create a new lock which can be used to coordinate tasks.  Locks start in
        the unlocked state.

        In addition to the methods below, locks can be used in an ``async with`` statement.
        """

    def locked(self) -> bool:
        """
        Returns ``True`` if the lock is locked, otherwise ``False``.
        """
        ...

    def release(self) -> None:
        """
        Release the lock.  If any tasks are waiting on the lock then the next one in the
        queue is scheduled to run and the lock remains locked.  Otherwise, no tasks are
        waiting an the lock becomes unlocked.
        """
        ...

    def acquire(self) -> Generator[None, None, Incomplete]:
        """
        Wait for the lock to be in the unlocked state and then lock it in an atomic
        way.  Only one task can acquire the lock at any one time.

        This is a coroutine.
        """
        ...

    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc, tb): ...
