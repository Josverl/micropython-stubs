"""
Module: 'network' on micropython-v1.26.0-esp32-ESP32_GENERIC-SPIRAM
"""

# MCU: {'variant': 'SPIRAM', 'build': '', 'arch': 'xtensawin', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'board_id': 'ESP32_GENERIC-SPIRAM', 'mpy': 'v6.3', 'ver': '1.26.0', 'family': 'micropython', 'cpu': 'ESP32', 'version': '1.26.0'}
# Stubber: v1.25.1
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

PHY_KSZ8851SNL: Final[int] = 100
PHY_RTL8201: Final[int] = 3
PHY_KSZ8081: Final[int] = 6
PHY_LAN8720: Final[int] = 1
PHY_LAN8670: Final[int] = 7
PHY_LAN8710: Final[int] = 0
PHY_DM9051: Final[int] = 101
PHY_KSZ8041: Final[int] = 5
MODE_LR: Final[int] = 8
PHY_IP101: Final[int] = 2
PHY_DP83848: Final[int] = 4
PHY_GENERIC: Final[int] = 8
STAT_NO_AP_FOUND_W_COMPATIBLE_SECURITY: Final[int] = 210
STAT_IDLE: Final[int] = 1000
PHY_W5500: Final[int] = 102
STAT_HANDSHAKE_TIMEOUT: Final[int] = 204
STAT_NO_AP_FOUND_IN_RSSI_THRESHOLD: Final[int] = 212
STAT_NO_AP_FOUND: Final[int] = 201
STAT_NO_AP_FOUND_IN_AUTHMODE_THRESHOLD: Final[int] = 211
STAT_ASSOC_FAIL: Final[int] = 203
STAT_GOT_IP: Final[int] = 1010
STAT_WRONG_PASSWORD: Final[int] = 202
STAT_CONNECT_FAIL: Final[int] = 203
STAT_BEACON_TIMEOUT: Final[int] = 200
STAT_CONNECTING: Final[int] = 1001
AUTH_WPA2_PSK: Final[int] = 3
AUTH_WPA3_EXT_PSK_MIXED_MODE: Final[int] = 12
AUTH_WPA2_ENTERPRISE: Final[int] = 5
AUTH_WPA3_EXT_PSK: Final[int] = 11
AUTH_WPA2_WPA3_PSK: Final[int] = 7
AUTH_WPA3_ENT_192: Final[int] = 10
AUTH_MAX: Final[int] = 16
AUTH_WEP: Final[int] = 1
AP_IF: Final[int] = 1
AUTH_WAPI_PSK: Final[int] = 8
AUTH_OPEN: Final[int] = 0
AUTH_OWE: Final[int] = 9
MODE_11N: Final[int] = 4
ETH_STOPPED: Final[int] = 2
AUTH_WPA3_PSK: Final[int] = 6
ETH_STARTED: Final[int] = 1
MODE_11G: Final[int] = 2
STA_IF: Final[int] = 0
MODE_11B: Final[int] = 1
AUTH_WPA_WPA2_PSK: Final[int] = 4
ETH_INITIALIZED: Final[int] = 0
AUTH_WPA_PSK: Final[int] = 2
ETH_GOT_IP: Final[int] = 5
ETH_CONNECTED: Final[int] = 3
ETH_DISCONNECTED: Final[int] = 4

def country(*args, **kwargs) -> Incomplete: ...
def hostname(*args, **kwargs) -> Incomplete: ...
def ipconfig(*args, **kwargs) -> Incomplete: ...
def phy_mode(*args, **kwargs) -> Incomplete: ...
def LAN(*args, **kwargs) -> Incomplete: ...

class WLAN:
    SEC_WPA2_WPA3: Final[int] = 7
    SEC_WPA2_WPA3_ENT: Final[int] = 15
    SEC_WPA: Final[int] = 2
    SEC_WPA2_ENT: Final[int] = 5
    SEC_WPA2: Final[int] = 3
    SEC_WPA3_EXT_PSK: Final[int] = 11
    SEC_WPA3_EXT_PSK_MIXED_MODE: Final[int] = 12
    SEC_WPA3: Final[int] = 6
    SEC_WPA3_ENT_192: Final[int] = 10
    SEC_WPA3_ENT: Final[int] = 14
    SEC_WPA_WPA2: Final[int] = 4
    PM_NONE: Final[int] = 0
    PM_PERFORMANCE: Final[int] = 1
    SEC_WEP: Final[int] = 1
    IF_STA: Final[int] = 0
    IF_AP: Final[int] = 1
    SEC_OWE: Final[int] = 9
    SEC_WAPI: Final[int] = 8
    PM_POWERSAVE: Final[int] = 2
    SEC_OPEN: Final[int] = 0
    SEC_DPP: Final[int] = 13
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

class PPP:
    SEC_CHAP: Final[int] = 2
    SEC_PAP: Final[int] = 1
    SEC_NONE: Final[int] = 0
    AUTH_CHAP: Final[int] = 2
    AUTH_PAP: Final[int] = 1
    AUTH_NONE: Final[int] = 0
    def ifconfig(self, *args, **kwargs) -> Incomplete: ...
    def ipconfig(self, *args, **kwargs) -> Incomplete: ...
    def isconnected(self, *args, **kwargs) -> Incomplete: ...
    def poll(self, *args, **kwargs) -> Incomplete: ...
    def status(self, *args, **kwargs) -> Incomplete: ...
    def disconnect(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
