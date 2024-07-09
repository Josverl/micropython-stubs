"""
Module: 'umachine' on micropython-v1.22.2-rp2-RPI_PICO
"""

# MCU: {'build': '', 'ver': '1.22.2', 'version': '1.22.2', 'port': 'rp2', 'board': 'RPI_PICO', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.23.0
from __future__ import annotations
from _typeshed import Incomplete

WDT_RESET: int = 3
PWRON_RESET: int = 1

def dht_readinto(*args, **kwargs) -> Incomplete: ...
def enable_irq(*args, **kwargs) -> Incomplete: ...
def disable_irq(*args, **kwargs) -> Incomplete: ...
def bitstream(*args, **kwargs) -> Incomplete: ...
def deepsleep(*args, **kwargs) -> Incomplete: ...
def bootloader(*args, **kwargs) -> Incomplete: ...
def soft_reset(*args, **kwargs) -> Incomplete: ...
def reset(*args, **kwargs) -> Incomplete: ...
def freq(*args, **kwargs) -> Incomplete: ...
def reset_cause(*args, **kwargs) -> Incomplete: ...
def idle(*args, **kwargs) -> Incomplete: ...
def time_pulse_us(*args, **kwargs) -> Incomplete: ...
def lightsleep(*args, **kwargs) -> Incomplete: ...
def unique_id(*args, **kwargs) -> Incomplete: ...

class WDT:
    def feed(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

mem8: Incomplete  ## <class 'mem'> = <8-bit memory>
mem32: Incomplete  ## <class 'mem'> = <32-bit memory>
mem16: Incomplete  ## <class 'mem'> = <16-bit memory>

class PWM:
    def duty_u16(self, *args, **kwargs) -> Incomplete: ...
    def freq(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def duty_ns(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class ADC:
    CORE_TEMP: int = 4
    def read_u16(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class I2C:
    def readfrom_mem_into(self, *args, **kwargs) -> Incomplete: ...
    def readfrom_into(self, *args, **kwargs) -> Incomplete: ...
    def readfrom_mem(self, *args, **kwargs) -> Incomplete: ...
    def writeto_mem(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def writeto(self, *args, **kwargs) -> Incomplete: ...
    def writevto(self, *args, **kwargs) -> Incomplete: ...
    def start(self, *args, **kwargs) -> Incomplete: ...
    def readfrom(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def stop(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class I2S:
    RX: int = 0
    MONO: int = 0
    STEREO: int = 1
    TX: int = 1
    def shift(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Pin:
    ALT_SPI: int = 1
    IN: int = 0
    ALT_USB: int = 9
    ALT_UART: int = 2
    IRQ_FALLING: int = 4
    OUT: int = 1
    OPEN_DRAIN: int = 2
    IRQ_RISING: int = 8
    PULL_DOWN: int = 2
    ALT_SIO: int = 5
    ALT_GPCK: int = 8
    ALT: int = 3
    PULL_UP: int = 1
    ALT_I2C: int = 3
    ALT_PWM: int = 4
    ALT_PIO1: int = 7
    ALT_PIO0: int = 6
    def low(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def toggle(self, *args, **kwargs) -> Incomplete: ...
    def off(self, *args, **kwargs) -> Incomplete: ...
    def on(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def value(self, *args, **kwargs) -> Incomplete: ...
    def high(self, *args, **kwargs) -> Incomplete: ...

    class cpu:
        GPIO26: Pin  ## = Pin(GPIO26, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO25: Pin  ## = Pin(GPIO25, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO27: Pin  ## = Pin(GPIO27, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO28: Pin  ## = Pin(GPIO28, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO22: Pin  ## = Pin(GPIO22, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO24: Pin  ## = Pin(GPIO24, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO23: Pin  ## = Pin(GPIO23, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO9: Pin  ## = Pin(GPIO9, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO7: Pin  ## = Pin(GPIO7, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO6: Pin  ## = Pin(GPIO6, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO8: Pin  ## = Pin(GPIO8, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO29: Pin  ## = Pin(GPIO29, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO3: Pin  ## = Pin(GPIO3, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO5: Pin  ## = Pin(GPIO5, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO4: Pin  ## = Pin(GPIO4, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO12: Pin  ## = Pin(GPIO12, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO11: Pin  ## = Pin(GPIO11, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO13: Pin  ## = Pin(GPIO13, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO14: Pin  ## = Pin(GPIO14, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO0: Pin  ## = Pin(GPIO0, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO10: Pin  ## = Pin(GPIO10, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO1: Pin  ## = Pin(GPIO1, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO21: Pin  ## = Pin(GPIO21, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO2: Pin  ## = Pin(GPIO2, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO19: Pin  ## = Pin(GPIO19, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO20: Pin  ## = Pin(GPIO20, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO15: Pin  ## = Pin(GPIO15, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO16: Pin  ## = Pin(GPIO16, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO18: Pin  ## = Pin(GPIO18, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO17: Pin  ## = Pin(GPIO17, mode=ALT, pull=PULL_DOWN, alt=31)
        def __init__(self, *argv, **kwargs) -> None: ...

    class board:
        GP27: Pin  ## = Pin(GPIO27, mode=ALT, pull=PULL_DOWN, alt=31)
        GP26: Pin  ## = Pin(GPIO26, mode=ALT, pull=PULL_DOWN, alt=31)
        GP28: Pin  ## = Pin(GPIO28, mode=ALT, pull=PULL_DOWN, alt=31)
        LED: Pin  ## = Pin(GPIO25, mode=ALT, pull=PULL_DOWN, alt=31)
        GP21: Pin  ## = Pin(GPIO21, mode=ALT, pull=PULL_DOWN, alt=31)
        GP25: Pin  ## = Pin(GPIO25, mode=ALT, pull=PULL_DOWN, alt=31)
        GP22: Pin  ## = Pin(GPIO22, mode=ALT, pull=PULL_DOWN, alt=31)
        GP8: Pin  ## = Pin(GPIO8, mode=ALT, pull=PULL_DOWN, alt=31)
        GP7: Pin  ## = Pin(GPIO7, mode=ALT, pull=PULL_DOWN, alt=31)
        GP9: Pin  ## = Pin(GPIO9, mode=ALT, pull=PULL_DOWN, alt=31)
        GP3: Pin  ## = Pin(GPIO3, mode=ALT, pull=PULL_DOWN, alt=31)
        GP4: Pin  ## = Pin(GPIO4, mode=ALT, pull=PULL_DOWN, alt=31)
        GP6: Pin  ## = Pin(GPIO6, mode=ALT, pull=PULL_DOWN, alt=31)
        GP5: Pin  ## = Pin(GPIO5, mode=ALT, pull=PULL_DOWN, alt=31)
        GP12: Pin  ## = Pin(GPIO12, mode=ALT, pull=PULL_DOWN, alt=31)
        GP11: Pin  ## = Pin(GPIO11, mode=ALT, pull=PULL_DOWN, alt=31)
        GP13: Pin  ## = Pin(GPIO13, mode=ALT, pull=PULL_DOWN, alt=31)
        GP20: Pin  ## = Pin(GPIO20, mode=ALT, pull=PULL_DOWN, alt=31)
        GP0: Pin  ## = Pin(GPIO0, mode=ALT, pull=PULL_DOWN, alt=31)
        GP10: Pin  ## = Pin(GPIO10, mode=ALT, pull=PULL_DOWN, alt=31)
        GP1: Pin  ## = Pin(GPIO1, mode=ALT, pull=PULL_DOWN, alt=31)
        GP19: Pin  ## = Pin(GPIO19, mode=ALT, pull=PULL_DOWN, alt=31)
        GP18: Pin  ## = Pin(GPIO18, mode=ALT, pull=PULL_DOWN, alt=31)
        GP2: Pin  ## = Pin(GPIO2, mode=ALT, pull=PULL_DOWN, alt=31)
        GP14: Pin  ## = Pin(GPIO14, mode=ALT, pull=PULL_DOWN, alt=31)
        GP15: Pin  ## = Pin(GPIO15, mode=ALT, pull=PULL_DOWN, alt=31)
        GP17: Pin  ## = Pin(GPIO17, mode=ALT, pull=PULL_DOWN, alt=31)
        GP16: Pin  ## = Pin(GPIO16, mode=ALT, pull=PULL_DOWN, alt=31)
        def __init__(self, *argv, **kwargs) -> None: ...

    def __init__(self, *argv, **kwargs) -> None: ...

class SoftSPI:
    LSB: int = 0
    MSB: int = 1
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def write_readinto(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Timer:
    PERIODIC: int = 1
    ONE_SHOT: int = 0
    def init(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class UART:
    INV_TX: int = 1
    RTS: int = 2
    CTS: int = 1
    INV_RX: int = 2
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def sendbreak(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def flush(self, *args, **kwargs) -> Incomplete: ...
    def txdone(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def any(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class SoftI2C:
    def readfrom_mem_into(self, *args, **kwargs) -> Incomplete: ...
    def readfrom_into(self, *args, **kwargs) -> Incomplete: ...
    def readfrom_mem(self, *args, **kwargs) -> Incomplete: ...
    def writeto_mem(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def writeto(self, *args, **kwargs) -> Incomplete: ...
    def writevto(self, *args, **kwargs) -> Incomplete: ...
    def start(self, *args, **kwargs) -> Incomplete: ...
    def readfrom(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def stop(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class RTC:
    def datetime(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class SPI:
    LSB: int = 0
    MSB: int = 1
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def write_readinto(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Signal:
    def off(self, *args, **kwargs) -> Incomplete: ...
    def on(self, *args, **kwargs) -> Incomplete: ...
    def value(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
