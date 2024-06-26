"""
Module: 'network' on micropython-v1.21.0-esp32-ESP32_GENERIC_C3
"""

# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'ESP32_GENERIC_C3', 'family': 'micropython', 'build': '', 'arch': '', 'ver': '1.21.0', 'cpu': 'ESP32C3'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

STA_IF: int = 0
MODE_11B: int = 1
STAT_ASSOC_FAIL: int = 203
MODE_11G: int = 2
MODE_LR: int = 8
MODE_11N: int = 4
STAT_IDLE: int = 1000
STAT_BEACON_TIMEOUT: int = 200
STAT_NO_AP_FOUND: int = 201
STAT_CONNECTING: int = 1001
STAT_HANDSHAKE_TIMEOUT: int = 204
STAT_GOT_IP: int = 1010
STAT_WRONG_PASSWORD: int = 202
AUTH_OWE: int = 9
AUTH_WPA_WPA2_PSK: int = 4
AUTH_WAPI_PSK: int = 8
AP_IF: int = 1
AUTH_OPEN: int = 0
AUTH_MAX: int = 10
AUTH_WPA3_PSK: int = 6
AUTH_WEP: int = 1
AUTH_WPA_PSK: int = 2
AUTH_WPA2_ENTERPRISE: int = 5
AUTH_WPA2_WPA3_PSK: int = 7
AUTH_WPA2_PSK: int = 3

def country(*args, **kwargs) -> Incomplete: ...
def hostname(*args, **kwargs) -> Incomplete: ...
def phy_mode(*args, **kwargs) -> Incomplete: ...
def PPP(*args, **kwargs) -> Incomplete: ...

class WLAN:
    PM_PERFORMANCE: int = 1
    PM_POWERSAVE: int = 2
    PM_NONE: int = 0
    def status(self, *args, **kwargs) -> Incomplete: ...
    def ifconfig(self, *args, **kwargs) -> Incomplete: ...
    def isconnected(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def disconnect(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
