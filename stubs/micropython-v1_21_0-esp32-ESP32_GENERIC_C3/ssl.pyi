"""
Module: 'ssl' on micropython-v1.21.0-esp32-ESP32_GENERIC_C3
"""

# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'ESP32_GENERIC_C3', 'family': 'micropython', 'build': '', 'arch': '', 'ver': '1.21.0', 'cpu': 'ESP32C3'}
# Stubber: v1.23.0
from __future__ import annotations
from _typeshed import Incomplete

CERT_REQUIRED: int = 2
PROTOCOL_TLS_CLIENT: int = 0
PROTOCOL_TLS_SERVER: int = 1
CERT_OPTIONAL: int = 1
CERT_NONE: int = 0

def wrap_socket(*args, **kwargs) -> Incomplete: ...

class SSLContext:
    def wrap_socket(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
