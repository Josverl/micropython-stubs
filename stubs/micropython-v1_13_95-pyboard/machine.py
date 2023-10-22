"""
Module: 'machine' on pyboard 1.13.0-95
"""
# MCU: (sysname='pyboard', nodename='pyboard', release='1.13.0', version='v1.13-95-g0fff2e03f on 2020-10-03', machine='PYBv1.1 with STM32F405RG')
# Stubber: 1.3.4 - updated
from typing import Any


class ADC:
    """"""

    CORE_TEMP = 16
    CORE_VBAT = 18
    CORE_VREF = 17
    VREF = 65535

    def read_u16(self, *args) -> Any:
        pass


DEEPSLEEP_RESET = 4
HARD_RESET = 2


class I2C:
    """"""

    def init(self, *args) -> Any:
        pass

    def readfrom(self, *args) -> Any:
        pass

    def readfrom_into(self, *args) -> Any:
        pass

    def readfrom_mem(self, *args) -> Any:
        pass

    def readfrom_mem_into(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def scan(self, *args) -> Any:
        pass

    def start(self, *args) -> Any:
        pass

    def stop(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass

    def writeto(self, *args) -> Any:
        pass

    def writeto_mem(self, *args) -> Any:
        pass

    def writevto(self, *args) -> Any:
        pass


PWRON_RESET = 1


class Pin:
    """"""

    AF1_TIM1 = 1
    AF1_TIM2 = 1
    AF2_TIM3 = 2
    AF2_TIM4 = 2
    AF2_TIM5 = 2
    AF3_TIM10 = 3
    AF3_TIM11 = 3
    AF3_TIM8 = 3
    AF3_TIM9 = 3
    AF4_I2C1 = 4
    AF4_I2C2 = 4
    AF5_SPI1 = 5
    AF5_SPI2 = 5
    AF7_USART1 = 7
    AF7_USART2 = 7
    AF7_USART3 = 7
    AF8_UART4 = 8
    AF8_USART6 = 8
    AF9_CAN1 = 9
    AF9_CAN2 = 9
    AF9_TIM12 = 9
    AF9_TIM13 = 9
    AF9_TIM14 = 9
    AF_OD = 18
    AF_PP = 2
    ALT = 2
    ALT_OPEN_DRAIN = 18
    ANALOG = 3
    IN = 0
    IRQ_FALLING = 270598144
    IRQ_RISING = 269549568
    OPEN_DRAIN = 17
    OUT = 1
    OUT_OD = 17
    OUT_PP = 1
    PULL_DOWN = 2
    PULL_NONE = 0
    PULL_UP = 1

    def af(self, *args) -> Any:
        pass

    def af_list(self, *args) -> Any:
        pass

    board = None
    cpu = None

    def debug(self, *args) -> Any:
        pass

    def dict(self, *args) -> Any:
        pass

    def gpio(self, *args) -> Any:
        pass

    def high(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def irq(self, *args) -> Any:
        pass

    def low(self, *args) -> Any:
        pass

    def mapper(self, *args) -> Any:
        pass

    def mode(self, *args) -> Any:
        pass

    def name(self, *args) -> Any:
        pass

    def names(self, *args) -> Any:
        pass

    def off(self, *args) -> Any:
        pass

    def on(self, *args) -> Any:
        pass

    def pin(self, *args) -> Any:
        pass

    def port(self, *args) -> Any:
        pass

    def pull(self, *args) -> Any:
        pass

    def value(self, *args) -> Any:
        pass


class RTC:
    """"""

    def calibration(self, *args) -> Any:
        pass

    def datetime(self, *args) -> Any:
        pass

    def info(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def wakeup(self, *args) -> Any:
        pass


SOFT_RESET = 0


class SPI:
    """"""

    LSB = 128
    MSB = 0

    def deinit(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass

    def write_readinto(self, *args) -> Any:
        pass


class Signal:
    """"""

    def off(self, *args) -> Any:
        pass

    def on(self, *args) -> Any:
        pass

    def value(self, *args) -> Any:
        pass


class SoftI2C:
    """"""

    def init(self, *args) -> Any:
        pass

    def readfrom(self, *args) -> Any:
        pass

    def readfrom_into(self, *args) -> Any:
        pass

    def readfrom_mem(self, *args) -> Any:
        pass

    def readfrom_mem_into(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def scan(self, *args) -> Any:
        pass

    def start(self, *args) -> Any:
        pass

    def stop(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass

    def writeto(self, *args) -> Any:
        pass

    def writeto_mem(self, *args) -> Any:
        pass

    def writevto(self, *args) -> Any:
        pass


class SoftSPI:
    """"""

    LSB = 128
    MSB = 0

    def deinit(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass

    def write_readinto(self, *args) -> Any:
        pass


class Timer:
    """"""

    ONE_SHOT = 1
    PERIODIC = 2

    def deinit(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass


class UART:
    """"""

    CTS = 512
    IRQ_RXIDLE = 16
    RTS = 256

    def any(self, *args) -> Any:
        pass

    def deinit(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def irq(self, *args) -> Any:
        pass

    def read(self, *args) -> Any:
        pass

    def readchar(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def readline(self, *args) -> Any:
        pass

    def sendbreak(self, *args) -> Any:
        pass

    def write(self, *args) -> Any:
        pass

    def writechar(self, *args) -> Any:
        pass


class WDT:
    """"""

    def feed(self, *args) -> Any:
        pass


WDT_RESET = 3


def bootloader(*args) -> Any:
    pass


def deepsleep(*args) -> Any:
    pass


def disable_irq(*args) -> Any:
    pass


def enable_irq(*args) -> Any:
    pass


def freq(*args) -> Any:
    pass


def idle(*args) -> Any:
    pass


def info(*args) -> Any:
    pass


def lightsleep(*args) -> Any:
    pass


mem16 = None
mem32 = None
mem8 = None


def reset(*args) -> Any:
    pass


def reset_cause(*args) -> Any:
    pass


def rng(*args) -> Any:
    pass


def sleep(*args) -> Any:
    pass


def soft_reset(*args) -> Any:
    pass


def time_pulse_us(*args) -> Any:
    pass


def unique_id(*args) -> Any:
    pass
