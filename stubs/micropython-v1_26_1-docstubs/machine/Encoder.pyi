""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, Optional
from typing_extensions import TypeVar, TypeAlias, Awaitable

class Encoder:
    """
    Returns the singleton Encoder object for the the given *id*. Values of *id*
    depend on a particular port and its hardware. Values 0, 1, etc. are commonly
    used to select hardware block #0, #1, etc.

    Additional arguments are passed to the :meth:`init` method described below,
    and will cause the Encoder instance to be re-initialised and reset.

    On ESP32, the *id* corresponds to a :ref:`PCNT unit <esp32.PCNT>`.
    """
    def __init__(self, id, *args, **kwargs) -> None: ...
    def init(self, phase_a, phase_b, *args, **kwargs) -> Incomplete:
        """
        Initialise and reset the Encoder with the given parameters:

        - *phase_a* specifies the first input pin as a
          :ref:`machine.Pin <machine.Pin>` object.

        - *phase_b* specifies the second input pin as a
          :ref:`machine.Pin <machine.Pin>` object.

        These pins may be omitted on ports that have predefined pins for a given
        hardware block.

        Additional keyword-only parameters that may be supported by a port are:

        - *filter_ns* specifies a minimum period of time in nanoseconds that the
          source signal needs to be stable for a pulse to be counted. Implementations
          should use the longest filter supported by the hardware that is less than
          or equal to this value. The default is 0 (no filter). *(Supported on ESP32)*

        - *phases* specifies the number of signal edges to count and thus the
          granularity of the decoding. e.g. 4 phases corresponds to "4x quadrature
          decoding", and will result in four counts per pulse. Ports may support
          either 1, 2, or 4 phases and the default is 1 phase. *(Supported on ESP32)*
        """
        ...
    def deinit(self) -> None:
        """
        Stops the Encoder, disabling any interrupts and releasing hardware resources.
        A Soft Reset should deinitialize all Encoder objects.
        """
        ...
    def value(self, value: Optional[Any] = None) -> Incomplete:
        """
        Get, and optionally set, the encoder value as a signed integer.
        Implementations should aim to do the get and set atomically.

        See :meth:`machine.Counter.value` for details about overflow of this value.
        """
        ...
