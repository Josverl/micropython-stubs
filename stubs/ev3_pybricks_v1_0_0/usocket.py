"""
Module: 'usocket' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any

AF_INET = 2
AF_INET6 = 10
AF_UNIX = 1
MSG_DONTROUTE = 4
MSG_DONTWAIT = 64
SOCK_DGRAM = 2
SOCK_RAW = 3
SOCK_STREAM = 1
SOL_SOCKET = 1
SO_BROADCAST = 6
SO_ERROR = 4
SO_KEEPALIVE = 9
SO_LINGER = 13
SO_REUSEADDR = 2


def getaddrinfo():
    pass


def inet_ntop():
    pass


def inet_pton():
    pass


def sockaddr():
    pass


class socket:
    """"""

    def accept(self, *argv) -> Any:
        pass

    def bind(self, *argv) -> Any:
        pass

    def close(self, *argv) -> Any:
        pass

    def connect(self, *argv) -> Any:
        pass

    def fileno(self, *argv) -> Any:
        pass

    def listen(self, *argv) -> Any:
        pass

    def makefile(self, *argv) -> Any:
        pass

    def read(self, *argv) -> Any:
        pass

    def readinto(self, *argv) -> Any:
        pass

    def readline(self, *argv) -> Any:
        pass

    def recv(self, *argv) -> Any:
        pass

    def recvfrom(self, *argv) -> Any:
        pass

    def send(self, *argv) -> Any:
        pass

    def sendto(self, *argv) -> Any:
        pass

    def setblocking(self, *argv) -> Any:
        pass

    def setsockopt(self, *argv) -> Any:
        pass

    def write(self, *argv) -> Any:
        pass
