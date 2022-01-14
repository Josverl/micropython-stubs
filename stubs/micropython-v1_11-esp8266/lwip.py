"""
Module: 'lwip' on esp8266 v1.11
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.11-8-g48dcbbe60 on 2019-05-29', machine='ESP module with ESP8266')
# Stubber: 1.1.0 - updated
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


def callback(*args) -> Any:
    pass


def getaddrinfo(*args) -> Any:
    pass


def print_pcbs(*args) -> Any:
    pass


def reset(*args) -> Any:
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

    def makefile(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def readline(self, *args) -> Any:
        pass

    def recv(self, *args) -> Any:
        pass

    def recvfrom(self, *args) -> Any:
        pass

    def send(self, *args) -> Any:
        pass

    def sendall(self, *args) -> Any:
        pass

    def sendto(self, *args) -> Any:
        pass

    def setblocking(self, *args) -> Any:
        pass

    def setsockopt(self, *args) -> Any:
        pass

    def settimeout(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass
