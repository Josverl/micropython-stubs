"""
Module: 'ssl' on micropython-v1.21.0-rp2-RPI_PICO_W
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

CERT_REQUIRED = 2  # type: int
PROTOCOL_TLS_CLIENT = 0  # type: int
PROTOCOL_TLS_SERVER = 1  # type: int
CERT_OPTIONAL = 1  # type: int
CERT_NONE = 0  # type: int


def wrap_socket(*args, **kwargs) -> Incomplete:
    ...


class SSLContext:
    def wrap_socket(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
