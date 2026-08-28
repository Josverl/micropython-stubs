"""
Module: 'ssl' on micropython-v1.29.0-esp32-ESP32_GENERIC_S2
"""

# MCU: {'variant': '', 'build': '', 'arch': 'xtensawin', 'port': 'esp32', 'board': 'ESP32_GENERIC_S2', 'board_id': 'ESP32_GENERIC_S2', 'mpy': 'v6.3', 'ver': '1.29.0', 'family': 'micropython', 'cpu': 'ESP32-S2', 'version': '1.29.0'}
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

def wrap_socket(x0, x1, x2, x3) -> Incomplete: ...

class SSLContext:
    def load_verify_locations(self, x1, x2) -> Incomplete: ...
    def wrap_socket(self, x1, x2, x3, x4) -> Incomplete: ...
    def load_cert_chain(self, x1, x2) -> Incomplete: ...

    verify_mode: Incomplete  ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None: ...
