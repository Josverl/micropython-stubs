"""
Module: 'tls' on micropython-v1.29.0-esp32-ESP32_GENERIC_P4-PRE_REV3_C6_WIFI
"""

# MCU: {'variant': 'PRE_REV3_C6_WIFI', 'build': '', 'arch': 'unknown', 'port': 'esp32', 'board': 'ESP32_GENERIC_P4', 'board_id': 'ESP32_GENERIC_P4-PRE_REV3_C6_WIFI', 'mpy': 'v6.3', 'ver': '1.29.0', 'family': 'micropython', 'cpu': 'ESP32-P4', 'version': '1.29.0'}
# Stubber: v1.28.6
from __future__ import annotations

from typing import Final

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
    def load_verify_locations(self, *args, **kwargs) -> Incomplete: ...
    def set_ciphers(self, *args, **kwargs) -> Incomplete: ...
    def wrap_socket(self, *args, **kwargs) -> Incomplete: ...
    def load_cert_chain(self, *args, **kwargs) -> Incomplete: ...
    def get_ciphers(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
