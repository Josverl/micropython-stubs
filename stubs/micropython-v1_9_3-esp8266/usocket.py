"""
Module: 'usocket' on esp8266 v1.9.3
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.0.0(5a875ba)', version='v1.9.3-8-g63826ac5c on 2017-11-01', machine='ESP module with ESP8266')
# Stubber: 1.1.2 - updated
from typing import Any

AF_INET = 2
AF_INET6 = 10
IPPROTO_IP = 0
IP_ADD_MEMBERSHIP = 1024
SOCK_DGRAM = 2
SOCK_RAW = 3
SOCK_STREAM = 1
SOL_SOCKET = 1
SO_REUSEADDR = 4


def callback():
    pass


def getaddrinfo():
    pass


def print_pcbs():
    pass


def reset():
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

    def sendall(self, *argv) -> Any:
        pass

    def sendto(self, *argv) -> Any:
        pass

    def setblocking(self, *argv) -> Any:
        pass

    def setsockopt(self, *argv) -> Any:
        pass

    def settimeout(self, *argv) -> Any:
        pass

    def write(self, *argv) -> Any:
        pass
