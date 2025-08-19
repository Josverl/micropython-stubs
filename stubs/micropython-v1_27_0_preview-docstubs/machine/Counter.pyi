""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, Optional
from typing_extensions import TypeVar, TypeAlias, Awaitable

class Counter:
    """
    Returns the singleton Counter object for the the given *id*. Values of *id*
    depend on a particular port and its hardware. Values 0, 1, etc. are commonly
    used to select hardware block #0, #1, etc.

    Additional arguments are passed to the :meth:`init` method described below,
    and will cause the Counter instance to be re-initialised and reset.

    On ESP32, the *id* corresponds to a :ref:`PCNT unit <esp32.PCNT>`.
    """

    RISING: Incomplete
    """Select the pulse edge."""
    FALLING: Incomplete
    """Select the pulse edge."""
    UP: Incomplete
    """Select the counting direction."""
    DOWN: Incomplete
    """Select the counting direction."""
    def __init__(self, id, *args, **kwargs) -> None: ...
    def init(self, src, *args, **kwargs) -> Incomplete:
        """
        Initialise and reset the Counter with the given parameters:

        - *src* specifies the input pin as a :ref:`machine.Pin <machine.Pin>` object.
          May be omitted on ports that have a predefined pin for a given hardware
          block.

        Additional keyword-only parameters that may be supported by a port are:

        - *edge* specifies the edge to count. Either ``Counter.RISING`` (the default)
          or ``Counter.FALLING``. *(Supported on ESP32)*

        - *direction* specifies the direction to count. Either ``Counter.UP`` (the
          default) or ``Counter.DOWN``. *(Supported on ESP32)*

        - *filter_ns* specifies a minimum period of time in nanoseconds that the
          source signal needs to be stable for a pulse to be counted. Implementations
          should use the longest filter supported by the hardware that is less than
          or equal to this value. The default is 0 (no filter). *(Supported on ESP32)*
        """
        ...

    def deinit(self) -> None:
        """
        Stops the Counter, disabling any interrupts and releasing hardware resources.
        A Soft Reset should deinitialize all Counter objects.
        """
        ...

    def value(self, value: Optional[Any] = None) -> Incomplete:
        """
        Get, and optionally set, the counter value as a signed integer.
        Implementations must aim to do the get and set atomically (i.e. without
        leading to skipped counts).

        This counter value could exceed the range of a :term:`small integer`, which
        means that calling :meth:`Counter.value` could cause a heap allocation, but
        implementations should aim to ensure that internal state only uses small
        integers and therefore will not allocate until the user calls
        :meth:`Counter.value`.

        For example, on ESP32, the internal state counts overflows of the hardware
        counter (every 32000 counts), which means that it will not exceed the small
        integer range until ``2**30 * 32000`` counts (slightly over 1 year at 1MHz).

        In general, it is recommended that you should use ``Counter.value(0)`` to reset
        the counter (i.e. to measure the counts since the last call), and this will
        avoid this problem.
        """
        ...
