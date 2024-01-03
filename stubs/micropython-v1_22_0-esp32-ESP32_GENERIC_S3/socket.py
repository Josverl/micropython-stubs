"""
Module: 'socket' on micropython-v1.22.0-esp32-ESP32_GENERIC_S3
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'cpu': 'ESP32S3', 'mpy': 'v6.2', 'arch': 'xtensawin'}
# Stubber: v1.16.2
from _typeshed import Incomplete

SOCK_STREAM = 1  # type: int
SOCK_DGRAM = 2  # type: int
SOCK_RAW = 3  # type: int
SO_BROADCAST = 32  # type: int
SOL_SOCKET = 4095  # type: int
SO_BINDTODEVICE = 4107  # type: int
SO_REUSEADDR = 4  # type: int
AF_INET6 = 10  # type: int
IP_ADD_MEMBERSHIP = 3  # type: int
AF_INET = 2  # type: int
IPPROTO_UDP = 17  # type: int
IPPROTO_IP = 0  # type: int
IPPROTO_TCP = 6  # type: int


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

    def fileno(self, *args, **kwargs) -> Incomplete:
        ...

    def sendall(self, *args, **kwargs) -> Incomplete:
        ...

    def setsockopt(self, *args, **kwargs) -> Incomplete:
        ...

    def setblocking(self, *args, **kwargs) -> Incomplete:
        ...

    def sendto(self, *args, **kwargs) -> Incomplete:
        ...

    def settimeout(self, *args, **kwargs) -> Incomplete:
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
