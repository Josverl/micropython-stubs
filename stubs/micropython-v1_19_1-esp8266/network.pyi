from typing import Any

STA_IF: int
STAT_CONNECT_FAIL: int
STAT_CONNECTING: int
MODE_11N: int
STAT_GOT_IP: int
STAT_WRONG_PASSWORD: int
STAT_NO_AP_FOUND: int
STAT_IDLE: int
MODE_11G: int
AUTH_WEP: int
AUTH_OPEN: int
AP_IF: int
AUTH_WPA2_PSK: int
MODE_11B: int
AUTH_WPA_WPA2_PSK: int
AUTH_WPA_PSK: int

def phy_mode(*args, **kwargs) -> Any: ...
def WLAN(*args, **kwargs) -> Any: ...
