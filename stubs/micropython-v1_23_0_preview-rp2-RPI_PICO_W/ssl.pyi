"""
Module: 'ssl' on micropython-v1.23.0-preview-rp2-RPI_PICO_W
"""
# MCU: {'build': 'preview.205.g2b6f81f2b', 'ver': '1.23.0-preview-preview.205.g2b6f81f2b', 'version': '1.23.0-preview', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete

MBEDTLS_VERSION: str = "Mbed TLS 3.5.1"
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
