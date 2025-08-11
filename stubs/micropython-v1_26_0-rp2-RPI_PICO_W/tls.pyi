"""
Module: 'tls' on micropython-v1.26.0-rp2-RPI_PICO_W
"""

# MCU: {'mpy': 'v6.3', 'build': '', 'ver': '1.26.0', 'arch': 'armv6m', 'version': '1.26.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'family': 'micropython', 'board_id': 'RPI_PICO_W', 'variant': '', 'cpu': 'RP2040'}
# Stubber: v1.25.1
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

PROTOCOL_TLS_SERVER: Final[int] = 1
PROTOCOL_DTLS_CLIENT: Final[int] = 2
PROTOCOL_DTLS_SERVER: Final[int] = 3
PROTOCOL_TLS_CLIENT: Final[int] = 0
MBEDTLS_VERSION: Final[str] = "Mbed TLS 3.6.2"
CERT_NONE: Final[int] = 0
CERT_OPTIONAL: Final[int] = 1
CERT_REQUIRED: Final[int] = 2

class SSLContext:
    def load_verify_locations(self, *args, **kwargs) -> Incomplete: ...
    def set_ciphers(self, *args, **kwargs) -> Incomplete: ...
    def wrap_socket(self, *args, **kwargs) -> Incomplete: ...
    def load_cert_chain(self, *args, **kwargs) -> Incomplete: ...
    def get_ciphers(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
