"""
TLS/SSL wrapper for socket objects.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/ssl.html

CPython module: :mod:`python:ssl` https://docs.python.org/3/library/ssl.html .

This module provides access to Transport Layer Security (previously and
widely known as “Secure Sockets Layer”) encryption and peer authentication
facilities for network sockets, both client-side and server-side.
"""

# source version: v1.26.1
# origin module:: repos/micropython/docs/library/ssl.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing import List
from typing_extensions import TypeVar, TypeAlias, Awaitable
from typing_extensions import TypeAlias
from _mpy_shed import mp_available, StrOrBytesPath
import socket
from tls import *

SSLError: Incomplete
"""This exception does NOT exist. Instead its base class, OSError, is used."""
PROTOCOL_TLS_CLIENT: Incomplete
"""Supported values for the *protocol* parameter."""
PROTOCOL_TLS_SERVER: Incomplete
"""Supported values for the *protocol* parameter."""
PROTOCOL_DTLS_CLIENT  : Incomplete # (when DTLS support is enabled): Incomplete
"""Supported values for the *protocol* parameter."""
PROTOCOL_DTLS_SERVER  : Incomplete # (when DTLS support is enabled): Incomplete
"""Supported values for the *protocol* parameter."""
CERT_NONE: Incomplete
"""\
Supported values for *cert_reqs* parameter, and the :attr:`SSLContext.verify_mode`
attribute.
"""
CERT_OPTIONAL: Incomplete
"""\
Supported values for *cert_reqs* parameter, and the :attr:`SSLContext.verify_mode`
attribute.
"""
CERT_REQUIRED: Incomplete
"""\
Supported values for *cert_reqs* parameter, and the :attr:`SSLContext.verify_mode`
attribute.
"""
MBEDTLS_VERSION: str = "Mbed TLS 3.6.0"
class SSLContext():
    """
    Create a new SSLContext instance.  The *protocol* argument must be one of the ``PROTOCOL_*``
    constants.
    """
    def __init__(self, *args) -> None:
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
    def load_verify_locations(self, cafile=None, cadata: bytes | None = None) -> None:
        """
           Load the CA certificate chain that will validate the peer's certificate.
           *cafile* is the file path of the CA certificates.  *cadata* is a bytes object
           containing the CA certificates.  Only one of these arguments should be provided.
        """
        ...
    def get_ciphers(self) -> List[str]:
        """
           Get a list of enabled ciphers, returned as a list of strings.
        """
        ...
    def set_ciphers(self, ciphers) -> None:
        """
           Set the available ciphers for sockets created with this context.  *ciphers* should be
           a list of strings in the `IANA cipher suite format <https://wiki.mozilla.org/Security/Cipher_Suites>`_ .
        """
        ...
    def wrap_socket(self,
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
        
           - *client_id* is a MicroPython-specific extension argument used only when implementing a DTLS
             Server. See :ref:`dtls` for details.
        """
        ...

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# End duplicated section 
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


@mp_available()  # force merge
def wrap_socket(
    sock: socket.socket,
    *,
    server_side: bool = False,
    key: Incomplete = None,
    cert: Incomplete = None,
    cert_reqs: int = 0,
    cadata: bytes | None = None,
    server_hostname: str | None = None,
    do_handshake: bool = True,
) -> SSLSocket:
    """
        Wrap the given *sock* and return a new wrapped-socket object.  The implementation
        of this function is to first create an `SSLContext` and then call the `SSLContext.wrap_socket`
        method on that context object.  The arguments *sock*, *server_side* and *server_hostname* are
        passed through unchanged to the method call.  The argument *do_handshake* is passed through as
        *do_handshake_on_connect*.  The remaining arguments have the following behaviour:
    
       - *cert_reqs* determines whether the peer (server or client) must present a valid certificate.
         Note that for mbedtls based ports, ``ssl.CERT_NONE`` and ``ssl.CERT_OPTIONAL`` will not
         validate any certificate, only ``ssl.CERT_REQUIRED`` will.
    
       - *cadata* is a bytes object containing the CA certificate chain (in DER format) that will
         validate the peer's certificate.  Currently only a single DER-encoded certificate is supported.
    
       Depending on the underlying module implementation in a particular
       :term:`MicroPython port`, some or all keyword arguments above may be not supported.
    """
    ...
class SSLSocket:
    #TODO : SSLSocket is undocumented
    # ref: micropython\extmod\modtls_axtls.c ( read ... close) 

    # repos\micropython\extmod\modtls_mbedtls.c
    @mp_available()  # force merge
    def read(self, *argv, **kwargs) -> Incomplete: ...
    @mp_available()  # force merge
    def readinto(self, *argv, **kwargs) -> Incomplete: ...
    @mp_available()  # force merge
    def readline(self, *argv, **kwargs) -> Incomplete: ...
    @mp_available()  # force merge
    def write(self, *argv, **kwargs) -> Incomplete: ...
    @mp_available()  # force merge
    def setblocking(self, *argv, **kwargs) -> Incomplete: ...
    @mp_available()  # force merge
    def close(self, *argv, **kwargs) -> Incomplete: ...
    #if MICROPY_PY_SSL_FINALISER
    @mp_available(macro="MICROPY_PY_SSL_FINALISER")  # force merge
    def __del__(self, *argv, **kwargs) -> Incomplete: ...
    #endif
    # ifdef MICROPY_UNIX_COVERAGE
    @mp_available(macro="MICROPY_UNIX_COVERAGE")  # force merge
    def ioctl(self, *argv, **kwargs) -> Incomplete: ...
    #endif
    #ifdef (MBEDTLS_SSL_KEEP_PEER_CERTIFICATE)
    @mp_available(macro="MBEDTLS_SSL_KEEP_PEER_CERTIFICATE")  # force merge
    def getpeercert(self, *argv, **kwargs) -> Incomplete: ...
    #endif
    @mp_available()  # force merge
    def cipher(self, *argv, **kwargs) -> Incomplete: ...
    #ifdef MBEDTLS_SSL_PROTO_DTLS
    @mp_available(macro="MBEDTLS_SSL_PROTO_DTLS")  # force merge
    def recv(self, *argv, **kwargs) -> Incomplete: ...
    @mp_available(macro="MBEDTLS_SSL_PROTO_DTLS")  # force merge
    def recv_into(self, *argv, **kwargs) -> Incomplete: ...
    @mp_available(macro="MBEDTLS_SSL_PROTO_DTLS")  # force merge
    def send(self, *argv, **kwargs) -> Incomplete: ...
    @mp_available(macro="MBEDTLS_SSL_PROTO_DTLS")  # force merge
    def sendall(self, *argv, **kwargs) -> Incomplete: ...
