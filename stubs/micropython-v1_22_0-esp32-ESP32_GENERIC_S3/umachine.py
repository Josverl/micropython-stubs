"""
Module: 'umachine' on micropython-v1.22.0-esp32-ESP32_GENERIC_S3
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'cpu': 'ESP32S3', 'mpy': 'v6.2', 'arch': 'xtensawin'}
# Stubber: v1.16.2
from _typeshed import Incomplete

WDT_RESET = 3  # type: int
SLEEP = 2  # type: int
PWRON_RESET = 1  # type: int
PIN_WAKE = 2  # type: int
SOFT_RESET = 5  # type: int
ULP_WAKE = 6  # type: int
TOUCHPAD_WAKE = 5  # type: int
TIMER_WAKE = 4  # type: int
DEEPSLEEP = 4  # type: int
EXT1_WAKE = 3  # type: int
DEEPSLEEP_RESET = 4  # type: int
HARD_RESET = 2  # type: int
EXT0_WAKE = 2  # type: int


def soft_reset(*args, **kwargs) -> Incomplete:
    ...


def dht_readinto(*args, **kwargs) -> Incomplete:
    ...


def bitstream(*args, **kwargs) -> Incomplete:
    ...


def unique_id(*args, **kwargs) -> Incomplete:
    ...


def time_pulse_us(*args, **kwargs) -> Incomplete:
    ...


def bootloader(*args, **kwargs) -> Incomplete:
    ...


def deepsleep(*args, **kwargs) -> Incomplete:
    ...


def disable_irq(*args, **kwargs) -> Incomplete:
    ...


def reset(*args, **kwargs) -> Incomplete:
    ...


def reset_cause(*args, **kwargs) -> Incomplete:
    ...


def sleep(*args, **kwargs) -> Incomplete:
    ...


def lightsleep(*args, **kwargs) -> Incomplete:
    ...


def enable_irq(*args, **kwargs) -> Incomplete:
    ...


def freq(*args, **kwargs) -> Incomplete:
    ...


def idle(*args, **kwargs) -> Incomplete:
    ...


def wake_reason(*args, **kwargs) -> Incomplete:
    ...


class PWM:
    def duty_u16(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def freq(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def duty_ns(self, *args, **kwargs) -> Incomplete:
        ...

    def duty(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Pin:
    OPEN_DRAIN = 7  # type: int
    OUT = 3  # type: int
    IRQ_RISING = 1  # type: int
    WAKE_LOW = 4  # type: int
    WAKE_HIGH = 5  # type: int
    PULL_DOWN = 1  # type: int
    PULL_UP = 2  # type: int
    DRIVE_1 = 1  # type: int
    IRQ_FALLING = 2  # type: int
    DRIVE_0 = 0  # type: int
    IN = 1  # type: int
    DRIVE_2 = 2  # type: int
    DRIVE_3 = 3  # type: int

    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def on(self, *args, **kwargs) -> Incomplete:
        ...

    def off(self, *args, **kwargs) -> Incomplete:
        ...

    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    class board:
        def __init__(self, *argv, **kwargs) -> None:
            ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


mem8: Incomplete  ## <class 'mem'> = <8-bit memory>
mem32: Incomplete  ## <class 'mem'> = <32-bit memory>
mem16: Incomplete  ## <class 'mem'> = <16-bit memory>


class I2S:
    RX = 9  # type: int
    MONO = 0  # type: int
    STEREO = 1  # type: int
    TX = 5  # type: int

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


class ADC:
    ATTN_2_5DB = 1  # type: int
    WIDTH_12BIT = 12  # type: int
    ATTN_6DB = 2  # type: int
    ATTN_11DB = 3  # type: int
    ATTN_0DB = 0  # type: int

    def read_u16(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def read_uv(self, *args, **kwargs) -> Incomplete:
        ...

    def width(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def block(self, *args, **kwargs) -> Incomplete:
        ...

    def atten(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADCBlock:
    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def connect(self, *args, **kwargs) -> Incomplete:
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


class WDT:
    def feed(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SoftSPI:
    LSB = 1  # type: int
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


class Timer:
    ONE_SHOT = 0  # type: int
    PERIODIC = 1  # type: int

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class TouchPad:
    def config(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class UART:
    INV_CTS = 8  # type: int
    CTS = 2  # type: int
    INV_TX = 32  # type: int
    INV_RTS = 64  # type: int
    INV_RX = 4  # type: int
    RTS = 1  # type: int

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


class RTC:
    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def memory(self, *args, **kwargs) -> Incomplete:
        ...

    def datetime(self, *args, **kwargs) -> Incomplete:
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


class SDCard:
    def ioctl(self, *args, **kwargs) -> Incomplete:
        ...

    def readblocks(self, *args, **kwargs) -> Incomplete:
        ...

    def writeblocks(self, *args, **kwargs) -> Incomplete:
        ...

    def info(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SPI:
    LSB = 1  # type: int
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


class Signal:
    def off(self, *args, **kwargs) -> Incomplete:
        ...

    def on(self, *args, **kwargs) -> Incomplete:
        ...

    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
