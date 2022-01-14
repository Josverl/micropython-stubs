"""
Module: 'network' on esp32_LoBo
MCU: (sysname='esp32_LoBo', nodename='esp32_LoBo', release='3.2.24', version='ESP32_LoBo_v3.2.24 on 2018-09-06', machine='ESP32 board with ESP32')
Stubber: 1.0.0 - updated
"""
from typing import Any

AP_IF = 1
AUTH_OPEN = 0
AUTH_WEP = 1
AUTH_WPA2_PSK = 3
AUTH_WPA_PSK = 2
AUTH_WPA_WPA2_PSK = 4
MODE_11B = 1
MODE_11G = 2
MODE_11N = 4
STA_IF = 0


def WLAN(*args) -> Any:
    pass


def WLANcallback(*args) -> Any:
    pass


class ftp:
    """"""

    def pause(self, *args) -> Any:
        pass

    def resume(self, *args) -> Any:
        pass

    def stack(self, *args) -> Any:
        pass

    def start(self, *args) -> Any:
        pass

    def status(self, *args) -> Any:
        pass

    def stop(self, *args) -> Any:
        pass


class mDNS:
    """"""

    def addService(self, *args) -> Any:
        pass

    def queryHost(self, *args) -> Any:
        pass

    def queryService(self, *args) -> Any:
        pass

    def removeService(self, *args) -> Any:
        pass

    def start(self, *args) -> Any:
        pass

    def stop(self, *args) -> Any:
        pass


class mqtt:
    """"""

    def config(self, *args) -> Any:
        pass

    def free(self, *args) -> Any:
        pass

    def publish(self, *args) -> Any:
        pass

    def start(self, *args) -> Any:
        pass

    def status(self, *args) -> Any:
        pass

    def stop(self, *args) -> Any:
        pass

    def subscribe(self, *args) -> Any:
        pass

    def unsubscribe(self, *args) -> Any:
        pass


def phy_mode(*args) -> Any:
    pass


class telnet:
    """"""

    def pause(self, *args) -> Any:
        pass

    def resume(self, *args) -> Any:
        pass

    def stack(self, *args) -> Any:
        pass

    def start(self, *args) -> Any:
        pass

    def status(self, *args) -> Any:
        pass

    def stop(self, *args) -> Any:
        pass
