"""
Asynchronous I/O scheduler for writing concurrent code.

MicroPython module: https://docs.micropython.org/en/v1.22.1/library/asyncio.html

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
Module: 'uasyncio.__init__' on micropython-v1.22.1-rp2-RPI_PICO_W
"""
# MCU: {'family': 'micropython', 'version': '1.22.1', 'build': '', 'ver': '1.22.1', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.17.1
from __future__ import annotations
from typing import Any, Coroutine, List, Tuple, Generator
from _typeshed import Incomplete

_attrs: dict = {}

def current_task() -> Task:
    """
    Return the `Task` object associated with the currently running task.
    """
    ...

def get_event_loop() -> Incomplete:
    """
    Return the event loop used to schedule and run tasks.  See `Loop`.
    """
    ...

def create_task(coro) -> Task:
    """
    Create a new task from the given coroutine and schedule it to run.

    Returns the corresponding `Task` object.
    """
    ...

def wait_for_ms(awaitable, timeout) -> Coroutine[Incomplete, Any, Any]:
    """
    Similar to `wait_for` but *timeout* is an integer in milliseconds.

    This is a coroutine, and a MicroPython extension.
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

def ticks_diff(*args, **kwargs) -> Incomplete: ...
def ticks_add(*args, **kwargs) -> Incomplete: ...
def sleep_ms(t) -> Coroutine[Incomplete, Any, Any]:
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

class TaskQueue:
    def push(self, *args, **kwargs) -> Incomplete: ...
    def peek(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def pop(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

open_connection: Generator  ## = <generator>

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
    wait: Generator  ## = <generator>
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
    def default_exception_handler(self, context) -> Incomplete:
        """
        The default exception handler that is called.
        """
        ...
    def set_exception_handler(self, handler) -> None:
        """
        Set the exception handler to call when a Task raises an exception that is not
        caught.  The *handler* should accept two arguments: ``(loop, context)``.
        """
        ...
    def run_forever(self) -> Incomplete:
        """
        Run the event loop until `stop()` is called.
        """
        ...
    def run_until_complete(self, awaitable) -> Incomplete:
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
    def create_task(self, coro) -> Task:
        """
        Create a task from the given *coro* and return the new `Task` object.
        """
        ...
    def call_exception_handler(self, context) -> Incomplete:
        """
        Call the current exception handler.  The argument *context* is passed through and
        is a dictionary containing keys: ``'message'``, ``'exception'``, ``'future'``.
        """
        ...
    _exc_handler: Incomplete  ## <class 'NoneType'> = None
    def __init__(self, *argv, **kwargs) -> None: ...

class Task:
    """
    This object wraps a coroutine into a running task.  Tasks can be waited on
    using ``await task``, which will wait for the task to complete and return
    the return value of the task.

    Tasks should not be created directly, rather use `create_task` to create them.
    """

    def __init__(self, *argv, **kwargs) -> None: ...

wait_for: Generator  ## = <generator>

class CancelledError(Exception): ...

start_server: Generator  ## = <generator>

class ThreadSafeFlag:
    """
    Create a new flag which can be used to synchronise a task with code running
    outside the asyncio loop, such as other threads, IRQs, or scheduler
    callbacks.  Flags start in the cleared state.  The class does not currently
    work under the Unix build of MicroPython.
    """

    def set(self) -> None:
        """
        Set the flag.  If there is a task waiting on the flag, it will be scheduled
        to run.
        """
        ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def clear(self) -> None:
        """
        Clear the flag. This may be used to ensure that a possibly previously-set
        flag is clear before waiting for it.
        """
        ...
    wait: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class StreamWriter:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awritestr: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    awrite: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class StreamReader:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awritestr: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    awrite: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class SingletonGenerator:
    def __init__(self, *argv, **kwargs) -> None: ...

gather: Generator  ## = <generator>

class TimeoutError(Exception): ...

class IOQueue:
    def queue_read(self, *args, **kwargs) -> Incomplete: ...
    def wait_io_event(self, *args, **kwargs) -> Incomplete: ...
    def queue_write(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def _enqueue(self, *args, **kwargs) -> Incomplete: ...
    def _dequeue(self, *args, **kwargs) -> Incomplete: ...
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
    acquire: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
