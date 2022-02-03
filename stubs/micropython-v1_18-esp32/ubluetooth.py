"""
Module: 'ubluetooth' on micropython-v1.18-esp32
"""
# MCU: {'ver': 'v1.18', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.18.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.18.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any


class BLE:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def active(self, *args, **kwargs) -> Any:
        ...

    def config(self, *args, **kwargs) -> Any:
        ...

    def gap_advertise(self, *args, **kwargs) -> Any:
        ...

    def gap_connect(self, *args, **kwargs) -> Any:
        ...

    def gap_disconnect(self, *args, **kwargs) -> Any:
        ...

    def gap_scan(self, *args, **kwargs) -> Any:
        ...

    def gattc_discover_characteristics(self, *args, **kwargs) -> Any:
        ...

    def gattc_discover_descriptors(self, *args, **kwargs) -> Any:
        ...

    def gattc_discover_services(self, *args, **kwargs) -> Any:
        ...

    def gattc_exchange_mtu(self, *args, **kwargs) -> Any:
        ...

    def gattc_read(self, *args, **kwargs) -> Any:
        ...

    def gattc_write(self, *args, **kwargs) -> Any:
        ...

    def gatts_indicate(self, *args, **kwargs) -> Any:
        ...

    def gatts_notify(self, *args, **kwargs) -> Any:
        ...

    def gatts_read(self, *args, **kwargs) -> Any:
        ...

    def gatts_register_services(self, *args, **kwargs) -> Any:
        ...

    def gatts_set_buffer(self, *args, **kwargs) -> Any:
        ...

    def gatts_write(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...


FLAG_INDICATE = 32  # type: int
FLAG_NOTIFY = 16  # type: int
FLAG_READ = 2  # type: int
FLAG_WRITE = 8  # type: int
FLAG_WRITE_NO_RESPONSE = 4  # type: int


class UUID:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...
