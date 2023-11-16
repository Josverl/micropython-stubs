"""
Module: 'uhashlib' on micropython-v1.21.0-rp2-RPI_PICO_W
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
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


class sha1:
    """
    Create an SHA1 hasher object and optionally feed ``data`` into it.
    """

    def digest(self, *args, **kwargs) -> Incomplete:
        ...

    def update(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, data: Optional[Any] = ...) -> None:
        ...
