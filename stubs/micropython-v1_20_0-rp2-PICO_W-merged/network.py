"""
Module: 'network' on micropython-v1.20-rp2-PICO_W
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20', 'build': '', 'ver': 'v1.20', 'port': 'rp2', 'board': 'PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.12.2
from typing import Any

STA_IF = 0  # type: int
STAT_IDLE = 0  # type: int
STAT_NO_AP_FOUND = -2  # type: int
STAT_WRONG_PASSWORD = -3  # type: int
STAT_GOT_IP = 3  # type: int
AP_IF = 1  # type: int
STAT_CONNECTING = 1  # type: int
STAT_CONNECT_FAIL = -1  # type: int


def route(*args, **kwargs) -> Any:
    ...


def hostname(*args, **kwargs) -> Any:
    ...


def country(*args, **kwargs) -> Any:
    ...


class WLAN:
    def isconnected(self, *args, **kwargs) -> Any:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def ifconfig(self, *args, **kwargs) -> Any:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...

    def send_ethernet(self, *args, **kwargs) -> Any:
        ...

    def status(self, *args, **kwargs) -> Any:
        ...

    def config(self, *args, **kwargs) -> Any:
        ...

    def active(self, *args, **kwargs) -> Any:
        ...

    def disconnect(self, *args, **kwargs) -> Any:
        ...

    def connect(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
