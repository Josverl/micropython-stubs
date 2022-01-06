"""
Module: 'esp32' on micropython-esp32-1.11
"""
# MCU: {'ver': '1.11', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.11.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.11.0'}
# Stubber: 1.4.2
from typing import Any


class ULP:
    ''
    RESERVE_MEM = 0 # type: int
    def load_binary(self, *args) -> Any:
        ...

    def run(self, *args) -> Any:
        ...

    def set_wakeup_period(self, *args) -> Any:
        ...

WAKEUP_ALL_LOW = False # type: bool
WAKEUP_ANY_HIGH = True # type: bool
def hall_sensor(*args) -> Any:
    ...

def raw_temperature(*args) -> Any:
    ...

def wake_on_ext0(*args) -> Any:
    ...

def wake_on_ext1(*args) -> Any:
    ...

def wake_on_touch(*args) -> Any:
    ...

