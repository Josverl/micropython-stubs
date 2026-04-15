"""
Module: 'ssl' on micropython-v1.29.0-preview-esp32-ESP32_GENERIC
"""

# MCU: {'variant': '', 'build': 'preview.381.g50348ce0eb.dirty', 'arch': 'xtensawin', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'board_id': 'ESP32_GENERIC', 'mpy': 'v6.3', 'ver': '1.29.0-preview-preview.381.g50348ce0eb.dirty', 'family': 'micropython', 'cpu': 'ESP32', 'version': '1.29.0-preview'}
# Stubber: v1.28.1
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

PROTOCOL_TLS_SERVER: Final[int] = 1
PROTOCOL_DTLS_CLIENT: Final[int] = 2
PROTOCOL_DTLS_SERVER: Final[int] = 3
PROTOCOL_TLS_CLIENT: Final[int] = 0
MBEDTLS_VERSION: Final[str] = "Mbed TLS 3.6.4"
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
