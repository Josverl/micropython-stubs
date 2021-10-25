AP_IF: int
AUTH_OPEN: int
AUTH_WEP: int
AUTH_WPA2_PSK: int
AUTH_WPA_PSK: int
AUTH_WPA_WPA2_PSK: int
MODE_11B: int
MODE_11G: int
MODE_11N: int
STAT_CONNECTING: int
STAT_CONNECT_FAIL: int
STAT_GOT_IP: int
STAT_IDLE: int
STAT_NO_AP_FOUND: int
STAT_WRONG_PASSWORD: int
STA_IF: int

def WLAN() -> None: ...
def phy_mode() -> None: ...
