"""
Network configuration.

MicroPython module: https://docs.micropython.org/en/v1.24.1/library/network.html

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
    print(nic.ipconfig("addr4"))

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
Module: 'network' on micropython-v1.24.1-stm32-PYBV11
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'stm32', 'board': 'PYBV11', 'cpu': 'STM32F405RG', 'mpy': 'v6.3', 'arch': 'armv7emsp'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, List, Optional, Tuple

STA_IF: int = 0
AP_IF: int = 1

def hostname(*args, **kwargs) -> Incomplete: ...
def route(*args, **kwargs) -> Incomplete: ...
def country(*args, **kwargs) -> Incomplete: ...
