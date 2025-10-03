"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/
"""

from typing import Any, Awaitable

class _Response:
    """
    Response wrapper class for fetch API responses.

    Wraps the JavaScript Response object and provides methods to extract
    the response body in various formats.
    """

    def __init__(self, response: Any) -> None:
        """
        Initialize a Response wrapper.

        Args:
            response: The JavaScript Response object to wrap
        """
        ...

    def __getattr__(self, attr: str) -> Any:
        ...

    async def arrayBuffer(self) -> memoryview:
        """
        Read the response body as an ArrayBuffer.

        Returns:
            A memoryview of the response body bytes
        """
        ...

    async def blob(self) -> Any:
        """
        Read the response body as a Blob.

        Returns:
            A JavaScript Blob object
        """
        ...

    async def bytearray(self) -> bytearray:
        """
        Read the response body as a Python bytearray.

        Returns:
            The response body as a bytearray
        """
        ...

    async def json(self) -> Any:
        """
        Parse the response body as JSON.

        Returns:
            The parsed JSON data (dict, list, or primitive types)
        """
        ...

    async def text(self) -> str:
        """
        Read the response body as text.

        Returns:
            The response body as a string
        """
        ...

class _DirectResponse:
    """
    Direct response wrapper for immediate fetch responses.

    Provides direct access to response data without additional wrapping.
    """

    @staticmethod
    def setup(promise: Any, response: Any) -> _Response:
        """
        Setup a response wrapper from a promise and response object.

        Args:
            promise: The JavaScript Promise object
            response: The JavaScript Response object

        Returns:
            A _Response wrapper instance
        """
        ...

    def __init__(self, promise: Any) -> None:
        """
        Initialize a DirectResponse wrapper.

        Args:
            promise: The JavaScript Promise to wrap
        """
        ...

    async def arrayBuffer(self) -> memoryview:
        """
        Read the response body as an ArrayBuffer.

        Returns:
            A memoryview of the response body bytes
        """
        ...

    async def blob(self) -> Any:
        """
        Read the response body as a Blob.

        Returns:
            A JavaScript Blob object
        """
        ...

    async def bytearray(self) -> bytearray:
        """
        Read the response body as a Python bytearray.

        Returns:
            The response body as a bytearray
        """
        ...

    async def json(self) -> Any:
        """
        Parse the response body as JSON.

        Returns:
            The parsed JSON data (dict, list, or primitive types)
        """
        ...

    async def text(self) -> str:
        """
        Read the response body as text.

        Returns:
            The response body as a string
        """
        ...

def fetch(url: str, **kw: Any) -> Awaitable[_Response]:
    """
    Fetch a resource from the network.

    This is a Python wrapper around the JavaScript Fetch API, providing
    an async interface for making HTTP requests.

    Args:
        url: The URL to fetch
        **kw: Additional keyword arguments passed to the fetch request
              (e.g., method, headers, body, mode, credentials, etc.)

    Returns:
        An awaitable that resolves to a _Response object

    Example:
        response = await fetch("https://api.example.com/data")
        data = await response.json()
    """
    ...
