"""
Module: 'hashlib' on micropython-v1.20.0-rp2-PICO_W
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'rp2', 'board': 'PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.12.2
from typing import Optional, Any
from _typeshed import Incomplete as Incomplete


class sha256:
    """
    Create an SHA256 hasher object and optionally feed ``data`` into it.
    """

    def digest(self, *args, **kwargs) -> Any:
        ...

    def update(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, data: Optional[Any] = ...) -> None:
        ...


class sha1:
    """
    Create an SHA1 hasher object and optionally feed ``data`` into it.
    """

    def digest(self, *args, **kwargs) -> Any:
        ...

    def update(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, data: Optional[Any] = ...) -> None:
        ...
