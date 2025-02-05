"""
Module: 'usocket' on micropython-v1.21.0-esp8266-ESP8266_GENERIC
"""

# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensa', 'ver': '1.21.0', 'cpu': 'ESP8266'}
# Stubber: v1.23.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

SOCK_STREAM: int = 1
SOCK_RAW: int = 3
SOCK_DGRAM: int = 2
SOL_SOCKET: int = 1
SO_BROADCAST: int = 32
SO_REUSEADDR: int = 4
AF_INET6: int = 10
AF_INET: int = 2
IP_DROP_MEMBERSHIP: int = 1025
IPPROTO_IP: int = 0
IP_ADD_MEMBERSHIP: int = 1024

def reset(*args, **kwargs) -> Incomplete: ...
def print_pcbs(*args, **kwargs) -> Incomplete: ...
def getaddrinfo(*args, **kwargs) -> Incomplete: ...
def callback(*args, **kwargs) -> Incomplete: ...

class socket: ...
