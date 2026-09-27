"""
TLS/SSL wrapper for socket objects.

MicroPython module: https://docs.micropython.org/en/v1.24.0/library/ssl.html

CPython module: :mod:`python:ssl` https://docs.python.org/3/library/ssl.html .

This module provides access to Transport Layer Security (previously and
widely known as “Secure Sockets Layer”) encryption and peer authentication
facilities for network sockets, both client-side and server-side.

---
Module: 'tls' on micropython-v1.29.0-esp32-ESP32_GENERIC_C2
"""

# MCU: {'variant': '', 'build': '', 'arch': 'rv32imc', 'port': 'esp32', 'board': 'ESP32_GENERIC_C2', 'board_id': 'ESP32_GENERIC_C2', 'mpy': 'v6.3', 'ver': '1.29.0', 'family': 'micropython', 'cpu': 'ESP32-C2', 'version': '1.29.0'}
# Stubber: v1.28.6
from __future__ import annotations

import socket
from ssl import SSLSocket
from typing import Final

from _mpy_shed import mp_available
from _typeshed import Incomplete

PROTOCOL_TLS_SERVER: Final[int] = 1
PROTOCOL_DTLS_CLIENT: Final[int] = 2
PROTOCOL_DTLS_SERVER: Final[int] = 3
PROTOCOL_TLS_CLIENT: Final[int] = 0
MBEDTLS_VERSION: Final[str] = "Mbed TLS 3.6.5"
CERT_NONE: Final[int] = 0
CERT_OPTIONAL: Final[int] = 1
CERT_REQUIRED: Final[int] = 2

class SSLContext:
    """
    Create a new SSLContext instance.  The *protocol* argument must be one of the ``PROTOCOL_*``
    constants.
    """

    # Implemented by the C level attr handler, so not visible to createstubs.
    # mp_available
    verify_mode: int
    """Certificate verification mode: `CERT_NONE`, `CERT_OPTIONAL` or `CERT_REQUIRED`."""
    def load_verify_locations(self, cafile=None, cadata: bytes | None = None) -> None:
        """
        Load the CA certificate chain that will validate the peer's certificate.
        *cafile* is the file path of the CA certificates.  *cadata* is a bytes object
        containing the CA certificates.  Only one of these arguments should be provided.
        """
        ...
    def set_ciphers(self, *args, **kwargs) -> Incomplete: ...
    def wrap_socket(
        self,
        sock: socket.socket,
        *,
        server_side: bool = False,
        do_handshake_on_connect: bool = True,
        server_hostname: str | None = None,
    ) -> SSLSocket:
        """
        Takes a `stream` *sock* (usually socket.socket instance of ``SOCK_STREAM`` type),
        and returns an instance of ssl.SSLSocket, wrapping the underlying stream.
        The returned object has the usual `stream` interface methods like
        ``read()``, ``write()``, etc.

        - *server_side* selects whether the wrapped socket is on the server or client side.
          A server-side SSL socket should be created from a normal socket returned from
          :meth:`~socket.socket.accept()` on a non-SSL listening server socket.

        - *do_handshake_on_connect* determines whether the handshake is done as part of the ``wrap_socket``
          or whether it is deferred to be done as part of the initial reads or writes
          For blocking sockets doing the handshake immediately is standard. For non-blocking
          sockets (i.e. when the *sock* passed into ``wrap_socket`` is in non-blocking mode)
          the handshake should generally be deferred because otherwise ``wrap_socket`` blocks
          until it completes. Note that in AXTLS the handshake can be deferred until the first
          read or write but it then blocks until completion.

        - *server_hostname* is for use as a client, and sets the hostname to check against the received
          server certificate.  It also sets the name for Server Name Indication (SNI), allowing the server
          to present the proper certificate.
        """
        ...
    @mp_available()  # force merge
    def load_cert_chain(self, certfile, keyfile) -> None:
        """
        Load a private key and the corresponding certificate.  The *certfile* is a string
        with the file path of the certificate.  The *keyfile* is a string with the file path
        of the private key.

        Admonition:Difference to CPython
           :class: attention

           MicroPython extension: *certfile* and *keyfile* can be bytes objects instead of
           strings, in which case they are interpreted as the actual certificate/key data.
        """
        ...
    def get_ciphers(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *args) -> None: ...
