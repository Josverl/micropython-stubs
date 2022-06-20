"""
Module: 'pyb' on micropython-v1.19.1-stm32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'stm32', 'port': 'stm32', 'machine': 'PYBv1.1 with STM32F405RG', 'release': '1.19.1', 'nodename': 'pyboard', 'name': 'micropython', 'family': 'micropython', 'sysname': 'pyboard', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Any


def main(*args, **kwargs) -> Any:
    ...


def stop(*args, **kwargs) -> Any:
    ...


SD: Any  ## <class 'SDCard'> = <SDCard>


class DAC:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    CIRCULAR = 256  # type: int
    NORMAL = 0  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def noise(self, *args, **kwargs) -> Any:
        ...

    def triangle(self, *args, **kwargs) -> Any:
        ...

    def write_timed(self, *args, **kwargs) -> Any:
        ...


class RTC:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def calibration(self, *args, **kwargs) -> Any:
        ...

    def datetime(self, *args, **kwargs) -> Any:
        ...

    def info(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def wakeup(self, *args, **kwargs) -> Any:
        ...


class ADC:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def read_timed(self, *args, **kwargs) -> Any:
        ...

    def read_timed_multi(self, *args, **kwargs) -> Any:
        ...


class ADCAll:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def read_channel(self, *args, **kwargs) -> Any:
        ...

    def read_core_temp(self, *args, **kwargs) -> Any:
        ...

    def read_core_vbat(self, *args, **kwargs) -> Any:
        ...

    def read_core_vref(self, *args, **kwargs) -> Any:
        ...

    def read_vref(self, *args, **kwargs) -> Any:
        ...


class Accel:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def filtered_xyz(self, *args, **kwargs) -> Any:
        ...

    def tilt(self, *args, **kwargs) -> Any:
        ...

    def x(self, *args, **kwargs) -> Any:
        ...

    def y(self, *args, **kwargs) -> Any:
        ...

    def z(self, *args, **kwargs) -> Any:
        ...


class CAN:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def any(self, *args, **kwargs) -> Any:
        ...

    def send(self, *args, **kwargs) -> Any:
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

    def clearfilter(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def info(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def recv(self, *args, **kwargs) -> Any:
        ...

    def restart(self, *args, **kwargs) -> Any:
        ...

    def rxcallback(self, *args, **kwargs) -> Any:
        ...

    def setfilter(self, *args, **kwargs) -> Any:
        ...

    def state(self, *args, **kwargs) -> Any:
        ...


class ExtInt:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    EVT_FALLING = 270663680  # type: int
    EVT_RISING = 269615104  # type: int
    EVT_RISING_FALLING = 271712256  # type: int
    IRQ_FALLING = 270598144  # type: int
    IRQ_RISING = 269549568  # type: int
    IRQ_RISING_FALLING = 271646720  # type: int

    def disable(self, *args, **kwargs) -> Any:
        ...

    def enable(self, *args, **kwargs) -> Any:
        ...

    def line(self, *args, **kwargs) -> Any:
        ...

    def regs(self, *args, **kwargs) -> Any:
        ...

    def swint(self, *args, **kwargs) -> Any:
        ...


class Flash:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def readblocks(self, *args, **kwargs) -> Any:
        ...

    def writeblocks(self, *args, **kwargs) -> Any:
        ...


class I2C:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def send(self, *args, **kwargs) -> Any:
        ...

    CONTROLLER = 0  # type: int
    MASTER = 0  # type: int
    PERIPHERAL = 1  # type: int
    SLAVE = 1  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def is_ready(self, *args, **kwargs) -> Any:
        ...

    def mem_read(self, *args, **kwargs) -> Any:
        ...

    def mem_write(self, *args, **kwargs) -> Any:
        ...

    def recv(self, *args, **kwargs) -> Any:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...


class LCD:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def get(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def command(self, *args, **kwargs) -> Any:
        ...

    def contrast(self, *args, **kwargs) -> Any:
        ...

    def fill(self, *args, **kwargs) -> Any:
        ...

    def light(self, *args, **kwargs) -> Any:
        ...

    def pixel(self, *args, **kwargs) -> Any:
        ...

    def show(self, *args, **kwargs) -> Any:
        ...

    def text(self, *args, **kwargs) -> Any:
        ...


class LED:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def intensity(self, *args, **kwargs) -> Any:
        ...

    def off(self, *args, **kwargs) -> Any:
        ...

    def on(self, *args, **kwargs) -> Any:
        ...

    def toggle(self, *args, **kwargs) -> Any:
        ...


class Pin:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    @classmethod
    def dict(cls, *args, **kwargs) -> Any:
        ...

    def value(self, *args, **kwargs) -> Any:
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

    def af(self, *args, **kwargs) -> Any:
        ...

    def af_list(self, *args, **kwargs) -> Any:
        ...

    class board:
        """"""

        def __init__(self, *argv, **kwargs) -> None:
            """"""
            ...

        LED_BLUE: Any  ## <class 'Pin'> = Pin(Pin.cpu.B4, mode=Pin.OUT)
        LED_GREEN: Any  ## <class 'Pin'> = Pin(Pin.cpu.A14, mode=Pin.OUT)
        LED_RED: Any  ## <class 'Pin'> = Pin(Pin.cpu.A13, mode=Pin.OUT)
        LED_YELLOW: Any  ## <class 'Pin'> = Pin(Pin.cpu.A15, mode=Pin.OUT)
        MMA_AVDD: Any  ## <class 'Pin'> = Pin(Pin.cpu.B5, mode=Pin.OUT)
        MMA_INT: Any  ## <class 'Pin'> = Pin(Pin.cpu.B2, mode=Pin.IN)
        SD: Any  ## <class 'Pin'> = Pin(Pin.cpu.A8, mode=Pin.IN, pull=Pin.PULL_UP)
        SD_CK: Any  ## <class 'Pin'> = Pin(Pin.cpu.C12, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        SD_CMD: Any  ## <class 'Pin'> = Pin(Pin.cpu.D2, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        SD_D0: Any  ## <class 'Pin'> = Pin(Pin.cpu.C8, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        SD_D1: Any  ## <class 'Pin'> = Pin(Pin.cpu.C9, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        SD_D2: Any  ## <class 'Pin'> = Pin(Pin.cpu.C10, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        SD_D3: Any  ## <class 'Pin'> = Pin(Pin.cpu.C11, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        SD_SW: Any  ## <class 'Pin'> = Pin(Pin.cpu.A8, mode=Pin.IN, pull=Pin.PULL_UP)
        SW: Any  ## <class 'Pin'> = Pin(Pin.cpu.B3, mode=Pin.IN, pull=Pin.PULL_UP)
        USB_DM: Any  ## <class 'Pin'> = Pin(Pin.cpu.A11, mode=Pin.ALT, alt=10)
        USB_DP: Any  ## <class 'Pin'> = Pin(Pin.cpu.A12, mode=Pin.ALT, alt=10)
        USB_ID: Any  ## <class 'Pin'> = Pin(Pin.cpu.A10, mode=Pin.ALT_OPEN_DRAIN, pull=Pin.PULL_UP, alt=10)
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

        def __init__(self, *argv, **kwargs) -> None:
            """"""
            ...

        A0: Any  ## <class 'Pin'> = Pin(Pin.cpu.A0, mode=Pin.IN)
        A1: Any  ## <class 'Pin'> = Pin(Pin.cpu.A1, mode=Pin.IN)
        A10: Any  ## <class 'Pin'> = Pin(Pin.cpu.A10, mode=Pin.ALT_OPEN_DRAIN, pull=Pin.PULL_UP, alt=10)
        A11: Any  ## <class 'Pin'> = Pin(Pin.cpu.A11, mode=Pin.ALT, alt=10)
        A12: Any  ## <class 'Pin'> = Pin(Pin.cpu.A12, mode=Pin.ALT, alt=10)
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
        C10: Any  ## <class 'Pin'> = Pin(Pin.cpu.C10, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C11: Any  ## <class 'Pin'> = Pin(Pin.cpu.C11, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C12: Any  ## <class 'Pin'> = Pin(Pin.cpu.C12, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C13: Any  ## <class 'Pin'> = Pin(Pin.cpu.C13, mode=Pin.IN)
        C2: Any  ## <class 'Pin'> = Pin(Pin.cpu.C2, mode=Pin.IN)
        C3: Any  ## <class 'Pin'> = Pin(Pin.cpu.C3, mode=Pin.IN)
        C4: Any  ## <class 'Pin'> = Pin(Pin.cpu.C4, mode=Pin.IN)
        C5: Any  ## <class 'Pin'> = Pin(Pin.cpu.C5, mode=Pin.IN)
        C6: Any  ## <class 'Pin'> = Pin(Pin.cpu.C6, mode=Pin.IN)
        C7: Any  ## <class 'Pin'> = Pin(Pin.cpu.C7, mode=Pin.IN)
        C8: Any  ## <class 'Pin'> = Pin(Pin.cpu.C8, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C9: Any  ## <class 'Pin'> = Pin(Pin.cpu.C9, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        D2: Any  ## <class 'Pin'> = Pin(Pin.cpu.D2, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)

    @classmethod
    def debug(cls, *args, **kwargs) -> Any:
        ...

    def gpio(self, *args, **kwargs) -> Any:
        ...

    def high(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def low(self, *args, **kwargs) -> Any:
        ...

    @classmethod
    def mapper(cls, *args, **kwargs) -> Any:
        ...

    def mode(self, *args, **kwargs) -> Any:
        ...

    def name(self, *args, **kwargs) -> Any:
        ...

    def names(self, *args, **kwargs) -> Any:
        ...

    def off(self, *args, **kwargs) -> Any:
        ...

    def on(self, *args, **kwargs) -> Any:
        ...

    def pin(self, *args, **kwargs) -> Any:
        ...

    def port(self, *args, **kwargs) -> Any:
        ...

    def pull(self, *args, **kwargs) -> Any:
        ...


class SDCard:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def info(self, *args, **kwargs) -> Any:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def power(self, *args, **kwargs) -> Any:
        ...

    def present(self, *args, **kwargs) -> Any:
        ...

    def readblocks(self, *args, **kwargs) -> Any:
        ...

    def writeblocks(self, *args, **kwargs) -> Any:
        ...


class SPI:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def send(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    CONTROLLER = 260  # type: int
    LSB = 128  # type: int
    MASTER = 260  # type: int
    MSB = 0  # type: int
    PERIPHERAL = 0  # type: int
    SLAVE = 0  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def recv(self, *args, **kwargs) -> Any:
        ...

    def send_recv(self, *args, **kwargs) -> Any:
        ...

    def write_readinto(self, *args, **kwargs) -> Any:
        ...


class Servo:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def angle(self, *args, **kwargs) -> Any:
        ...

    def calibration(self, *args, **kwargs) -> Any:
        ...

    def pulse_width(self, *args, **kwargs) -> Any:
        ...

    def speed(self, *args, **kwargs) -> Any:
        ...


class Switch:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def value(self, *args, **kwargs) -> Any:
        ...

    def callback(self, *args, **kwargs) -> Any:
        ...


class Timer:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

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

    def callback(self, *args, **kwargs) -> Any:
        ...

    def channel(self, *args, **kwargs) -> Any:
        ...

    def counter(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def freq(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def period(self, *args, **kwargs) -> Any:
        ...

    def prescaler(self, *args, **kwargs) -> Any:
        ...

    def source_freq(self, *args, **kwargs) -> Any:
        ...


class UART:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def any(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    CTS = 512  # type: int
    IRQ_RXIDLE = 16  # type: int
    RTS = 256  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def readchar(self, *args, **kwargs) -> Any:
        ...

    def sendbreak(self, *args, **kwargs) -> Any:
        ...

    def writechar(self, *args, **kwargs) -> Any:
        ...


class USB_HID:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def send(self, *args, **kwargs) -> Any:
        ...

    def recv(self, *args, **kwargs) -> Any:
        ...


class USB_VCP:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def any(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def send(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    CTS = 2  # type: int
    IRQ_RX = 1  # type: int
    RTS = 1  # type: int

    def init(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def isconnected(self, *args, **kwargs) -> Any:
        ...

    def readlines(self, *args, **kwargs) -> Any:
        ...

    def recv(self, *args, **kwargs) -> Any:
        ...

    def setinterrupt(self, *args, **kwargs) -> Any:
        ...


def bootloader(*args, **kwargs) -> Any:
    ...


def country(*args, **kwargs) -> Any:
    ...


def delay(*args, **kwargs) -> Any:
    ...


def dht_readinto(*args, **kwargs) -> Any:
    ...


def disable_irq(*args, **kwargs) -> Any:
    ...


def elapsed_micros(*args, **kwargs) -> Any:
    ...


def elapsed_millis(*args, **kwargs) -> Any:
    ...


def enable_irq(*args, **kwargs) -> Any:
    ...


def fault_debug(*args, **kwargs) -> Any:
    ...


def freq(*args, **kwargs) -> Any:
    ...


def hard_reset(*args, **kwargs) -> Any:
    ...


def have_cdc(*args, **kwargs) -> Any:
    ...


def hid(*args, **kwargs) -> Any:
    ...


hid_keyboard = ()  # type: tuple
hid_mouse = ()  # type: tuple


def info(*args, **kwargs) -> Any:
    ...


def micros(*args, **kwargs) -> Any:
    ...


def millis(*args, **kwargs) -> Any:
    ...


def mount(*args, **kwargs) -> Any:
    ...


def pwm(*args, **kwargs) -> Any:
    ...


def repl_info(*args, **kwargs) -> Any:
    ...


def repl_uart(*args, **kwargs) -> Any:
    ...


def rng(*args, **kwargs) -> Any:
    ...


def servo(*args, **kwargs) -> Any:
    ...


def standby(*args, **kwargs) -> Any:
    ...


def sync(*args, **kwargs) -> Any:
    ...


def udelay(*args, **kwargs) -> Any:
    ...


def unique_id(*args, **kwargs) -> Any:
    ...


def usb_mode(*args, **kwargs) -> Any:
    ...


def wfi(*args, **kwargs) -> Any:
    ...
