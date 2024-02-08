from _typeshed import Incomplete
from tls import CERT_OPTIONAL as CERT_OPTIONAL, CERT_REQUIRED as CERT_REQUIRED, MBEDTLS_VERSION as MBEDTLS_VERSION

class SSLContext:
    _context: Incomplete
    def __init__(self, *args) -> None: ...
    @property
    def verify_mode(self): ...
    @verify_mode.setter
    def verify_mode(self, val) -> None: ...
    def load_cert_chain(self, certfile, keyfile) -> None: ...
    def load_verify_locations(self, cafile: Incomplete | None = ..., cadata: Incomplete | None = ...) -> None: ...
    def wrap_socket(self, sock, server_side: bool = ..., do_handshake_on_connect: bool = ..., server_hostname: Incomplete | None = ...): ...

def wrap_socket(
    sock,
    server_side: bool = ...,
    key: Incomplete | None = ...,
    cert: Incomplete | None = ...,
    cert_reqs=...,
    cadata: Incomplete | None = ...,
    server_hostname: Incomplete | None = ...,
    do_handshake: bool = ...,
): ...
