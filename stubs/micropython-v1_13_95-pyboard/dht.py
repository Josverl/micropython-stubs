"""
Module: 'dht' on pyboard 1.13.0-95
"""
# MCU: (sysname='pyboard', nodename='pyboard', release='1.13.0', version='v1.13-95-g0fff2e03f on 2020-10-03', machine='PYBv1.1 with STM32F405RG')
# Stubber: 1.3.4 - updated
from typing import Any


class DHT11:
    """"""

    def humidity(self, *args) -> Any:
        pass

    def measure(self, *args) -> Any:
        pass

    def temperature(self, *args) -> Any:
        pass


class DHT22:
    """"""

    def humidity(self, *args) -> Any:
        pass

    def measure(self, *args) -> Any:
        pass

    def temperature(self, *args) -> Any:
        pass


class DHTBase:
    """"""

    def measure(self, *args) -> Any:
        pass


def dht_readinto(*args) -> Any:
    pass
