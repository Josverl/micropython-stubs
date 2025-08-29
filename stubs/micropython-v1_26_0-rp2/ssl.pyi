"""
Module: 'ssl' on micropython-v1.26.0-rp2
"""

# MCU: {'family': 'micropython', 'version': '1.26.0', 'build': '', 'ver': '1.26.0', 'port': 'rp2', 'board': '', 'cpu': 'RP2040', 'mpy': 'v6.3', 'arch': 'armv6m'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

PROTOCOL_TLS_SERVER: int = 1
PROTOCOL_DTLS_CLIENT: int = 2
PROTOCOL_DTLS_SERVER: int = 3
PROTOCOL_TLS_CLIENT: int = 0
MBEDTLS_VERSION: str = "Mbed TLS 3.6.2"
CERT_NONE: int = 0
CERT_OPTIONAL: int = 1
CERT_REQUIRED: int = 2

def wrap_socket(*args, **kwargs) -> Incomplete: ...

class SSLContext:
    def load_verify_locations(self, *args, **kwargs) -> Incomplete: ...
    def wrap_socket(self, *args, **kwargs) -> Incomplete: ...
    def load_cert_chain(self, *args, **kwargs) -> Incomplete: ...

    verify_mode: Incomplete  ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None: ...
