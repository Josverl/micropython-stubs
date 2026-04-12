"""
Module: 'ssl' on micropython-v1.28.0-rp2-ARDUINO_NANO_RP2040_CONNECT
"""

# MCU: {'mpy': 'v6.3', 'build': '', 'ver': '1.28.0', 'arch': 'armv6m', 'version': '1.28.0', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'family': 'micropython', 'board_id': 'ARDUINO_NANO_RP2040_CONNECT', 'variant': '', 'cpu': 'RP2040'}
# Stubber: v1.28.1
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

def wrap_socket(*args, **kwargs) -> Incomplete: ...

class SSLContext:
    def load_verify_locations(self, *args, **kwargs) -> Incomplete: ...
    def wrap_socket(self, *args, **kwargs) -> Incomplete: ...
    def load_cert_chain(self, *args, **kwargs) -> Incomplete: ...

    verify_mode: Incomplete  ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None: ...
