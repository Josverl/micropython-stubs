from typing import Any

def __init__(*args) -> None: ...

AP_IF: int
AUTH_MAX: int
AUTH_OPEN: int
AUTH_WEP: int
AUTH_WPA2_PSK: int
AUTH_WPA_PSK: int
AUTH_WPA_WPA2_PSK: int
MODE_11B: int
MODE_11G: int
MODE_11N: int
PHY_IP101: int
PHY_LAN8720: int
PHY_TLK110: int

def PPP(*args) -> Any: ...

STAT_ASSOC_FAIL: int
STAT_BEACON_TIMEOUT: int
STAT_CONNECTING: int
STAT_GOT_IP: int
STAT_HANDSHAKE_TIMEOUT: int
STAT_IDLE: int
STAT_NO_AP_FOUND: int
STAT_WRONG_PASSWORD: int
STA_IF: int

def WLAN(*args) -> Any: ...
def phy_mode(*args) -> Any: ...
