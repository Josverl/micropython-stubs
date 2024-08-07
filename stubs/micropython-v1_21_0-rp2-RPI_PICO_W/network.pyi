"""
Module: 'network' on micropython-v1.21.0-rp2-RPI_PICO_W
"""

# MCU: {'build': '', 'ver': '1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.23.0
from __future__ import annotations
from _typeshed import Incomplete

STA_IF: int = 0
STAT_IDLE: int = 0
STAT_NO_AP_FOUND: int = -2
STAT_WRONG_PASSWORD: int = -3
STAT_GOT_IP: int = 3
AP_IF: int = 1
STAT_CONNECTING: int = 1
STAT_CONNECT_FAIL: int = -1

def route(*args, **kwargs) -> Incomplete: ...
def hostname(*args, **kwargs) -> Incomplete: ...
def country(*args, **kwargs) -> Incomplete: ...

class WLAN:
    PM_PERFORMANCE: int = 10555714
    PM_POWERSAVE: int = 17
    PM_NONE: int = 16
    def isconnected(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def ifconfig(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def send_ethernet(self, *args, **kwargs) -> Incomplete: ...
    def status(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def disconnect(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
