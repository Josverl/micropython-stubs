"""
Module: 'ak8963' on esp32_LoBo
MCU: (sysname='esp32_LoBo', nodename='esp32_LoBo', release='3.2.24', version='ESP32_LoBo_v3.2.24 on 2018-09-06', machine='ESP32 board with ESP32')
Stubber: 1.0.0
"""

class AK8963:
    ''
    def _register_char():
        pass

    def _register_short():
        pass

    def _register_three_shorts():
        pass

    adjustement = None
    magnetic = None
    whoami = None

class I2C:
    ''
    CBTYPE_ADDR = 1
    CBTYPE_NONE = 0
    CBTYPE_RXDATA = 2
    CBTYPE_TXDATA = 4
    MASTER = 1
    READ = 1
    SLAVE = 0
    WRITE = 0
    def address():
        pass

    def begin():
        pass

    def callback():
        pass

    def clock_timing():
        pass

    def data_timing():
        pass

    def deinit():
        pass

    def end():
        pass

    def getdata():
        pass

    def init():
        pass

    def is_ready():
        pass

    def read_byte():
        pass

    def read_bytes():
        pass

    def readfrom():
        pass

    def readfrom_into():
        pass

    def readfrom_mem():
        pass

    def readfrom_mem_into():
        pass

    def resetbusy():
        pass

    def scan():
        pass

    def setdata():
        pass

    def start():
        pass

    def start_timing():
        pass

    def stop():
        pass

    def stop_timing():
        pass

    def timeout():
        pass

    def write_byte():
        pass

    def write_bytes():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass

MODE_CONTINOUS_MEASURE_1 = 2
MODE_CONTINOUS_MEASURE_2 = 6
MODE_EXTERNAL_TRIGGER_MEASURE = 4
MODE_SINGLE_MEASURE = 1
OUTPUT_14_BIT = 0
OUTPUT_16_BIT = 16

class Pin:
    ''
    IN = 1
    INOUT = 3
    INOUT_OD = 7
    IRQ_ANYEDGE = 3
    IRQ_DISABLE = 0
    IRQ_FALLING = 2
    IRQ_HILEVEL = 5
    IRQ_LOLEVEL = 4
    IRQ_RISING = 1
    OUT = 2
    OUT_OD = 6
    PULL_DOWN = 1
    PULL_FLOAT = 3
    PULL_UP = 0
    PULL_UPDOWN = 2
    def init():
        pass

    def irqvalue():
        pass

    def value():
        pass

_MODE_FUSE_ROM_ACCESS = 15
_MODE_POWER_DOWN = 0
_MODE_SELF_TEST = 8
_SO_14BIT = 0.6
_SO_16BIT = 0.15
def const():
    pass

ustruct = None
