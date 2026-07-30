"""
Module: 'deflate' on micropython-v1.29.0-preview-esp32-ESP32_GENERIC_C6
"""

# MCU: {'variant': '', 'build': 'preview.657.gf013bb5195', 'arch': 'rv32imc', 'port': 'esp32', 'board': 'ESP32_GENERIC_C6', 'board_id': 'ESP32_GENERIC_C6', 'mpy': 'v6.3', 'ver': '1.29.0-preview-preview.657.gf013bb5195', 'family': 'micropython', 'cpu': 'ESP32-C6', 'version': '1.29.0-preview'}
# Stubber: v1.28.3
from __future__ import annotations

from typing import Final

from _typeshed import Incomplete

GZIP: Final[int] = 3
RAW: Final[int] = 1
ZLIB: Final[int] = 2
AUTO: Final[int] = 0

class DeflateIO:
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
