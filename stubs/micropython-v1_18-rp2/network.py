"""
Module: 'network' on micropython-v1.18-rp2
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.18.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2', 'ver': 'v1.18', 'release': '1.18.0'}
# Stubber: 1.5.3
from typing import Any

AP_IF = 1  # type: int
STA_IF = 0  # type: int


class WLAN:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    OPEN = 1  # type: int
    WEP = 3  # type: int
    WPA_PSK = 2  # type: int

    def active(self, *args, **kwargs) -> Any:
        ...

    def config(self, *args, **kwargs) -> Any:
        ...

    def connect(self, *args, **kwargs) -> Any:
        ...

    def disconnect(self, *args, **kwargs) -> Any:
        ...

    def ifconfig(self, *args, **kwargs) -> Any:
        ...

    def isconnected(self, *args, **kwargs) -> Any:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...

    def status(self, *args, **kwargs) -> Any:
        ...


def route(*args, **kwargs) -> Any:
    ...
