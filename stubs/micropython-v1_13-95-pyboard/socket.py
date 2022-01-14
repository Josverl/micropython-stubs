"""
Module: 'socket' on pyboard 1.13.0-95
"""
# MCU: (sysname='pyboard', nodename='pyboard', release='1.13.0', version='v1.13-95-g0fff2e03f on 2020-10-03', machine='PYBv1.1 with STM32F405RG')
# Stubber: 1.3.4 - updated
from typing import Any

AF_INET = 2
AF_INET6 = 10
SOCK_DGRAM = 2
SOCK_RAW = 3
SOCK_STREAM = 1


def getaddrinfo(*args) -> Any:
    pass


class socket:
    """"""

    def accept(self, *args) -> Any:
        pass

    def bind(self, *args) -> Any:
        pass

    def close(self, *args) -> Any:
        pass

    def connect(self, *args) -> Any:
        pass

    def listen(self, *args) -> Any:
        pass

    def recv(self, *args) -> Any:
        pass

    def recvfrom(self, *args) -> Any:
        pass

    def send(self, *args) -> Any:
        pass

    def sendto(self, *args) -> Any:
        pass

    def setblocking(self, *args) -> Any:
        pass

    def setsockopt(self, *args) -> Any:
        pass

    def settimeout(self, *args) -> Any:
        pass
