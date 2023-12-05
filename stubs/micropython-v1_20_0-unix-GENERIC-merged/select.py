"""
Wait for events on a set of streams.

MicroPython module: https://docs.micropython.org/en/v1.20.0/library/select.html

CPython module: :mod:`python:select` https://docs.python.org/3/library/select.html .

This module provides functions to efficiently wait for events on multiple
`streams <stream>` (select streams which are ready for operations).
"""
# MCU: {'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'unix', 'board': 'linux_[GCC_9.4.0]_version', 'cpu': '', 'mpy': '', 'arch': ''}
# Stubber: v1.15.1
from typing import Iterator, List, Optional, Tuple, Any
from _typeshed import Incomplete

POLLOUT = 4  # type: int
POLLIN = 1  # type: int
POLLHUP = 16  # type: int
POLLERR = 8  # type: int


class poll:
    """
    Create an instance of the Poll class.
    """

    def __init__(self) -> None:
        ...

    def register(self, obj, eventmask: Optional[Any] = None) -> None:
        """
        Register `stream` *obj* for polling. *eventmask* is logical OR of:

        * ``select.POLLIN``  - data available for reading
        * ``select.POLLOUT`` - more data can be written

        Note that flags like ``select.POLLHUP`` and ``select.POLLERR`` are
        *not* valid as input eventmask (these are unsolicited events which
        will be returned from `poll()` regardless of whether they are asked
        for). This semantics is per POSIX.

        *eventmask* defaults to ``select.POLLIN | select.POLLOUT``.

        It is OK to call this function multiple times for the same *obj*.
        Successive calls will update *obj*'s eventmask to the value of
        *eventmask* (i.e. will behave as `modify()`).
        """
        ...

    def unregister(self, obj) -> Incomplete:
        """
        Unregister *obj* from polling.
        """
        ...

    def modify(self, obj, eventmask) -> None:
        """
        Modify the *eventmask* for *obj*. If *obj* is not registered, `OSError`
        is raised with error of ENOENT.
        """
        ...

    def poll(self, timeout=-1, /) -> List:
        """
        Wait for at least one of the registered objects to become ready or have an
        exceptional condition, with optional timeout in milliseconds (if *timeout*
        arg is not specified or -1, there is no timeout).

        Returns list of (``obj``, ``event``, ...) tuples. There may be other elements in
        tuple, depending on a platform and version, so don't assume that its size is 2.
        The ``event`` element specifies which events happened with a stream and
        is a combination of ``select.POLL*`` constants described above. Note that
        flags ``select.POLLHUP`` and ``select.POLLERR`` can be returned at any time
        (even if were not asked for), and must be acted on accordingly (the
        corresponding stream unregistered from poll and likely closed), because
        otherwise all further invocations of `poll()` may return immediately with
        these flags set for this stream again.

        In case of timeout, an empty list is returned.

        Difference to CPython

           Tuples returned may contain more than 2 elements as described above.
        """
        ...

    def ipoll(self, timeout=-1, flags=0, /) -> Iterator[Tuple]:
        """
        Like :meth:`poll.poll`, but instead returns an iterator which yields a
        `callee-owned tuple`. This function provides an efficient, allocation-free
        way to poll on streams.

        If *flags* is 1, one-shot behaviour for events is employed: streams for
        which events happened will have their event masks automatically reset
        (equivalent to ``poll.modify(obj, 0)``), so new events for such a stream
        won't be processed until new mask is set with `poll.modify()`. This
        behaviour is useful for asynchronous I/O schedulers.

        Difference to CPython

           This function is a MicroPython extension.
        """
        ...
