"""
Module: 'network' on micropython-v1.22.0-esp32-ESP32_GENERIC_S3
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'cpu': 'ESP32S3', 'mpy': 'v6.2', 'arch': 'xtensawin'}
# Stubber: v1.16.2
from _typeshed import Incomplete

PHY_KSZ8081 = 6  # type: int
PHY_KSZ8041 = 5  # type: int
MODE_11G = 2  # type: int
PHY_KSZ8851SNL = 100  # type: int
PHY_LAN8710 = 0  # type: int
MODE_LR = 8  # type: int
MODE_11N = 4  # type: int
PHY_IP101 = 2  # type: int
PHY_DM9051 = 101  # type: int
PHY_DP83848 = 4  # type: int
STAT_GOT_IP = 1010  # type: int
STAT_CONNECTING = 1001  # type: int
PHY_LAN8720 = 1  # type: int
STAT_HANDSHAKE_TIMEOUT = 204  # type: int
STAT_IDLE = 1000  # type: int
PHY_W5500 = 102  # type: int
PHY_RTL8201 = 3  # type: int
STAT_BEACON_TIMEOUT = 200  # type: int
STAT_WRONG_PASSWORD = 202  # type: int
STAT_ASSOC_FAIL = 203  # type: int
STAT_NO_AP_FOUND = 201  # type: int
AUTH_WPA2_ENTERPRISE = 5  # type: int
AUTH_WEP = 1  # type: int
MODE_11B = 1  # type: int
AUTH_WPA2_PSK = 3  # type: int
AUTH_WPA2_WPA3_PSK = 7  # type: int
AUTH_MAX = 10  # type: int
AP_IF = 1  # type: int
AUTH_WAPI_PSK = 8  # type: int
AUTH_OPEN = 0  # type: int
AUTH_OWE = 9  # type: int
ETH_STARTED = 1  # type: int
ETH_INITIALIZED = 0  # type: int
AUTH_WPA3_PSK = 6  # type: int
ETH_STOPPED = 2  # type: int
STA_IF = 0  # type: int
AUTH_WPA_WPA2_PSK = 4  # type: int
AUTH_WPA_PSK = 2  # type: int
ETH_GOT_IP = 5  # type: int
ETH_CONNECTED = 3  # type: int
ETH_DISCONNECTED = 4  # type: int


def phy_mode(*args, **kwargs) -> Incomplete:
    ...


def country(*args, **kwargs) -> Incomplete:
    ...


def hostname(*args, **kwargs) -> Incomplete:
    ...


def LAN(*args, **kwargs) -> Incomplete:
    ...


def PPP(*args, **kwargs) -> Incomplete:
    ...


class WLAN:
    PM_PERFORMANCE = 1  # type: int
    PM_POWERSAVE = 2  # type: int
    PM_NONE = 0  # type: int

    def status(self, *args, **kwargs) -> Incomplete:
        ...

    def ifconfig(self, *args, **kwargs) -> Incomplete:
        ...

    def isconnected(self, *args, **kwargs) -> Incomplete:
        ...

    def scan(self, *args, **kwargs) -> Incomplete:
        ...

    def disconnect(self, *args, **kwargs) -> Incomplete:
        ...

    def active(self, *args, **kwargs) -> Incomplete:
        ...

    def config(self, *args, **kwargs) -> Incomplete:
        ...

    def connect(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
