"""
Module: 'pyscript' on micropython-v1.27.0-preview-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.27.0-preview', 'build': '252', 'ver': '1.27.0-preview-252', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

config: dict = {}
RUNNING_IN_WORKER: Final[bool] = False
def when(*args, **kwargs) -> Incomplete:
    ...

def fetch(*args, **kwargs) -> Incomplete:
    ...

def current_target(*args, **kwargs) -> Incomplete:
    ...

def display(*args, **kwargs) -> Incomplete:
    ...


class Storage():
    def popitem(self, *args, **kwargs) -> Incomplete:
        ...

    def pop(self, *args, **kwargs) -> Incomplete:
        ...

    def values(self, *args, **kwargs) -> Incomplete:
        ...

    def setdefault(self, *args, **kwargs) -> Incomplete:
        ...

    def update(self, *args, **kwargs) -> Incomplete:
        ...

    def keys(self, *args, **kwargs) -> Incomplete:
        ...

    def copy(self, *args, **kwargs) -> Incomplete:
        ...

    def get(self, *args, **kwargs) -> Incomplete:
        ...

    def items(self, *args, **kwargs) -> Incomplete:
        ...

    @classmethod
    def fromkeys(cls, *args, **kwargs) -> Incomplete:
        ...

    def sync(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def clear(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class WebSocket():
    OPEN: Final[int] = 1
    CLOSED: Final[int] = 3
    CLOSING: Final[int] = 2
    CONNECTING: Final[int] = 0
    def send(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

workers: Incomplete ## <class '_ReadOnlyProxy'> = <_ReadOnlyProxy object at ...>
def create_named_worker(*args, **kwargs) -> Generator:  ## = <generator>
    ...

@classmethod
def py_import(cls, *args, **kwargs) -> Incomplete:
    ...

@classmethod
def PyWorker(cls, *args, **kwargs) -> Incomplete:
    ...


class Event():
    def add_listener(self, *args, **kwargs) -> Incomplete:
        ...

    def remove_listener(self, *args, **kwargs) -> Incomplete:
        ...

    def trigger(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

sync: Incomplete ## <class 'NotSupported'> = <NotSupported pyscript.sync [pyscript.sync works only when running in a worker]>
def storage(*args, **kwargs) -> Generator:  ## = <generator>
    ...


class HTML():
    def _repr_html_(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

document: Incomplete ## <class 'JsProxy'> = <JsProxy 7>
js_modules: Incomplete ## <class 'JsProxy'> = <JsProxy 2>
@classmethod
def js_import(cls, *args, **kwargs) -> Incomplete:
    ...

