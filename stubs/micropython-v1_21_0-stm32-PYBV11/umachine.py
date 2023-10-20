"""
Module: 'umachine' on micropython-v1.21.0-stm32-PYBV11
"""
# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': 'v1.21.0', 'cpu': 'STM32F405RG'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

HARD_RESET = 2  # type: int
PWRON_RESET = 1  # type: int
SOFT_RESET = 0  # type: int
DEEPSLEEP_RESET = 4  # type: int
WDT_RESET = 3  # type: int


def idle(*args, **kwargs) -> Incomplete:
    ...


def freq(*args, **kwargs) -> Incomplete:
    ...


def info(*args, **kwargs) -> Incomplete:
    ...


def dht_readinto(*args, **kwargs) -> Incomplete:
    ...


def enable_irq(*args, **kwargs) -> Incomplete:
    ...


def disable_irq(*args, **kwargs) -> Incomplete:
    ...


def deepsleep(*args, **kwargs) -> Incomplete:
    ...


def soft_reset(*args, **kwargs) -> Incomplete:
    ...


def sleep(*args, **kwargs) -> Incomplete:
    ...


def time_pulse_us(*args, **kwargs) -> Incomplete:
    ...


def lightsleep(*args, **kwargs) -> Incomplete:
    ...


def reset(*args, **kwargs) -> Incomplete:
    ...


def rng(*args, **kwargs) -> Incomplete:
    ...


def reset_cause(*args, **kwargs) -> Incomplete:
    ...


def unique_id(*args, **kwargs) -> Incomplete:
    ...


def bootloader(*args, **kwargs) -> Incomplete:
    ...


def bitstream(*args, **kwargs) -> Incomplete:
    ...


class Pin:
    AF_OD = 18  # type: int
    AF9_TIM14 = 9  # type: int
    ALT_OPEN_DRAIN = 18  # type: int
    AF_PP = 2  # type: int
    ALT = 2  # type: int
    AF9_CAN1 = 9  # type: int
    AF8_USART6 = 8  # type: int
    AF9_TIM13 = 9  # type: int
    AF9_CAN2 = 9  # type: int
    AF9_TIM12 = 9  # type: int
    PULL_UP = 1  # type: int
    OUT_PP = 1  # type: int
    OUT_OD = 17  # type: int
    ANALOG = 3  # type: int
    PULL_DOWN = 2  # type: int
    PULL_NONE = 0  # type: int
    IRQ_FALLING = 270598144  # type: int
    IN = 0  # type: int
    OUT = 1  # type: int
    IRQ_RISING = 269549568  # type: int
    OPEN_DRAIN = 17  # type: int
    AF2_TIM5 = 2  # type: int
    AF3_TIM10 = 3  # type: int
    AF3_TIM11 = 3  # type: int
    AF3_TIM8 = 3  # type: int
    AF3_TIM9 = 3  # type: int
    AF2_TIM4 = 2  # type: int
    AF1_TIM1 = 1  # type: int
    AF1_TIM2 = 1  # type: int
    AF2_TIM3 = 2  # type: int
    AF8_UART4 = 8  # type: int
    AF6_I2S2 = 6  # type: int
    AF7_USART1 = 7  # type: int
    AF7_USART2 = 7  # type: int
    AF7_USART3 = 7  # type: int
    AF4_I2C1 = 4  # type: int
    AF5_SPI2 = 5  # type: int
    AF4_I2C2 = 4  # type: int
    AF5_I2S2 = 5  # type: int
    AF5_SPI1 = 5  # type: int

    def mode(self, *args, **kwargs) -> Incomplete:
        ...

    def name(self, *args, **kwargs) -> Incomplete:
        ...

    def pull(self, *args, **kwargs) -> Incomplete:
        ...

    def low(self, *args, **kwargs) -> Incomplete:
        ...

    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def pin(self, *args, **kwargs) -> Incomplete:
        ...

    def port(self, *args, **kwargs) -> Incomplete:
        ...

    def names(self, *args, **kwargs) -> Incomplete:
        ...

    def on(self, *args, **kwargs) -> Incomplete:
        ...

    def off(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def af_list(self, *args, **kwargs) -> Incomplete:
        ...

    def af(self, *args, **kwargs) -> Incomplete:
        ...

    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def high(self, *args, **kwargs) -> Incomplete:
        ...

    def gpio(self, *args, **kwargs) -> Incomplete:
        ...

    @classmethod
    def dict(cls, *args, **kwargs) -> Incomplete:
        ...

    @classmethod
    def debug(cls, *args, **kwargs) -> Incomplete:
        ...

    class cpu:
        B9: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B9, mode=Pin.IN)
        B8: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B8, mode=Pin.IN)
        B7: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B7, mode=Pin.IN)
        C0: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C0, mode=Pin.IN)
        C1: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C1, mode=Pin.IN)
        C10: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C10, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        B3: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B3, mode=Pin.IN, pull=Pin.PULL_UP)
        B2: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B2, mode=Pin.IN)
        B6: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B6, mode=Pin.IN)
        B4: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B4, mode=Pin.OUT)
        B5: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B5, mode=Pin.OUT)
        B15: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B15, mode=Pin.IN)
        C7: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C7, mode=Pin.IN)
        C6: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C6, mode=Pin.IN)
        C5: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C5, mode=Pin.IN)
        C8: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C8, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C9: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C9, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C11: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C11, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C13: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C13, mode=Pin.IN)
        C12: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C12, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C4: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C4, mode=Pin.IN)
        C2: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C2, mode=Pin.IN)
        C3: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C3, mode=Pin.IN)
        D2: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.D2, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        A15: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A15, mode=Pin.OUT)
        A14: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A14, mode=Pin.OUT)
        A13: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A13, mode=Pin.OUT)
        A2: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A2, mode=Pin.IN)
        A3: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A3, mode=Pin.IN)
        A4: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A4, mode=Pin.IN)
        A1: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A1, mode=Pin.IN)
        A0: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A0, mode=Pin.IN)
        A12: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A12, mode=Pin.ALT, alt=10)
        A10: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A10, mode=Pin.ALT_OPEN_DRAIN, pull=Pin.PULL_UP, alt=10)
        A11: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A11, mode=Pin.ALT, alt=10)
        B14: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B14, mode=Pin.IN)
        B11: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B11, mode=Pin.IN)
        B10: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B10, mode=Pin.IN)
        B1: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B1, mode=Pin.IN)
        B12: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B12, mode=Pin.IN)
        B13: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B13, mode=Pin.IN)
        A5: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A5, mode=Pin.IN)
        A7: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A7, mode=Pin.IN)
        A6: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A6, mode=Pin.IN)
        B0: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B0, mode=Pin.IN)
        A8: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A8, mode=Pin.IN, pull=Pin.PULL_UP)
        A9: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A9, mode=Pin.IN)

        def __init__(self, *argv, **kwargs) -> None:
            ...

    @classmethod
    def mapper(cls, *args, **kwargs) -> Incomplete:
        ...

    class board:
        X5: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A4, mode=Pin.IN)
        X18: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C13, mode=Pin.IN)
        X4: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A3, mode=Pin.IN)
        X8: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A7, mode=Pin.IN)
        X6: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A5, mode=Pin.IN)
        X7: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A6, mode=Pin.IN)
        X2: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A1, mode=Pin.IN)
        X3: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A2, mode=Pin.IN)
        X19: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C0, mode=Pin.IN)
        X22: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C3, mode=Pin.IN)
        X20: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C1, mode=Pin.IN)
        X21: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C2, mode=Pin.IN)
        Y5: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B12, mode=Pin.IN)
        X9: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B6, mode=Pin.IN)
        Y4: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B9, mode=Pin.IN)
        Y8: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B15, mode=Pin.IN)
        Y6: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B13, mode=Pin.IN)
        Y7: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B14, mode=Pin.IN)
        Y10: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B11, mode=Pin.IN)
        Y3: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B8, mode=Pin.IN)
        Y1: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C6, mode=Pin.IN)
        Y2: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C7, mode=Pin.IN)
        Y11: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B0, mode=Pin.IN)
        Y12: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B1, mode=Pin.IN)
        Y9: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B10, mode=Pin.IN)
        SD_CK: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C12, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        X17: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B3, mode=Pin.IN, pull=Pin.PULL_UP)
        SD: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A8, mode=Pin.IN, pull=Pin.PULL_UP)
        SD_D1: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C9, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        SD_CMD: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.D2, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        SD_D0: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C8, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        LED_GREEN: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A14, mode=Pin.OUT)
        MMA_INT: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B2, mode=Pin.IN)
        LED_BLUE: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B4, mode=Pin.OUT)
        MMA_AVDD: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B5, mode=Pin.OUT)
        LED_RED: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A13, mode=Pin.OUT)
        LED_YELLOW: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A15, mode=Pin.OUT)
        X1: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A0, mode=Pin.IN)
        SD_D2: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C10, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        USB_VBUS: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A9, mode=Pin.IN)
        X12: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C5, mode=Pin.IN)
        X10: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B7, mode=Pin.IN)
        X11: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C4, mode=Pin.IN)
        SD_SW: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A8, mode=Pin.IN, pull=Pin.PULL_UP)
        USB_ID: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A10, mode=Pin.ALT_OPEN_DRAIN, pull=Pin.PULL_UP, alt=10)
        SD_D3: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.C11, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        USB_DP: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A12, mode=Pin.ALT, alt=10)
        SW: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.B3, mode=Pin.IN, pull=Pin.PULL_UP)
        USB_DM: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.A11, mode=Pin.ALT, alt=10)

        def __init__(self, *argv, **kwargs) -> None:
            ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S:
    RX = 768  # type: int
    MONO = 0  # type: int
    STEREO = 1  # type: int
    TX = 512  # type: int

    def shift(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SPI:
    LSB = 128  # type: int
    MSB = 0  # type: int

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def write_readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


mem8: Incomplete  ## <class 'mem'> = <8-bit memory>


class RTC:
    def info(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def wakeup(self, *args, **kwargs) -> Incomplete:
        ...

    def datetime(self, *args, **kwargs) -> Incomplete:
        ...

    def calibration(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2C:
    def readfrom_mem_into(self, *args, **kwargs) -> Incomplete:
        ...

    def readfrom_into(self, *args, **kwargs) -> Incomplete:
        ...

    def readfrom_mem(self, *args, **kwargs) -> Incomplete:
        ...

    def writeto_mem(self, *args, **kwargs) -> Incomplete:
        ...

    def scan(self, *args, **kwargs) -> Incomplete:
        ...

    def writeto(self, *args, **kwargs) -> Incomplete:
        ...

    def writevto(self, *args, **kwargs) -> Incomplete:
        ...

    def start(self, *args, **kwargs) -> Incomplete:
        ...

    def readfrom(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def stop(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC:
    VREF = 65535  # type: int
    CORE_VREF = 256  # type: int
    CORE_VBAT = 258  # type: int
    CORE_TEMP = 257  # type: int

    def read_u16(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class WDT:
    def feed(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Timer:
    PERIODIC = 2  # type: int
    ONE_SHOT = 1  # type: int

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SoftSPI:
    LSB = 128  # type: int
    MSB = 0  # type: int

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def write_readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class UART:
    IRQ_RXIDLE = 16  # type: int
    CTS = 512  # type: int
    RTS = 256  # type: int

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def txdone(self, *args, **kwargs) -> Incomplete:
        ...

    def sendbreak(self, *args, **kwargs) -> Incomplete:
        ...

    def readchar(self, *args, **kwargs) -> Incomplete:
        ...

    def writechar(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def any(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def readline(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


mem32: Incomplete  ## <class 'mem'> = <32-bit memory>
mem16: Incomplete  ## <class 'mem'> = <16-bit memory>


class SoftI2C:
    def readfrom_mem_into(self, *args, **kwargs) -> Incomplete:
        ...

    def readfrom_into(self, *args, **kwargs) -> Incomplete:
        ...

    def readfrom_mem(self, *args, **kwargs) -> Incomplete:
        ...

    def writeto_mem(self, *args, **kwargs) -> Incomplete:
        ...

    def scan(self, *args, **kwargs) -> Incomplete:
        ...

    def writeto(self, *args, **kwargs) -> Incomplete:
        ...

    def writevto(self, *args, **kwargs) -> Incomplete:
        ...

    def start(self, *args, **kwargs) -> Incomplete:
        ...

    def readfrom(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def stop(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Signal:
    def off(self, *args, **kwargs) -> Incomplete:
        ...

    def on(self, *args, **kwargs) -> Incomplete:
        ...

    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
