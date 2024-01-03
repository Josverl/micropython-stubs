"""
Module: '_espnow' on micropython-v1.22.0-esp32-Generic_ESP32S3_module
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'esp32', 'board': 'Generic_ESP32S3_module', 'cpu': 'ESP32S3', 'mpy': 'v6.2', 'arch': 'xtensawin'}
# Stubber: v1.16.2
from _typeshed import Incomplete

MAX_DATA_LEN = 250  # type: int
MAX_TOTAL_PEER_NUM = 20  # type: int
MAX_ENCRYPT_PEER_NUM = 6  # type: int
ADDR_LEN = 6  # type: int
KEY_LEN = 16  # type: int


class ESPNowBase:
    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def mod_peer(self, *args, **kwargs) -> Incomplete:
        ...

    def get_peers(self, *args, **kwargs) -> Incomplete:
        ...

    def stats(self, *args, **kwargs) -> Incomplete:
        ...

    def set_pmk(self, *args, **kwargs) -> Incomplete:
        ...

    def peer_count(self, *args, **kwargs) -> Incomplete:
        ...

    def recvinto(self, *args, **kwargs) -> Incomplete:
        ...

    def send(self, *args, **kwargs) -> Incomplete:
        ...

    def active(self, *args, **kwargs) -> Incomplete:
        ...

    def any(self, *args, **kwargs) -> Incomplete:
        ...

    def get_peer(self, *args, **kwargs) -> Incomplete:
        ...

    def del_peer(self, *args, **kwargs) -> Incomplete:
        ...

    def add_peer(self, *args, **kwargs) -> Incomplete:
        ...

    def config(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
