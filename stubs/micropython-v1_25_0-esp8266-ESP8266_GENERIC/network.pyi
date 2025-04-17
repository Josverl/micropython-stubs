"""
Module: 'network' on micropython-v1.25.0-esp8266-ESP8266_GENERIC
"""
# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensa', 'ver': '1.25.0', 'cpu': 'ESP8266'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

STA_IF: Final[int] = 0
STAT_CONNECT_FAIL: Final[int] = 4
STAT_CONNECTING: Final[int] = 1
MODE_11N: Final[int] = 3
STAT_GOT_IP: Final[int] = 5
STAT_WRONG_PASSWORD: Final[int] = 2
STAT_NO_AP_FOUND: Final[int] = 3
STAT_IDLE: Final[int] = 0
MODE_11G: Final[int] = 2
AUTH_WEP: Final[int] = 1
AUTH_OPEN: Final[int] = 0
AP_IF: Final[int] = 1
AUTH_WPA2_PSK: Final[int] = 3
MODE_11B: Final[int] = 1
AUTH_WPA_WPA2_PSK: Final[int] = 4
AUTH_WPA_PSK: Final[int] = 2
def hostname(*args, **kwargs) -> Incomplete:
    ...

def ipconfig(*args, **kwargs) -> Incomplete:
    ...

def phy_mode(*args, **kwargs) -> Incomplete:
    ...

def country(*args, **kwargs) -> Incomplete:
    ...


class WLAN():
    SEC_WEP: Final[int] = 1
    SEC_OPEN: Final[int] = 0
    SEC_WPA_WPA2: Final[int] = 4
    SEC_WPA: Final[int] = 2
    SEC_WPA2: Final[int] = 3
    IF_STA: Final[int] = 0
    IF_AP: Final[int] = 1
    PM_POWERSAVE: Final[int] = 1
    PM_NONE: Final[int] = 0
    PM_PERFORMANCE: Final[int] = 2
    def ifconfig(self, *args, **kwargs) -> Incomplete:
        ...

    def ipconfig(self, *args, **kwargs) -> Incomplete:
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

