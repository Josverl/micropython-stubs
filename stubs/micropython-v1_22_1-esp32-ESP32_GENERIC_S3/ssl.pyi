"""
Module: 'ssl' on micropython-v1.22.1-esp32-ESP32_GENERIC_S3
"""
# MCU: {'version': '1.22.1', 'mpy': 'v6.2', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.22.1', 'cpu': 'ESP32S3'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete

MBEDTLS_VERSION: str = "mbed TLS 3.4.1"
PROTOCOL_TLS_SERVER: int = 1
PROTOCOL_TLS_CLIENT: int = 0
CERT_NONE: int = 0
CERT_REQUIRED: int = 2
CERT_OPTIONAL: int = 1

def wrap_socket(*args, **kwargs) -> Incomplete: ...

class SSLContext:
    def load_verify_locations(self, *args, **kwargs) -> Incomplete: ...
    def set_ciphers(self, *args, **kwargs) -> Incomplete: ...
    def wrap_socket(self, *args, **kwargs) -> Incomplete: ...
    def load_cert_chain(self, *args, **kwargs) -> Incomplete: ...
    def get_ciphers(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
