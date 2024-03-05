"""
Module: 'usocket' on micropython-v1.21.0-unix-linux_[GCC_9.4.0]_version
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'unix', 'board': 'linux_[GCC_9.4.0]_version', 'cpu': '', 'mpy': '', 'arch': ''}
# Stubber: v1.15.1
from typing import Any
from _typeshed import Incomplete

SOL_SOCKET = 1  # type: int
SO_BROADCAST = 6  # type: int
SOCK_STREAM = 1  # type: int
SO_REUSEADDR = 2  # type: int
SO_LINGER = 13  # type: int
SO_ERROR = 4  # type: int
SO_KEEPALIVE = 9  # type: int
AF_INET6 = 10  # type: int
AF_UNIX = 1  # type: int
AF_INET = 2  # type: int
SOCK_RAW = 3  # type: int
SOCK_DGRAM = 2  # type: int
MSG_DONTROUTE = 4  # type: int
MSG_DONTWAIT = 64  # type: int


def sockaddr(*args, **kwargs) -> Incomplete:
    ...


def inet_pton(*args, **kwargs) -> Incomplete:
    ...


def inet_ntop(*args, **kwargs) -> Incomplete:
    ...


def getaddrinfo(*args, **kwargs) -> Incomplete:
    ...


class socket:
    def recv(self, *args, **kwargs) -> Incomplete:
        ...

    def makefile(self, *args, **kwargs) -> Incomplete:
        ...

    def listen(self, *args, **kwargs) -> Incomplete:
        ...

    def fileno(self, *args, **kwargs) -> Incomplete:
        ...

    def settimeout(self, *args, **kwargs) -> Incomplete:
        ...

    def recvfrom(self, *args, **kwargs) -> Incomplete:
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
