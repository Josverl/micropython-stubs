"""
Module: 'ubluetooth' on micropython-v1.18-rp2
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.18.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2', 'ver': 'v1.18', 'release': '1.18.0'}
# Stubber: 1.5.3
from typing import Any


class BLE():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
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

    def gap_pair(self, *args, **kwargs) -> Any:
        ...

    def gap_passkey(self, *args, **kwargs) -> Any:
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

    def l2cap_connect(self, *args, **kwargs) -> Any:
        ...

    def l2cap_disconnect(self, *args, **kwargs) -> Any:
        ...

    def l2cap_listen(self, *args, **kwargs) -> Any:
        ...

    def l2cap_recvinto(self, *args, **kwargs) -> Any:
        ...

    def l2cap_send(self, *args, **kwargs) -> Any:
        ...

FLAG_INDICATE = 32 # type: int
FLAG_NOTIFY = 16 # type: int
FLAG_READ = 2 # type: int
FLAG_WRITE = 8 # type: int
FLAG_WRITE_NO_RESPONSE = 4 # type: int

class UUID():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
