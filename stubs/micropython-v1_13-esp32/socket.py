"""
Module: 'socket' on micropython-v1.13-266-esp32
"""
# MCU: {'ver': 'v1.13-266', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.13.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.13.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '266', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
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
