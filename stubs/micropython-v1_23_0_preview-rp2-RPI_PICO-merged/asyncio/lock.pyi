"""
Module: 'asyncio.lock' on micropython-v1.23.0-preview-rp2-RPI_PICO
"""
# MCU: {'family': 'micropython', 'version': '1.23.0-preview', 'build': 'preview.58.gc3ca3612d', 'ver': '1.23.0-preview-preview.58.gc3ca3612d', 'port': 'rp2', 'board': 'RPI_PICO', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.17.1
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...

    acquire: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
