"""
Module: 'ussl' on micropython-v1.19.1-esp8266
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp8266', 'port': 'esp8266', 'machine': 'ESP module (1M) with ESP8266', 'release': '1.19.1', 'nodename': 'esp8266', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp8266', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import IO, Any
from _typeshed import Incomplete as Incomplete
from stdlib.ssl import *


def wrap_socket(
    sock,
    server_side: bool = ...,
    keyfile: Incomplete | None = ...,
    certfile: Incomplete | None = ...,
    cert_reqs: Incomplete | None = ...,
    ca_certs: Incomplete | None = ...,
    do_handshake: bool = ...,
) -> IO:
    """
    Takes a `stream` *sock* (usually socket.socket instance of ``SOCK_STREAM`` type),
    and returns an instance of ssl.SSLSocket, which wraps the underlying stream in
    an SSL context. Returned object has the usual `stream` interface methods like
    ``read()``, ``write()``, etc.
    A server-side SSL socket should be created from a normal socket returned from
    :meth:`~socket.socket.accept()` on a non-SSL listening server socket.

    - *do_handshake* determines whether the handshake is done as part of the ``wrap_socket``
      or whether it is deferred to be done as part of the initial reads or writes
      (there is no ``do_handshake`` method as in CPython).
      For blocking sockets doing the handshake immediately is standard. For non-blocking
      sockets (i.e. when the *sock* passed into ``wrap_socket`` is in non-blocking mode)
      the handshake should generally be deferred because otherwise ``wrap_socket`` blocks
      until it completes. Note that in AXTLS the handshake can be deferred until the first
      read or write but it then blocks until completion.

    Depending on the underlying module implementation in a particular
    :term:`MicroPython port`, some or all keyword arguments above may be not supported.
    """
    ...
