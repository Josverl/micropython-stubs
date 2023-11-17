"""
Module: 'onewire' on micropython-v1.21.0-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'cpu': 'SPIRAM', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.14.0
from _typeshed import Incomplete


class OneWire:
    MATCH_ROM = 85  # type: int
    SKIP_ROM = 204  # type: int
    SEARCH_ROM = 240  # type: int

    def select_rom(self, *args, **kwargs) -> Incomplete:
        ...

    def writebyte(self, *args, **kwargs) -> Incomplete:
        ...

    def crc8(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def readbyte(self, *args, **kwargs) -> Incomplete:
        ...

    def readbit(self, *args, **kwargs) -> Incomplete:
        ...

    def writebit(self, *args, **kwargs) -> Incomplete:
        ...

    def reset(self, *args, **kwargs) -> Incomplete:
        ...

    def scan(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class OneWireError(Exception):
    ...
