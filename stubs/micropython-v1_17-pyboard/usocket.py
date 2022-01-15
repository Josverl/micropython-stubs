"""
Module: 'usocket' on micropython-v1.17-pyboard
"""
# MCU: {'ver': 'v1.17', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.17.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.17.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.2
from typing import Any

AF_INET = 2  # type: int
AF_INET6 = 10  # type: int
SOCK_DGRAM = 2  # type: int
SOCK_RAW = 3  # type: int
SOCK_STREAM = 1  # type: int


def getaddrinfo(*args) -> Any:
    ...


class socket:
    """"""

    def close(self, *args) -> Any:
        ...

    def send(self, *args) -> Any:
        ...

    def accept(self, *args) -> Any:
        ...

    def bind(self, *args) -> Any:
        ...

    def connect(self, *args) -> Any:
        ...

    def listen(self, *args) -> Any:
        ...

    def recv(self, *args) -> Any:
        ...

    def recvfrom(self, *args) -> Any:
        ...

    def sendto(self, *args) -> Any:
        ...

    def setblocking(self, *args) -> Any:
        ...

    def setsockopt(self, *args) -> Any:
        ...

    def settimeout(self, *args) -> Any:
        ...
