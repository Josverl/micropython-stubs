"""
Module: 'copy' on micropython-v1.26.0-preview-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.26.0-preview', 'build': '293', 'ver': '1.26.0-preview-293', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

_copy_dispatch: dict = {}
_deepcopy_dispatch: dict = {}
def _deepcopy_atomic(*args, **kwargs) -> Incomplete:
    ...

def _copy_with_copy_method(*args, **kwargs) -> Incomplete:
    ...

def _deepcopy_tuple(*args, **kwargs) -> Incomplete:
    ...

def _deepcopy_method(*args, **kwargs) -> Incomplete:
    ...

def _deepcopy_dict(*args, **kwargs) -> Incomplete:
    ...

def _deepcopy_list(*args, **kwargs) -> Incomplete:
    ...

def deepcopy(*args, **kwargs) -> Incomplete:
    ...

def _copy_with_constructor(*args, **kwargs) -> Incomplete:
    ...

def copy(*args, **kwargs) -> Incomplete:
    ...

def _reconstruct(*args, **kwargs) -> Incomplete:
    ...

def _copy_immutable(*args, **kwargs) -> Incomplete:
    ...

def _keep_alive(*args, **kwargs) -> Incomplete:
    ...


class error():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class t():
    def discard(self, *args, **kwargs) -> Incomplete:
        ...

    def isdisjoint(self, *args, **kwargs) -> Incomplete:
        ...

    def intersection_update(self, *args, **kwargs) -> Incomplete:
        ...

    def intersection(self, *args, **kwargs) -> Incomplete:
        ...

    def issubset(self, *args, **kwargs) -> Incomplete:
        ...

    def symmetric_difference_update(self, *args, **kwargs) -> Incomplete:
        ...

    def symmetric_difference(self, *args, **kwargs) -> Incomplete:
        ...

    def issuperset(self, *args, **kwargs) -> Incomplete:
        ...

    def union(self, *args, **kwargs) -> Incomplete:
        ...

    def difference_update(self, *args, **kwargs) -> Incomplete:
        ...

    def pop(self, *args, **kwargs) -> Incomplete:
        ...

    def copy(self, *args, **kwargs) -> Incomplete:
        ...

    def clear(self, *args, **kwargs) -> Incomplete:
        ...

    def remove(self, *args, **kwargs) -> Incomplete:
        ...

    def difference(self, *args, **kwargs) -> Incomplete:
        ...

    def add(self, *args, **kwargs) -> Incomplete:
        ...

    def update(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class _EmptyClass():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class OrderedDict():
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

    def copy(self, *args, **kwargs) -> Incomplete:
        ...

    def clear(self, *args, **kwargs) -> Incomplete:
        ...

    def keys(self, *args, **kwargs) -> Incomplete:
        ...

    def get(self, *args, **kwargs) -> Incomplete:
        ...

    def items(self, *args, **kwargs) -> Incomplete:
        ...

    @classmethod
    def fromkeys(cls, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Error(Exception):
    ...
PyStringMap: Incomplete ## <class 'NoneType'> = None
