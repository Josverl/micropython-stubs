"""
Asynchronous I/O scheduler for writing concurrent code.

Core functions
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Callable, Coroutine, Dict, Generic, Iterable, List, Tuple

from _mpy_shed import AnyReadableBuf
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar  # noqa: UP035

from .stream import Stream
from .task import Task as Task
from .task import TaskQueue as TaskQueue

_T = TypeVar("_T")
_C: TypeAlias = Coroutine[Any, None, _T] | Awaitable[_T]
# StreamReader: TypeAlias = Stream
# StreamWriter: TypeAlias = Stream

class CancelledError(BaseException): ...
class TimeoutError(Exception): ...

_exc_context: Incomplete

class SingletonGenerator:
    state: Incomplete
    exc: Incomplete
    def __init__(self) -> None: ...
    def __iter__(self): ...
    def __next__(self) -> None: ...

def sleep_ms(t, sgen=...) -> Coroutine[Incomplete, Any, Any]:
    """
    Sleep for *t* milliseconds.

    This is a coroutine, and a MicroPython extension.
    """
    ...

def sleep(t) -> Coroutine[Incomplete, Any, Any]:
    """
    Sleep for *t* seconds (can be a float).

    This is a coroutine.
    """
    ...

class IOQueue:
    poller: Incomplete
    map: Incomplete
    def __init__(self) -> None: ...
    def _enqueue(self, s, idx) -> None: ...
    def _dequeue(self, s) -> None: ...
    def queue_read(self, s) -> None: ...
    def queue_write(self, s) -> None: ...
    def remove(self, task) -> None: ...
    def wait_io_event(self, dt) -> None: ...

def _promote_to_task(aw): ...
def create_task(coro) -> Task:
    """
    Create a new task from the given coroutine and schedule it to run.

    Returns the corresponding `Task` object.
    """
    ...

def run_until_complete(main_task: Incomplete | None = None): ...
def run(coro) -> _T:
    """
    Create a new task from the given coroutine and run it until it completes.

    Returns the value returned by *coro*.
    """
    ...

async def _stopper() -> None: ...

cur_task: Incomplete
_stop_task: Incomplete

class Loop:
    """
    This represents the object which schedules and runs tasks.  It cannot be
    created, use `get_event_loop` instead.
    """

    _exc_handler: Incomplete
    def create_task(coro) -> Task:
        """
        Create a task from the given *coro* and return the new `Task` object.
        """
        ...

    def run_forever(self) -> None:
        """
        Run the event loop until `stop()` is called.
        """
        ...

    def run_until_complete(aw) -> None:
        """
        Run the given *awaitable* until it completes.  If *awaitable* is not a task
        then it will be promoted to one.
        """
        ...

    def stop(self) -> None:
        """
        Stop the event loop.
        """
        ...

    def close(self) -> None:
        """
        Close the event loop.
        """
        ...

    def set_exception_handler(handler) -> None:
        """
        Set the exception handler to call when a Task raises an exception that is not
        caught.  The *handler* should accept two arguments: ``(loop, context)``.
        """
        ...

    def get_exception_handler(self) -> None:
        """
        Get the current exception handler.  Returns the handler, or ``None`` if no
        custom handler is set.
        """
        ...

    def default_exception_handler(loop, context) -> None:
        """
        The default exception handler that is called.
        """
        ...

    def call_exception_handler(context) -> None:
        """
        Call the current exception handler.  The argument *context* is passed through and
        is a dictionary containing keys: ``'message'``, ``'exception'``, ``'future'``.
        """
        ...

def get_event_loop(runq_len: int = 0, waitq_len: int = 0) -> Loop:
    """
    Return the event loop used to schedule and run tasks.  See `Loop`.
    """
    ...

def current_task() -> Task:
    """
    Return the `Task` object associated with the currently running task.
    """
    ...

def new_event_loop() -> Loop:
    """
    Reset the event loop and return it.

    Note: since MicroPython only has a single event loop this function just
    resets the loop's state, it does not create a new one.
    """
    ...
