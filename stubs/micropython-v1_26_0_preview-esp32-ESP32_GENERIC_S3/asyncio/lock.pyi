"""
Module: 'asyncio.lock' on micropython-v1.26.0-preview-esp32-ESP32_GENERIC_S3
"""

# MCU: {'variant': '', 'build': 'preview.434.g096ff8b9e', 'arch': 'xtensawin', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'board_id': 'ESP32_GENERIC_S3', 'mpy': 'v6.3', 'ver': '1.26.0-preview-preview.434.g096ff8b9e', 'family': 'micropython', 'cpu': 'ESP32S3', 'version': '1.26.0-preview'}
# Stubber: v1.25.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...
    def acquire(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    def __init__(self, *argv, **kwargs) -> None: ...
