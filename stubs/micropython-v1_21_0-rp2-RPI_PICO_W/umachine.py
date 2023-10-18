"""
Module: 'umachine' on micropython-v1.21.0-rp2-RPI_PICO_W
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

WDT_RESET = 3  # type: int
PWRON_RESET = 1  # type: int


def dht_readinto(*args, **kwargs) -> Incomplete:
    ...


def enable_irq(*args, **kwargs) -> Incomplete:
    ...


def disable_irq(*args, **kwargs) -> Incomplete:
    ...


def bitstream(*args, **kwargs) -> Incomplete:
    ...


def deepsleep(*args, **kwargs) -> Incomplete:
    ...


def bootloader(*args, **kwargs) -> Incomplete:
    ...


def soft_reset(*args, **kwargs) -> Incomplete:
    ...


def reset(*args, **kwargs) -> Incomplete:
    ...


def freq(*args, **kwargs) -> Incomplete:
    ...


def reset_cause(*args, **kwargs) -> Incomplete:
    ...


def idle(*args, **kwargs) -> Incomplete:
    ...


def time_pulse_us(*args, **kwargs) -> Incomplete:
    ...


def lightsleep(*args, **kwargs) -> Incomplete:
    ...


def unique_id(*args, **kwargs) -> Incomplete:
    ...


class WDT:
    def feed(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


mem8: Incomplete  ## <class 'mem'> = <8-bit memory>
mem32: Incomplete  ## <class 'mem'> = <32-bit memory>
mem16: Incomplete  ## <class 'mem'> = <16-bit memory>


class PWM:
    def duty_u16(self, *args, **kwargs) -> Incomplete:
        ...

    def freq(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def duty_ns(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC:
    CORE_TEMP = 4  # type: int

    def read_u16(self, *args, **kwargs) -> Incomplete:
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


class I2S:
    RX = 0  # type: int
    MONO = 0  # type: int
    STEREO = 1  # type: int
    TX = 1  # type: int

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


class Pin:
    ALT_SPI = 1  # type: int
    IN = 0  # type: int
    ALT_USB = 9  # type: int
    ALT_UART = 2  # type: int
    IRQ_FALLING = 4  # type: int
    OUT = 1  # type: int
    OPEN_DRAIN = 2  # type: int
    IRQ_RISING = 8  # type: int
    PULL_DOWN = 2  # type: int
    ALT_SIO = 5  # type: int
    ALT_GPCK = 8  # type: int
    ALT = 3  # type: int
    PULL_UP = 1  # type: int
    ALT_I2C = 3  # type: int
    ALT_PWM = 4  # type: int
    ALT_PIO1 = 7  # type: int
    ALT_PIO0 = 6  # type: int

    def low(self, *args, **kwargs) -> Incomplete:
        ...

    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def toggle(self, *args, **kwargs) -> Incomplete:
        ...

    def off(self, *args, **kwargs) -> Incomplete:
        ...

    def on(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def high(self, *args, **kwargs) -> Incomplete:
        ...

    class cpu:
        GPIO20: Incomplete  ## <class 'Pin'> = Pin(GPIO20, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO25: Incomplete  ## <class 'Pin'> = Pin(GPIO25, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO26: Incomplete  ## <class 'Pin'> = Pin(GPIO26, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO27: Incomplete  ## <class 'Pin'> = Pin(GPIO27, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO24: Incomplete  ## <class 'Pin'> = Pin(GPIO24, mode=ALT, alt=31)
        GPIO21: Incomplete  ## <class 'Pin'> = Pin(GPIO21, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO22: Incomplete  ## <class 'Pin'> = Pin(GPIO22, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO23: Incomplete  ## <class 'Pin'> = Pin(GPIO23, mode=ALT, alt=31)
        GPIO28: Incomplete  ## <class 'Pin'> = Pin(GPIO28, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO6: Incomplete  ## <class 'Pin'> = Pin(GPIO6, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO7: Incomplete  ## <class 'Pin'> = Pin(GPIO7, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO8: Incomplete  ## <class 'Pin'> = Pin(GPIO8, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO5: Incomplete  ## <class 'Pin'> = Pin(GPIO5, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO29: Incomplete  ## <class 'Pin'> = Pin(GPIO29, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO3: Incomplete  ## <class 'Pin'> = Pin(GPIO3, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO4: Incomplete  ## <class 'Pin'> = Pin(GPIO4, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO9: Incomplete  ## <class 'Pin'> = Pin(GPIO9, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO2: Incomplete  ## <class 'Pin'> = Pin(GPIO2, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO1: Incomplete  ## <class 'Pin'> = Pin(GPIO1, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO10: Incomplete  ## <class 'Pin'> = Pin(GPIO10, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO11: Incomplete  ## <class 'Pin'> = Pin(GPIO11, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO0: Incomplete  ## <class 'Pin'> = Pin(GPIO0, mode=ALT, pull=PULL_DOWN, alt=31)
        EXT_GPIO0: Incomplete  ## <class 'Pin'> = Pin(EXT_GPIO0, mode=IN)
        EXT_GPIO1: Incomplete  ## <class 'Pin'> = Pin(EXT_GPIO1, mode=IN)
        EXT_GPIO2: Incomplete  ## <class 'Pin'> = Pin(EXT_GPIO2, mode=IN)
        GPIO12: Incomplete  ## <class 'Pin'> = Pin(GPIO12, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO17: Incomplete  ## <class 'Pin'> = Pin(GPIO17, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO18: Incomplete  ## <class 'Pin'> = Pin(GPIO18, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO19: Incomplete  ## <class 'Pin'> = Pin(GPIO19, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO16: Incomplete  ## <class 'Pin'> = Pin(GPIO16, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO13: Incomplete  ## <class 'Pin'> = Pin(GPIO13, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO14: Incomplete  ## <class 'Pin'> = Pin(GPIO14, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO15: Incomplete  ## <class 'Pin'> = Pin(GPIO15, mode=ALT, pull=PULL_DOWN, alt=31)

        def __init__(self, *argv, **kwargs) -> None:
            ...

    class board:
        GP3: Incomplete  ## <class 'Pin'> = Pin(GPIO3, mode=ALT, pull=PULL_DOWN, alt=31)
        GP28: Incomplete  ## <class 'Pin'> = Pin(GPIO28, mode=ALT, pull=PULL_DOWN, alt=31)
        GP4: Incomplete  ## <class 'Pin'> = Pin(GPIO4, mode=ALT, pull=PULL_DOWN, alt=31)
        GP5: Incomplete  ## <class 'Pin'> = Pin(GPIO5, mode=ALT, pull=PULL_DOWN, alt=31)
        GP22: Incomplete  ## <class 'Pin'> = Pin(GPIO22, mode=ALT, pull=PULL_DOWN, alt=31)
        GP27: Incomplete  ## <class 'Pin'> = Pin(GPIO27, mode=ALT, pull=PULL_DOWN, alt=31)
        GP26: Incomplete  ## <class 'Pin'> = Pin(GPIO26, mode=ALT, pull=PULL_DOWN, alt=31)
        WL_GPIO2: Incomplete  ## <class 'Pin'> = Pin(EXT_GPIO2, mode=IN)
        WL_GPIO0: Incomplete  ## <class 'Pin'> = Pin(EXT_GPIO0, mode=IN)
        LED: Incomplete  ## <class 'Pin'> = Pin(EXT_GPIO0, mode=IN)
        WL_GPIO1: Incomplete  ## <class 'Pin'> = Pin(EXT_GPIO1, mode=IN)
        GP6: Incomplete  ## <class 'Pin'> = Pin(GPIO6, mode=ALT, pull=PULL_DOWN, alt=31)
        GP7: Incomplete  ## <class 'Pin'> = Pin(GPIO7, mode=ALT, pull=PULL_DOWN, alt=31)
        GP9: Incomplete  ## <class 'Pin'> = Pin(GPIO9, mode=ALT, pull=PULL_DOWN, alt=31)
        GP8: Incomplete  ## <class 'Pin'> = Pin(GPIO8, mode=ALT, pull=PULL_DOWN, alt=31)
        GP12: Incomplete  ## <class 'Pin'> = Pin(GPIO12, mode=ALT, pull=PULL_DOWN, alt=31)
        GP11: Incomplete  ## <class 'Pin'> = Pin(GPIO11, mode=ALT, pull=PULL_DOWN, alt=31)
        GP13: Incomplete  ## <class 'Pin'> = Pin(GPIO13, mode=ALT, pull=PULL_DOWN, alt=31)
        GP14: Incomplete  ## <class 'Pin'> = Pin(GPIO14, mode=ALT, pull=PULL_DOWN, alt=31)
        GP0: Incomplete  ## <class 'Pin'> = Pin(GPIO0, mode=ALT, pull=PULL_DOWN, alt=31)
        GP10: Incomplete  ## <class 'Pin'> = Pin(GPIO10, mode=ALT, pull=PULL_DOWN, alt=31)
        GP1: Incomplete  ## <class 'Pin'> = Pin(GPIO1, mode=ALT, pull=PULL_DOWN, alt=31)
        GP21: Incomplete  ## <class 'Pin'> = Pin(GPIO21, mode=ALT, pull=PULL_DOWN, alt=31)
        GP2: Incomplete  ## <class 'Pin'> = Pin(GPIO2, mode=ALT, pull=PULL_DOWN, alt=31)
        GP19: Incomplete  ## <class 'Pin'> = Pin(GPIO19, mode=ALT, pull=PULL_DOWN, alt=31)
        GP20: Incomplete  ## <class 'Pin'> = Pin(GPIO20, mode=ALT, pull=PULL_DOWN, alt=31)
        GP15: Incomplete  ## <class 'Pin'> = Pin(GPIO15, mode=ALT, pull=PULL_DOWN, alt=31)
        GP16: Incomplete  ## <class 'Pin'> = Pin(GPIO16, mode=ALT, pull=PULL_DOWN, alt=31)
        GP18: Incomplete  ## <class 'Pin'> = Pin(GPIO18, mode=ALT, pull=PULL_DOWN, alt=31)
        GP17: Incomplete  ## <class 'Pin'> = Pin(GPIO17, mode=ALT, pull=PULL_DOWN, alt=31)

        def __init__(self, *argv, **kwargs) -> None:
            ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SoftSPI:
    LSB = 0  # type: int
    MSB = 1  # type: int

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


class Timer:
    PERIODIC = 1  # type: int
    ONE_SHOT = 0  # type: int

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class UART:
    INV_TX = 1  # type: int
    RTS = 2  # type: int
    CTS = 1  # type: int
    INV_RX = 2  # type: int

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def sendbreak(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def txdone(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
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


class RTC:
    def datetime(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SPI:
    LSB = 0  # type: int
    MSB = 1  # type: int

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


class Signal:
    def off(self, *args, **kwargs) -> Incomplete:
        ...

    def on(self, *args, **kwargs) -> Incomplete:
        ...

    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
