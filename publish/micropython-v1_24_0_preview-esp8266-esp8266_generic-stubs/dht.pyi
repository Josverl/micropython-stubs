"""
Module: 'dht' on micropython-v1.24.0-preview-esp8266-ESP8266_GENERIC
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': 'preview.60.gcebc9b0ae', 'arch': 'xtensa', 'ver': '1.24.0-preview-preview.60.gcebc9b0ae', 'cpu': 'ESP8266'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

def dht_readinto(*args, **kwargs) -> Incomplete: ...

class DHTBase:
    def measure(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class DHT22:
    def measure(self, *args, **kwargs) -> Incomplete: ...
    def temperature(self, *args, **kwargs) -> Incomplete: ...
    def humidity(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class DHT11:
    def measure(self, *args, **kwargs) -> Incomplete: ...
    def temperature(self, *args, **kwargs) -> Incomplete: ...
    def humidity(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
