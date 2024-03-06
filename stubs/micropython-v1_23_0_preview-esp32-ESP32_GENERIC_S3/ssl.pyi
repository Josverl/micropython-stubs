"""
Module: 'ssl' on micropython-v1.23.0-preview-esp32-ESP32_GENERIC_S3
"""
# MCU: {'version': '1.23.0-preview', 'mpy': 'v6.2', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'family': 'micropython', 'build': 'preview.176.g90e517862', 'arch': 'xtensawin', 'ver': '1.23.0-preview-preview.176.g90e517862', 'cpu': 'ESP32S3'}
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
    def wrap_socket(self, *args, **kwargs) -> Incomplete: ...
    def load_cert_chain(self, *args, **kwargs) -> Incomplete: ...

    verify_mode: Incomplete  ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None: ...
