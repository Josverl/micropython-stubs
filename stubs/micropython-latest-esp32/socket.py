"""
Module: 'socket' on micropython-v1.20.0-449-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'family': 'micropython', 'build': '449', 'arch': 'xtensawin', 'ver': 'v1.20.0-449', 'cpu': 'SPIRAM'})
# Stubber: v1.13.7
from typing import Any

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


def getaddrinfo(*args, **kwargs) -> Any:
    ...


class socket:
    def recvfrom(self, *args, **kwargs) -> Any:
        ...

    def recv(self, *args, **kwargs) -> Any:
        ...

    def makefile(self, *args, **kwargs) -> Any:
        ...

    def listen(self, *args, **kwargs) -> Any:
        ...

    def fileno(self, *args, **kwargs) -> Any:
        ...

    def sendall(self, *args, **kwargs) -> Any:
        ...

    def setsockopt(self, *args, **kwargs) -> Any:
        ...

    def setblocking(self, *args, **kwargs) -> Any:
        ...

    def sendto(self, *args, **kwargs) -> Any:
        ...

    def settimeout(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    def connect(self, *args, **kwargs) -> Any:
        ...

    def send(self, *args, **kwargs) -> Any:
        ...

    def bind(self, *args, **kwargs) -> Any:
        ...

    def accept(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
