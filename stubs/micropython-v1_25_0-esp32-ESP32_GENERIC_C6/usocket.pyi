"""
Module: 'usocket' on micropython-v1.25.0-esp32-ESP32_GENERIC_C6
"""

# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC_C6', 'family': 'micropython', 'build': '', 'arch': 'rv32imc', 'ver': '1.25.0', 'cpu': 'ESP32C6'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

SOCK_STREAM: Final[int] = 1
SOL_SOCKET: Final[int] = 4095
SOCK_RAW: Final[int] = 3
TCP_NODELAY: Final[int] = 1
SO_REUSEADDR: Final[int] = 4
SO_BINDTODEVICE: Final[int] = 4107
SO_BROADCAST: Final[int] = 32
AF_INET6: Final[int] = 10
IPPROTO_IP: Final[int] = 0
AF_INET: Final[int] = 2
SOCK_DGRAM: Final[int] = 2
IP_ADD_MEMBERSHIP: Final[int] = 3
IPPROTO_TCP: Final[int] = 6
IPPROTO_UDP: Final[int] = 17

def getaddrinfo(*args, **kwargs) -> Incomplete: ...

class socket:
    def recvfrom(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def makefile(self, *args, **kwargs) -> Incomplete: ...
    def listen(self, *args, **kwargs) -> Incomplete: ...
    def fileno(self, *args, **kwargs) -> Incomplete: ...
    def sendall(self, *args, **kwargs) -> Incomplete: ...
    def setsockopt(self, *args, **kwargs) -> Incomplete: ...
    def setblocking(self, *args, **kwargs) -> Incomplete: ...
    def sendto(self, *args, **kwargs) -> Incomplete: ...
    def settimeout(self, *args, **kwargs) -> Incomplete: ...
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
