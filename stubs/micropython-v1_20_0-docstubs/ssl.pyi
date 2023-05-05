"""
TLS/SSL wrapper for socket objects. See: https://docs.micropython.org/en/v1.20.0/library/ssl.html

|see_cpython_module| :mod:`python:ssl` https://docs.python.org/3/library/ssl.html .

This module provides access to Transport Layer Security (previously and
widely known as “Secure Sockets Layer”) encryption and peer authentication
facilities for network sockets, both client-side and server-side.
"""

# source version: v1_20_0
# origin module:: repos/micropython/docs/library/ssl.rst
from typing import Any

SSLError: Any = ...
"""This exception does NOT exist. Instead its base class, OSError, is used."""
CERT_NONE: Any = ...
"""Supported values for *cert_reqs* parameter."""
CERT_OPTIONAL: Any = ...
"""Supported values for *cert_reqs* parameter."""
CERT_REQUIRED: Any = ...
"""Supported values for *cert_reqs* parameter."""

def wrap_socket(
    sock, server_side=False, keyfile=None, certfile=None, cert_reqs=None, cadata=None, server_hostname=None, do_handshake=True
) -> Any:
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

    - *cert_reqs* determines whether the peer (server or client) must present a valid certificate.
      Note that for mbedtls based ports, ``ssl.CERT_NONE`` and ``ssl.CERT_OPTIONAL`` will not
      validate any certificate, only ``ssl.CERT_REQUIRED`` will.

    - *cadata* is a bytes object containing the CA certificate chain (in DER format) that will
      validate the peer's certificate.  Currently only a single DER-encoded certificate is supported.

    - *server_hostname* is for use as a client, and sets the hostname to check against the received
      server certificate.  It also sets the name for Server Name Indication (SNI), allowing the server
      to present the proper certificate.

    Depending on the underlying module implementation in a particular
    :term:`MicroPython port`, some or all keyword arguments above may be not supported.
    """
    ...
