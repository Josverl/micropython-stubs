"""
Module: 'uasyncio.event' on micropython-esp32-1.16
"""
# MCU: {'ver': '1.16', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.16.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.16.0', 'machine': 'ESP32 module with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.9

class Event:
    ''
    def clear():
        pass

    def is_set():
        pass

    def set():
        pass

    wait = None

class ThreadSafeFlag:
    ''
    def ioctl():
        pass

    def set():
        pass

    wait = None
core = None
uio = None
