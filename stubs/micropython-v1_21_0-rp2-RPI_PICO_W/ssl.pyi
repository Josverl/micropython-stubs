"""
Module: 'ssl' on micropython-v1.21.0-rp2-RPI_PICO_W
"""

# MCU: {'build': '', 'ver': '1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
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
