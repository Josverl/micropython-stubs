"""
Module: 'network' on micropython-v1.20.0-esp32-GENERIC_S3
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': 'v1.20.0', 'cpu': 'ESP32S3'})
# Stubber: v1.13.7
from typing import Any

STA_IF = 0  # type: int
STAT_WRONG_PASSWORD = 202  # type: int
STAT_ASSOC_FAIL = 203  # type: int
MODE_11G = 2  # type: int
MODE_LR = 8  # type: int
MODE_11N = 4  # type: int
STAT_IDLE = 1000  # type: int
STAT_BEACON_TIMEOUT = 200  # type: int
STAT_NO_AP_FOUND = 201  # type: int
STAT_CONNECTING = 1001  # type: int
STAT_HANDSHAKE_TIMEOUT = 204  # type: int
STAT_GOT_IP = 1010  # type: int
AUTH_WAPI_PSK = 8  # type: int
MODE_11B = 1  # type: int
AUTH_WEP = 1  # type: int
AP_IF = 1  # type: int
AUTH_OPEN = 0  # type: int
AUTH_MAX = 9  # type: int
AUTH_WPA_PSK = 2  # type: int
AUTH_WPA2_ENTERPRISE = 5  # type: int
AUTH_WPA_WPA2_PSK = 4  # type: int
AUTH_WPA2_PSK = 3  # type: int
AUTH_WPA3_PSK = 6  # type: int
AUTH_WPA2_WPA3_PSK = 7  # type: int


def country(*args, **kwargs) -> Any:
    ...


def hostname(*args, **kwargs) -> Any:
    ...


def phy_mode(*args, **kwargs) -> Any:
    ...


def WLAN(*args, **kwargs) -> Any:
    ...


def PPP(*args, **kwargs) -> Any:
    ...
