"""
Module: '_espnow' on micropython-v1.20.0-449-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'family': 'micropython', 'build': '449', 'arch': 'xtensawin', 'ver': 'v1.20.0-449', 'cpu': 'SPIRAM'})
# Stubber: v1.13.7
from typing import Any

MAX_DATA_LEN = 250 # type: int
MAX_TOTAL_PEER_NUM = 20 # type: int
MAX_ENCRYPT_PEER_NUM = 6 # type: int
ADDR_LEN = 6 # type: int
KEY_LEN = 16 # type: int

class ESPNowBase():
    def irq(self, *args, **kwargs) -> Any:
        ...

    def mod_peer(self, *args, **kwargs) -> Any:
        ...

    def get_peers(self, *args, **kwargs) -> Any:
        ...

    def stats(self, *args, **kwargs) -> Any:
        ...

    def set_pmk(self, *args, **kwargs) -> Any:
        ...

    def peer_count(self, *args, **kwargs) -> Any:
        ...

    def recvinto(self, *args, **kwargs) -> Any:
        ...

    def send(self, *args, **kwargs) -> Any:
        ...

    def active(self, *args, **kwargs) -> Any:
        ...

    def any(self, *args, **kwargs) -> Any:
        ...

    def get_peer(self, *args, **kwargs) -> Any:
        ...

    def del_peer(self, *args, **kwargs) -> Any:
        ...

    def add_peer(self, *args, **kwargs) -> Any:
        ...

    def config(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

