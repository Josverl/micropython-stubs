"""
Module: 'machine' on micropython-v1.19.1-stm32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'stm32', 'port': 'stm32', 'machine': 'PYBv1.1 with STM32F405RG', 'release': '1.19.1', 'nodename': 'pyboard', 'name': 'micropython', 'family': 'micropython', 'sysname': 'pyboard', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Any

HARD_RESET = 2  # type: int
PWRON_RESET = 1  # type: int
SOFT_RESET = 0  # type: int
DEEPSLEEP_RESET = 4  # type: int
WDT_RESET = 3  # type: int


def idle(*args, **kwargs) -> Any:
    ...


def freq(*args, **kwargs) -> Any:
    ...


def info(*args, **kwargs) -> Any:
    ...


def deepsleep(*args, **kwargs) -> Any:
    ...


def enable_irq(*args, **kwargs) -> Any:
    ...


def disable_irq(*args, **kwargs) -> Any:
    ...


def unique_id(*args, **kwargs) -> Any:
    ...


def soft_reset(*args, **kwargs) -> Any:
    ...


def sleep(*args, **kwargs) -> Any:
    ...


def time_pulse_us(*args, **kwargs) -> Any:
    ...


def lightsleep(*args, **kwargs) -> Any:
    ...


def reset(*args, **kwargs) -> Any:
    ...


def rng(*args, **kwargs) -> Any:
    ...


def reset_cause(*args, **kwargs) -> Any:
    ...


def bootloader(*args, **kwargs) -> Any:
    ...


def bitstream(*args, **kwargs) -> Any:
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

    def mode(self, *args, **kwargs) -> Any:
        ...

    def name(self, *args, **kwargs) -> Any:
        ...

    def pull(self, *args, **kwargs) -> Any:
        ...

    def low(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def pin(self, *args, **kwargs) -> Any:
        ...

    def port(self, *args, **kwargs) -> Any:
        ...

    def names(self, *args, **kwargs) -> Any:
        ...

    def on(self, *args, **kwargs) -> Any:
        ...

    def off(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def af_list(self, *args, **kwargs) -> Any:
        ...

    def af(self, *args, **kwargs) -> Any:
        ...

    def value(self, *args, **kwargs) -> Any:
        ...

    def high(self, *args, **kwargs) -> Any:
        ...

    def gpio(self, *args, **kwargs) -> Any:
        ...

    @classmethod
    def dict(cls, *args, **kwargs) -> Any:
        ...

    @classmethod
    def debug(cls, *args, **kwargs) -> Any:
        ...

    class cpu:
        B9: Any  ## <class 'Pin'> = Pin(Pin.cpu.B9, mode=Pin.IN)
        B8: Any  ## <class 'Pin'> = Pin(Pin.cpu.B8, mode=Pin.IN)
        B7: Any  ## <class 'Pin'> = Pin(Pin.cpu.B7, mode=Pin.IN)
        C0: Any  ## <class 'Pin'> = Pin(Pin.cpu.C0, mode=Pin.IN)
        C1: Any  ## <class 'Pin'> = Pin(Pin.cpu.C1, mode=Pin.IN)
        C10: Any  ## <class 'Pin'> = Pin(Pin.cpu.C10, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        B3: Any  ## <class 'Pin'> = Pin(Pin.cpu.B3, mode=Pin.IN, pull=Pin.PULL_UP)
        B2: Any  ## <class 'Pin'> = Pin(Pin.cpu.B2, mode=Pin.IN)
        B6: Any  ## <class 'Pin'> = Pin(Pin.cpu.B6, mode=Pin.IN)
        B4: Any  ## <class 'Pin'> = Pin(Pin.cpu.B4, mode=Pin.OUT)
        B5: Any  ## <class 'Pin'> = Pin(Pin.cpu.B5, mode=Pin.OUT)
        B15: Any  ## <class 'Pin'> = Pin(Pin.cpu.B15, mode=Pin.IN)
        C7: Any  ## <class 'Pin'> = Pin(Pin.cpu.C7, mode=Pin.IN)
        C6: Any  ## <class 'Pin'> = Pin(Pin.cpu.C6, mode=Pin.IN)
        C5: Any  ## <class 'Pin'> = Pin(Pin.cpu.C5, mode=Pin.IN)
        C8: Any  ## <class 'Pin'> = Pin(Pin.cpu.C8, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C9: Any  ## <class 'Pin'> = Pin(Pin.cpu.C9, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C11: Any  ## <class 'Pin'> = Pin(Pin.cpu.C11, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C13: Any  ## <class 'Pin'> = Pin(Pin.cpu.C13, mode=Pin.IN)
        C12: Any  ## <class 'Pin'> = Pin(Pin.cpu.C12, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        C4: Any  ## <class 'Pin'> = Pin(Pin.cpu.C4, mode=Pin.IN)
        C2: Any  ## <class 'Pin'> = Pin(Pin.cpu.C2, mode=Pin.IN)
        C3: Any  ## <class 'Pin'> = Pin(Pin.cpu.C3, mode=Pin.IN)
        D2: Any  ## <class 'Pin'> = Pin(Pin.cpu.D2, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        A15: Any  ## <class 'Pin'> = Pin(Pin.cpu.A15, mode=Pin.OUT)
        A14: Any  ## <class 'Pin'> = Pin(Pin.cpu.A14, mode=Pin.OUT)
        A13: Any  ## <class 'Pin'> = Pin(Pin.cpu.A13, mode=Pin.OUT)
        A2: Any  ## <class 'Pin'> = Pin(Pin.cpu.A2, mode=Pin.IN)
        A3: Any  ## <class 'Pin'> = Pin(Pin.cpu.A3, mode=Pin.IN)
        A4: Any  ## <class 'Pin'> = Pin(Pin.cpu.A4, mode=Pin.IN)
        A1: Any  ## <class 'Pin'> = Pin(Pin.cpu.A1, mode=Pin.IN)
        A0: Any  ## <class 'Pin'> = Pin(Pin.cpu.A0, mode=Pin.IN)
        A12: Any  ## <class 'Pin'> = Pin(Pin.cpu.A12, mode=Pin.ALT, alt=10)
        A10: Any  ## <class 'Pin'> = Pin(Pin.cpu.A10, mode=Pin.ALT_OPEN_DRAIN, pull=Pin.PULL_UP, alt=10)
        A11: Any  ## <class 'Pin'> = Pin(Pin.cpu.A11, mode=Pin.ALT, alt=10)
        B14: Any  ## <class 'Pin'> = Pin(Pin.cpu.B14, mode=Pin.IN)
        B11: Any  ## <class 'Pin'> = Pin(Pin.cpu.B11, mode=Pin.IN)
        B10: Any  ## <class 'Pin'> = Pin(Pin.cpu.B10, mode=Pin.IN)
        B1: Any  ## <class 'Pin'> = Pin(Pin.cpu.B1, mode=Pin.IN)
        B12: Any  ## <class 'Pin'> = Pin(Pin.cpu.B12, mode=Pin.IN)
        B13: Any  ## <class 'Pin'> = Pin(Pin.cpu.B13, mode=Pin.IN)
        A5: Any  ## <class 'Pin'> = Pin(Pin.cpu.A5, mode=Pin.IN)
        A7: Any  ## <class 'Pin'> = Pin(Pin.cpu.A7, mode=Pin.IN)
        A6: Any  ## <class 'Pin'> = Pin(Pin.cpu.A6, mode=Pin.IN)
        B0: Any  ## <class 'Pin'> = Pin(Pin.cpu.B0, mode=Pin.IN)
        A8: Any  ## <class 'Pin'> = Pin(Pin.cpu.A8, mode=Pin.IN, pull=Pin.PULL_UP)
        A9: Any  ## <class 'Pin'> = Pin(Pin.cpu.A9, mode=Pin.IN)

        def __init__(self, *argv, **kwargs) -> None:
            ...

    @classmethod
    def mapper(cls, *args, **kwargs) -> Any:
        ...

    class board:
        X5: Any  ## <class 'Pin'> = Pin(Pin.cpu.A4, mode=Pin.IN)
        X18: Any  ## <class 'Pin'> = Pin(Pin.cpu.C13, mode=Pin.IN)
        X4: Any  ## <class 'Pin'> = Pin(Pin.cpu.A3, mode=Pin.IN)
        X8: Any  ## <class 'Pin'> = Pin(Pin.cpu.A7, mode=Pin.IN)
        X6: Any  ## <class 'Pin'> = Pin(Pin.cpu.A5, mode=Pin.IN)
        X7: Any  ## <class 'Pin'> = Pin(Pin.cpu.A6, mode=Pin.IN)
        X2: Any  ## <class 'Pin'> = Pin(Pin.cpu.A1, mode=Pin.IN)
        X3: Any  ## <class 'Pin'> = Pin(Pin.cpu.A2, mode=Pin.IN)
        X19: Any  ## <class 'Pin'> = Pin(Pin.cpu.C0, mode=Pin.IN)
        X22: Any  ## <class 'Pin'> = Pin(Pin.cpu.C3, mode=Pin.IN)
        X20: Any  ## <class 'Pin'> = Pin(Pin.cpu.C1, mode=Pin.IN)
        X21: Any  ## <class 'Pin'> = Pin(Pin.cpu.C2, mode=Pin.IN)
        Y5: Any  ## <class 'Pin'> = Pin(Pin.cpu.B12, mode=Pin.IN)
        X9: Any  ## <class 'Pin'> = Pin(Pin.cpu.B6, mode=Pin.IN)
        Y4: Any  ## <class 'Pin'> = Pin(Pin.cpu.B9, mode=Pin.IN)
        Y8: Any  ## <class 'Pin'> = Pin(Pin.cpu.B15, mode=Pin.IN)
        Y6: Any  ## <class 'Pin'> = Pin(Pin.cpu.B13, mode=Pin.IN)
        Y7: Any  ## <class 'Pin'> = Pin(Pin.cpu.B14, mode=Pin.IN)
        Y10: Any  ## <class 'Pin'> = Pin(Pin.cpu.B11, mode=Pin.IN)
        Y3: Any  ## <class 'Pin'> = Pin(Pin.cpu.B8, mode=Pin.IN)
        Y1: Any  ## <class 'Pin'> = Pin(Pin.cpu.C6, mode=Pin.IN)
        Y2: Any  ## <class 'Pin'> = Pin(Pin.cpu.C7, mode=Pin.IN)
        Y11: Any  ## <class 'Pin'> = Pin(Pin.cpu.B0, mode=Pin.IN)
        Y12: Any  ## <class 'Pin'> = Pin(Pin.cpu.B1, mode=Pin.IN)
        Y9: Any  ## <class 'Pin'> = Pin(Pin.cpu.B10, mode=Pin.IN)
        SD_CK: Any  ## <class 'Pin'> = Pin(Pin.cpu.C12, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        X17: Any  ## <class 'Pin'> = Pin(Pin.cpu.B3, mode=Pin.IN, pull=Pin.PULL_UP)
        SD: Any  ## <class 'Pin'> = Pin(Pin.cpu.A8, mode=Pin.IN, pull=Pin.PULL_UP)
        SD_D1: Any  ## <class 'Pin'> = Pin(Pin.cpu.C9, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        SD_CMD: Any  ## <class 'Pin'> = Pin(Pin.cpu.D2, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        SD_D0: Any  ## <class 'Pin'> = Pin(Pin.cpu.C8, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        LED_GREEN: Any  ## <class 'Pin'> = Pin(Pin.cpu.A14, mode=Pin.OUT)
        MMA_INT: Any  ## <class 'Pin'> = Pin(Pin.cpu.B2, mode=Pin.IN)
        LED_BLUE: Any  ## <class 'Pin'> = Pin(Pin.cpu.B4, mode=Pin.OUT)
        MMA_AVDD: Any  ## <class 'Pin'> = Pin(Pin.cpu.B5, mode=Pin.OUT)
        LED_RED: Any  ## <class 'Pin'> = Pin(Pin.cpu.A13, mode=Pin.OUT)
        LED_YELLOW: Any  ## <class 'Pin'> = Pin(Pin.cpu.A15, mode=Pin.OUT)
        X1: Any  ## <class 'Pin'> = Pin(Pin.cpu.A0, mode=Pin.IN)
        SD_D2: Any  ## <class 'Pin'> = Pin(Pin.cpu.C10, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        USB_VBUS: Any  ## <class 'Pin'> = Pin(Pin.cpu.A9, mode=Pin.IN)
        X12: Any  ## <class 'Pin'> = Pin(Pin.cpu.C5, mode=Pin.IN)
        X10: Any  ## <class 'Pin'> = Pin(Pin.cpu.B7, mode=Pin.IN)
        X11: Any  ## <class 'Pin'> = Pin(Pin.cpu.C4, mode=Pin.IN)
        SD_SW: Any  ## <class 'Pin'> = Pin(Pin.cpu.A8, mode=Pin.IN, pull=Pin.PULL_UP)
        USB_ID: Any  ## <class 'Pin'> = Pin(Pin.cpu.A10, mode=Pin.ALT_OPEN_DRAIN, pull=Pin.PULL_UP, alt=10)
        SD_D3: Any  ## <class 'Pin'> = Pin(Pin.cpu.C11, mode=Pin.ALT, pull=Pin.PULL_UP, alt=12)
        USB_DP: Any  ## <class 'Pin'> = Pin(Pin.cpu.A12, mode=Pin.ALT, alt=10)
        SW: Any  ## <class 'Pin'> = Pin(Pin.cpu.B3, mode=Pin.IN, pull=Pin.PULL_UP)
        USB_DM: Any  ## <class 'Pin'> = Pin(Pin.cpu.A11, mode=Pin.ALT, alt=10)

        def __init__(self, *argv, **kwargs) -> None:
            ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S:
    RX = 768  # type: int
    MONO = 0  # type: int
    STEREO = 1  # type: int
    TX = 512  # type: int

    def shift(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SPI:
    LSB = 128  # type: int
    MSB = 0  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def write_readinto(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


mem8: Any  ## <class 'mem'> = <8-bit memory>


class RTC:
    def info(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def wakeup(self, *args, **kwargs) -> Any:
        ...

    def datetime(self, *args, **kwargs) -> Any:
        ...

    def calibration(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2C:
    def readfrom_mem_into(self, *args, **kwargs) -> Any:
        ...

    def readfrom_into(self, *args, **kwargs) -> Any:
        ...

    def readfrom_mem(self, *args, **kwargs) -> Any:
        ...

    def writeto_mem(self, *args, **kwargs) -> Any:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...

    def writeto(self, *args, **kwargs) -> Any:
        ...

    def writevto(self, *args, **kwargs) -> Any:
        ...

    def start(self, *args, **kwargs) -> Any:
        ...

    def readfrom(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def stop(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC:
    VREF = 65535  # type: int
    CORE_VREF = 17  # type: int
    CORE_VBAT = 18  # type: int
    CORE_TEMP = 16  # type: int

    def read_u16(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class WDT:
    def feed(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Timer:
    PERIODIC = 2  # type: int
    ONE_SHOT = 1  # type: int

    def init(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SoftSPI:
    LSB = 128  # type: int
    MSB = 0  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def write_readinto(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class UART:
    CTS = 512  # type: int
    RTS = 256  # type: int
    IRQ_RXIDLE = 16  # type: int

    def readchar(self, *args, **kwargs) -> Any:
        ...

    def sendbreak(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def writechar(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def any(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


mem32: Any  ## <class 'mem'> = <32-bit memory>
mem16: Any  ## <class 'mem'> = <16-bit memory>


class SoftI2C:
    def readfrom_mem_into(self, *args, **kwargs) -> Any:
        ...

    def readfrom_into(self, *args, **kwargs) -> Any:
        ...

    def readfrom_mem(self, *args, **kwargs) -> Any:
        ...

    def writeto_mem(self, *args, **kwargs) -> Any:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...

    def writeto(self, *args, **kwargs) -> Any:
        ...

    def writevto(self, *args, **kwargs) -> Any:
        ...

    def start(self, *args, **kwargs) -> Any:
        ...

    def readfrom(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def stop(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Signal:
    def off(self, *args, **kwargs) -> Any:
        ...

    def on(self, *args, **kwargs) -> Any:
        ...

    def value(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
