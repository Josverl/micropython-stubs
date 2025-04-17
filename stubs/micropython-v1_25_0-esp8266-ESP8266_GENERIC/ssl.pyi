"""
Module: 'ssl' on micropython-v1.25.0-esp8266-ESP8266_GENERIC
"""
# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensa', 'ver': '1.25.0', 'cpu': 'ESP8266'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

PROTOCOL_TLS_CLIENT: Final[int] = 0
PROTOCOL_TLS_SERVER: Final[int] = 1
CERT_NONE: Final[int] = 0
def wrap_socket(*args, **kwargs) -> Incomplete:
    ...


class SSLContext():
    def load_verify_locations(self, *args, **kwargs) -> Incomplete:
        ...

    def wrap_socket(self, *args, **kwargs) -> Incomplete:
        ...

    def load_cert_chain(self, *args, **kwargs) -> Incomplete:
        ...

    verify_mode: Incomplete ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None:
        ...

