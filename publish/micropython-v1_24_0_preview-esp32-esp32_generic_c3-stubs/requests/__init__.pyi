"""
Module: 'requests.__init__' on micropython-v1.24.0-preview-esp32-ESP32_GENERIC_C3
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC_C3', 'family': 'micropython', 'build': 'preview.66.gf60c71d13', 'arch': '', 'ver': '1.24.0-preview-preview.66.gf60c71d13', 'cpu': 'ESP32C3'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

def head(*args, **kwargs) -> Incomplete: ...
def delete(*args, **kwargs) -> Incomplete: ...
def patch(*args, **kwargs) -> Incomplete: ...
def post(*args, **kwargs) -> Incomplete: ...
def get(*args, **kwargs) -> Incomplete: ...
def request(*args, **kwargs) -> Incomplete: ...
def put(*args, **kwargs) -> Incomplete: ...

class Response:
    def json(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    content: Incomplete  ## <class 'property'> = <property>
    text: Incomplete  ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None: ...
