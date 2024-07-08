"""
Module: 'network' on micropython-v1.23.0-esp32-ESP32_GENERIC
"""

# MCU: {'version': '1.23.0', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.23.0', 'cpu': 'ESP32'}
# Stubber: v1.23.0
from __future__ import annotations
from _typeshed import Incomplete

PHY_KSZ8081: int = 6
PHY_KSZ8041: int = 5
MODE_11G: int = 2
PHY_KSZ8851SNL: int = 100
PHY_LAN8710: int = 0
MODE_LR: int = 8
MODE_11N: int = 4
PHY_IP101: int = 2
PHY_DM9051: int = 101
PHY_DP83848: int = 4
STAT_GOT_IP: int = 1010
STAT_CONNECTING: int = 1001
PHY_LAN8720: int = 1
STAT_HANDSHAKE_TIMEOUT: int = 204
STAT_IDLE: int = 1000
PHY_W5500: int = 102
PHY_RTL8201: int = 3
STAT_BEACON_TIMEOUT: int = 200
STAT_WRONG_PASSWORD: int = 202
STAT_ASSOC_FAIL: int = 203
STAT_NO_AP_FOUND: int = 201
AUTH_WPA2_ENTERPRISE: int = 5
AUTH_WEP: int = 1
MODE_11B: int = 1
AUTH_WPA2_PSK: int = 3
AUTH_WPA2_WPA3_PSK: int = 7
AUTH_MAX: int = 10
AP_IF: int = 1
AUTH_WAPI_PSK: int = 8
AUTH_OPEN: int = 0
AUTH_OWE: int = 9
ETH_STARTED: int = 1
ETH_INITIALIZED: int = 0
AUTH_WPA3_PSK: int = 6
ETH_STOPPED: int = 2
STA_IF: int = 0
AUTH_WPA_WPA2_PSK: int = 4
AUTH_WPA_PSK: int = 2
ETH_GOT_IP: int = 5
ETH_CONNECTED: int = 3
ETH_DISCONNECTED: int = 4

def phy_mode(*args, **kwargs) -> Incomplete: ...
def country(*args, **kwargs) -> Incomplete: ...
def hostname(*args, **kwargs) -> Incomplete: ...
def LAN(*args, **kwargs) -> Incomplete: ...
def PPP(*args, **kwargs) -> Incomplete: ...

class WLAN:
    SEC_WPA: int = 2
    SEC_WPA2: int = 3
    SEC_WEP: int = 1
    SEC_WAPI: int = 8
    SEC_WPA3: int = 6
    SEC_WPA2_ENT: int = 5
    SEC_WPA2_WPA3: int = 7
    SEC_WPA_WPA2: int = 4
    IF_STA: int = 0
    PM_NONE: int = 0
    IF_AP: int = 1
    SEC_OWE: int = 9
    SEC_OPEN: int = 0
    PM_PERFORMANCE: int = 1
    PM_POWERSAVE: int = 2
    def status(self, *args, **kwargs) -> Incomplete: ...
    def ifconfig(self, *args, **kwargs) -> Incomplete: ...
    def isconnected(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def disconnect(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
