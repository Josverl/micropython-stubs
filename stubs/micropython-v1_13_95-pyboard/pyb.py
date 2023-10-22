"""
Module: 'pyb' on pyboard 1.13.0-95
"""
# MCU: (sysname='pyboard', nodename='pyboard', release='1.13.0', version='v1.13-95-g0fff2e03f on 2020-10-03', machine='PYBv1.1 with STM32F405RG')
# Stubber: 1.3.4 - updated
from typing import Any


class ADC:
    """"""

    def read(self, *args) -> Any:
        pass

    def read_timed(self, *args) -> Any:
        pass

    def read_timed_multi(self, *args) -> Any:
        pass


class ADCAll:
    """"""

    def read_channel(self, *args) -> Any:
        pass

    def read_core_temp(self, *args) -> Any:
        pass

    def read_core_vbat(self, *args) -> Any:
        pass

    def read_core_vref(self, *args) -> Any:
        pass

    def read_vref(self, *args) -> Any:
        pass


class Accel:
    """"""

    def filtered_xyz(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass

    def tilt(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass

    def x(self, *args) -> Any:
        pass

    def y(self, *args) -> Any:
        pass

    def z(self, *args) -> Any:
        pass


class CAN:
    """"""

    BUS_OFF = 4
    ERROR_ACTIVE = 1
    ERROR_PASSIVE = 3
    ERROR_WARNING = 2
    LIST16 = 1
    LIST32 = 3
    LOOPBACK = 67108864
    MASK16 = 0
    MASK32 = 2
    NORMAL = 0
    SILENT = 134217728
    SILENT_LOOPBACK = 201326592
    STOPPED = 0

    def any(self, *args) -> Any:
        pass

    def clearfilter(self, *args) -> Any:
        pass

    def deinit(self, *args) -> Any:
        pass

    def info(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def initfilterbanks(self, *args) -> Any:
        pass

    def recv(self, *args) -> Any:
        pass

    def restart(self, *args) -> Any:
        pass

    def rxcallback(self, *args) -> Any:
        pass

    def send(self, *args) -> Any:
        pass

    def setfilter(self, *args) -> Any:
        pass

    def state(self, *args) -> Any:
        pass


class DAC:
    """"""

    CIRCULAR = 256
    NORMAL = 0

    def deinit(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def noise(self, *args) -> Any:
        pass

    def triangle(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass

    def write_timed(self, *args) -> Any:
        pass


class ExtInt:
    """"""

    EVT_FALLING = 270663680
    EVT_RISING = 269615104
    EVT_RISING_FALLING = 271712256
    IRQ_FALLING = 270598144
    IRQ_RISING = 269549568
    IRQ_RISING_FALLING = 271646720

    def disable(self, *args) -> Any:
        pass

    def enable(self, *args) -> Any:
        pass

    def line(self, *args) -> Any:
        pass

    def regs(self, *args) -> Any:
        pass

    def swint(self, *args) -> Any:
        pass


class Flash:
    """"""

    def ioctl(self, *args) -> Any:
        pass

    def readblocks(self, *args) -> Any:
        pass

    def writeblocks(self, *args) -> Any:
        pass


class I2C:
    """"""

    MASTER = 0
    SLAVE = 1

    def deinit(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def is_ready(self, *args) -> Any:
        pass

    def mem_read(self, *args) -> Any:
        pass

    def mem_write(self, *args) -> Any:
        pass

    def recv(self, *args) -> Any:
        pass

    def scan(self, *args) -> Any:
        pass

    def send(self, *args) -> Any:
        pass


class LCD:
    """"""

    def command(self, *args) -> Any:
        pass

    def contrast(self, *args) -> Any:
        pass

    def fill(self, *args) -> Any:
        pass

    def get(self, *args) -> Any:
        pass

    def light(self, *args) -> Any:
        pass

    def pixel(self, *args) -> Any:
        pass

    def show(self, *args) -> Any:
        pass

    def text(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass


class LED:
    """"""

    def intensity(self, *args) -> Any:
        pass

    def off(self, *args) -> Any:
        pass

    def on(self, *args) -> Any:
        pass

    def toggle(self, *args) -> Any:
        pass


class Pin:
    """"""

    AF1_TIM1 = 1
    AF1_TIM2 = 1
    AF2_TIM3 = 2
    AF2_TIM4 = 2
    AF2_TIM5 = 2
    AF3_TIM10 = 3
    AF3_TIM11 = 3
    AF3_TIM8 = 3
    AF3_TIM9 = 3
    AF4_I2C1 = 4
    AF4_I2C2 = 4
    AF5_SPI1 = 5
    AF5_SPI2 = 5
    AF7_USART1 = 7
    AF7_USART2 = 7
    AF7_USART3 = 7
    AF8_UART4 = 8
    AF8_USART6 = 8
    AF9_CAN1 = 9
    AF9_CAN2 = 9
    AF9_TIM12 = 9
    AF9_TIM13 = 9
    AF9_TIM14 = 9
    AF_OD = 18
    AF_PP = 2
    ALT = 2
    ALT_OPEN_DRAIN = 18
    ANALOG = 3
    IN = 0
    IRQ_FALLING = 270598144
    IRQ_RISING = 269549568
    OPEN_DRAIN = 17
    OUT = 1
    OUT_OD = 17
    OUT_PP = 1
    PULL_DOWN = 2
    PULL_NONE = 0
    PULL_UP = 1

    def af(self, *args) -> Any:
        pass

    def af_list(self, *args) -> Any:
        pass

    board = None
    cpu = None

    def debug(self, *args) -> Any:
        pass

    def dict(self, *args) -> Any:
        pass

    def gpio(self, *args) -> Any:
        pass

    def high(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def irq(self, *args) -> Any:
        pass

    def low(self, *args) -> Any:
        pass

    def mapper(self, *args) -> Any:
        pass

    def mode(self, *args) -> Any:
        pass

    def name(self, *args) -> Any:
        pass

    def names(self, *args) -> Any:
        pass

    def off(self, *args) -> Any:
        pass

    def on(self, *args) -> Any:
        pass

    def pin(self, *args) -> Any:
        pass

    def port(self, *args) -> Any:
        pass

    def pull(self, *args) -> Any:
        pass

    def value(self, *args) -> Any:
        pass


class RTC:
    """"""

    def calibration(self, *args) -> Any:
        pass

    def datetime(self, *args) -> Any:
        pass

    def info(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def wakeup(self, *args) -> Any:
        pass


SD = None


class SDCard:
    """"""

    def info(self, *args) -> Any:
        pass

    def ioctl(self, *args) -> Any:
        pass

    def power(self, *args) -> Any:
        pass

    def present(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass

    def readblocks(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass

    def writeblocks(self, *args) -> Any:
        pass


class SPI:
    """"""

    LSB = 128
    MASTER = 260
    MSB = 0
    SLAVE = 0

    def deinit(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def recv(self, *args) -> Any:
        pass

    def send(self, *args) -> Any:
        pass

    def send_recv(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass

    def write_readinto(self, *args) -> Any:
        pass


class Servo:
    """"""

    def angle(self, *args) -> Any:
        pass

    def calibration(self, *args) -> Any:
        pass

    def pulse_width(self, *args) -> Any:
        pass

    def speed(self, *args) -> Any:
        pass


class Switch:
    """"""

    def callback(self, *args) -> Any:
        pass

    def value(self, *args) -> Any:
        pass


class Timer:
    """"""

    BOTH = 10
    BRK_HIGH = 2
    BRK_LOW = 1
    BRK_OFF = 0
    CENTER = 32
    DOWN = 16
    ENC_A = 9
    ENC_AB = 11
    ENC_B = 10
    FALLING = 2
    HIGH = 0
    IC = 8
    LOW = 2
    OC_ACTIVE = 3
    OC_FORCED_ACTIVE = 6
    OC_FORCED_INACTIVE = 7
    OC_INACTIVE = 4
    OC_TIMING = 2
    OC_TOGGLE = 5
    PWM = 0
    PWM_INVERTED = 1
    RISING = 0
    UP = 0

    def callback(self, *args) -> Any:
        pass

    def channel(self, *args) -> Any:
        pass

    def counter(self, *args) -> Any:
        pass

    def deinit(self, *args) -> Any:
        pass

    def freq(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def period(self, *args) -> Any:
        pass

    def prescaler(self, *args) -> Any:
        pass

    def source_freq(self, *args) -> Any:
        pass


class UART:
    """"""

    CTS = 512
    IRQ_RXIDLE = 16
    RTS = 256

    def any(self, *args) -> Any:
        pass

    def deinit(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def irq(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass

    def readchar(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def readline(self, *args) -> Any:
        pass

    def sendbreak(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass

    def writechar(self, *args) -> Any:
        pass


class USB_HID:
    """"""

    def recv(self, *args) -> Any:
        pass

    def send(self, *args) -> Any:
        pass


class USB_VCP:
    """"""

    CTS = 2
    RTS = 1

    def any(self, *args) -> Any:
        pass

    def close(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def isconnected(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def readline(self, *args) -> Any:
        pass

    def readlines(self, *args) -> Any:
        pass

    def recv(self, *args) -> Any:
        pass

    def send(self, *args) -> Any:
        pass

    def setinterrupt(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass


def bootloader(*args) -> Any:
    pass


def country(*args) -> Any:
    pass


def delay(*args) -> Any:
    pass


def dht_readinto(*args) -> Any:
    pass


def disable_irq(*args) -> Any:
    pass


def elapsed_micros(*args) -> Any:
    pass


def elapsed_millis(*args) -> Any:
    pass


def enable_irq(*args) -> Any:
    pass


def fault_debug(*args) -> Any:
    pass


def freq(*args) -> Any:
    pass


def hard_reset(*args) -> Any:
    pass


def have_cdc(*args) -> Any:
    pass


def hid(*args) -> Any:
    pass


hid_keyboard = None
hid_mouse = None


def info(*args) -> Any:
    pass


def main(*args) -> Any:
    pass


def micros(*args) -> Any:
    pass


def millis(*args) -> Any:
    pass


def mount(*args) -> Any:
    pass


def pwm(*args) -> Any:
    pass


def repl_info(*args) -> Any:
    pass


def repl_uart(*args) -> Any:
    pass


def rng(*args) -> Any:
    pass


def servo(*args) -> Any:
    pass


def standby(*args) -> Any:
    pass


def stop(*args) -> Any:
    pass


def sync(*args) -> Any:
    pass


def udelay(*args) -> Any:
    pass


def unique_id(*args) -> Any:
    pass


def usb_mode(*args) -> Any:
    pass


def wfi(*args) -> Any:
    pass
