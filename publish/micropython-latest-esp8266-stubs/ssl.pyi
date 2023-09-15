"""
TLS/SSL wrapper for socket objects.

MicroPython module: https://docs.micropython.org/en/latest/library/ssl.html

CPython module: :mod:`python:ssl` https://docs.python.org/3/library/ssl.html .

This module provides access to Transport Layer Security (previously and
widely known as “Secure Sockets Layer”) encryption and peer authentication
facilities for network sockets, both client-side and server-side.
"""
from typing import Any
from _typeshed import Incomplete
from stdlib.ssl import *

def wrap_socket(
    sock, server_side=False, keyfile=None, certfile=None, cert_reqs=None, cadata=None, server_hostname=None, do_handshake=True
) -> wrappedsocket:
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
