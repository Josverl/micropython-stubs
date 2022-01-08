"""
Module: 'flowlib.units._adc' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1
ADDRESS = 72

class Adc:
    ''
    def _available():
        pass

    def _read_u16():
        pass

    def _write_u8():
        pass

    def deinit():
        pass

    def measure_set():
        pass

    voltage = None
GAIN_EIGHT = 3
GAIN_FOUR = 2
GAIN_ONE = 0
GAIN_TWO = 1
MODE_CONTIN = 0
MODE_SINGLE = 16
OSMODE_STATE = 128
RATE_15 = 12
RATE_240 = 0
RATE_30 = 8
RATE_60 = 4
def const():
    pass

i2c_bus = None
struct = None
unit = None
