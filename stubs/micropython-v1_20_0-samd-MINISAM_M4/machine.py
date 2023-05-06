"""
Module: 'machine' on micropython-v1.20.0-samd-MINISAM_M4
"""
# MCU: OrderedDict({'build': '', 'ver': 'v1.20.0', 'version': '1.20.0', 'port': 'samd', 'board': 'MINISAM_M4', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51G19A', 'arch': 'armv7emsp'})
# Stubber: v1.13.7
from typing import Any

PWRON_RESET = 1  # type: int
HARD_RESET = 16  # type: int
SOFT_RESET = 64  # type: int
WDT_RESET = 32  # type: int
DEEPSLEEP_RESET = 128  # type: int


def disable_irq(*args, **kwargs) -> Any:
    ...


def reset_cause(*args, **kwargs) -> Any:
    ...


def enable_irq(*args, **kwargs) -> Any:
    ...


def bitstream(*args, **kwargs) -> Any:
    ...


def dht_readinto(*args, **kwargs) -> Any:
    ...


def bootloader(*args, **kwargs) -> Any:
    ...


def soft_reset(*args, **kwargs) -> Any:
    ...


def freq(*args, **kwargs) -> Any:
    ...


def reset(*args, **kwargs) -> Any:
    ...


def time_pulse_us(*args, **kwargs) -> Any:
    ...


def lightsleep(*args, **kwargs) -> Any:
    ...


def idle(*args, **kwargs) -> Any:
    ...


def unique_id(*args, **kwargs) -> Any:
    ...


class WDT:
    def timeout_ms(self, *args, **kwargs) -> Any:
        ...

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
    def read_u16(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class DAC:
    def write(self, *args, **kwargs) -> Any:
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


class Pin:
    OUT = 1  # type: int
    OPEN_DRAIN = 2  # type: int
    LOW_POWER = 0  # type: int
    PULL_DOWN = 2  # type: int
    PULL_OFF = 0  # type: int
    PULL_UP = 1  # type: int
    IRQ_RISING = 1  # type: int
    HIGH_POWER = 1  # type: int
    IN = 0  # type: int
    IRQ_FALLING = 2  # type: int

    def irq(self, *args, **kwargs) -> Any:
        ...

    def toggle(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def on(self, *args, **kwargs) -> Any:
        ...

    def low(self, *args, **kwargs) -> Any:
        ...

    def off(self, *args, **kwargs) -> Any:
        ...

    def high(self, *args, **kwargs) -> Any:
        ...

    def value(self, *args, **kwargs) -> Any:
        ...

    def disable(self, *args, **kwargs) -> Any:
        ...

    def drive(self, *args, **kwargs) -> Any:
        ...

    class board:
        LED: Any  ## <class 'Pin'> = Pin("LED", mode=OUT, pull=PULL_OFF, GPIO=PA15)
        MOSI: Any  ## <class 'Pin'> = Pin("MOSI", mode=IN, pull=PULL_OFF, GPIO=PB22)
        MISO: Any  ## <class 'Pin'> = Pin("MISO", mode=IN, pull=PULL_OFF, GPIO=PB23)
        D5: Any  ## <class 'Pin'> = Pin("D5", mode=IN, pull=PULL_OFF, GPIO=PA21)
        DOTSTAR_DATA: Any  ## <class 'Pin'> = Pin("DOTSTAR_DATA", mode=IN, pull=PULL_OFF, GPIO=PB03)
        DOTSTAR_CLK: Any  ## <class 'Pin'> = Pin("DOTSTAR_CLK", mode=IN, pull=PULL_OFF, GPIO=PB02)
        USB_DP: Any  ## <class 'Pin'> = Pin("USB_DP", mode=OUT, pull=PULL_OFF, GPIO=PA25)
        SWDIO: Any  ## <class 'Pin'> = Pin("SWDIO", mode=IN, pull=PULL_OFF, GPIO=PA31)
        SCK: Any  ## <class 'Pin'> = Pin("SCK", mode=IN, pull=PULL_OFF, GPIO=PA01)
        USB_DM: Any  ## <class 'Pin'> = Pin("USB_DM", mode=OUT, pull=PULL_OFF, GPIO=PA24)
        SCL: Any  ## <class 'Pin'> = Pin("SCL", mode=IN, pull=PULL_OFF, GPIO=PA13)
        SWCLK: Any  ## <class 'Pin'> = Pin("SWCLK", mode=IN, pull=PULL_OFF, GPIO=PA30)
        SDA: Any  ## <class 'Pin'> = Pin("SDA", mode=IN, pull=PULL_OFF, GPIO=PA12)
        A3_D12: Any  ## <class 'Pin'> = Pin("A3_D12", mode=IN, pull=PULL_OFF, GPIO=PA04)
        A5: Any  ## <class 'Pin'> = Pin("A5", mode=IN, pull=PULL_OFF, GPIO=PA06)
        A4_D13: Any  ## <class 'Pin'> = Pin("A4_D13", mode=IN, pull=PULL_OFF, GPIO=PA05)
        A0_D9: Any  ## <class 'Pin'> = Pin("A0_D9", mode=IN, pull=PULL_OFF, GPIO=PA02)
        A2_D11: Any  ## <class 'Pin'> = Pin("A2_D11", mode=IN, pull=PULL_OFF, GPIO=PB09)
        A1_D10: Any  ## <class 'Pin'> = Pin("A1_D10", mode=IN, pull=PULL_OFF, GPIO=PB08)
        D4: Any  ## <class 'Pin'> = Pin("D4", mode=IN, pull=PULL_OFF, GPIO=PA20)
        D1: Any  ## <class 'Pin'> = Pin("D1", mode=IN, pull=PULL_OFF, GPIO=PA17)
        A6_D2: Any  ## <class 'Pin'> = Pin("A6_D2", mode=IN, pull=PULL_OFF, GPIO=PA07)
        D3: Any  ## <class 'Pin'> = Pin("D3", mode=IN, pull=PULL_OFF, GPIO=PA19)
        AREF: Any  ## <class 'Pin'> = Pin("AREF", mode=IN, pull=PULL_OFF, GPIO=PA03)
        D0: Any  ## <class 'Pin'> = Pin("D0", mode=IN, pull=PULL_OFF, GPIO=PA16)
        BUTTON: Any  ## <class 'Pin'> = Pin("BUTTON", mode=IN, pull=PULL_OFF, GPIO=PA00)

        def __init__(self, *argv, **kwargs) -> None:
            ...

    class cpu:
        PA23: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA23)
        PA24: Any  ## <class 'Pin'> = Pin("USB_DM", mode=OUT, pull=PULL_OFF, GPIO=PA24)
        PA25: Any  ## <class 'Pin'> = Pin("USB_DP", mode=OUT, pull=PULL_OFF, GPIO=PA25)
        PA27: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA27)
        PA18: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA18)
        PA22: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA22)
        PA19: Any  ## <class 'Pin'> = Pin("D3", mode=IN, pull=PULL_OFF, GPIO=PA19)
        PA20: Any  ## <class 'Pin'> = Pin("D4", mode=IN, pull=PULL_OFF, GPIO=PA20)
        PA21: Any  ## <class 'Pin'> = Pin("D5", mode=IN, pull=PULL_OFF, GPIO=PA21)
        PB09: Any  ## <class 'Pin'> = Pin("A2_D11", mode=IN, pull=PULL_OFF, GPIO=PB09)
        PB10: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB10)
        PB11: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB11)
        PB22: Any  ## <class 'Pin'> = Pin("MOSI", mode=IN, pull=PULL_OFF, GPIO=PB22)
        PA30: Any  ## <class 'Pin'> = Pin("SWCLK", mode=IN, pull=PULL_OFF, GPIO=PA30)
        PB08: Any  ## <class 'Pin'> = Pin("A1_D10", mode=IN, pull=PULL_OFF, GPIO=PB08)
        PA31: Any  ## <class 'Pin'> = Pin("SWDIO", mode=IN, pull=PULL_OFF, GPIO=PA31)
        PB02: Any  ## <class 'Pin'> = Pin("DOTSTAR_CLK", mode=IN, pull=PULL_OFF, GPIO=PB02)
        PB03: Any  ## <class 'Pin'> = Pin("DOTSTAR_DATA", mode=IN, pull=PULL_OFF, GPIO=PB03)
        PB23: Any  ## <class 'Pin'> = Pin("MISO", mode=IN, pull=PULL_OFF, GPIO=PB23)
        PA04: Any  ## <class 'Pin'> = Pin("A3_D12", mode=IN, pull=PULL_OFF, GPIO=PA04)
        PA05: Any  ## <class 'Pin'> = Pin("A4_D13", mode=IN, pull=PULL_OFF, GPIO=PA05)
        PA06: Any  ## <class 'Pin'> = Pin("A5", mode=IN, pull=PULL_OFF, GPIO=PA06)
        PA07: Any  ## <class 'Pin'> = Pin("A6_D2", mode=IN, pull=PULL_OFF, GPIO=PA07)
        PA17: Any  ## <class 'Pin'> = Pin("D1", mode=IN, pull=PULL_OFF, GPIO=PA17)
        PA03: Any  ## <class 'Pin'> = Pin("AREF", mode=IN, pull=PULL_OFF, GPIO=PA03)
        PA00: Any  ## <class 'Pin'> = Pin("BUTTON", mode=IN, pull=PULL_OFF, GPIO=PA00)
        PA01: Any  ## <class 'Pin'> = Pin("SCK", mode=IN, pull=PULL_OFF, GPIO=PA01)
        PA02: Any  ## <class 'Pin'> = Pin("A0_D9", mode=IN, pull=PULL_OFF, GPIO=PA02)
        PA13: Any  ## <class 'Pin'> = Pin("SCL", mode=IN, pull=PULL_OFF, GPIO=PA13)
        PA14: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA14)
        PA15: Any  ## <class 'Pin'> = Pin("LED", mode=OUT, pull=PULL_OFF, GPIO=PA15)
        PA16: Any  ## <class 'Pin'> = Pin("D0", mode=IN, pull=PULL_OFF, GPIO=PA16)
        PA08: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA08)
        PA12: Any  ## <class 'Pin'> = Pin("SDA", mode=IN, pull=PULL_OFF, GPIO=PA12)
        PA09: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA09)
        PA10: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA10)
        PA11: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA11)

        def __init__(self, *argv, **kwargs) -> None:
            ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SoftSPI:
    LSB = 1  # type: int
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


class Timer:
    PERIODIC = 2  # type: int
    ONE_SHOT = 1  # type: int

    def init(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class UART:
    def flush(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def txdone(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def sendbreak(self, *args, **kwargs) -> Any:
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

    def init(self, *args, **kwargs) -> Any:
        ...

    def calibration(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SPI:
    LSB = 1  # type: int
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


class Signal:
    def off(self, *args, **kwargs) -> Any:
        ...

    def on(self, *args, **kwargs) -> Any:
        ...

    def value(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
