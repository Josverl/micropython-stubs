"""
Module: 'ubluetooth' on micropython-v1.20.0-esp32-GENERIC
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'esp32', 'board': 'GENERIC', 'cpu': 'ESP32', 'mpy': 'v6.1', 'arch': 'xtensawin'})
# Stubber: v1.13.4
from typing import Any

FLAG_NOTIFY = 16  # type: int
FLAG_READ = 2  # type: int
FLAG_WRITE = 8  # type: int
FLAG_INDICATE = 32  # type: int
FLAG_WRITE_NO_RESPONSE = 4  # type: int


class UUID:
    def __init__(self, *argv, **kwargs) -> None:
        ...


class BLE:
    def gattc_write(self, *args, **kwargs) -> Any:
        ...

    def gatts_indicate(self, *args, **kwargs) -> Any:
        ...

    def gattc_discover_services(self, *args, **kwargs) -> Any:
        ...

    def gattc_read(self, *args, **kwargs) -> Any:
        ...

    def gattc_exchange_mtu(self, *args, **kwargs) -> Any:
        ...

    def gatts_set_buffer(self, *args, **kwargs) -> Any:
        ...

    def gatts_write(self, *args, **kwargs) -> Any:
        ...

    def gatts_notify(self, *args, **kwargs) -> Any:
        ...

    def gatts_register_services(self, *args, **kwargs) -> Any:
        ...

    def gatts_read(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def gap_advertise(self, *args, **kwargs) -> Any:
        ...

    def gap_connect(self, *args, **kwargs) -> Any:
        ...

    def gattc_discover_descriptors(self, *args, **kwargs) -> Any:
        ...

    def config(self, *args, **kwargs) -> Any:
        ...

    def active(self, *args, **kwargs) -> Any:
        ...

    def gap_scan(self, *args, **kwargs) -> Any:
        ...

    def gattc_discover_characteristics(self, *args, **kwargs) -> Any:
        ...

    def gap_disconnect(self, *args, **kwargs) -> Any:
        ...

    def gap_passkey(self, *args, **kwargs) -> Any:
        ...

    def gap_pair(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
