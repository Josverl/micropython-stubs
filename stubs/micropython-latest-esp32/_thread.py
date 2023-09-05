"""
Module: '_thread' on micropython-v1.20.0-449-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'family': 'micropython', 'build': '449', 'arch': 'xtensawin', 'ver': 'v1.20.0-449', 'cpu': 'SPIRAM'})
# Stubber: v1.13.7
from typing import Any

def get_ident(*args, **kwargs) -> Any:
    ...

def start_new_thread(*args, **kwargs) -> Any:
    ...

def stack_size(*args, **kwargs) -> Any:
    ...

def exit(*args, **kwargs) -> Any:
    ...

def allocate_lock(*args, **kwargs) -> Any:
    ...


class LockType():
    def locked(self, *args, **kwargs) -> Any:
        ...

    def release(self, *args, **kwargs) -> Any:
        ...

    def acquire(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

