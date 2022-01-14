"""
Module: 'uasyncio.stream' on pyboard 1.13.0-95
"""
# MCU: (sysname='pyboard', nodename='pyboard', release='1.13.0', version='v1.13-95-g0fff2e03f on 2020-10-03', machine='PYBv1.1 with STM32F405RG')
# Stubber: 1.3.4 - updated
from typing import Any


class Server:
    """"""

    _serve = None

    def close(self, *args) -> Any:
        pass

    wait_closed = None


class Stream:
    """"""

    aclose = None
    awrite = None
    awritestr = None

    def close(self, *args) -> Any:
        pass

    drain = None

    def get_extra_info(self, *args) -> Any:
        pass

    read = None
    readexactly = None
    readline = None
    wait_closed = None

    def write(self, *args) -> Any:
        pass


class StreamReader:
    """"""

    aclose = None
    awrite = None
    awritestr = None

    def close(self, *args) -> Any:
        pass

    drain = None

    def get_extra_info(self, *args) -> Any:
        pass

    read = None
    readexactly = None
    readline = None
    wait_closed = None

    def write(self, *args) -> Any:
        pass


class StreamWriter:
    """"""

    aclose = None
    awrite = None
    awritestr = None

    def close(self, *args) -> Any:
        pass

    drain = None

    def get_extra_info(self, *args) -> Any:
        pass

    read = None
    readexactly = None
    readline = None
    wait_closed = None

    def write(self, *args) -> Any:
        pass


core = None
open_connection = None
start_server = None
stream_awrite = None
