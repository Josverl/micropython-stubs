"""
Asynchronous I/O scheduler for writing concurrent code.

MicroPython module: https://docs.micropython.org/en/v1.24.1/library/asyncio.html

CPython module:
`asyncio `<https://docs.python.org/3.8/library/asyncio.html>

Example::

    import asyncio

    async def blink(led, period_ms):
        while True:
            led.on()
            await asyncio.sleep_ms(5)
            led.off()
            await asyncio.sleep_ms(period_ms)

    async def main(led1, led2):
        asyncio.create_task(blink(led1, 700))
        asyncio.create_task(blink(led2, 400))
        await asyncio.sleep_ms(10_000)

    # Running on a pyboard
    from pyb import LED
    asyncio.run(main(LED(1), LED(2)))

    # Running on a generic board
    from machine import Pin
    asyncio.run(main(Pin(1), Pin(2)))

Core functions
--------------

---
Module: 'uasyncio.core' on micropython-v1.24.1-esp32-ESP32_GENERIC
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'cpu': 'ESP32', 'mpy': 'v6.3', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Callable, Coroutine, Dict, Generic, Iterable, List, Tuple, Generator
from _typeshed import Incomplete
from _mpy_shed import AnyReadableBuf
from abc import ABC
from typing_extensions import Awaitable, TypeAlias, TypeVar

_T = TypeVar("_T")
_C: TypeAlias = Coroutine[Any, None, _T] | Awaitable[_T]
StreamReader: TypeAlias = "Stream"
StreamWriter: TypeAlias = "Stream"

_exc_context: dict = {}

def _promote_to_task(*args, **kwargs) -> Incomplete: ...
def ticks(*args, **kwargs) -> Incomplete: ...
def ticks_diff(*args, **kwargs) -> Incomplete: ...
def ticks_add(*args, **kwargs) -> Incomplete: ...
def new_event_loop() -> Loop:
    """
    Reset the event loop and return it.

    Note: since MicroPython only has a single event loop this function just
    resets the loop's state, it does not create a new one.
    """
    ...

def run_until_complete(*args, **kwargs) -> Incomplete: ...
def create_task(coro: _C, /) -> Task:
    """
    Create a new task from the given coroutine and schedule it to run.

    Returns the corresponding `Task` object.
    """
    ...

def get_event_loop() -> Loop:
    """
    Return the event loop used to schedule and run tasks.  See `Loop`.
    """
    ...

def current_task() -> Task:
    """
    Return the `Task` object associated with the currently running task.
    """
    ...

def sleep(t: float, /) -> Coroutine[Incomplete, Any, Any]:
    """
    Sleep for *t* seconds (can be a float).

    This is a coroutine.
    """
    ...

def run(coro: Coroutine[Any, None, _T] | Awaitable[_T], /) -> _T:
    """
    Create a new task from the given coroutine and run it until it completes.

    Returns the value returned by *coro*.
    """
    ...

def sleep_ms(t: int, /) -> Coroutine[Incomplete, Any, Any]:
    """
    Sleep for *t* milliseconds.

    This is a coroutine, and a MicroPython extension.
    """
    ...

cur_task: Incomplete  ## <class 'NoneType'> = None
_stopper: Generator  ## = <generator>
_task_queue: Incomplete  ## <class 'TaskQueue'> = <TaskQueue>

class CancelledError(Exception): ...

class Task(Awaitable[_T], Iterable[_T], Generic[_T], ABC):
    """
    class Task
    ----------
    """

    def __init__(self, *argv, **kwargs) -> None:
        """
        This object wraps a coroutine into a running task.  Tasks can be waited on
        using ``await task``, which will wait for the task to complete and return
        the return value of the task.

        Tasks should not be created directly, rather use `create_task` to create them.
        """

class TaskQueue:
    def push(self, *args, **kwargs) -> Incomplete: ...
    def peek(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def pop(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Loop:
    """
    This represents the object which schedules and runs tasks.  It cannot be
    created, use `get_event_loop` instead.
    """

    def get_exception_handler(self) -> None:
        """
        Get the current exception handler.  Returns the handler, or ``None`` if no
        custom handler is set.
        """
        ...

    def default_exception_handler(self, context: Dict[str, Any], /) -> None:
        """
        The default exception handler that is called.
        """
        ...

    def set_exception_handler(self, handler: Callable[[Loop, Dict[str, Any]], None] | None, /) -> None:
        """
        Set the exception handler to call when a Task raises an exception that is not
        caught.  The *handler* should accept two arguments: ``(loop, context)``.
        """
        ...

    def run_forever(self) -> None:
        """
        Run the event loop until `stop()` is called.
        """
        ...

    def run_until_complete(self, awaitable: Awaitable[_T], /) -> None:
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

    def create_task(self, coro: _C, /) -> Task:
        """
        Create a task from the given *coro* and return the new `Task` object.
        """
        ...

    def call_exception_handler(self, context: Dict[str, Any], /) -> None:
        """
        Call the current exception handler.  The argument *context* is passed through and
        is a dictionary containing keys: ``'message'``, ``'exception'``, ``'future'``.
        """
        ...
    _exc_handler: Incomplete  ## <class 'NoneType'> = None
    def __init__(self, *argv, **kwargs) -> None:
        """
        This represents the object which schedules and runs tasks.  It cannot be
        created, use `get_event_loop` instead.
        """

class SingletonGenerator:
    def __init__(self, *argv, **kwargs) -> None: ...

class IOQueue:
    def queue_read(self, *args, **kwargs) -> Incomplete: ...
    def wait_io_event(self, *args, **kwargs) -> Incomplete: ...
    def queue_write(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def _enqueue(self, *args, **kwargs) -> Incomplete: ...
    def _dequeue(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

_stop_task: Incomplete  ## <class 'NoneType'> = None
_io_queue: Incomplete  ## <class 'IOQueue'> = <IOQueue object at ...>

class TimeoutError(Exception): ...
