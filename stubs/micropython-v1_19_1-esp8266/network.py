"""
Module: 'network' on micropython-v1.19.1-esp8266
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp8266', 'port': 'esp8266', 'machine': 'ESP module (1M) with ESP8266', 'release': '1.19.1', 'nodename': 'esp8266', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp8266', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Any

AP_IF = 1  # type: int
AUTH_OPEN = 0  # type: int
AUTH_WEP = 1  # type: int
AUTH_WPA2_PSK = 3  # type: int
AUTH_WPA_PSK = 2  # type: int
AUTH_WPA_WPA2_PSK = 4  # type: int
MODE_11B = 1  # type: int
MODE_11G = 2  # type: int
MODE_11N = 3  # type: int
STAT_CONNECTING = 1  # type: int
STAT_CONNECT_FAIL = 4  # type: int
STAT_GOT_IP = 5  # type: int
STAT_IDLE = 0  # type: int
STAT_NO_AP_FOUND = 3  # type: int
STAT_WRONG_PASSWORD = 2  # type: int
STA_IF = 0  # type: int


def WLAN(*args, **kwargs) -> Any:
    ...


def phy_mode(*args, **kwargs) -> Any:
    ...
