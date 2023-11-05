from typing import Any

PHY_LAN8720: int
PHY_DP83848: int
PHY_IP101: int
PHY_LAN8710: int
MODE_LR: int
MODE_11B: int
MODE_11G: int
MODE_11N: int
STAT_NO_AP_FOUND: int
PHY_RTL8201: int
STAT_GOT_IP: int
STAT_HANDSHAKE_TIMEOUT: int
STAT_IDLE: int
STAT_CONNECTING: int
STAT_WRONG_PASSWORD: int
STAT_ASSOC_FAIL: int
STAT_BEACON_TIMEOUT: int
AUTH_WPA3_PSK: int
AUTH_WPA2_ENTERPRISE: int
AUTH_WPA2_PSK: int
AUTH_WPA2_WPA3_PSK: int
AUTH_WEP: int
AP_IF: int
AUTH_MAX: int
AUTH_OPEN: int
STA_IF: int
AUTH_WPA_PSK: int
ETH_INITIALIZED: int
ETH_STARTED: int
ETH_STOPPED: int
ETH_GOT_IP: int
AUTH_WPA_WPA2_PSK: int
ETH_CONNECTED: int
ETH_DISCONNECTED: int

def phy_mode(*args, **kwargs) -> Any: ...
def country(*args, **kwargs) -> Any: ...
def hostname(*args, **kwargs) -> Any: ...
def LAN(*args, **kwargs) -> Any: ...
def WLAN(*args, **kwargs) -> Any: ...
def PPP(*args, **kwargs) -> Any: ...
