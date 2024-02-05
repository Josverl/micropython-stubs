"""
Module: 'network' on micropython-v1.22.1-rp2-ARDUINO_NANO_RP2040_CONNECT
"""
# MCU: {'build': '', 'ver': '1.22.1', 'version': '1.22.1', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.16.3
from __future__ import annotations
from _typeshed import Incomplete

STA_IF: int = 0
AP_IF: int = 1

def route(*args, **kwargs) -> Incomplete: ...
def hostname(*args, **kwargs) -> Incomplete: ...
def country(*args, **kwargs) -> Incomplete: ...

class WLAN:
    WEP: int = 3
    WPA_PSK: int = 2
    OPEN: int = 1
    def ifconfig(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def isconnected(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def status(self, *args, **kwargs) -> Incomplete: ...
    def disconnect(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...