"""
Module: 'usocket' on micropython-v1.15-esp8266
"""
# MCU: {'ver': 'v1.15', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.15', 'name': 'micropython', 'mpy': 9733, 'version': '1.15', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.0
from typing import Any

AF_INET = 2  # type: int
AF_INET6 = 10  # type: int
IPPROTO_IP = 0  # type: int
IP_ADD_MEMBERSHIP = 1024  # type: int
SOCK_DGRAM = 2  # type: int
SOCK_RAW = 3  # type: int
SOCK_STREAM = 1  # type: int
SOL_SOCKET = 1  # type: int
SO_REUSEADDR = 4  # type: int


def callback(*args) -> Any:
    ...


def getaddrinfo(*args) -> Any:
    ...


def print_pcbs(*args) -> Any:
    ...


def reset(*args) -> Any:
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
