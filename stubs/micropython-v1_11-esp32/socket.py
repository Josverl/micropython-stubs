"""
Module: 'socket' on micropython-v1.11-esp32
"""
# MCU: {'ver': 'v1.11', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.11.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.11.0'}
# Stubber: 1.5.0
from typing import Any


def __init__(*args) -> Any:
    ...


AF_INET = 2  # type: int
AF_INET6 = 10  # type: int
IPPROTO_IP = 0  # type: int
IPPROTO_TCP = 6  # type: int
IPPROTO_UDP = 17  # type: int
IP_ADD_MEMBERSHIP = 3  # type: int
SOCK_DGRAM = 2  # type: int
SOCK_RAW = 3  # type: int
SOCK_STREAM = 1  # type: int
SOL_SOCKET = 4095  # type: int
SO_REUSEADDR = 4  # type: int


def getaddrinfo(*args) -> Any:
    ...


class socket:
    """"""

    def close(self, *args) -> Any:
        ...

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def readline(self, *args) -> Any:
        ...

    def send(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    def accept(self, *args) -> Any:
        ...

    def bind(self, *args) -> Any:
        ...

    def connect(self, *args) -> Any:
        ...

    def fileno(self, *args) -> Any:
        ...

    def listen(self, *args) -> Any:
        ...

    def makefile(self, *args) -> Any:
        ...

    def recv(self, *args) -> Any:
        ...

    def recvfrom(self, *args) -> Any:
        ...

    def sendall(self, *args) -> Any:
        ...

    def sendto(self, *args) -> Any:
        ...

    def setblocking(self, *args) -> Any:
        ...

    def setsockopt(self, *args) -> Any:
        ...

    def settimeout(self, *args) -> Any:
        ...
