"""
Module: 'pyb' on micropython-v1.23.0-preview-stm32-PYBV11
"""
# MCU: {'version': '1.23.0-preview', 'mpy': 'v6.2', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': 'preview.203.gd712feb68', 'arch': 'armv7emsp', 'ver': '1.23.0-preview-preview.203.gd712feb68', 'cpu': 'STM32F405RG'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete

hid_mouse: tuple = ()
hid_keyboard: tuple = ()

def hard_reset(*args, **kwargs) -> Incomplete: ...
def have_cdc(*args, **kwargs) -> Incomplete: ...
def hid(*args, **kwargs) -> Incomplete: ...
def info(*args, **kwargs) -> Incomplete: ...
def wfi(*args, **kwargs) -> Incomplete: ...
def elapsed_micros(*args, **kwargs) -> Incomplete: ...
def freq(*args, **kwargs) -> Incomplete: ...
def disable_irq(*args, **kwargs) -> Incomplete: ...
def fault_debug(*args, **kwargs) -> Incomplete: ...
def elapsed_millis(*args, **kwargs) -> Incomplete: ...
def enable_irq(*args, **kwargs) -> Incomplete: ...
def sync(*args, **kwargs) -> Incomplete: ...
def servo(*args, **kwargs) -> Incomplete: ...
def standby(*args, **kwargs) -> Incomplete: ...
def usb_mode(*args, **kwargs) -> Incomplete: ...
def udelay(*args, **kwargs) -> Incomplete: ...
def unique_id(*args, **kwargs) -> Incomplete: ...
def micros(*args, **kwargs) -> Incomplete: ...
def mount(*args, **kwargs) -> Incomplete: ...
def rng(*args, **kwargs) -> Incomplete: ...
def millis(*args, **kwargs) -> Incomplete: ...
def repl_uart(*args, **kwargs) -> Incomplete: ...
def pwm(*args, **kwargs) -> Incomplete: ...
def repl_info(*args, **kwargs) -> Incomplete: ...
def stop(*args, **kwargs) -> Incomplete: ...
def delay(*args, **kwargs) -> Incomplete: ...
def main(*args, **kwargs) -> Incomplete: ...
def bootloader(*args, **kwargs) -> Incomplete: ...
def country(*args, **kwargs) -> Incomplete: ...

class DAC:
    CIRCULAR: int = 256
    NORMAL: int = 0
    def noise(self, *args, **kwargs) -> Incomplete: ...
    def write_timed(self, *args, **kwargs) -> Incomplete: ...
    def triangle(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class ExtInt:
    IRQ_FALLING: int = 270598144
    IRQ_RISING_FALLING: int = 271646720
    IRQ_RISING: int = 269549568
    EVT_FALLING: int = 270663680
    EVT_RISING_FALLING: int = 271712256
    EVT_RISING: int = 269615104
    def line(self, *args, **kwargs) -> Incomplete: ...
    def regs(self, *args, **kwargs) -> Incomplete: ...
    def swint(self, *args, **kwargs) -> Incomplete: ...
    def enable(self, *args, **kwargs) -> Incomplete: ...
    def disable(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Flash:
    def readblocks(self, *args, **kwargs) -> Incomplete: ...
    def writeblocks(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class I2C:
    PERIPHERAL: int = 1
    MASTER: int = 0
    CONTROLLER: int = 0
    SLAVE: int = 1
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def mem_read(self, *args, **kwargs) -> Incomplete: ...
    def mem_write(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def is_ready(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class LCD:
    def fill(self, *args, **kwargs) -> Incomplete: ...
    def light(self, *args, **kwargs) -> Incomplete: ...
    def pixel(self, *args, **kwargs) -> Incomplete: ...
    def show(self, *args, **kwargs) -> Incomplete: ...
    def text(self, *args, **kwargs) -> Incomplete: ...
    def contrast(self, *args, **kwargs) -> Incomplete: ...
    def get(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def command(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class CAN:
    MASK16: int = 0
    MASK32: int = 2
    LOOPBACK: int = 67108864
    LIST32: int = 3
    SILENT_LOOPBACK: int = 201326592
    NORMAL: int = 0
    SILENT: int = 134217728
    STOPPED: int = 0
    ERROR_ACTIVE: int = 1
    BUS_OFF: int = 4
    LIST16: int = 1
    ERROR_PASSIVE: int = 3
    ERROR_WARNING: int = 2
    def restart(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def rxcallback(self, *args, **kwargs) -> Incomplete: ...
    def setfilter(self, *args, **kwargs) -> Incomplete: ...
    def state(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def any(self, *args, **kwargs) -> Incomplete: ...
    def info(self, *args, **kwargs) -> Incomplete: ...
    def clearfilter(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class ADC:
    def read_timed(self, *args, **kwargs) -> Incomplete: ...
    def read_timed_multi(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class ADCAll:
    def read_core_vbat(self, *args, **kwargs) -> Incomplete: ...
    def read_core_vref(self, *args, **kwargs) -> Incomplete: ...
    def read_vref(self, *args, **kwargs) -> Incomplete: ...
    def read_core_temp(self, *args, **kwargs) -> Incomplete: ...
    def read_channel(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Accel:
    def x(self, *args, **kwargs) -> Incomplete: ...
    def tilt(self, *args, **kwargs) -> Incomplete: ...
    def y(self, *args, **kwargs) -> Incomplete: ...
    def z(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def filtered_xyz(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class USB_VCP:
    RTS: int = 1
    CTS: int = 2
    IRQ_RX: int = 1
    def readlines(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def isconnected(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def setinterrupt(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def any(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Timer:
    OC_FORCED_ACTIVE: int = 6
    OC_FORCED_INACTIVE: int = 7
    OC_INACTIVE: int = 4
    OC_ACTIVE: int = 3
    LOW: int = 2
    IC: int = 8
    PWM_INVERTED: int = 1
    RISING: int = 0
    OC_TIMING: int = 2
    PWM: int = 0
    OC_TOGGLE: int = 5
    UP: int = 0
    BRK_LOW: int = 1
    BRK_OFF: int = 0
    CENTER: int = 32
    BRK_HIGH: int = 2
    BOTH: int = 10
    HIGH: int = 0
    ENC_B: int = 10
    FALLING: int = 2
    DOWN: int = 16
    ENC_AB: int = 11
    ENC_A: int = 9
    def freq(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def period(self, *args, **kwargs) -> Incomplete: ...
    def prescaler(self, *args, **kwargs) -> Incomplete: ...
    def source_freq(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def callback(self, *args, **kwargs) -> Incomplete: ...
    def channel(self, *args, **kwargs) -> Incomplete: ...
    def counter(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Switch:
    def callback(self, *args, **kwargs) -> Incomplete: ...
    def value(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Servo:
    def speed(self, *args, **kwargs) -> Incomplete: ...
    def pulse_width(self, *args, **kwargs) -> Incomplete: ...
    def calibration(self, *args, **kwargs) -> Incomplete: ...
    def angle(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class UART:
    IRQ_RXIDLE: int = 16
    CTS: int = 512
    RTS: int = 256
    def init(self, *args, **kwargs) -> Incomplete: ...
    def flush(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def txdone(self, *args, **kwargs) -> Incomplete: ...
    def sendbreak(self, *args, **kwargs) -> Incomplete: ...
    def readchar(self, *args, **kwargs) -> Incomplete: ...
    def writechar(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def any(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class USB_HID:
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class LED:
    def toggle(self, *args, **kwargs) -> Incomplete: ...
    def on(self, *args, **kwargs) -> Incomplete: ...
    def off(self, *args, **kwargs) -> Incomplete: ...
    def intensity(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class RTC:
    def info(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def wakeup(self, *args, **kwargs) -> Incomplete: ...
    def datetime(self, *args, **kwargs) -> Incomplete: ...
    def calibration(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Pin:
    AF_OD: int = 18
    AF9_TIM14: int = 9
    ALT_OPEN_DRAIN: int = 18
    AF_PP: int = 2
    ALT: int = 2
    AF9_CAN1: int = 9
    AF8_USART6: int = 8
    AF9_TIM13: int = 9
    AF9_CAN2: int = 9
    AF9_TIM12: int = 9
    PULL_UP: int = 1
    OUT_PP: int = 1
    OUT_OD: int = 17
    ANALOG: int = 3
    PULL_DOWN: int = 2
    PULL_NONE: int = 0
    IRQ_FALLING: int = 270598144
    IN: int = 0
    OUT: int = 1
    IRQ_RISING: int = 269549568
    OPEN_DRAIN: int = 17
    AF2_TIM5: int = 2
    AF3_TIM10: int = 3
    AF3_TIM11: int = 3
    AF3_TIM8: int = 3
    AF3_TIM9: int = 3
    AF2_TIM4: int = 2
    AF1_TIM1: int = 1
    AF1_TIM2: int = 1
    AF2_TIM3: int = 2
    AF8_UART4: int = 8
    AF6_I2S2: int = 6
    AF7_USART1: int = 7
    AF7_USART2: int = 7
    AF7_USART3: int = 7
    AF4_I2C1: int = 4
    AF5_SPI2: int = 5
    AF4_I2C2: int = 4
    AF5_I2S2: int = 5
    AF5_SPI1: int = 5
    def mode(self, *args, **kwargs) -> Incomplete: ...
    def name(self, *args, **kwargs) -> Incomplete: ...
    def pull(self, *args, **kwargs) -> Incomplete: ...
    def low(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def pin(self, *args, **kwargs) -> Incomplete: ...
    def port(self, *args, **kwargs) -> Incomplete: ...
    def names(self, *args, **kwargs) -> Incomplete: ...
    def on(self, *args, **kwargs) -> Incomplete: ...
    def off(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def af_list(self, *args, **kwargs) -> Incomplete: ...
    def af(self, *args, **kwargs) -> Incomplete: ...
    def value(self, *args, **kwargs) -> Incomplete: ...
    def high(self, *args, **kwargs) -> Incomplete: ...
    def gpio(self, *args, **kwargs) -> Incomplete: ...
    @classmethod
    def dict(cls, *args, **kwargs) -> Incomplete: ...
    @classmethod
    def debug(cls, *args, **kwargs) -> Incomplete: ...

    class cpu:
        B9: Pin  ## = Pin(Pin.cpu.B9, mode=Pin.IN)
        B8: Pin  ## = Pin(Pin.cpu.B8, mode=Pin.IN)
        B7: Pin  ## = Pin(Pin.cpu.B7, mode=Pin.IN)
        C0: Pin  ## = Pin(Pin.cpu.C0, mode=Pin.IN)
        C1: Pin  ## = Pin(Pin.cpu.C1, mode=Pin.IN)
        C10: Pin  ## = Pin(Pin.cpu.C10, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        B3: Pin  ## = Pin(Pin.cpu.B3, mode=Pin.IN, pull=Pin.PULL_UP)
        B2: Pin  ## = Pin(Pin.cpu.B2, mode=Pin.IN)
        B6: Pin  ## = Pin(Pin.cpu.B6, mode=Pin.IN)
        B4: Pin  ## = Pin(Pin.cpu.B4, mode=Pin.OUT)
        B5: Pin  ## = Pin(Pin.cpu.B5, mode=Pin.OUT)
        B15: Pin  ## = Pin(Pin.cpu.B15, mode=Pin.IN)
        C7: Pin  ## = Pin(Pin.cpu.C7, mode=Pin.IN)
        C6: Pin  ## = Pin(Pin.cpu.C6, mode=Pin.IN)
        C5: Pin  ## = Pin(Pin.cpu.C5, mode=Pin.IN)
        C8: Pin  ## = Pin(Pin.cpu.C8, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C9: Pin  ## = Pin(Pin.cpu.C9, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C11: Pin  ## = Pin(Pin.cpu.C11, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C13: Pin  ## = Pin(Pin.cpu.C13, mode=Pin.IN)
        C12: Pin  ## = Pin(Pin.cpu.C12, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C4: Pin  ## = Pin(Pin.cpu.C4, mode=Pin.IN)
        C2: Pin  ## = Pin(Pin.cpu.C2, mode=Pin.IN)
        C3: Pin  ## = Pin(Pin.cpu.C3, mode=Pin.IN)
        D2: Pin  ## = Pin(Pin.cpu.D2, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        A15: Pin  ## = Pin(Pin.cpu.A15, mode=Pin.OUT)
        A14: Pin  ## = Pin(Pin.cpu.A14, mode=Pin.OUT)
        A13: Pin  ## = Pin(Pin.cpu.A13, mode=Pin.OUT)
        A2: Pin  ## = Pin(Pin.cpu.A2, mode=Pin.IN)
        A3: Pin  ## = Pin(Pin.cpu.A3, mode=Pin.IN)
        A4: Pin  ## = Pin(Pin.cpu.A4, mode=Pin.IN)
        A1: Pin  ## = Pin(Pin.cpu.A1, mode=Pin.IN)
        A0: Pin  ## = Pin(Pin.cpu.A0, mode=Pin.IN)
        A12: Pin  ## = Pin(Pin.cpu.A12, mode=Pin.ALT, alt=10)
        A10: Pin  ## = Pin(Pin.cpu.A10, mode=Pin.ALT_OPEN_DRAIN, pull=Pin.PULL_UP, alt=10)
        A11: Pin  ## = Pin(Pin.cpu.A11, mode=Pin.ALT, alt=10)
        B14: Pin  ## = Pin(Pin.cpu.B14, mode=Pin.IN)
        B11: Pin  ## = Pin(Pin.cpu.B11, mode=Pin.IN)
        B10: Pin  ## = Pin(Pin.cpu.B10, mode=Pin.IN)
        B1: Pin  ## = Pin(Pin.cpu.B1, mode=Pin.IN)
        B12: Pin  ## = Pin(Pin.cpu.B12, mode=Pin.IN)
        B13: Pin  ## = Pin(Pin.cpu.B13, mode=Pin.IN)
        A5: Pin  ## = Pin(Pin.cpu.A5, mode=Pin.IN)
        A7: Pin  ## = Pin(Pin.cpu.A7, mode=Pin.IN)
        A6: Pin  ## = Pin(Pin.cpu.A6, mode=Pin.IN)
        B0: Pin  ## = Pin(Pin.cpu.B0, mode=Pin.IN)
        A8: Pin  ## = Pin(Pin.cpu.A8, mode=Pin.IN, pull=Pin.PULL_UP)
        A9: Pin  ## = Pin(Pin.cpu.A9, mode=Pin.IN)
        def __init__(self, *argv, **kwargs) -> None: ...

    @classmethod
    def mapper(cls, *args, **kwargs) -> Incomplete: ...

    class board:
        X5: Pin  ## = Pin(Pin.cpu.A4, mode=Pin.IN)
        X18: Pin  ## = Pin(Pin.cpu.C13, mode=Pin.IN)
        X4: Pin  ## = Pin(Pin.cpu.A3, mode=Pin.IN)
        X8: Pin  ## = Pin(Pin.cpu.A7, mode=Pin.IN)
        X6: Pin  ## = Pin(Pin.cpu.A5, mode=Pin.IN)
        X7: Pin  ## = Pin(Pin.cpu.A6, mode=Pin.IN)
        X2: Pin  ## = Pin(Pin.cpu.A1, mode=Pin.IN)
        X3: Pin  ## = Pin(Pin.cpu.A2, mode=Pin.IN)
        X19: Pin  ## = Pin(Pin.cpu.C0, mode=Pin.IN)
        X22: Pin  ## = Pin(Pin.cpu.C3, mode=Pin.IN)
        X20: Pin  ## = Pin(Pin.cpu.C1, mode=Pin.IN)
        X21: Pin  ## = Pin(Pin.cpu.C2, mode=Pin.IN)
        Y5: Pin  ## = Pin(Pin.cpu.B12, mode=Pin.IN)
        X9: Pin  ## = Pin(Pin.cpu.B6, mode=Pin.IN)
        Y4: Pin  ## = Pin(Pin.cpu.B9, mode=Pin.IN)
        Y8: Pin  ## = Pin(Pin.cpu.B15, mode=Pin.IN)
        Y6: Pin  ## = Pin(Pin.cpu.B13, mode=Pin.IN)
        Y7: Pin  ## = Pin(Pin.cpu.B14, mode=Pin.IN)
        Y10: Pin  ## = Pin(Pin.cpu.B11, mode=Pin.IN)
        Y3: Pin  ## = Pin(Pin.cpu.B8, mode=Pin.IN)
        Y1: Pin  ## = Pin(Pin.cpu.C6, mode=Pin.IN)
        Y2: Pin  ## = Pin(Pin.cpu.C7, mode=Pin.IN)
        Y11: Pin  ## = Pin(Pin.cpu.B0, mode=Pin.IN)
        Y12: Pin  ## = Pin(Pin.cpu.B1, mode=Pin.IN)
        Y9: Pin  ## = Pin(Pin.cpu.B10, mode=Pin.IN)
        SD_CK: Pin  ## = Pin(Pin.cpu.C12, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        X17: Pin  ## = Pin(Pin.cpu.B3, mode=Pin.IN, pull=Pin.PULL_UP)
        SD: Pin  ## = Pin(Pin.cpu.A8, mode=Pin.IN, pull=Pin.PULL_UP)
        SD_D1: Pin  ## = Pin(Pin.cpu.C9, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        SD_CMD: Pin  ## = Pin(Pin.cpu.D2, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        SD_D0: Pin  ## = Pin(Pin.cpu.C8, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        LED_GREEN: Pin  ## = Pin(Pin.cpu.A14, mode=Pin.OUT)
        MMA_INT: Pin  ## = Pin(Pin.cpu.B2, mode=Pin.IN)
        LED_BLUE: Pin  ## = Pin(Pin.cpu.B4, mode=Pin.OUT)
        MMA_AVDD: Pin  ## = Pin(Pin.cpu.B5, mode=Pin.OUT)
        LED_RED: Pin  ## = Pin(Pin.cpu.A13, mode=Pin.OUT)
        LED_YELLOW: Pin  ## = Pin(Pin.cpu.A15, mode=Pin.OUT)
        X1: Pin  ## = Pin(Pin.cpu.A0, mode=Pin.IN)
        SD_D2: Pin  ## = Pin(Pin.cpu.C10, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        USB_VBUS: Pin  ## = Pin(Pin.cpu.A9, mode=Pin.IN)
        X12: Pin  ## = Pin(Pin.cpu.C5, mode=Pin.IN)
        X10: Pin  ## = Pin(Pin.cpu.B7, mode=Pin.IN)
        X11: Pin  ## = Pin(Pin.cpu.C4, mode=Pin.IN)
        SD_SW: Pin  ## = Pin(Pin.cpu.A8, mode=Pin.IN, pull=Pin.PULL_UP)
        USB_ID: Pin  ## = Pin(Pin.cpu.A10, mode=Pin.ALT_OPEN_DRAIN, pull=Pin.PULL_UP, alt=10)
        SD_D3: Pin  ## = Pin(Pin.cpu.C11, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        USB_DP: Pin  ## = Pin(Pin.cpu.A12, mode=Pin.ALT, alt=10)
        SW: Pin  ## = Pin(Pin.cpu.B3, mode=Pin.IN, pull=Pin.PULL_UP)
        USB_DM: Pin  ## = Pin(Pin.cpu.A11, mode=Pin.ALT, alt=10)
        def __init__(self, *argv, **kwargs) -> None: ...

    def __init__(self, *argv, **kwargs) -> None: ...

class SPI:
    MASTER: int = 260
    LSB: int = 128
    SLAVE: int = 0
    MSB: int = 0
    PERIPHERAL: int = 0
    CONTROLLER: int = 260
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def send_recv(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def write_readinto(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

SD: Incomplete  ## <class 'SDCard'> = <SDCard>

class SDCard:
    def writeblocks(self, *args, **kwargs) -> Incomplete: ...
    def power(self, *args, **kwargs) -> Incomplete: ...
    def present(self, *args, **kwargs) -> Incomplete: ...
    def readblocks(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def info(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
