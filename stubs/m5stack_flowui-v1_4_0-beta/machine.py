"""
Module: 'machine' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
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

    def atten(self, *argv) -> Any:
        pass

    def collect(self, *argv) -> Any:
        pass

    def collected(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def progress(self, *argv) -> Any:
        pass

    def read(self, *argv) -> Any:
        pass

    def read_timed(self, *argv) -> Any:
        pass

    def readraw(self, *argv) -> Any:
        pass

    def stopcollect(self, *argv) -> Any:
        pass

    def vref(self, *argv) -> Any:
        pass

    def width(self, *argv) -> Any:
        pass


class DAC:
    """"""

    CIRCULAR = 1
    NOISE = 4
    NORMAL = 1
    RAMP = 2
    SAWTOOTH = 3
    SINE = 0
    TRIANGLE = 1

    def beep(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def freq(self, *argv) -> Any:
        pass

    def stopwave(self, *argv) -> Any:
        pass

    def waveform(self, *argv) -> Any:
        pass

    def wavplay(self, *argv) -> Any:
        pass

    def write(self, *argv) -> Any:
        pass

    def write_buffer(self, *argv) -> Any:
        pass

    def write_timed(self, *argv) -> Any:
        pass


DEEPSLEEP = 4
DEEPSLEEP_RESET = 4
EXT0_WAKE = 2
EXT1_WAKE = 3
HARD_RESET = 2


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


class I2S:
    """"""

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

    def adc_enable(self, *argv) -> Any:
        pass

    def bits(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def nchannels(self, *argv) -> Any:
        pass

    def read(self, *argv) -> Any:
        pass

    def sample_rate(self, *argv) -> Any:
        pass

    def set_adc_pin(self, *argv) -> Any:
        pass

    def set_dac_mode(self, *argv) -> Any:
        pass

    def set_pin(self, *argv) -> Any:
        pass

    def start(self, *argv) -> Any:
        pass

    def stop(self, *argv) -> Any:
        pass

    def volume(self, *argv) -> Any:
        pass

    def write(self, *argv) -> Any:
        pass


class Neopixel:
    """"""

    BLACK = 0
    BLUE = 255
    CYAN = 65535
    GRAY = 8421504
    GREEN = 32768

    def HSBtoRGB(self, *argv) -> Any:
        pass

    def HSBtoRGBint(self, *argv) -> Any:
        pass

    LIME = 65280
    MAGENTA = 16711935
    MAROON = 8388608
    NAVY = 128
    OLIVE = 8421376
    PURPLE = 8388736
    RED = 16711680

    def RGBtoHSB(self, *argv) -> Any:
        pass

    SILVER = 12632256
    TEAL = 32896
    TYPE_RGB = 0
    TYPE_RGBW = 1
    WHITE = 16777215
    YELLOW = 16776960

    def brightness(self, *argv) -> Any:
        pass

    def clear(self, *argv) -> Any:
        pass

    def color_order(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def get(self, *argv) -> Any:
        pass

    def info(self, *argv) -> Any:
        pass

    def rainbow(self, *argv) -> Any:
        pass

    def set(self, *argv) -> Any:
        pass

    def setHSB(self, *argv) -> Any:
        pass

    def setHSBint(self, *argv) -> Any:
        pass

    def setWhite(self, *argv) -> Any:
        pass

    def show(self, *argv) -> Any:
        pass

    def timings(self, *argv) -> Any:
        pass


PIN_WAKE = 2


class PWM:
    """"""

    def deinit(self, *argv) -> Any:
        pass

    def duty(self, *argv) -> Any:
        pass

    def freq(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def list(self, *argv) -> Any:
        pass

    def pause(self, *argv) -> Any:
        pass

    def resume(self, *argv) -> Any:
        pass


PWRON_RESET = 1


class Pin:
    """"""

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

    def deinit(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def irq(self, *argv) -> Any:
        pass

    def off(self, *argv) -> Any:
        pass

    def on(self, *argv) -> Any:
        pass

    def value(self, *argv) -> Any:
        pass


class RTC:
    """"""

    def datetime(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def memory(self, *argv) -> Any:
        pass


SLEEP = 2
SOFT_RESET = 5


class Signal:
    """"""

    def off(self, *argv) -> Any:
        pass

    def on(self, *argv) -> Any:
        pass

    def value(self, *argv) -> Any:
        pass


TIMER_WAKE = 4
TOUCHPAD_WAKE = 5


class Timer:
    """"""

    ONE_SHOT = 0
    PERIODIC = 1

    def deinit(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def value(self, *argv) -> Any:
        pass


class TouchPad:
    """"""

    def config(self, *argv) -> Any:
        pass

    def read(self, *argv) -> Any:
        pass


class UART:
    """"""

    def any(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def read(self, *argv) -> Any:
        pass

    def readinto(self, *argv) -> Any:
        pass

    def readline(self, *argv) -> Any:
        pass

    def sendbreak(self, *argv) -> Any:
        pass

    def write(self, *argv) -> Any:
        pass


ULP_WAKE = 6


class WDT:
    """"""

    def feed(self, *argv) -> Any:
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
