"""
Module: 'ssl' on micropython-v1.22.0.preview-unix-linux_[GCC_9.4.0]_version
"""
# MCU: {'family': 'micropython', 'version': '1.22.0.preview', 'build': '', 'ver': 'v1.22.0.preview', 'port': 'unix', 'board': 'linux_[GCC_9.4.0]_version', 'cpu': '', 'mpy': '', 'arch': ''}
# Stubber: v1.15.1
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
