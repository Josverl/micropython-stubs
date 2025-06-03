""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, Optional
from typing_extensions import TypeVar, TypeAlias, Awaitable

class PPP:
    """
    Create a PPP driver object.

    Arguments are:

      - *stream* is any object that supports the stream protocol, but is most commonly a
        :class:`machine.UART` instance.  This stream object must have an ``irq()`` method
        and an ``IRQ_RXIDLE`` constant, for use by `PPP.connect`.
    """

    SEC_NONE: Incomplete
    """The type of connection security."""
    SEC_PAP: Incomplete
    """The type of connection security."""
    SEC_CHAP: Incomplete
    """The type of connection security."""
    def __init__(self, stream) -> None: ...
    def connect(self, security=SEC_NONE, user=None, key=None) -> Incomplete:
        """
        Initiate a PPP connection with the given parameters:

          - *security* is the type of security, either ``PPP.SEC_NONE``, ``PPP.SEC_PAP``,
            or ``PPP.SEC_CHAP``.
          - *user* is an optional user name to use with the security mode.
          - *key* is an optional password to use with the security mode.

        When this method is called the underlying stream has its interrupt configured to call
        `PPP.poll` via ``stream.irq(ppp.poll, stream.IRQ_RXIDLE)``.  This makes sure the
        stream is polled, and data passed up the PPP stack, wheverver data becomes available
        on the stream.

        The connection proceeds asynchronously, in the background.
        """
        ...

    def disconnect(self) -> Incomplete:
        """
        Terminate the connection.  This must be called to cleanly close the PPP connection.
        """
        ...

    def isconnected(self) -> bool:
        """
        Returns ``True`` if the PPP link is connected and up.
        Returns ``False`` otherwise.
        """
        ...

    def status(self) -> Incomplete:
        """
        Returns the PPP status.
        """
        ...

    def config(self, config_parameters) -> Incomplete:
        """
        Sets or gets parameters of the PPP interface. The only parameter that can be
        retrieved and set is the underlying stream, using::

           stream = PPP.config("stream")
           PPP.config(stream=stream)
        """
        ...

    def ipconfig(self, param) -> Incomplete:
        """
        See `AbstractNIC.ipconfig`.
        """
        ...

    def ifconfig(self, configtuple: Optional[Any] = None) -> Incomplete:
        """
        See `AbstractNIC.ifconfig`.
        """
        ...

    def poll(self) -> Incomplete:
        """
        Poll the underlying stream for data, and pass it up the PPP stack.
        This is called automatically if the stream is a UART with a RXIDLE interrupt,
        so it's not usually necessary to call it manually.
        """
        ...
