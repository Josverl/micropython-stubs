"""
Asynchronous I/O scheduler for writing concurrent code.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/asyncio.html

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
Module: 'asyncio.__init__' on micropython-v1.21.0-unix-linux_[GCC_9.4.0]_version
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'unix', 'board': 'linux_[GCC_9.4.0]_version', 'cpu': '', 'mpy': '', 'arch': ''}
# Stubber: v1.15.1
from typing import Coroutine, List, Tuple, Any
from _typeshed import Incomplete


def ticks_diff(*args, **kwargs) -> Incomplete:
    ...


def run_until_complete(*args, **kwargs) -> Incomplete:
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


def run(coro) -> Incomplete:
    """
    Create a new task from the given coroutine and run it until it completes.

    Returns the value returned by *coro*.
    """
    ...


def new_event_loop() -> Incomplete:
    """
    Reset the event loop and return it.

    Note: since MicroPython only has a single event loop this function just
    resets the loop's state, it does not create a new one.
    """
    ...


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


def ticks(*args, **kwargs) -> Incomplete:
    ...


def sleep_ms(t) -> Coroutine[Incomplete, Any, Any]:
    """
    Sleep for *t* milliseconds.

    This is a coroutine, and a MicroPython extension.
    """
    ...


def ticks_add(*args, **kwargs) -> Incomplete:
    ...


def sleep(t) -> Coroutine[Incomplete, Any, Any]:
    """
    Sleep for *t* seconds (can be a float).

    This is a coroutine.
    """
    ...


wait_for: Incomplete  ## <class 'generator'> = <generator>
gather: Incomplete  ## <class 'generator'> = <generator>


class Loop:
    """
    This represents the object which schedules and runs tasks.  It cannot be
    created, use `get_event_loop` instead.
    """

    def call_exception_handler(self, context) -> Incomplete:
        """
        Call the current exception handler.  The argument *context* is passed through and
        is a dictionary containing keys: ``'message'``, ``'exception'``, ``'future'``.
        """
        ...

    def run_forever(self) -> Incomplete:
        """
        Run the event loop until `stop()` is called.
        """
        ...

    def set_exception_handler(self, handler) -> None:
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

    def default_exception_handler(self, context) -> Incomplete:
        """
        The default exception handler that is called.
        """
        ...

    def run_until_complete(self, awaitable) -> Incomplete:
        """
        Run the given *awaitable* until it completes.  If *awaitable* is not a task
        then it will be promoted to one.
        """
        ...

    def close(self) -> None:
        """
        Close the event loop.
        """
        ...

    def stop(self) -> None:
        """
        Stop the event loop.
        """
        ...

    def create_task(self, coro) -> Task:
        """
        Create a task from the given *coro* and return the new `Task` object.
        """
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class IOQueue:
    def queue_write(self, *args, **kwargs) -> Incomplete:
        ...

    def queue_read(self, *args, **kwargs) -> Incomplete:
        ...

    def wait_io_event(self, *args, **kwargs) -> Incomplete:
        ...

    def remove(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


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

    wait: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class CancelledError(Exception):
    ...
