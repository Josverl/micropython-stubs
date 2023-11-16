"""
Module: 'hashlib' on micropython-v1.21.0-samd-SEEED_WIO_TERMINAL
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51P19A', 'arch': 'armv7emsp'}
# Stubber: v1.13.8
from typing import Optional, Any
from _typeshed import Incomplete as Incomplete, Incomplete


class sha256:
    """
    Create an SHA256 hasher object and optionally feed ``data`` into it.
    """

    def digest(self, *args, **kwargs) -> Incomplete:
        ...

    def update(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, data: Optional[Any] = ...) -> None:
        ...
