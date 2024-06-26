"""
Module: '_asyncio' on micropython-v1.24.0-preview-esp32-ESP32_GENERIC_C3
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC_C3', 'family': 'micropython', 'build': 'preview.86.g557d31ed2', 'arch': '', 'ver': '1.24.0-preview-preview.86.g557d31ed2', 'cpu': 'ESP32C3'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

class TaskQueue:
    def push(self, *args, **kwargs) -> Incomplete: ...
    def peek(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def pop(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Task:
    def __init__(self, *argv, **kwargs) -> None: ...
