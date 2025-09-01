"""
Module: 'tls' on micropython-v1.26.0-esp8266-ESP8266_GENERIC
"""

# MCU: {'variant': '', 'build': '', 'arch': 'xtensa', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'board_id': 'ESP8266_GENERIC', 'mpy': 'v6.3', 'ver': '1.26.0', 'family': 'micropython', 'cpu': 'ESP8266', 'version': '1.26.0'}
# Stubber: v1.26.0
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

PROTOCOL_TLS_CLIENT: Final[int] = 0
PROTOCOL_TLS_SERVER: Final[int] = 1
CERT_NONE: Final[int] = 0

class SSLContext:
    def wrap_socket(self, *args, **kwargs) -> Incomplete: ...
    def load_cert_chain(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
