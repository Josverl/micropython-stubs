"""
Module: 'flowlib.i2c_bus' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1

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

M_BUS = None
PAHUB0 = None
PAHUB1 = None
PAHUB2 = None
PAHUB3 = None
PAHUB4 = None
PAHUB5 = None
PORTA = None
PORTC = None

class Pahub_I2C:
    ''
    def deinit():
        pass

    def is_ready():
        pass

    def readfrom():
        pass

    def readfrom_into():
        pass

    def readfrom_mem():
        pass

    def readfrom_mem_into():
        pass

    def scan():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass

bus_0 = None
bus_1 = None
bus_other = None

class easyI2C:
    ''
    def available():
        pass

    def read():
        pass

    def read_reg():
        pass

    def read_u16():
        pass

    def read_u8():
        pass

    def scan():
        pass

    def write_u16():
        pass

    def write_u8():
        pass

def get():
    pass

struct = None
time = None
