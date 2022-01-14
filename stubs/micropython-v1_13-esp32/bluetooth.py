"""
Module: 'bluetooth' on esp32 1.13.0-103
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.13.0', version='v1.13-103-gb137d064e on 2020-10-09', machine='ESP32 module (spiram) with ESP32')
# Stubber: 1.3.4 - updated
from typing import Any


class BLE:
    """"""

    def active(self, *args) -> Any:
        pass

    def config(self, *args) -> Any:
        pass

    def gap_advertise(self, *args) -> Any:
        pass

    def gap_connect(self, *args) -> Any:
        pass

    def gap_disconnect(self, *args) -> Any:
        pass

    def gap_scan(self, *args) -> Any:
        pass

    def gattc_discover_characteristics(self, *args) -> Any:
        pass

    def gattc_discover_descriptors(self, *args) -> Any:
        pass

    def gattc_discover_services(self, *args) -> Any:
        pass

    def gattc_exchange_mtu(self, *args) -> Any:
        pass

    def gattc_read(self, *args) -> Any:
        pass

    def gattc_write(self, *args) -> Any:
        pass

    def gatts_indicate(self, *args) -> Any:
        pass

    def gatts_notify(self, *args) -> Any:
        pass

    def gatts_read(self, *args) -> Any:
        pass

    def gatts_register_services(self, *args) -> Any:
        pass

    def gatts_set_buffer(self, *args) -> Any:
        pass

    def gatts_write(self, *args) -> Any:
        pass

    def irq(self, *args) -> Any:
        pass


FLAG_INDICATE = 32
FLAG_NOTIFY = 16
FLAG_READ = 2
FLAG_WRITE = 8
FLAG_WRITE_NO_RESPONSE = 4


class UUID:
    """"""
