from _typeshed import Incomplete as Incomplete

PHY_KSZ8081: int
PHY_KSZ8041: int
MODE_11G: int
PHY_KSZ8851SNL: int
PHY_LAN8710: int
MODE_LR: int
MODE_11N: int
PHY_IP101: int
PHY_DM9051: int
PHY_DP83848: int
STAT_GOT_IP: int
STAT_CONNECTING: int
PHY_LAN8720: int
STAT_HANDSHAKE_TIMEOUT: int
STAT_IDLE: int
PHY_W5500: int
PHY_RTL8201: int
STAT_BEACON_TIMEOUT: int
STAT_WRONG_PASSWORD: int
STAT_ASSOC_FAIL: int
STAT_NO_AP_FOUND: int
AUTH_WPA2_ENTERPRISE: int
AUTH_WEP: int
MODE_11B: int
AUTH_WPA2_PSK: int
AUTH_WPA2_WPA3_PSK: int
AUTH_MAX: int
AP_IF: int
AUTH_WAPI_PSK: int
AUTH_OPEN: int
AUTH_OWE: int
ETH_STARTED: int
ETH_INITIALIZED: int
AUTH_WPA3_PSK: int
ETH_STOPPED: int
STA_IF: int
AUTH_WPA_WPA2_PSK: int
AUTH_WPA_PSK: int
ETH_GOT_IP: int
ETH_CONNECTED: int
ETH_DISCONNECTED: int

def phy_mode(*args, **kwargs) -> Incomplete: ...
def country(*args, **kwargs) -> Incomplete: ...
def hostname(*args, **kwargs) -> Incomplete: ...
def LAN(*args, **kwargs) -> Incomplete: ...
def PPP(*args, **kwargs) -> Incomplete: ...

class WLAN:
    PM_PERFORMANCE: int
    PM_POWERSAVE: int
    PM_NONE: int
    def status(self, *args, **kwargs) -> Incomplete: ...
    def ifconfig(self, *args, **kwargs) -> Incomplete: ...
    def isconnected(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def disconnect(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
