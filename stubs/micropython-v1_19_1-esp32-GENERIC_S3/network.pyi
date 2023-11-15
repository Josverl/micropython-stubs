from typing import Any

STAT_ASSOC_FAIL: int
STAT_BEACON_TIMEOUT: int
STAT_CONNECTING: int
MODE_11N: int
MODE_11G: int
MODE_11B: int
STAT_NO_AP_FOUND: int
STAT_WRONG_PASSWORD: int
STAT_GOT_IP: int
STAT_IDLE: int
STAT_HANDSHAKE_TIMEOUT: int
STA_IF: int
AUTH_WAPI_PSK: int
AUTH_WPA_WPA2_PSK: int
AUTH_WEP: int
AP_IF: int
AUTH_OPEN: int
AUTH_MAX: int
AUTH_WPA3_PSK: int
AUTH_WPA2_ENTERPRISE: int
AUTH_WPA_PSK: int
AUTH_WPA2_PSK: int
AUTH_WPA2_WPA3_PSK: int

def WLAN(*args, **kwargs) -> Any: ...
def phy_mode(*args, **kwargs) -> Any: ...
def PPP(*args, **kwargs) -> Any: ...
