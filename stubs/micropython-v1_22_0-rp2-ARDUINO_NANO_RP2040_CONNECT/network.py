"""
Module: 'network' on micropython-v1.22.0-rp2-ARDUINO_NANO_RP2040_CONNECT
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.16.2
from _typeshed import Incomplete

STA_IF = 0  # type: int
AP_IF = 1  # type: int


def route(*args, **kwargs) -> Incomplete:
    ...


def hostname(*args, **kwargs) -> Incomplete:
    ...


def country(*args, **kwargs) -> Incomplete:
    ...


class WLAN:
    WEP = 3  # type: int
    WPA_PSK = 2  # type: int
    OPEN = 1  # type: int

    def ifconfig(self, *args, **kwargs) -> Incomplete:
        ...

    def ioctl(self, *args, **kwargs) -> Incomplete:
        ...

    def isconnected(self, *args, **kwargs) -> Incomplete:
        ...

    def scan(self, *args, **kwargs) -> Incomplete:
        ...

    def status(self, *args, **kwargs) -> Incomplete:
        ...

    def disconnect(self, *args, **kwargs) -> Incomplete:
        ...

    def active(self, *args, **kwargs) -> Incomplete:
        ...

    def config(self, *args, **kwargs) -> Incomplete:
        ...

    def connect(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
