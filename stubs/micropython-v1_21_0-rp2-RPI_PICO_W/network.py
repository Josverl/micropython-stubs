"""
Module: 'network' on micropython-v1.21.0-rp2-RPI_PICO_W
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

STA_IF = 0  # type: int
STAT_IDLE = 0  # type: int
STAT_NO_AP_FOUND = -2  # type: int
STAT_WRONG_PASSWORD = -3  # type: int
STAT_GOT_IP = 3  # type: int
AP_IF = 1  # type: int
STAT_CONNECTING = 1  # type: int
STAT_CONNECT_FAIL = -1  # type: int


def route(*args, **kwargs) -> Incomplete:
    ...


def hostname(*args, **kwargs) -> Incomplete:
    ...


def country(*args, **kwargs) -> Incomplete:
    ...


class WLAN:
    PM_PERFORMANCE = 10555714  # type: int
    PM_POWERSAVE = 17  # type: int
    PM_NONE = 16  # type: int

    def isconnected(self, *args, **kwargs) -> Incomplete:
        ...

    def ioctl(self, *args, **kwargs) -> Incomplete:
        ...

    def ifconfig(self, *args, **kwargs) -> Incomplete:
        ...

    def scan(self, *args, **kwargs) -> Incomplete:
        ...

    def send_ethernet(self, *args, **kwargs) -> Incomplete:
        ...

    def status(self, *args, **kwargs) -> Incomplete:
        ...

    def config(self, *args, **kwargs) -> Incomplete:
        ...

    def active(self, *args, **kwargs) -> Incomplete:
        ...

    def disconnect(self, *args, **kwargs) -> Incomplete:
        ...

    def connect(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
