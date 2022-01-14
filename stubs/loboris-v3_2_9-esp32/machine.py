"""
Module: 'machine' on esp32_LoBo 3.2.9
"""
# MCU: (sysname='esp32_LoBo', nodename='esp32_LoBo', release='3.2.9', version='ESP32_LoBo_v3.2.9 on 2018-04-12', machine='ESP32 board with ESP32')
# Stubber: 1.1.2 - updated
from typing import Any


class ADC:
    """"""

    ATTN_0DB = 0
    ATTN_11DB = 3
    ATTN_2_5DB = 1
    ATTN_6DB = 2
    HALL = 8
    WIDTH_10BIT = 1
    WIDTH_11BIT = 2
    WIDTH_12BIT = 3
    WIDTH_9BIT = 0

    def atten(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass

    def readraw(self, *args) -> Any:
        pass

    def vref(self, *args) -> Any:
        pass

    def width(self, *args) -> Any:
        pass


class DAC:
    """"""

    def write(self, *args) -> Any:
        pass


class DHT:
    """"""

    DHT11 = 0
    DHT2X = 1

    def read(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass


EXT1_ALLLOW = 0
EXT1_ANYHIGH = 1
EXT1_ANYLOW = 2


class I2C:
    """"""

    CB_DATA = 3
    CB_READ = 1
    CB_WRITE = 2
    MASTER = 1
    READ = 1
    SLAVE = 0
    WRITE = 0

    def address(self, *args) -> Any:
        pass

    def begin(self, *args) -> Any:
        pass

    def callback(self, *args) -> Any:
        pass

    def deinit(self, *args) -> Any:
        pass

    def end(self, *args) -> Any:
        pass

    def getdata(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def read_byte(self, *args) -> Any:
        pass

    def read_bytes(self, *args) -> Any:
        pass

    def readfrom(self, *args) -> Any:
        pass

    def readfrom_into(self, *args) -> Any:
        pass

    def readfrom_mem(self, *args) -> Any:
        pass

    def readfrom_mem_into(self, *args) -> Any:
        pass

    def scan(self, *args) -> Any:
        pass

    def setdata(self, *args) -> Any:
        pass

    def slavewrite(self, *args) -> Any:
        pass

    def start(self, *args) -> Any:
        pass

    def stop(self, *args) -> Any:
        pass

    def write_byte(self, *args) -> Any:
        pass

    def write_bytes(self, *args) -> Any:
        pass

    def writeto(self, *args) -> Any:
        pass

    def writeto_mem(self, *args) -> Any:
        pass


LOG_DEBUG = 4
LOG_ERROR = 1
LOG_INFO = 3
LOG_NONE = 0
LOG_VERBOSE = 5
LOG_WARN = 2


class Neopixel:
    """"""

    BLACK = 0
    BLUE = 255
    CYAN = 65535
    GRAY = 8421504
    GREEN = 32768

    def HSBtoRGB(self, *args) -> Any:
        pass

    def HSBtoRGBint(self, *args) -> Any:
        pass

    LIME = 65280
    MAGENTA = 16711935
    MAROON = 8388608
    NAVY = 128
    OLIVE = 8421376
    PURPLE = 8388736
    RED = 16711680

    def RGBtoHSB(self, *args) -> Any:
        pass

    SILVER = 12632256
    TEAL = 32896
    TYPE_RGB = 0
    TYPE_RGBW = 1
    WHITE = 16777215
    YELLOW = 16776960

    def brightness(self, *args) -> Any:
        pass

    def clear(self, *args) -> Any:
        pass

    def color_order(self, *args) -> Any:
        pass

    def deinit(self, *args) -> Any:
        pass

    def get(self, *args) -> Any:
        pass

    def info(self, *args) -> Any:
        pass

    def rainbow(self, *args) -> Any:
        pass

    def set(self, *args) -> Any:
        pass

    def setHSB(self, *args) -> Any:
        pass

    def setHSBint(self, *args) -> Any:
        pass

    def setWhite(self, *args) -> Any:
        pass

    def show(self, *args) -> Any:
        pass

    def timings(self, *args) -> Any:
        pass


class Onewire:
    """"""

    def crc8(self, *args) -> Any:
        pass

    def deinit(self, *args) -> Any:
        pass

    ds18x20 = None

    def readbyte(self, *args) -> Any:
        pass

    def readbytes(self, *args) -> Any:
        pass

    def reset(self, *args) -> Any:
        pass

    def rom_code(self, *args) -> Any:
        pass

    def scan(self, *args) -> Any:
        pass

    def search(self, *args) -> Any:
        pass

    def writebyte(self, *args) -> Any:
        pass

    def writebytes(self, *args) -> Any:
        pass


class PWM:
    """"""

    def deinit(self, *args) -> Any:
        pass

    def duty(self, *args) -> Any:
        pass

    def freq(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def list(self, *args) -> Any:
        pass

    def pause(self, *args) -> Any:
        pass

    def resume(self, *args) -> Any:
        pass


class Pin:
    """"""

    IN = 1
    INOUT = 3
    INOUT_OD = 7
    IRQ_ANYEDGE = 3
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

    def init(self, *args) -> Any:
        pass

    def irq(self, *args) -> Any:
        pass

    def value(self, *args) -> Any:
        pass


class RTC:
    """"""

    EXT1_ALLHIGH = 2
    EXT1_ALLLOW = 0
    EXT1_ANYHIGH = 1

    def clear(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def now(self, *args) -> Any:
        pass

    def ntp_state(self, *args) -> Any:
        pass

    def ntp_sync(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass

    def read_string(self, *args) -> Any:
        pass

    def synced(self, *args) -> Any:
        pass

    def wake_on_ext0(self, *args) -> Any:
        pass

    def wake_on_ext1(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass

    def write_string(self, *args) -> Any:
        pass


class SPI:
    """"""

    HSPI = 1
    LSB = 1
    MSB = 0
    VSPI = 2

    def deinit(self, *args) -> Any:
        pass

    def deselect(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass

    def readfrom_mem(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def select(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass

    def write_readinto(self, *args) -> Any:
        pass


class Signal:
    """"""

    def off(self, *args) -> Any:
        pass

    def on(self, *args) -> Any:
        pass

    def value(self, *args) -> Any:
        pass


class Timer:
    """"""

    CHRONO = 2
    EXTBASE = 3
    EXTENDED = 3
    ONE_SHOT = 0
    PERIODIC = 1

    def callback(self, *args) -> Any:
        pass

    def deinit(self, *args) -> Any:
        pass

    def events(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def isrunning(self, *args) -> Any:
        pass

    def pause(self, *args) -> Any:
        pass

    def period(self, *args) -> Any:
        pass

    def reshot(self, *args) -> Any:
        pass

    def resume(self, *args) -> Any:
        pass

    def start(self, *args) -> Any:
        pass

    def stop(self, *args) -> Any:
        pass

    def timernum(self, *args) -> Any:
        pass

    def value(self, *args) -> Any:
        pass


class TouchPad:
    """"""

    def config(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass


class UART:
    """"""

    CBTYPE_DATA = 1
    CBTYPE_ERROR = 3
    CBTYPE_PATTERN = 2

    def any(self, *args) -> Any:
        pass

    def callback(self, *args) -> Any:
        pass

    def flush(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def readline(self, *args) -> Any:
        pass

    def readln(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass


def deepsleep(*args) -> Any:
    pass


def disable_irq(*args) -> Any:
    pass


def enable_irq(*args) -> Any:
    pass


def freq(*args) -> Any:
    pass


def heap_info(*args) -> Any:
    pass


def idle(*args) -> Any:
    pass


def internal_temp(*args) -> Any:
    pass


def loglevel(*args) -> Any:
    pass


mem16 = None
mem32 = None
mem8 = None


def nvs_erase(*args) -> Any:
    pass


def nvs_erase_all(*args) -> Any:
    pass


def nvs_getint(*args) -> Any:
    pass


def nvs_getstr(*args) -> Any:
    pass


def nvs_setint(*args) -> Any:
    pass


def nvs_setstr(*args) -> Any:
    pass


def random(*args) -> Any:
    pass


def redirectlog(*args) -> Any:
    pass


def reset(*args) -> Any:
    pass


def restorelog(*args) -> Any:
    pass


def stdin_disable(*args) -> Any:
    pass


def stdin_get(*args) -> Any:
    pass


def stdout_put(*args) -> Any:
    pass


def time_pulse_us(*args) -> Any:
    pass


def unique_id(*args) -> Any:
    pass


def wake_description(*args) -> Any:
    pass


def wake_reason(*args) -> Any:
    pass
