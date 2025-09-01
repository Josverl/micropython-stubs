"""
TLS/SSL wrapper for socket objects.

MicroPython module: https://docs.micropython.org/en/v1.24.0/library/ssl.html

CPython module: :mod:`python:ssl` https://docs.python.org/3/library/ssl.html .

This module provides access to Transport Layer Security (previously and
widely known as “Secure Sockets Layer”) encryption and peer authentication
facilities for network sockets, both client-side and server-side.
"""
# MicroPython Implementation is split across two modules: tls and ssl
# This is the tls module 

from __future__ import annotations

from _mpy_shed import mp_available
import socket
from ssl import SSLSocket
from typing import overload

from _typeshed import Incomplete

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# This section is duplicated in tls and ssl modules
# as cpython stdlib does not include a tls module 
# todo: avoid duplication by moving to _mpy_shed
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

MBEDTLS_VERSION: str = "Mbed TLS 3.6.0"
PROTOCOL_TLS_SERVER: int = 1
PROTOCOL_TLS_CLIENT: int = 0
CERT_NONE: int = 0
CERT_REQUIRED: int = 2
CERT_OPTIONAL: int = 1

class SSLContext:
    """
    Create a new SSLContext instance.  The *protocol* argument must be one of the ``PROTOCOL_*``
    constants.
    """

    _context: Incomplete
    def __init__(self, *args) -> None: ...

    # verify_mode: Incomplete  ## <class 'property'> = <property>
    @property
    def verify_mode(self) -> Incomplete: ...
    @verify_mode.setter
    def verify_mode(self, val: Incomplete) -> None: ...

    def load_verify_locations(self, cafile=None, cadata: bytes | None = None) -> None:
        """
        Load the CA certificate chain that will validate the peer's certificate.
        *cafile* is the file path of the CA certificates.  *cadata* is a bytes object
        containing the CA certificates.  Only one of these arguments should be provided.
        """
        ...

    def wrap_socket(
        self,
        sock: socket,
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


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# End duplicated section 
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
