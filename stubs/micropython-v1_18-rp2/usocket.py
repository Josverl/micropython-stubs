"""
Module: 'usocket' on micropython-v1.18-rp2
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.18.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2', 'ver': 'v1.18', 'release': '1.18.0'}
# Stubber: 1.5.3
from typing import Any

AF_INET = 2 # type: int
AF_INET6 = 10 # type: int
SOCK_DGRAM = 2 # type: int
SOCK_RAW = 3 # type: int
SOCK_STREAM = 1 # type: int
def getaddrinfo(*args, **kwargs) -> Any:
    ...


class socket():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
    def close(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def send(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def accept(self, *args, **kwargs) -> Any:
        ...

    def bind(self, *args, **kwargs) -> Any:
        ...

    def connect(self, *args, **kwargs) -> Any:
        ...

    def listen(self, *args, **kwargs) -> Any:
        ...

    def recv(self, *args, **kwargs) -> Any:
        ...

    def recvfrom(self, *args, **kwargs) -> Any:
        ...

    def sendto(self, *args, **kwargs) -> Any:
        ...

    def setblocking(self, *args, **kwargs) -> Any:
        ...

    def setsockopt(self, *args, **kwargs) -> Any:
        ...

    def settimeout(self, *args, **kwargs) -> Any:
        ...

