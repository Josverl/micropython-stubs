"""
Module: 'machine' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1

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

    def collect():
        pass

    def collected():
        pass

    def deinit():
        pass

    def progress():
        pass

    def read():
        pass

    def read_timed():
        pass

    def readraw():
        pass

    def stopcollect():
        pass

    def vref():
        pass

    def width():
        pass


class DAC:
    ''
    CIRCULAR = 1
    NOISE = 4
    NORMAL = 1
    RAMP = 2
    SAWTOOTH = 3
    SINE = 0
    TRIANGLE = 1
    def beep():
        pass

    def deinit():
        pass

    def freq():
        pass

    def stopwave():
        pass

    def waveform():
        pass

    def wavplay():
        pass

    def write():
        pass

    def write_buffer():
        pass

    def write_timed():
        pass

DEEPSLEEP = 4
DEEPSLEEP_RESET = 4
EXT0_WAKE = 2
EXT1_WAKE = 3
HARD_RESET = 2

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


class I2S:
    ''
    CHANNEL_ALL_LEFT = 2
    CHANNEL_ALL_RIGHT = 1
    CHANNEL_ONLY_LEFT = 4
    CHANNEL_ONLY_RIGHT = 3
    CHANNEL_RIGHT_LEFT = 0
    DAC_BOTH_EN = 3
    DAC_DISABLE = 0
    DAC_LEFT_EN = 2
    DAC_RIGHT_EN = 1
    FORMAT_I2S = 1
    FORMAT_I2S_LSB = 4
    FORMAT_I2S_MSB = 2
    FORMAT_PCM = 8
    FORMAT_PCM_LONG = 32
    FORMAT_PCM_SHORT = 16
    I2S_NUM_0 = 0
    I2S_NUM_1 = 1
    MODE_ADC_BUILT_IN = 32
    MODE_DAC_BUILT_IN = 16
    MODE_MASTER = 1
    MODE_PDM = 64
    MODE_RX = 8
    MODE_SLAVE = 2
    MODE_TX = 4
    def adc_enable():
        pass

    def bits():
        pass

    def deinit():
        pass

    def init():
        pass

    def nchannels():
        pass

    def read():
        pass

    def sample_rate():
        pass

    def set_adc_pin():
        pass

    def set_dac_mode():
        pass

    def set_pin():
        pass

    def start():
        pass

    def stop():
        pass

    def volume():
        pass

    def write():
        pass


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

PIN_WAKE = 2

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

PWRON_RESET = 1

class Pin:
    ''
    IN = 1
    INOUT = 3
    IRQ_FALLING = 2
    IRQ_RISING = 1
    OPEN_DRAIN = 7
    OUT = 3
    OUT_OD = 6
    PULL_DOWN = 1
    PULL_FLOAT = 3
    PULL_HOLD = 4
    PULL_UP = 2
    WAKE_HIGH = 5
    WAKE_LOW = 4
    def deinit():
        pass

    def init():
        pass

    def irq():
        pass

    def off():
        pass

    def on():
        pass

    def value():
        pass


class RTC:
    ''
    def datetime():
        pass

    def init():
        pass

    def memory():
        pass

SLEEP = 2
SOFT_RESET = 5

class Signal:
    ''
    def off():
        pass

    def on():
        pass

    def value():
        pass

TIMER_WAKE = 4
TOUCHPAD_WAKE = 5

class Timer:
    ''
    ONE_SHOT = 0
    PERIODIC = 1
    def deinit():
        pass

    def init():
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
    def any():
        pass

    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def readline():
        pass

    def sendbreak():
        pass

    def write():
        pass

ULP_WAKE = 6

class WDT:
    ''
    def feed():
        pass

WDT_RESET = 3
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

def lightsleep():
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

def reset():
    pass

def reset_cause():
    pass

def sleep():
    pass

def time_pulse_us():
    pass

def unique_id():
    pass

def wake_reason():
    pass

