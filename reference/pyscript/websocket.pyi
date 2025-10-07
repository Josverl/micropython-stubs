"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/
"""

from typing import Any, Literal

code: dict[str, int]
"""Dictionary of WebSocket close codes (e.g., NORMAL_CLOSURE, GOING_AWAY)."""

protocols: list[str]
"""List of supported WebSocket sub-protocols."""

reason: dict[str, str]
"""Dictionary mapping close codes to reason strings."""

methods: dict[str, str]
"""Dictionary of WebSocket method names."""

class EventMessage:
    """
    Wrapper for WebSocket event messages.

    Provides access to WebSocket event properties such as data,
    origin, and other event-specific attributes.
    """

    def __init__(self, event: Any) -> None:
        """
        Initialize an EventMessage wrapper.

        Args:
            event: The JavaScript WebSocket event object to wrap
        """
        ...

    def __getattr__(self, attr: str) -> Any | memoryview | str:
        """
        Access event attributes.

        Args:
            attr: The attribute name (e.g., 'data', 'origin', 'type')

        Returns:
            The attribute value, which may be a memoryview for binary data,
            a string for text data, or other types depending on the attribute
        """
        ...

class WebSocket:
    """
    PyScript WebSocket client for bidirectional communication.

    Provides a Python interface to the browser's WebSocket API for
    establishing persistent connections to WebSocket servers.
    """

    CONNECTING: Literal[0]
    """WebSocket is connecting (readyState = 0)."""

    OPEN: Literal[1]
    """WebSocket connection is open (readyState = 1)."""

    CLOSING: Literal[2]
    """WebSocket is closing (readyState = 2)."""

    CLOSED: Literal[3]
    """WebSocket is closed (readyState = 3)."""

    def __init__(
        self,
        url: str | None = None,
        protocols: str | list[str] | None = None,
        **kw: Any,
    ) -> None:
        """
        Create a new WebSocket connection.

        Args:
            url: The WebSocket URL to connect to (ws:// or wss://)
            protocols: Optional sub-protocol(s) to use
            **kw: Additional keyword arguments for event handlers
                  (e.g., onopen, onmessage, onerror, onclose)

        Example:
            ws = WebSocket(
                url="wss://example.com/socket",
                onmessage=lambda msg: print(msg.data)
            )
        """
        ...

    def __getattr__(self, attr: str) -> Any:
        ...

    def __setattr__(self, attr: str, value: Any) -> None:
        ...

    def close(self, code: int = 1000, reason: str = "") -> None:
        """
        Close the WebSocket connection.

        Args:
            code: The close status code (default: 1000 for normal closure)
            reason: Optional human-readable reason string

        Example:
            ws.close(1000, "Client closing connection")
        """
        ...

    def send(self, data: str | bytes | bytearray | memoryview) -> None:
        """
        Send data through the WebSocket connection.

        Args:
            data: The data to send. Can be text (str) or binary data
                  (bytes, bytearray, memoryview)

        Example:
            ws.send("Hello, server!")
            ws.send(b"Binary data")
        """
        ...
