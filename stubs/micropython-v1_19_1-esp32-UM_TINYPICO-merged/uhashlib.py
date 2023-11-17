"""
Module: 'uhashlib' on micropython-v1.19.1-esp32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Optional, Any
from _typeshed import Incomplete as Incomplete


class sha1:
    """
    Create an SHA1 hasher object and optionally feed ``data`` into it.
    """

    def __init__(self, data: Optional[Any] = ...) -> None:
        """"""
        ...

    def update(self, *args, **kwargs) -> Any:
        ...

    def digest(self, *args, **kwargs) -> Any:
        ...


class sha256:
    """
    Create an SHA256 hasher object and optionally feed ``data`` into it.
    """

    def __init__(self, data: Optional[Any] = ...) -> None:
        """"""
        ...

    def update(self, *args, **kwargs) -> Any:
        ...

    def digest(self, *args, **kwargs) -> Any:
        ...
