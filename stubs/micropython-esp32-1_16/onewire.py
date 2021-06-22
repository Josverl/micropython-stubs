"""
Module: 'onewire' on micropython-esp32-1.16
"""
# MCU: {'ver': '1.16', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.16.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.16.0', 'machine': 'ESP32 module with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.9

class OneWire:
    ''
    MATCH_ROM = 85
    SEARCH_ROM = 240
    SKIP_ROM = 204
    def _search_rom():
        pass

    def crc8():
        pass

    def readbit():
        pass

    def readbyte():
        pass

    def readinto():
        pass

    def reset():
        pass

    def scan():
        pass

    def select_rom():
        pass

    def write():
        pass

    def writebit():
        pass

    def writebyte():
        pass


class OneWireError:
    ''
_ow = None
