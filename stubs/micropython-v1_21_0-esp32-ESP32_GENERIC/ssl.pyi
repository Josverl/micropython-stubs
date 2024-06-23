"""
Module: 'ssl' on micropython-v1.21.0-esp32-ESP32_GENERIC
"""

# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.21.0', 'cpu': 'ESP32'}
# Stubber: v1.20.0
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
