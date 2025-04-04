"""
Module: 'network' on micropython-v1.24.1-rp2-ARDUINO_NANO_RP2040_CONNECT
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'cpu': 'RP2040', 'mpy': 'v6.3', 'arch': 'armv6m'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

STA_IF: int = 0
AP_IF: int = 1

def hostname(*args, **kwargs) -> Incomplete: ...
def ipconfig(*args, **kwargs) -> Incomplete: ...
def route(*args, **kwargs) -> Incomplete: ...
def country(*args, **kwargs) -> Incomplete: ...

class WLAN:
    WPA_PSK: int = 2
    SEC_WEP: int = 3
    SEC_WPA_WPA2: int = 2
    WEP: int = 3
    SEC_OPEN: int = 1
    IF_AP: int = 1
    IF_STA: int = 0
    OPEN: int = 1
    def ipconfig(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def status(self, *args, **kwargs) -> Incomplete: ...
    def isconnected(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def ifconfig(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def disconnect(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
