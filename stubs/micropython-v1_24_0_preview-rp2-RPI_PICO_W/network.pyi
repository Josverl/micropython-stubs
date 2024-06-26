"""
Module: 'network' on micropython-v1.24.0-preview-rp2-RPI_PICO_W
"""

# MCU: {'build': 'preview.66.gf60c71d13', 'ver': '1.24.0-preview-preview.66.gf60c71d13', 'version': '1.24.0-preview', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.20.0
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

def hostname(*args, **kwargs) -> Incomplete: ...
def ipconfig(*args, **kwargs) -> Incomplete: ...
def route(*args, **kwargs) -> Incomplete: ...
def country(*args, **kwargs) -> Incomplete: ...

class WLAN:
    PM_POWERSAVE: int = 17
    PM_PERFORMANCE: int = 10555714
    SEC_OPEN: int = 0
    SEC_WPA_WPA2: int = 4194310
    IF_AP: int = 1
    PM_NONE: int = 16
    IF_STA: int = 0
    def ipconfig(self, *args, **kwargs) -> Incomplete: ...
    def status(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def send_ethernet(self, *args, **kwargs) -> Incomplete: ...
    def isconnected(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def ifconfig(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def disconnect(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
