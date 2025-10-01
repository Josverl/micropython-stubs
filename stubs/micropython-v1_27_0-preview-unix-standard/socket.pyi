"""
Module: 'socket' on micropython-v1.27.0-preview-unix-standard
"""
# MCU: {'family': 'micropython', 'version': '1.27.0-preview', 'build': '218', 'ver': '1.27.0-preview-218', 'port': 'unix', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'linux [GCC 12.4.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

SOL_SOCKET: Final[int] = 1
SO_BROADCAST: Final[int] = 6
SOCK_STREAM: Final[int] = 1
SOCK_RAW: Final[int] = 3
SO_LINGER: Final[int] = 13
SO_ERROR: Final[int] = 4
SO_KEEPALIVE: Final[int] = 9
SO_REUSEADDR: Final[int] = 2
AF_INET6: Final[int] = 10
AF_UNIX: Final[int] = 1
AF_INET: Final[int] = 2
SOCK_DGRAM: Final[int] = 2
MSG_PEEK: Final[int] = 2
MSG_DONTROUTE: Final[int] = 4
MSG_DONTWAIT: Final[int] = 64
def sockaddr(*args, **kwargs) -> Incomplete:
    ...

def inet_pton(*args, **kwargs) -> Incomplete:
    ...

def inet_ntop(*args, **kwargs) -> Incomplete:
    ...

def getaddrinfo(*args, **kwargs) -> Incomplete:
    ...


class socket():
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

