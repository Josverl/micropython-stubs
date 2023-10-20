"""
Module: 'usocket' on micropython-v1.21.0-stm32-PYBV11
"""
# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': 'v1.21.0', 'cpu': 'STM32F405RG'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

SO_KEEPALIVE = 8  # type: int
SO_BROADCAST = 32  # type: int
SOL_SOCKET = 4095  # type: int
SO_RCVTIMEO = 4102  # type: int
SO_REUSEADDR = 4  # type: int
SO_SNDTIMEO = 4101  # type: int
AF_INET6 = 10  # type: int
AF_INET = 2  # type: int
SOCK_STREAM = 1  # type: int
SOCK_DGRAM = 2  # type: int
SOCK_RAW = 3  # type: int


def getaddrinfo(*args, **kwargs) -> Incomplete:
    ...


class socket:
    def recvfrom(self, *args, **kwargs) -> Incomplete:
        ...

    def recv(self, *args, **kwargs) -> Incomplete:
        ...

    def makefile(self, *args, **kwargs) -> Incomplete:
        ...

    def listen(self, *args, **kwargs) -> Incomplete:
        ...

    def settimeout(self, *args, **kwargs) -> Incomplete:
        ...

    def sendall(self, *args, **kwargs) -> Incomplete:
        ...

    def setsockopt(self, *args, **kwargs) -> Incomplete:
        ...

    def setblocking(self, *args, **kwargs) -> Incomplete:
        ...

    def sendto(self, *args, **kwargs) -> Incomplete:
        ...

    def readline(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def connect(self, *args, **kwargs) -> Incomplete:
        ...

    def send(self, *args, **kwargs) -> Incomplete:
        ...

    def bind(self, *args, **kwargs) -> Incomplete:
        ...

    def accept(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
