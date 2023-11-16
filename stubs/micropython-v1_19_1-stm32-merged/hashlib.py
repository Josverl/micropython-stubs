"""
Module: 'hashlib' on micropython-v1.19.1-stm32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'stm32', 'port': 'stm32', 'machine': 'PYBv1.1 with STM32F405RG', 'release': '1.19.1', 'nodename': 'pyboard', 'name': 'micropython', 'family': 'micropython', 'sysname': 'pyboard', 'version': '1.19.1'}
# Stubber: 1.9.11
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
