""" """

from __future__ import annotations
from _typeshed import Incomplete

class ADCBlock:
    """
    Access the ADC peripheral identified by *id*, which may be an integer
    or string.

    The *bits* argument, if given, sets the resolution in bits of the
    conversion process.  If not specified then the previous or default
    resolution is used.
    """

    def __init__(self, id, *, bits) -> None: ...
    def init(self, *, bits) -> None:
        """
        Configure the ADC peripheral.  *bits* will set the resolution of the
        conversion process.
        """
        ...

    def connect(self, channel, source, *args, **kwargs) -> Incomplete:
        """
        Connect up a channel on the ADC peripheral so it is ready for sampling,
        and return an :ref:`ADC <machine.ADC>` object that represents that connection.

        The *channel* argument must be an integer, and *source* must be an object
        (for example a :ref:`Pin <machine.Pin>`) which can be connected up for sampling.

        If only *channel* is given then it is configured for sampling.

        If only *source* is given then that object is connected to a default
        channel ready for sampling.

        If both *channel* and *source* are given then they are connected together
        and made ready for sampling.

        Any additional keyword arguments are used to configure the returned ADC object,
        via its :meth:`init <machine.ADC.init>` method.
        """
        ...
