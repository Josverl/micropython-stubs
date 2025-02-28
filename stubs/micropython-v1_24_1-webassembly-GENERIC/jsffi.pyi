"""
Module: 'jsffi' on micropython-v1.24.1-webassembly
"""
# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'webassembly', 'board': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

def create_proxy(*args, **kwargs) -> Incomplete:
    ...

def mem_info(*args, **kwargs) -> Incomplete:
    ...

def to_js(*args, **kwargs) -> Incomplete:
    ...


class JsProxy():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class JsException(Exception):
    ...
