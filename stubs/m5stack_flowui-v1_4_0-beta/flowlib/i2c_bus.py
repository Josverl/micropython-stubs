"""
Module: 'flowlib.i2c_bus' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
from typing import Any


class I2C:
    """"""

    CBTYPE_ADDR = 1
    CBTYPE_NONE = 0
    CBTYPE_RXDATA = 2
    CBTYPE_TXDATA = 4
    MASTER = 1
    READ = 1
    SLAVE = 0
    WRITE = 0

    def address(self, *argv) -> Any:
        pass

    def begin(self, *argv) -> Any:
        pass

    def callback(self, *argv) -> Any:
        pass

    def clock_timing(self, *argv) -> Any:
        pass

    def data_timing(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def end(self, *argv) -> Any:
        pass

    def getdata(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def is_ready(self, *argv) -> Any:
        pass

    def read_byte(self, *argv) -> Any:
        pass

    def read_bytes(self, *argv) -> Any:
        pass

    def readfrom(self, *argv) -> Any:
        pass

    def readfrom_into(self, *argv) -> Any:
        pass

    def readfrom_mem(self, *argv) -> Any:
        pass

    def readfrom_mem_into(self, *argv) -> Any:
        pass

    def resetbusy(self, *argv) -> Any:
        pass

    def scan(self, *argv) -> Any:
        pass

    def setdata(self, *argv) -> Any:
        pass

    def start(self, *argv) -> Any:
        pass

    def start_timing(self, *argv) -> Any:
        pass

    def stop(self, *argv) -> Any:
        pass

    def stop_timing(self, *argv) -> Any:
        pass

    def timeout(self, *argv) -> Any:
        pass

    def write_byte(self, *argv) -> Any:
        pass

    def write_bytes(self, *argv) -> Any:
        pass

    def writeto(self, *argv) -> Any:
        pass

    def writeto_mem(self, *argv) -> Any:
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
    """"""

    def deinit(self, *argv) -> Any:
        pass

    def is_ready(self, *argv) -> Any:
        pass

    def readfrom(self, *argv) -> Any:
        pass

    def readfrom_into(self, *argv) -> Any:
        pass

    def readfrom_mem(self, *argv) -> Any:
        pass

    def readfrom_mem_into(self, *argv) -> Any:
        pass

    def scan(self, *argv) -> Any:
        pass

    def writeto(self, *argv) -> Any:
        pass

    def writeto_mem(self, *argv) -> Any:
        pass


bus_0 = None
bus_1 = None
bus_other = None


class easyI2C:
    """"""

    def available(self, *argv) -> Any:
        pass

    def read(self, *argv) -> Any:
        pass

    def read_reg(self, *argv) -> Any:
        pass

    def read_u16(self, *argv) -> Any:
        pass

    def read_u8(self, *argv) -> Any:
        pass

    def scan(self, *argv) -> Any:
        pass

    def write_u16(self, *argv) -> Any:
        pass

    def write_u8(self, *argv) -> Any:
        pass


def get():
    pass


struct = None
time = None
