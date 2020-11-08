"""
Module: 'machine' on esp32_LoBo 3.2.9
"""
# MCU: (sysname='esp32_LoBo', nodename='esp32_LoBo', release='3.2.9', version='ESP32_LoBo_v3.2.9 on 2018-04-12', machine='ESP32 board with ESP32')
# Stubber: 1.1.2

class ADC:
    ''
    ATTN_0DB = 0
    ATTN_11DB = 3
    ATTN_2_5DB = 1
    ATTN_6DB = 2
    HALL = 8
    WIDTH_10BIT = 1
    WIDTH_11BIT = 2
    WIDTH_12BIT = 3
    WIDTH_9BIT = 0
    def atten():
        pass

    def read():
        pass

    def readraw():
        pass

    def vref():
        pass

    def width():
        pass


class DAC:
    ''
    def write():
        pass


class DHT:
    ''
    DHT11 = 0
    DHT2X = 1
    def read():
        pass

    def readinto():
        pass

EXT1_ALLLOW = 0
EXT1_ANYHIGH = 1
EXT1_ANYLOW = 2

class I2C:
    ''
    CB_DATA = 3
    CB_READ = 1
    CB_WRITE = 2
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

    def deinit():
        pass

    def end():
        pass

    def getdata():
        pass

    def init():
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

    def scan():
        pass

    def setdata():
        pass

    def slavewrite():
        pass

    def start():
        pass

    def stop():
        pass

    def write_byte():
        pass

    def write_bytes():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass

LOG_DEBUG = 4
LOG_ERROR = 1
LOG_INFO = 3
LOG_NONE = 0
LOG_VERBOSE = 5
LOG_WARN = 2

class Neopixel:
    ''
    BLACK = 0
    BLUE = 255
    CYAN = 65535
    GRAY = 8421504
    GREEN = 32768
    def HSBtoRGB():
        pass

    def HSBtoRGBint():
        pass

    LIME = 65280
    MAGENTA = 16711935
    MAROON = 8388608
    NAVY = 128
    OLIVE = 8421376
    PURPLE = 8388736
    RED = 16711680
    def RGBtoHSB():
        pass

    SILVER = 12632256
    TEAL = 32896
    TYPE_RGB = 0
    TYPE_RGBW = 1
    WHITE = 16777215
    YELLOW = 16776960
    def brightness():
        pass

    def clear():
        pass

    def color_order():
        pass

    def deinit():
        pass

    def get():
        pass

    def info():
        pass

    def rainbow():
        pass

    def set():
        pass

    def setHSB():
        pass

    def setHSBint():
        pass

    def setWhite():
        pass

    def show():
        pass

    def timings():
        pass


class Onewire:
    ''
    def crc8():
        pass

    def deinit():
        pass

    ds18x20 = None
    def readbyte():
        pass

    def readbytes():
        pass

    def reset():
        pass

    def rom_code():
        pass

    def scan():
        pass

    def search():
        pass

    def writebyte():
        pass

    def writebytes():
        pass


class PWM:
    ''
    def deinit():
        pass

    def duty():
        pass

    def freq():
        pass

    def init():
        pass

    def list():
        pass

    def pause():
        pass

    def resume():
        pass


class Pin:
    ''
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
    def init():
        pass

    def irq():
        pass

    def value():
        pass


class RTC:
    ''
    EXT1_ALLHIGH = 2
    EXT1_ALLLOW = 0
    EXT1_ANYHIGH = 1
    def clear():
        pass

    def init():
        pass

    def now():
        pass

    def ntp_state():
        pass

    def ntp_sync():
        pass

    def read():
        pass

    def read_string():
        pass

    def synced():
        pass

    def wake_on_ext0():
        pass

    def wake_on_ext1():
        pass

    def write():
        pass

    def write_string():
        pass


class SPI:
    ''
    HSPI = 1
    LSB = 1
    MSB = 0
    VSPI = 2
    def deinit():
        pass

    def deselect():
        pass

    def init():
        pass

    def read():
        pass

    def readfrom_mem():
        pass

    def readinto():
        pass

    def select():
        pass

    def write():
        pass

    def write_readinto():
        pass


class Signal:
    ''
    def off():
        pass

    def on():
        pass

    def value():
        pass


class Timer:
    ''
    CHRONO = 2
    EXTBASE = 3
    EXTENDED = 3
    ONE_SHOT = 0
    PERIODIC = 1
    def callback():
        pass

    def deinit():
        pass

    def events():
        pass

    def init():
        pass

    def isrunning():
        pass

    def pause():
        pass

    def period():
        pass

    def reshot():
        pass

    def resume():
        pass

    def start():
        pass

    def stop():
        pass

    def timernum():
        pass

    def value():
        pass


class TouchPad:
    ''
    def config():
        pass

    def read():
        pass


class UART:
    ''
    CBTYPE_DATA = 1
    CBTYPE_ERROR = 3
    CBTYPE_PATTERN = 2
    def any():
        pass

    def callback():
        pass

    def flush():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def readline():
        pass

    def readln():
        pass

    def write():
        pass

def deepsleep():
    pass

def disable_irq():
    pass

def enable_irq():
    pass

def freq():
    pass

def heap_info():
    pass

def idle():
    pass

def internal_temp():
    pass

def loglevel():
    pass

mem16 = None
mem32 = None
mem8 = None
def nvs_erase():
    pass

def nvs_erase_all():
    pass

def nvs_getint():
    pass

def nvs_getstr():
    pass

def nvs_setint():
    pass

def nvs_setstr():
    pass

def random():
    pass

def redirectlog():
    pass

def reset():
    pass

def restorelog():
    pass

def stdin_disable():
    pass

def stdin_get():
    pass

def stdout_put():
    pass

def time_pulse_us():
    pass

def unique_id():
    pass

def wake_description():
    pass

def wake_reason():
    pass

