"""
Asynchronous I/O scheduler for writing concurrent code.

MicroPython module: https://docs.micropython.org/en/v1.22.0/library/asyncio.html

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
"""

from __future__ import annotations
from _typeshed import Incomplete, Incomplete as Incomplete
from typing import Any, Coroutine, List, Tuple

def ticks_diff(*args, **kwargs) -> Incomplete: ...
def get_event_loop() -> Incomplete:
    """
    Return the event loop used to schedule and run tasks.  See `Loop`.
    """
    ...

def current_task() -> Task:
    """
    Return the `Task` object associated with the currently running task.
    """
    ...

def create_task(coro) -> Task:
    """
    Create a new task from the given coroutine and schedule it to run.

    Returns the corresponding `Task` object.
    """
    ...

def new_event_loop() -> Incomplete:
    """
    Reset the event loop and return it.

    Note: since MicroPython only has a single event loop this function just
    resets the loop's state, it does not create a new one.
    """
    ...

def ticks(*args, **kwargs) -> Incomplete: ...
def run_until_complete(*args, **kwargs) -> Incomplete: ...
def run(coro) -> Incomplete:
    """
    Create a new task from the given coroutine and run it until it completes.

    Returns the value returned by *coro*.
    """
    ...

def wait_for_ms(awaitable, timeout) -> Coroutine[Incomplete, Any, Any]:
    """
    Similar to `wait_for` but *timeout* is an integer in milliseconds.

    This is a coroutine, and a MicroPython extension.
    """
    ...

def sleep_ms(t) -> Coroutine[Incomplete, Any, Any]:
    """
    Sleep for *t* milliseconds.

    This is a coroutine, and a MicroPython extension.
    """
    ...

def ticks_add(*args, **kwargs) -> Incomplete: ...
def sleep(t) -> Coroutine[Incomplete, Any, Any]:
    """
    Sleep for *t* seconds (can be a float).

    This is a coroutine.
    """
    ...

class TaskQueue:
    def push(self, *args, **kwargs) -> Incomplete: ...
    def peek(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def pop(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

open_connection: Incomplete

class Event:
    """
    Create a new event which can be used to synchronise tasks.  Events start
    in the cleared state.
    """

    def set(self) -> None:
        """
        Set the event.  Any tasks waiting on the event will be scheduled to run.

        Note: This must be called from within a task. It is not safe to call this
        from an IRQ, scheduler callback, or other thread. See `ThreadSafeFlag`.
        """
        ...

    def is_set(self) -> bool:
        """
        Returns ``True`` if the event is set, ``False`` otherwise.
        """
        ...

    def clear(self) -> None:
        """
        Clear the event.
        """
        ...
    wait: Incomplete
    def __init__(self, *argv, **kwargs) -> None: ...

class Lock:
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

    def release(self) -> Incomplete:
        """
        Release the lock.  If any tasks are waiting on the lock then the next one in the
        queue is scheduled to run and the lock remains locked.  Otherwise, no tasks are
        waiting an the lock becomes unlocked.
        """
        ...
    acquire: Incomplete
    def __init__(self, *argv, **kwargs) -> None: ...

class Task:
    """
    This object wraps a coroutine into a running task.  Tasks can be waited on
    using ``await task``, which will wait for the task to complete and return
    the return value of the task.

    Tasks should not be created directly, rather use `create_task` to create them.
    """

    def __init__(self, *argv, **kwargs) -> None: ...

wait_for: Incomplete

class CancelledError(Exception): ...
