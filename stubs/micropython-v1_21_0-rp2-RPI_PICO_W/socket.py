"""
Module: 'socket' on micropython-v1.21.0-rp2-RPI_PICO_W
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

SOCK_STREAM = 1  # type: int
SOCK_RAW = 3  # type: int
SOCK_DGRAM = 2  # type: int
SOL_SOCKET = 1  # type: int
SO_BROADCAST = 32  # type: int
SO_REUSEADDR = 4  # type: int
AF_INET6 = 10  # type: int
AF_INET = 2  # type: int
IP_DROP_MEMBERSHIP = 1025  # type: int
IPPROTO_IP = 0  # type: int
IP_ADD_MEMBERSHIP = 1024  # type: int


def reset(*args, **kwargs) -> Incomplete:
    ...


def print_pcbs(*args, **kwargs) -> Incomplete:
    ...


def getaddrinfo(*args, **kwargs) -> Incomplete:
    ...


def callback(*args, **kwargs) -> Incomplete:
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
