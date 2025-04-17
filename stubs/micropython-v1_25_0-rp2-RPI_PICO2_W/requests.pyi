"""
Module: 'requests' on micropython-v1.25.0-rp2-RPI_PICO2_W
"""

# MCU: {'build': '', 'ver': '1.25.0', 'version': '1.25.0', 'port': 'rp2', 'board': 'RPI_PICO2_W', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2350', 'arch': 'armv7emsp'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

def delete(*args, **kwargs) -> Incomplete: ...
def head(*args, **kwargs) -> Incomplete: ...
def patch(*args, **kwargs) -> Incomplete: ...
def post(*args, **kwargs) -> Incomplete: ...
def request(*args, **kwargs) -> Incomplete: ...
def put(*args, **kwargs) -> Incomplete: ...
def get(*args, **kwargs) -> Incomplete: ...

class Response:
    def json(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    content: Incomplete  ## <class 'property'> = <property>
    text: Incomplete  ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None: ...
