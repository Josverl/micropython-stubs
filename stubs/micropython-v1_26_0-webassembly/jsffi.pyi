"""
Module: 'jsffi' on micropython-v1.26.0-preview-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.26.0-preview', 'build': '293', 'ver': '1.26.0-preview-293', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
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
