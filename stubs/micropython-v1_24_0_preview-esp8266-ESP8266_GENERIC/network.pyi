"""
Module: 'network' on micropython-v1.24.0-preview-esp8266-ESP8266_GENERIC
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': 'preview.62.g908ab1cec', 'arch': 'xtensa', 'ver': '1.24.0-preview-preview.62.g908ab1cec', 'cpu': 'ESP8266'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

STA_IF: int = 0
STAT_CONNECT_FAIL: int = 4
STAT_CONNECTING: int = 1
MODE_11N: int = 3
STAT_GOT_IP: int = 5
STAT_WRONG_PASSWORD: int = 2
STAT_NO_AP_FOUND: int = 3
STAT_IDLE: int = 0
MODE_11G: int = 2
AUTH_WEP: int = 1
AUTH_OPEN: int = 0
AP_IF: int = 1
AUTH_WPA2_PSK: int = 3
MODE_11B: int = 1
AUTH_WPA_WPA2_PSK: int = 4
AUTH_WPA_PSK: int = 2

def hostname(*args, **kwargs) -> Incomplete: ...
def ipconfig(*args, **kwargs) -> Incomplete: ...
def phy_mode(*args, **kwargs) -> Incomplete: ...
def country(*args, **kwargs) -> Incomplete: ...

class WLAN:
    SEC_WEP: int = 1
    SEC_OPEN: int = 0
    SEC_WPA_WPA2: int = 4
    SEC_WPA: int = 2
    SEC_WPA2: int = 3
    IF_STA: int = 0
    IF_AP: int = 1
    PM_POWERSAVE: int = 1
    PM_NONE: int = 0
    PM_PERFORMANCE: int = 2
    def ifconfig(self, *args, **kwargs) -> Incomplete: ...
    def ipconfig(self, *args, **kwargs) -> Incomplete: ...
    def isconnected(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def status(self, *args, **kwargs) -> Incomplete: ...
    def disconnect(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
