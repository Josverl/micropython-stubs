"""
Module: 'socket' on micropython-v1.25.0-stm32-PYBV11
"""

# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': '1.25.0', 'cpu': 'STM32F405RG'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

SO_KEEPALIVE: Final[int] = 8
SO_BROADCAST: Final[int] = 32
SOL_SOCKET: Final[int] = 4095
SO_RCVTIMEO: Final[int] = 4102
SO_REUSEADDR: Final[int] = 4
SO_SNDTIMEO: Final[int] = 4101
AF_INET6: Final[int] = 10
AF_INET: Final[int] = 2
SOCK_STREAM: Final[int] = 1
SOCK_DGRAM: Final[int] = 2
SOCK_RAW: Final[int] = 3

def getaddrinfo(*args, **kwargs) -> Incomplete: ...

class socket:
    def recvfrom(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def makefile(self, *args, **kwargs) -> Incomplete: ...
    def listen(self, *args, **kwargs) -> Incomplete: ...
    def settimeout(self, *args, **kwargs) -> Incomplete: ...
    def sendall(self, *args, **kwargs) -> Incomplete: ...
    def setsockopt(self, *args, **kwargs) -> Incomplete: ...
    def setblocking(self, *args, **kwargs) -> Incomplete: ...
    def sendto(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def bind(self, *args, **kwargs) -> Incomplete: ...
    def accept(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
