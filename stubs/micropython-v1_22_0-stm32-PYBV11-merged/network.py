"""
Network configuration.

MicroPython module: https://docs.micropython.org/en/v1.22.0/library/network.html

This module provides network drivers and routing configuration. To use this
module, a MicroPython variant/build with network capabilities must be installed.
Network drivers for specific hardware are available within this module and are
used to configure hardware network interface(s). Network services provided
by configured interfaces are then available for use via the :mod:`socket`
module.

For example::

    # connect/ show IP config a specific network interface
    # see below for examples of specific drivers
    import network
    import time
    nic = network.Driver(...)
    if not nic.isconnected():
        nic.connect()
        print("Waiting for connection...")
        while not nic.isconnected():
            time.sleep(1)
    print(nic.ifconfig())

    # now use socket as usual
    import socket
    addr = socket.getaddrinfo('micropython.org', 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(b'GET / HTTP/1.1
Host: micropython.org

')
    data = s.recv(1000)
    s.close()

---
Module: 'network' on micropython-v1.22.0-stm32-PYBV11
"""

from __future__ import annotations

# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'stm32', 'board': 'PYBV11', 'cpu': 'STM32F405RG', 'mpy': 'v6.2', 'arch': 'armv7emsp'}
# Stubber: v1.16.2
from _typeshed import Incomplete
from typing import Any, List, Optional, Tuple, Union

STA_IF = 0  # type: int
AP_IF = 1  # type: int


def hostname(*args, **kwargs) -> Incomplete: ...


def route(*args, **kwargs) -> Incomplete: ...


def country(*args, **kwargs) -> Incomplete: ...
