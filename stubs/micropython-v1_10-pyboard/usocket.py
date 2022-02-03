"""
Module: 'usocket' on micropython-v1.10-pyboard
"""
# MCU: {'ver': 'v1.10', 'build': '', 'platform': 'pyboard', 'port': 'pyboard', 'machine': 'PYBv1.1 with STM32F405RG', 'release': '1.10.0', 'nodename': 'pyboard', 'name': 'micropython', 'family': 'micropython', 'sysname': 'pyboard', 'version': '1.10.0'}
# Stubber: 1.5.4
from typing import Any

AF_INET = 2  # type: int
AF_INET6 = 10  # type: int
SOCK_DGRAM = 2  # type: int
SOCK_RAW = 3  # type: int
SOCK_STREAM = 1  # type: int


def getaddrinfo(*args, **kwargs) -> Any:
    ...


class socket:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def accept(self, *args, **kwargs) -> Any:
        ...

    def bind(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    def connect(self, *args, **kwargs) -> Any:
        ...

    def listen(self, *args, **kwargs) -> Any:
        ...

    def recv(self, *args, **kwargs) -> Any:
        ...

    def recvfrom(self, *args, **kwargs) -> Any:
        ...

    def send(self, *args, **kwargs) -> Any:
        ...

    def sendto(self, *args, **kwargs) -> Any:
        ...

    def setblocking(self, *args, **kwargs) -> Any:
        ...

    def setsockopt(self, *args, **kwargs) -> Any:
        ...

    def settimeout(self, *args, **kwargs) -> Any:
        ...
