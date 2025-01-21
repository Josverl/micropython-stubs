"""
Asynchronous I/O scheduler for writing concurrent code.

Stream functions
"""

from __future__ import annotations

from collections.abc import Generator
from typing import Any, Coroutine

from _typeshed import Incomplete

class Stream:
    """
    This represents a TCP stream connection.  To minimise code this class implements
    both a reader and a writer, and both ``StreamReader`` and ``StreamWriter`` alias to
    this class.
    """

    s: Incomplete
    e: Incomplete
    out_buf: bytes
    def __init__(self, s, e={}) -> None:
        """
        This represents a TCP stream connection.  To minimise code this class implements
        both a reader and a writer, and both ``StreamReader`` and ``StreamWriter`` alias to
        this class.
        """

    def get_extra_info(self, v) -> str:
        """
        Get extra information about the stream, given by *v*.  The valid values for *v* are:
        ``peername``.
        """
        ...

    def close(self) -> None:
        """
        Close the stream.
        """
        ...

    async def wait_closed(self) -> None:
        """
        Wait for the stream to close.

        This is a coroutine.
        """
        ...

    def read(self, n: int = -1) -> Generator[Incomplete, None, Incomplete]:
        """
        Read up to *n* bytes and return them.  If *n* is not provided or -1 then read all
        bytes until EOF.  The returned value will be an empty bytes object if EOF is
        encountered before any bytes are read.

        This is a coroutine.
        """
        ...

    def readinto(self, buf) -> Generator[Incomplete, None, Incomplete]:
        """
        Read up to n bytes into *buf* with n being equal to the length of *buf*.

        Return the number of bytes read into *buf*.

        This is a coroutine, and a MicroPython extension.
        """
        ...

    def readexactly(self, n) -> Generator[Incomplete, None, Incomplete]:
        """
        Read exactly *n* bytes and return them as a bytes object.

        Raises an ``EOFError`` exception if the stream ends before reading *n* bytes.

        This is a coroutine.
        """
        ...

    def readline(self) -> Generator[Incomplete, None, Incomplete]:
        """
        Read a line and return it.

        This is a coroutine.
        """
        ...

    def write(self, buf) -> None:
        """
        Accumulated *buf* to the output buffer.  The data is only flushed when
        `Stream.drain` is called.  It is recommended to call `Stream.drain` immediately
        after calling this function.
        """
        ...

    def drain(self) -> Generator[Incomplete, Incomplete, Incomplete]:
        """
        Drain (write) all buffered output data out to the stream.

        This is a coroutine.
        """
        ...

def open_connection(
    host, port, ssl: Incomplete | None = None, server_hostname: Incomplete | None = None
) -> Generator[Incomplete, None, Incomplete]:
    """
    Open a TCP connection to the given *host* and *port*.  The *host* address will be
    resolved using `socket.getaddrinfo`, which is currently a blocking call.
    If *ssl* is a `ssl.SSLContext` object, this context is used to create the transport;
    if *ssl* is ``True``, a default context is used.

    Returns a pair of streams: a reader and a writer stream.
    Will raise a socket-specific ``OSError`` if the host could not be resolved or if
    the connection could not be made.

    This is a coroutine.
    """
    ...

class Server:
    """
    This represents the server class returned from `start_server`.  It can be used
    in an ``async with`` statement to close the server upon exit.
    """

    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
    state: bool
    def close(self) -> None:
        """
        Close the server.
        """
        ...

    async def wait_closed(self) -> None:
        """
        Wait for the server to close.

        This is a coroutine.
        """
        ...

    async def _serve(self, s, cb, ssl) -> Generator[Incomplete]: ...

async def start_server(
    cb, host, port, backlog: int = 5, ssl: Incomplete | None = None
) -> Coroutine[Server, Any, Any]:
    """
    Start a TCP server on the given *host* and *port*.  The *callback* will be
    called with incoming, accepted connections, and be passed 2 arguments: reader
    and writer streams for the connection.

    If *ssl* is a `ssl.SSLContext` object, this context is used to create the transport.

    Returns a `Server` object.

    This is a coroutine.
    """
    ...

async def stream_awrite(self, buf, off: int = 0, sz: int = -1) -> None: ...

class StreamReader:
    """
    Represents a reader object that provides APIs to read data from the IO stream. As an asynchronous iterable, the object supports the `async for` statement.
    It is not recommended to instantiate `StreamReader` objects directly; use open_connection() and start_server() instead.
    """

    # TODO: not documented in the micropython reference, but available runtime

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
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

class StreamWriter:
    """
    Represents a writer object that provides APIs to write data to the IO stream.
    It is not recommended to instantiate `StreamWriter` objects directly; use open_connection() and start_server() instead.
    """

    # TODO: not documented in the micropython reference, but available runtime

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
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
