"""
Module: 'umachine' on micropython-v1.20-rp2-PICO_W
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20', 'build': '', 'ver': 'v1.20', 'port': 'rp2', 'board': 'PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.12.2
from typing import Any

WDT_RESET = 3  # type: int
PWRON_RESET = 1  # type: int


def dht_readinto(*args, **kwargs) -> Any:
    ...


def enable_irq(*args, **kwargs) -> Any:
    ...


def disable_irq(*args, **kwargs) -> Any:
    ...


def bitstream(*args, **kwargs) -> Any:
    ...


def deepsleep(*args, **kwargs) -> Any:
    ...


def bootloader(*args, **kwargs) -> Any:
    ...


def soft_reset(*args, **kwargs) -> Any:
    ...


def reset(*args, **kwargs) -> Any:
    ...


def freq(*args, **kwargs) -> Any:
    ...


def reset_cause(*args, **kwargs) -> Any:
    ...


def idle(*args, **kwargs) -> Any:
    ...


def time_pulse_us(*args, **kwargs) -> Any:
    ...


def lightsleep(*args, **kwargs) -> Any:
    ...


def unique_id(*args, **kwargs) -> Any:
    ...


class WDT:
    def feed(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


mem8: Any  ## <class 'mem'> = <8-bit memory>
mem32: Any  ## <class 'mem'> = <32-bit memory>
mem16: Any  ## <class 'mem'> = <16-bit memory>


class PWM:
    def freq(self, *args, **kwargs) -> Any:
        ...

    def duty_u16(self, *args, **kwargs) -> Any:
        ...

    def duty_ns(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC:
    CORE_TEMP = 4  # type: int

    def read_u16(self, *args, **kwargs) -> Any:
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


class I2S:
    RX = 0  # type: int
    MONO = 0  # type: int
    STEREO = 1  # type: int
    TX = 1  # type: int

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

    def low(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def toggle(self, *args, **kwargs) -> Any:
        ...

    def off(self, *args, **kwargs) -> Any:
        ...

    def on(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def value(self, *args, **kwargs) -> Any:
        ...

    def high(self, *args, **kwargs) -> Any:
        ...

    class cpu:
        GPIO20: Any  ## <class 'Pin'> = Pin(GPIO20, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO25: Any  ## <class 'Pin'> = Pin(GPIO25, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO26: Any  ## <class 'Pin'> = Pin(GPIO26, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO27: Any  ## <class 'Pin'> = Pin(GPIO27, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO24: Any  ## <class 'Pin'> = Pin(GPIO24, mode=ALT, alt=31)
        GPIO21: Any  ## <class 'Pin'> = Pin(GPIO21, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO22: Any  ## <class 'Pin'> = Pin(GPIO22, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO23: Any  ## <class 'Pin'> = Pin(GPIO23, mode=ALT, alt=31)
        GPIO28: Any  ## <class 'Pin'> = Pin(GPIO28, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO6: Any  ## <class 'Pin'> = Pin(GPIO6, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO7: Any  ## <class 'Pin'> = Pin(GPIO7, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO8: Any  ## <class 'Pin'> = Pin(GPIO8, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO5: Any  ## <class 'Pin'> = Pin(GPIO5, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO29: Any  ## <class 'Pin'> = Pin(GPIO29, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO3: Any  ## <class 'Pin'> = Pin(GPIO3, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO4: Any  ## <class 'Pin'> = Pin(GPIO4, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO9: Any  ## <class 'Pin'> = Pin(GPIO9, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO2: Any  ## <class 'Pin'> = Pin(GPIO2, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO1: Any  ## <class 'Pin'> = Pin(GPIO1, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO10: Any  ## <class 'Pin'> = Pin(GPIO10, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO11: Any  ## <class 'Pin'> = Pin(GPIO11, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO0: Any  ## <class 'Pin'> = Pin(GPIO0, mode=ALT, pull=PULL_DOWN, alt=31)
        EXT_GPIO0: Any  ## <class 'Pin'> = Pin(EXT_GPIO0, mode=IN)
        EXT_GPIO1: Any  ## <class 'Pin'> = Pin(EXT_GPIO1, mode=IN)
        EXT_GPIO2: Any  ## <class 'Pin'> = Pin(EXT_GPIO2, mode=IN)
        GPIO12: Any  ## <class 'Pin'> = Pin(GPIO12, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO17: Any  ## <class 'Pin'> = Pin(GPIO17, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO18: Any  ## <class 'Pin'> = Pin(GPIO18, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO19: Any  ## <class 'Pin'> = Pin(GPIO19, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO16: Any  ## <class 'Pin'> = Pin(GPIO16, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO13: Any  ## <class 'Pin'> = Pin(GPIO13, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO14: Any  ## <class 'Pin'> = Pin(GPIO14, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO15: Any  ## <class 'Pin'> = Pin(GPIO15, mode=ALT, pull=PULL_DOWN, alt=31)

        def __init__(self, *argv, **kwargs) -> None:
            ...

    class board:
        GP3: Any  ## <class 'Pin'> = Pin(GPIO3, mode=ALT, pull=PULL_DOWN, alt=31)
        GP28: Any  ## <class 'Pin'> = Pin(GPIO28, mode=ALT, pull=PULL_DOWN, alt=31)
        GP4: Any  ## <class 'Pin'> = Pin(GPIO4, mode=ALT, pull=PULL_DOWN, alt=31)
        GP5: Any  ## <class 'Pin'> = Pin(GPIO5, mode=ALT, pull=PULL_DOWN, alt=31)
        GP22: Any  ## <class 'Pin'> = Pin(GPIO22, mode=ALT, pull=PULL_DOWN, alt=31)
        GP27: Any  ## <class 'Pin'> = Pin(GPIO27, mode=ALT, pull=PULL_DOWN, alt=31)
        GP26: Any  ## <class 'Pin'> = Pin(GPIO26, mode=ALT, pull=PULL_DOWN, alt=31)
        WL_GPIO2: Any  ## <class 'Pin'> = Pin(EXT_GPIO2, mode=IN)
        WL_GPIO0: Any  ## <class 'Pin'> = Pin(EXT_GPIO0, mode=IN)
        LED: Any  ## <class 'Pin'> = Pin(EXT_GPIO0, mode=IN)
        WL_GPIO1: Any  ## <class 'Pin'> = Pin(EXT_GPIO1, mode=IN)
        GP6: Any  ## <class 'Pin'> = Pin(GPIO6, mode=ALT, pull=PULL_DOWN, alt=31)
        GP7: Any  ## <class 'Pin'> = Pin(GPIO7, mode=ALT, pull=PULL_DOWN, alt=31)
        GP9: Any  ## <class 'Pin'> = Pin(GPIO9, mode=ALT, pull=PULL_DOWN, alt=31)
        GP8: Any  ## <class 'Pin'> = Pin(GPIO8, mode=ALT, pull=PULL_DOWN, alt=31)
        GP12: Any  ## <class 'Pin'> = Pin(GPIO12, mode=ALT, pull=PULL_DOWN, alt=31)
        GP11: Any  ## <class 'Pin'> = Pin(GPIO11, mode=ALT, pull=PULL_DOWN, alt=31)
        GP13: Any  ## <class 'Pin'> = Pin(GPIO13, mode=ALT, pull=PULL_DOWN, alt=31)
        GP14: Any  ## <class 'Pin'> = Pin(GPIO14, mode=ALT, pull=PULL_DOWN, alt=31)
        GP0: Any  ## <class 'Pin'> = Pin(GPIO0, mode=ALT, pull=PULL_DOWN, alt=31)
        GP10: Any  ## <class 'Pin'> = Pin(GPIO10, mode=ALT, pull=PULL_DOWN, alt=31)
        GP1: Any  ## <class 'Pin'> = Pin(GPIO1, mode=ALT, pull=PULL_DOWN, alt=31)
        GP21: Any  ## <class 'Pin'> = Pin(GPIO21, mode=ALT, pull=PULL_DOWN, alt=31)
        GP2: Any  ## <class 'Pin'> = Pin(GPIO2, mode=ALT, pull=PULL_DOWN, alt=31)
        GP19: Any  ## <class 'Pin'> = Pin(GPIO19, mode=ALT, pull=PULL_DOWN, alt=31)
        GP20: Any  ## <class 'Pin'> = Pin(GPIO20, mode=ALT, pull=PULL_DOWN, alt=31)
        GP15: Any  ## <class 'Pin'> = Pin(GPIO15, mode=ALT, pull=PULL_DOWN, alt=31)
        GP16: Any  ## <class 'Pin'> = Pin(GPIO16, mode=ALT, pull=PULL_DOWN, alt=31)
        GP18: Any  ## <class 'Pin'> = Pin(GPIO18, mode=ALT, pull=PULL_DOWN, alt=31)
        GP17: Any  ## <class 'Pin'> = Pin(GPIO17, mode=ALT, pull=PULL_DOWN, alt=31)

        def __init__(self, *argv, **kwargs) -> None:
            ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SoftSPI:
    LSB = 0  # type: int
    MSB = 1  # type: int

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


class Timer:
    PERIODIC = 1  # type: int
    ONE_SHOT = 0  # type: int

    def init(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class UART:
    INV_TX = 1  # type: int
    RTS = 2  # type: int
    CTS = 1  # type: int
    INV_RX = 2  # type: int

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def sendbreak(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def flush(self, *args, **kwargs) -> Any:
        ...

    def txdone(self, *args, **kwargs) -> Any:
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


class RTC:
    def datetime(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SPI:
    LSB = 0  # type: int
    MSB = 1  # type: int

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


class Signal:
    def off(self, *args, **kwargs) -> Any:
        ...

    def on(self, *args, **kwargs) -> Any:
        ...

    def value(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
