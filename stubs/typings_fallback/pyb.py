"""
Module: 'pyb' on micropython-v1.17-pyboard
"""
# MCU: {'ver': 'v1.17', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.17.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.17.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.2
from typing import Any


def main(*args) -> Any:
    ...


def stop(*args) -> Any:
    ...


SD: Any  ## <class 'SDCard'> = <SDCard>


class DAC:
    """"""

    def write(self, *args) -> Any:
        ...

    CIRCULAR = 256  # type: int
    NORMAL = 0  # type: int

    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def noise(self, *args) -> Any:
        ...

    def triangle(self, *args) -> Any:
        ...

    def write_timed(self, *args) -> Any:
        ...


class RTC:
    """"""

    def calibration(self, *args) -> Any:
        ...

    def datetime(self, *args) -> Any:
        ...

    def info(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def wakeup(self, *args) -> Any:
        ...


class ADC:
    """"""

    def read(self, *args) -> Any:
        ...

    def read_timed(self, *args) -> Any:
        ...

    def read_timed_multi(self, *args) -> Any:
        ...


class ADCAll:
    """"""

    def read_channel(self, *args) -> Any:
        ...

    def read_core_temp(self, *args) -> Any:
        ...

    def read_core_vbat(self, *args) -> Any:
        ...

    def read_core_vref(self, *args) -> Any:
        ...

    def read_vref(self, *args) -> Any:
        ...


class Accel:
    """"""

    def read(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    def filtered_xyz(self, *args) -> Any:
        ...

    def tilt(self, *args) -> Any:
        ...

    def x(self, *args) -> Any:
        ...

    def y(self, *args) -> Any:
        ...

    def z(self, *args) -> Any:
        ...


class CAN:
    """"""

    def any(self, *args) -> Any:
        ...

    def send(self, *args) -> Any:
        ...

    BUS_OFF = 4  # type: int
    ERROR_ACTIVE = 1  # type: int
    ERROR_PASSIVE = 3  # type: int
    ERROR_WARNING = 2  # type: int
    LIST16 = 1  # type: int
    LIST32 = 3  # type: int
    LOOPBACK = 67108864  # type: int
    MASK16 = 0  # type: int
    MASK32 = 2  # type: int
    NORMAL = 0  # type: int
    SILENT = 134217728  # type: int
    SILENT_LOOPBACK = 201326592  # type: int
    STOPPED = 0  # type: int

    def clearfilter(self, *args) -> Any:
        ...

    def deinit(self, *args) -> Any:
        ...

    def info(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    @classmethod
    def initfilterbanks(cls, *args) -> Any:
        ...

    def recv(self, *args) -> Any:
        ...

    def restart(self, *args) -> Any:
        ...

    def rxcallback(self, *args) -> Any:
        ...

    def setfilter(self, *args) -> Any:
        ...

    def state(self, *args) -> Any:
        ...


class ExtInt:
    """"""

    EVT_FALLING = 270663680  # type: int
    EVT_RISING = 269615104  # type: int
    EVT_RISING_FALLING = 271712256  # type: int
    IRQ_FALLING = 270598144  # type: int
    IRQ_RISING = 269549568  # type: int
    IRQ_RISING_FALLING = 271646720  # type: int

    def disable(self, *args) -> Any:
        ...

    def enable(self, *args) -> Any:
        ...

    def line(self, *args) -> Any:
        ...

    def regs(self, *args) -> Any:
        ...

    def swint(self, *args) -> Any:
        ...


class Flash:
    """"""

    def ioctl(self, *args) -> Any:
        ...

    def readblocks(self, *args) -> Any:
        ...

    def writeblocks(self, *args) -> Any:
        ...


class I2C:
    """"""

    def send(self, *args) -> Any:
        ...

    CONTROLLER = 0  # type: int
    MASTER = 0  # type: int
    PERIPHERAL = 1  # type: int
    SLAVE = 1  # type: int

    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def is_ready(self, *args) -> Any:
        ...

    def mem_read(self, *args) -> Any:
        ...

    def mem_write(self, *args) -> Any:
        ...

    def recv(self, *args) -> Any:
        ...

    def scan(self, *args) -> Any:
        ...


class LCD:
    """"""

    def get(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    def command(self, *args) -> Any:
        ...

    def contrast(self, *args) -> Any:
        ...

    def fill(self, *args) -> Any:
        ...

    def light(self, *args) -> Any:
        ...

    def pixel(self, *args) -> Any:
        ...

    def show(self, *args) -> Any:
        ...

    def text(self, *args) -> Any:
        ...


class LED:
    """"""

    def intensity(self, *args) -> Any:
        ...

    def off(self, *args) -> Any:
        ...

    def on(self, *args) -> Any:
        ...

    def toggle(self, *args) -> Any:
        ...


class Pin:
    """"""

    @classmethod
    def dict(cls, *args) -> Any:
        ...

    def value(self, *args) -> Any:
        ...

    AF1_TIM1 = 1  # type: int
    AF1_TIM2 = 1  # type: int
    AF2_TIM3 = 2  # type: int
    AF2_TIM4 = 2  # type: int
    AF2_TIM5 = 2  # type: int
    AF3_TIM10 = 3  # type: int
    AF3_TIM11 = 3  # type: int
    AF3_TIM8 = 3  # type: int
    AF3_TIM9 = 3  # type: int
    AF4_I2C1 = 4  # type: int
    AF4_I2C2 = 4  # type: int
    AF5_I2S2 = 5  # type: int
    AF5_SPI1 = 5  # type: int
    AF5_SPI2 = 5  # type: int
    AF6_I2S2 = 6  # type: int
    AF7_USART1 = 7  # type: int
    AF7_USART2 = 7  # type: int
    AF7_USART3 = 7  # type: int
    AF8_UART4 = 8  # type: int
    AF8_USART6 = 8  # type: int
    AF9_CAN1 = 9  # type: int
    AF9_CAN2 = 9  # type: int
    AF9_TIM12 = 9  # type: int
    AF9_TIM13 = 9  # type: int
    AF9_TIM14 = 9  # type: int
    AF_OD = 18  # type: int
    AF_PP = 2  # type: int
    ALT = 2  # type: int
    ALT_OPEN_DRAIN = 18  # type: int
    ANALOG = 3  # type: int
    IN = 0  # type: int
    IRQ_FALLING = 270598144  # type: int
    IRQ_RISING = 269549568  # type: int
    OPEN_DRAIN = 17  # type: int
    OUT = 1  # type: int
    OUT_OD = 17  # type: int
    OUT_PP = 1  # type: int
    PULL_DOWN = 2  # type: int
    PULL_NONE = 0  # type: int
    PULL_UP = 1  # type: int

    def af(self, *args) -> Any:
        ...

    def af_list(self, *args) -> Any:
        ...

    class board:
        """"""

        LED_BLUE: Any  ## <class 'Pin'> = Pin(Pin.cpu.B4, mode=Pin.OUT)
        LED_GREEN: Any  ## <class 'Pin'> = Pin(Pin.cpu.A14, mode=Pin.OUT)
        LED_RED: Any  ## <class 'Pin'> = Pin(Pin.cpu.A13, mode=Pin.OUT)
        LED_YELLOW: Any  ## <class 'Pin'> = Pin(Pin.cpu.A15, mode=Pin.OUT)
        MMA_AVDD: Any  ## <class 'Pin'> = Pin(Pin.cpu.B5, mode=Pin.OUT)
        MMA_INT: Any  ## <class 'Pin'> = Pin(Pin.cpu.B2, mode=Pin.IN)
        SD: Any  ## <class 'Pin'> = Pin(Pin.cpu.A8, mode=Pin.IN, pull=Pin.PULL_UP)
        SD_CK: Any  ## <class 'Pin'> = Pin(Pin.cpu.C12, mode=Pin.ALT, pull=Pin.PULL_UP, af=12)
        SD_CMD: Any  ## <class 'Pin'> = Pin(Pin.cpu.D2, mode=Pin.ALT, pull=Pin.PULL_UP, af=12)
        SD_D0: Any  ## <class 'Pin'> = Pin(Pin.cpu.C8, mode=Pin.ALT, pull=Pin.PULL_UP, af=12)
        SD_D1: Any  ## <class 'Pin'> = Pin(Pin.cpu.C9, mode=Pin.ALT, pull=Pin.PULL_UP, af=12)
        SD_D2: Any  ## <class 'Pin'> = Pin(Pin.cpu.C10, mode=Pin.ALT, pull=Pin.PULL_UP, af=12)
        SD_D3: Any  ## <class 'Pin'> = Pin(Pin.cpu.C11, mode=Pin.ALT, pull=Pin.PULL_UP, af=12)
        SD_SW: Any  ## <class 'Pin'> = Pin(Pin.cpu.A8, mode=Pin.IN, pull=Pin.PULL_UP)
        SW: Any  ## <class 'Pin'> = Pin(Pin.cpu.B3, mode=Pin.IN, pull=Pin.PULL_UP)
        USB_DM: Any  ## <class 'Pin'> = Pin(Pin.cpu.A11, mode=Pin.ALT, af=10)
        USB_DP: Any  ## <class 'Pin'> = Pin(Pin.cpu.A12, mode=Pin.ALT, af=10)
        USB_ID: Any  ## <class 'Pin'> = Pin(Pin.cpu.A10, mode=Pin.ALT_OPEN_DRAIN, pull=Pin.PULL_UP, af=10)
        USB_VBUS: Any  ## <class 'Pin'> = Pin(Pin.cpu.A9, mode=Pin.IN)
        X1: Any  ## <class 'Pin'> = Pin(Pin.cpu.A0, mode=Pin.IN)
        X10: Any  ## <class 'Pin'> = Pin(Pin.cpu.B7, mode=Pin.IN)
        X11: Any  ## <class 'Pin'> = Pin(Pin.cpu.C4, mode=Pin.IN)
        X12: Any  ## <class 'Pin'> = Pin(Pin.cpu.C5, mode=Pin.IN)
        X17: Any  ## <class 'Pin'> = Pin(Pin.cpu.B3, mode=Pin.IN, pull=Pin.PULL_UP)
        X18: Any  ## <class 'Pin'> = Pin(Pin.cpu.C13, mode=Pin.IN)
        X19: Any  ## <class 'Pin'> = Pin(Pin.cpu.C0, mode=Pin.IN)
        X2: Any  ## <class 'Pin'> = Pin(Pin.cpu.A1, mode=Pin.IN)
        X20: Any  ## <class 'Pin'> = Pin(Pin.cpu.C1, mode=Pin.IN)
        X21: Any  ## <class 'Pin'> = Pin(Pin.cpu.C2, mode=Pin.IN)
        X22: Any  ## <class 'Pin'> = Pin(Pin.cpu.C3, mode=Pin.IN)
        X3: Any  ## <class 'Pin'> = Pin(Pin.cpu.A2, mode=Pin.IN)
        X4: Any  ## <class 'Pin'> = Pin(Pin.cpu.A3, mode=Pin.IN)
        X5: Any  ## <class 'Pin'> = Pin(Pin.cpu.A4, mode=Pin.IN)
        X6: Any  ## <class 'Pin'> = Pin(Pin.cpu.A5, mode=Pin.IN)
        X7: Any  ## <class 'Pin'> = Pin(Pin.cpu.A6, mode=Pin.IN)
        X8: Any  ## <class 'Pin'> = Pin(Pin.cpu.A7, mode=Pin.IN)
        X9: Any  ## <class 'Pin'> = Pin(Pin.cpu.B6, mode=Pin.IN)
        Y1: Any  ## <class 'Pin'> = Pin(Pin.cpu.C6, mode=Pin.IN)
        Y10: Any  ## <class 'Pin'> = Pin(Pin.cpu.B11, mode=Pin.IN)
        Y11: Any  ## <class 'Pin'> = Pin(Pin.cpu.B0, mode=Pin.IN)
        Y12: Any  ## <class 'Pin'> = Pin(Pin.cpu.B1, mode=Pin.IN)
        Y2: Any  ## <class 'Pin'> = Pin(Pin.cpu.C7, mode=Pin.IN)
        Y3: Any  ## <class 'Pin'> = Pin(Pin.cpu.B8, mode=Pin.IN)
        Y4: Any  ## <class 'Pin'> = Pin(Pin.cpu.B9, mode=Pin.IN)
        Y5: Any  ## <class 'Pin'> = Pin(Pin.cpu.B12, mode=Pin.IN)
        Y6: Any  ## <class 'Pin'> = Pin(Pin.cpu.B13, mode=Pin.IN)
        Y7: Any  ## <class 'Pin'> = Pin(Pin.cpu.B14, mode=Pin.IN)
        Y8: Any  ## <class 'Pin'> = Pin(Pin.cpu.B15, mode=Pin.IN)
        Y9: Any  ## <class 'Pin'> = Pin(Pin.cpu.B10, mode=Pin.IN)

    class cpu:
        """"""

        A0: Any  ## <class 'Pin'> = Pin(Pin.cpu.A0, mode=Pin.IN)
        A1: Any  ## <class 'Pin'> = Pin(Pin.cpu.A1, mode=Pin.IN)
        A10: Any  ## <class 'Pin'> = Pin(Pin.cpu.A10, mode=Pin.ALT_OPEN_DRAIN, pull=Pin.PULL_UP, af=10)
        A11: Any  ## <class 'Pin'> = Pin(Pin.cpu.A11, mode=Pin.ALT, af=10)
        A12: Any  ## <class 'Pin'> = Pin(Pin.cpu.A12, mode=Pin.ALT, af=10)
        A13: Any  ## <class 'Pin'> = Pin(Pin.cpu.A13, mode=Pin.OUT)
        A14: Any  ## <class 'Pin'> = Pin(Pin.cpu.A14, mode=Pin.OUT)
        A15: Any  ## <class 'Pin'> = Pin(Pin.cpu.A15, mode=Pin.OUT)
        A2: Any  ## <class 'Pin'> = Pin(Pin.cpu.A2, mode=Pin.IN)
        A3: Any  ## <class 'Pin'> = Pin(Pin.cpu.A3, mode=Pin.IN)
        A4: Any  ## <class 'Pin'> = Pin(Pin.cpu.A4, mode=Pin.IN)
        A5: Any  ## <class 'Pin'> = Pin(Pin.cpu.A5, mode=Pin.IN)
        A6: Any  ## <class 'Pin'> = Pin(Pin.cpu.A6, mode=Pin.IN)
        A7: Any  ## <class 'Pin'> = Pin(Pin.cpu.A7, mode=Pin.IN)
        A8: Any  ## <class 'Pin'> = Pin(Pin.cpu.A8, mode=Pin.IN, pull=Pin.PULL_UP)
        A9: Any  ## <class 'Pin'> = Pin(Pin.cpu.A9, mode=Pin.IN)
        B0: Any  ## <class 'Pin'> = Pin(Pin.cpu.B0, mode=Pin.IN)
        B1: Any  ## <class 'Pin'> = Pin(Pin.cpu.B1, mode=Pin.IN)
        B10: Any  ## <class 'Pin'> = Pin(Pin.cpu.B10, mode=Pin.IN)
        B11: Any  ## <class 'Pin'> = Pin(Pin.cpu.B11, mode=Pin.IN)
        B12: Any  ## <class 'Pin'> = Pin(Pin.cpu.B12, mode=Pin.IN)
        B13: Any  ## <class 'Pin'> = Pin(Pin.cpu.B13, mode=Pin.IN)
        B14: Any  ## <class 'Pin'> = Pin(Pin.cpu.B14, mode=Pin.IN)
        B15: Any  ## <class 'Pin'> = Pin(Pin.cpu.B15, mode=Pin.IN)
        B2: Any  ## <class 'Pin'> = Pin(Pin.cpu.B2, mode=Pin.IN)
        B3: Any  ## <class 'Pin'> = Pin(Pin.cpu.B3, mode=Pin.IN, pull=Pin.PULL_UP)
        B4: Any  ## <class 'Pin'> = Pin(Pin.cpu.B4, mode=Pin.OUT)
        B5: Any  ## <class 'Pin'> = Pin(Pin.cpu.B5, mode=Pin.OUT)
        B6: Any  ## <class 'Pin'> = Pin(Pin.cpu.B6, mode=Pin.IN)
        B7: Any  ## <class 'Pin'> = Pin(Pin.cpu.B7, mode=Pin.IN)
        B8: Any  ## <class 'Pin'> = Pin(Pin.cpu.B8, mode=Pin.IN)
        B9: Any  ## <class 'Pin'> = Pin(Pin.cpu.B9, mode=Pin.IN)
        C0: Any  ## <class 'Pin'> = Pin(Pin.cpu.C0, mode=Pin.IN)
        C1: Any  ## <class 'Pin'> = Pin(Pin.cpu.C1, mode=Pin.IN)
        C10: Any  ## <class 'Pin'> = Pin(Pin.cpu.C10, mode=Pin.ALT, pull=Pin.PULL_UP, af=12)
        C11: Any  ## <class 'Pin'> = Pin(Pin.cpu.C11, mode=Pin.ALT, pull=Pin.PULL_UP, af=12)
        C12: Any  ## <class 'Pin'> = Pin(Pin.cpu.C12, mode=Pin.ALT, pull=Pin.PULL_UP, af=12)
        C13: Any  ## <class 'Pin'> = Pin(Pin.cpu.C13, mode=Pin.IN)
        C2: Any  ## <class 'Pin'> = Pin(Pin.cpu.C2, mode=Pin.IN)
        C3: Any  ## <class 'Pin'> = Pin(Pin.cpu.C3, mode=Pin.IN)
        C4: Any  ## <class 'Pin'> = Pin(Pin.cpu.C4, mode=Pin.IN)
        C5: Any  ## <class 'Pin'> = Pin(Pin.cpu.C5, mode=Pin.IN)
        C6: Any  ## <class 'Pin'> = Pin(Pin.cpu.C6, mode=Pin.IN)
        C7: Any  ## <class 'Pin'> = Pin(Pin.cpu.C7, mode=Pin.IN)
        C8: Any  ## <class 'Pin'> = Pin(Pin.cpu.C8, mode=Pin.ALT, pull=Pin.PULL_UP, af=12)
        C9: Any  ## <class 'Pin'> = Pin(Pin.cpu.C9, mode=Pin.ALT, pull=Pin.PULL_UP, af=12)
        D2: Any  ## <class 'Pin'> = Pin(Pin.cpu.D2, mode=Pin.ALT, pull=Pin.PULL_UP, af=12)

    @classmethod
    def debug(cls, *args) -> Any:
        ...

    def gpio(self, *args) -> Any:
        ...

    def high(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def irq(self, *args) -> Any:
        ...

    def low(self, *args) -> Any:
        ...

    @classmethod
    def mapper(cls, *args) -> Any:
        ...

    def mode(self, *args) -> Any:
        ...

    def name(self, *args) -> Any:
        ...

    def names(self, *args) -> Any:
        ...

    def off(self, *args) -> Any:
        ...

    def on(self, *args) -> Any:
        ...

    def pin(self, *args) -> Any:
        ...

    def port(self, *args) -> Any:
        ...

    def pull(self, *args) -> Any:
        ...


class SDCard:
    """"""

    def read(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    def info(self, *args) -> Any:
        ...

    def ioctl(self, *args) -> Any:
        ...

    def power(self, *args) -> Any:
        ...

    def present(self, *args) -> Any:
        ...

    def readblocks(self, *args) -> Any:
        ...

    def writeblocks(self, *args) -> Any:
        ...


class SPI:
    """"""

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def send(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    CONTROLLER = 260  # type: int
    LSB = 128  # type: int
    MASTER = 260  # type: int
    MSB = 0  # type: int
    PERIPHERAL = 0  # type: int
    SLAVE = 0  # type: int

    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def recv(self, *args) -> Any:
        ...

    def send_recv(self, *args) -> Any:
        ...

    def write_readinto(self, *args) -> Any:
        ...


class Servo:
    """"""

    def angle(self, *args) -> Any:
        ...

    def calibration(self, *args) -> Any:
        ...

    def pulse_width(self, *args) -> Any:
        ...

    def speed(self, *args) -> Any:
        ...


class Switch:
    """"""

    def value(self, *args) -> Any:
        ...

    def callback(self, *args) -> Any:
        ...


class Timer:
    """"""

    BOTH = 10  # type: int
    BRK_HIGH = 2  # type: int
    BRK_LOW = 1  # type: int
    BRK_OFF = 0  # type: int
    CENTER = 32  # type: int
    DOWN = 16  # type: int
    ENC_A = 9  # type: int
    ENC_AB = 11  # type: int
    ENC_B = 10  # type: int
    FALLING = 2  # type: int
    HIGH = 0  # type: int
    IC = 8  # type: int
    LOW = 2  # type: int
    OC_ACTIVE = 3  # type: int
    OC_FORCED_ACTIVE = 6  # type: int
    OC_FORCED_INACTIVE = 7  # type: int
    OC_INACTIVE = 4  # type: int
    OC_TIMING = 2  # type: int
    OC_TOGGLE = 5  # type: int
    PWM = 0  # type: int
    PWM_INVERTED = 1  # type: int
    RISING = 0  # type: int
    UP = 0  # type: int

    def callback(self, *args) -> Any:
        ...

    def channel(self, *args) -> Any:
        ...

    def counter(self, *args) -> Any:
        ...

    def deinit(self, *args) -> Any:
        ...

    def freq(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def period(self, *args) -> Any:
        ...

    def prescaler(self, *args) -> Any:
        ...

    def source_freq(self, *args) -> Any:
        ...


class UART:
    """"""

    def any(self, *args) -> Any:
        ...

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def readline(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    CTS = 512  # type: int
    IRQ_RXIDLE = 16  # type: int
    RTS = 256  # type: int

    def deinit(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def irq(self, *args) -> Any:
        ...

    def readchar(self, *args) -> Any:
        ...

    def sendbreak(self, *args) -> Any:
        ...

    def writechar(self, *args) -> Any:
        ...


class USB_HID:
    """"""

    def send(self, *args) -> Any:
        ...

    def recv(self, *args) -> Any:
        ...


class USB_VCP:
    """"""

    def any(self, *args) -> Any:
        ...

    def close(self, *args) -> Any:
        ...

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def readline(self, *args) -> Any:
        ...

    def send(self, *args) -> Any:
        ...

    def write(self, *args) -> Any:
        ...

    CTS = 2  # type: int
    IRQ_RX = 1  # type: int
    RTS = 1  # type: int

    def init(self, *args) -> Any:
        ...

    def irq(self, *args) -> Any:
        ...

    def isconnected(self, *args) -> Any:
        ...

    def readlines(self, *args) -> Any:
        ...

    def recv(self, *args) -> Any:
        ...

    def setinterrupt(self, *args) -> Any:
        ...


def bootloader(*args) -> Any:
    ...


def country(*args) -> Any:
    ...


def delay(*args) -> Any:
    ...


def dht_readinto(*args) -> Any:
    ...


def disable_irq(*args) -> Any:
    ...


def elapsed_micros(*args) -> Any:
    ...


def elapsed_millis(*args) -> Any:
    ...


def enable_irq(*args) -> Any:
    ...


def fault_debug(*args) -> Any:
    ...


def freq(*args) -> Any:
    ...


def hard_reset(*args) -> Any:
    ...


def have_cdc(*args) -> Any:
    ...


def hid(*args) -> Any:
    ...


hid_keyboard = ()  # type: tuple
hid_mouse = ()  # type: tuple


def info(*args) -> Any:
    ...


def micros(*args) -> Any:
    ...


def millis(*args) -> Any:
    ...


def mount(*args) -> Any:
    ...


def pwm(*args) -> Any:
    ...


def repl_info(*args) -> Any:
    ...


def repl_uart(*args) -> Any:
    ...


def rng(*args) -> Any:
    ...


def servo(*args) -> Any:
    ...


def standby(*args) -> Any:
    ...


def sync(*args) -> Any:
    ...


def udelay(*args) -> Any:
    ...


def unique_id(*args) -> Any:
    ...


def usb_mode(*args) -> Any:
    ...


def wfi(*args) -> Any:
    ...
