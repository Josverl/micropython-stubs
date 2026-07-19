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
from typing import Any, TypeVar

from _typeshed import Incomplete

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)

class TaskQueue:
    def __init__(self, *argv, **kwargs) -> None: ...
    def push(self, *args, **kwargs) -> Incomplete: ...
    def peek(self, *args, **kwargs) -> Incomplete: ...
    def pop(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...

class Future(Awaitable[_T]):
    def __await__(self) -> Generator[Any, None, _T]: ...
    def __iter__(self) -> Generator[Any, None, _T]: ...

# `Task` is a covariant subclass of the (invariant) `Future`, mirroring typeshed.
# That is sound here because MicroPython's `Task` has no `set_result()` (the only
# reason `Future` would otherwise need to stay invariant).
class Task(Future[_T_co]):  # type: ignore[type-var]  # pyright: ignore[reportInvalidTypeArguments]
    """
    This object wraps a coroutine into a running task.  Tasks can be waited on
    using ``await task``, which will wait for the task to complete and return
    the return value of the task.

    Tasks should not be created directly, rather use `create_task` to create them.
    """

    def __init__(self, coro: Coroutine[Any, Any, _T_co] | Generator[Any, None, _T_co], /) -> None: ...
    def cancel(self) -> bool: ...
    def done(self) -> bool: ...
