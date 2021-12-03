from typing import Any

class ADC:
    ATTN_0DB: int
    ATTN_11DB: int
    ATTN_2_5DB: int
    ATTN_6DB: int
    WIDTH_10BIT: int
    WIDTH_11BIT: int
    WIDTH_12BIT: int
    WIDTH_9BIT: int
    def atten() -> None: ...
    def read() -> None: ...
    def read_u16() -> None: ...
    def width() -> None: ...

class DAC:
    def write() -> None: ...

DEEPSLEEP: int
DEEPSLEEP_RESET: int
EXT0_WAKE: int
EXT1_WAKE: int
HARD_RESET: int

class I2C:
    def init() -> None: ...
    def readfrom() -> None: ...
    def readfrom_into() -> None: ...
    def readfrom_mem() -> None: ...
    def readfrom_mem_into() -> None: ...
    def readinto() -> None: ...
    def scan() -> None: ...
    def start() -> None: ...
    def stop() -> None: ...
    def write() -> None: ...
    def writeto() -> None: ...
    def writeto_mem() -> None: ...
    def writevto() -> None: ...

PIN_WAKE: int

class PWM:
    def deinit() -> None: ...
    def duty() -> None: ...
    def freq() -> None: ...
    def init() -> None: ...

PWRON_RESET: int

class Pin:
    IN: int
    IRQ_FALLING: int
    IRQ_RISING: int
    OPEN_DRAIN: int
    OUT: int
    PULL_DOWN: int
    PULL_HOLD: int
    PULL_UP: int
    WAKE_HIGH: int
    WAKE_LOW: int
    def init() -> None: ...
    def irq() -> None: ...
    def off() -> None: ...
    def on() -> None: ...
    def value() -> None: ...

class RTC:
    def datetime() -> None: ...
    def init() -> None: ...
    def memory() -> None: ...

class SDCard:
    def deinit() -> None: ...
    def info() -> None: ...
    def ioctl() -> None: ...
    def readblocks() -> None: ...
    def writeblocks() -> None: ...

SLEEP: int
SOFT_RESET: int

class SPI:
    LSB: int
    MSB: int
    def deinit() -> None: ...
    def init() -> None: ...
    def read() -> None: ...
    def readinto() -> None: ...
    def write() -> None: ...
    def write_readinto() -> None: ...

class Signal:
    def off() -> None: ...
    def on() -> None: ...
    def value() -> None: ...

class SoftI2C:
    def init() -> None: ...
    def readfrom() -> None: ...
    def readfrom_into() -> None: ...
    def readfrom_mem() -> None: ...
    def readfrom_mem_into() -> None: ...
    def readinto() -> None: ...
    def scan() -> None: ...
    def start() -> None: ...
    def stop() -> None: ...
    def write() -> None: ...
    def writeto() -> None: ...
    def writeto_mem() -> None: ...
    def writevto() -> None: ...

class SoftSPI:
    LSB: int
    MSB: int
    def deinit() -> None: ...
    def init() -> None: ...
    def read() -> None: ...
    def readinto() -> None: ...
    def write() -> None: ...
    def write_readinto() -> None: ...

TIMER_WAKE: int
TOUCHPAD_WAKE: int

class Timer:
    ONE_SHOT: int
    PERIODIC: int
    def deinit() -> None: ...
    def init() -> None: ...
    def value() -> None: ...

class TouchPad:
    def config() -> None: ...
    def read() -> None: ...

class UART:
    INV_CTS: int
    INV_RTS: int
    INV_RX: int
    INV_TX: int
    def any() -> None: ...
    def deinit() -> None: ...
    def init() -> None: ...
    def read() -> None: ...
    def readinto() -> None: ...
    def readline() -> None: ...
    def sendbreak() -> None: ...
    def write() -> None: ...

ULP_WAKE: int

class WDT:
    def feed() -> None: ...

WDT_RESET: int

def deepsleep() -> None: ...
def disable_irq() -> None: ...
def enable_irq() -> None: ...
def freq() -> None: ...
def idle() -> None: ...
def lightsleep() -> None: ...

mem16: Any
mem32: Any
mem8: Any

def reset() -> None: ...
def reset_cause() -> None: ...
def sleep() -> None: ...
def soft_reset() -> None: ...
def time_pulse_us() -> None: ...
def unique_id() -> None: ...
def wake_reason() -> None: ...
