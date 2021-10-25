AP_IF: int
AUTH_OPEN: int
AUTH_WEP: int
AUTH_WPA2_PSK: int
AUTH_WPA_PSK: int
AUTH_WPA_WPA2_PSK: int
MODE_11B: int
MODE_11G: int
MODE_11N: int
STA_IF: int

def WLAN() -> None: ...
def WLANcallback() -> None: ...
def phy_mode() -> None: ...
