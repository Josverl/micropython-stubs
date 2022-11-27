from typing import Any

DEEPSLEEP_RESET: int
HARD_RESET: int

class I2C:
    def __init__(self, *argv, **kwargs) -> None: ...
    def init(self, *args, **kwargs) -> Any: ...
    def readfrom(self, *args, **kwargs) -> Any: ...
    def readfrom_into(self, *args, **kwargs) -> Any: ...
    def readfrom_mem(self, *args, **kwargs) -> Any: ...
    def readfrom_mem_into(self, *args, **kwargs) -> Any: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def scan(self, *args, **kwargs) -> Any: ...
    def start(self, *args, **kwargs) -> Any: ...
    def stop(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def writeto(self, *args, **kwargs) -> Any: ...
    def writeto_mem(self, *args, **kwargs) -> Any: ...

PWRON_RESET: int

class Pin:
    def __init__(self, *argv, **kwargs) -> None: ...
    AF1_TIM1: int
    AF1_TIM2: int
    AF2_TIM3: int
    AF2_TIM4: int
    AF2_TIM5: int
    AF3_TIM10: int
    AF3_TIM11: int
    AF3_TIM8: int
    AF3_TIM9: int
    AF4_I2C1: int
    AF4_I2C2: int
    AF5_SPI1: int
    AF5_SPI2: int
    AF7_USART1: int
    AF7_USART2: int
    AF7_USART3: int
    AF8_UART4: int
    AF8_USART6: int
    AF9_CAN1: int
    AF9_CAN2: int
    AF9_TIM12: int
    AF9_TIM13: int
    AF9_TIM14: int
    AF_OD: int
    AF_PP: int
    ALT: int
    ALT_OPEN_DRAIN: int
    ANALOG: int
    IN: int
    IRQ_FALLING: int
    IRQ_RISING: int
    OPEN_DRAIN: int
    OUT: int
    OUT_OD: int
    OUT_PP: int
    PULL_DOWN: int
    PULL_NONE: int
    PULL_UP: int
    def af(self, *args, **kwargs) -> Any: ...
    def af_list(self, *args, **kwargs) -> Any: ...

    class board:
        def __init__(self, *argv, **kwargs) -> None: ...
        LED_BLUE: Any
        LED_GREEN: Any
        LED_RED: Any
        LED_YELLOW: Any
        MMA_AVDD: Any
        MMA_INT: Any
        SD: Any
        SD_CK: Any
        SD_CMD: Any
        SD_D0: Any
        SD_D1: Any
        SD_D2: Any
        SD_D3: Any
        SD_SW: Any
        SW: Any
        USB_DM: Any
        USB_DP: Any
        USB_ID: Any
        USB_VBUS: Any
        X1: Any
        X10: Any
        X11: Any
        X12: Any
        X17: Any
        X18: Any
        X19: Any
        X2: Any
        X20: Any
        X21: Any
        X22: Any
        X3: Any
        X4: Any
        X5: Any
        X6: Any
        X7: Any
        X8: Any
        X9: Any
        Y1: Any
        Y10: Any
        Y11: Any
        Y12: Any
        Y2: Any
        Y3: Any
        Y4: Any
        Y5: Any
        Y6: Any
        Y7: Any
        Y8: Any
        Y9: Any

    class cpu:
        def __init__(self, *argv, **kwargs) -> None: ...
        A0: Any
        A1: Any
        A10: Any
        A11: Any
        A12: Any
        A13: Any
        A14: Any
        A15: Any
        A2: Any
        A3: Any
        A4: Any
        A5: Any
        A6: Any
        A7: Any
        A8: Any
        A9: Any
        B0: Any
        B1: Any
        B10: Any
        B11: Any
        B12: Any
        B13: Any
        B14: Any
        B15: Any
        B2: Any
        B3: Any
        B4: Any
        B5: Any
        B6: Any
        B7: Any
        B8: Any
        B9: Any
        C0: Any
        C1: Any
        C10: Any
        C11: Any
        C12: Any
        C13: Any
        C2: Any
        C3: Any
        C4: Any
        C5: Any
        C6: Any
        C7: Any
        C8: Any
        C9: Any
        D2: Any
    @classmethod
    def debug(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def dict(cls, *args, **kwargs) -> Any: ...
    def gpio(self, *args, **kwargs) -> Any: ...
    def high(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def irq(self, *args, **kwargs) -> Any: ...
    def low(self, *args, **kwargs) -> Any: ...
    @classmethod
    def mapper(cls, *args, **kwargs) -> Any: ...
    def mode(self, *args, **kwargs) -> Any: ...
    def name(self, *args, **kwargs) -> Any: ...
    def names(self, *args, **kwargs) -> Any: ...
    def off(self, *args, **kwargs) -> Any: ...
    def on(self, *args, **kwargs) -> Any: ...
    def pin(self, *args, **kwargs) -> Any: ...
    def port(self, *args, **kwargs) -> Any: ...
    def pull(self, *args, **kwargs) -> Any: ...
    def value(self, *args, **kwargs) -> Any: ...

SOFT_RESET: int

class SPI:
    def __init__(self, *argv, **kwargs) -> None: ...
    LSB: int
    MSB: int
    def deinit(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def write_readinto(self, *args, **kwargs) -> Any: ...

class Signal:
    def __init__(self, *argv, **kwargs) -> None: ...
    def off(self, *args, **kwargs) -> Any: ...
    def on(self, *args, **kwargs) -> Any: ...
    def value(self, *args, **kwargs) -> Any: ...

class UART:
    def __init__(self, *argv, **kwargs) -> None: ...
    CTS: int
    IRQ_RXIDLE: int
    RTS: int
    def any(self, *args, **kwargs) -> Any: ...
    def deinit(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def irq(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def readchar(self, *args, **kwargs) -> Any: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def readline(self, *args, **kwargs) -> Any: ...
    def sendbreak(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def writechar(self, *args, **kwargs) -> Any: ...

class WDT:
    def __init__(self, *argv, **kwargs) -> None: ...
    def feed(self, *args, **kwargs) -> Any: ...

WDT_RESET: int

def bootloader(*args, **kwargs) -> Any: ...
def deepsleep(*args, **kwargs) -> Any: ...
def disable_irq(*args, **kwargs) -> Any: ...
def enable_irq(*args, **kwargs) -> Any: ...
def freq(*args, **kwargs) -> Any: ...
def idle(*args, **kwargs) -> Any: ...
def info(*args, **kwargs) -> Any: ...

mem16: Any
mem32: Any
mem8: Any

def reset(*args, **kwargs) -> Any: ...
def reset_cause(*args, **kwargs) -> Any: ...
def rng(*args, **kwargs) -> Any: ...
def sleep(*args, **kwargs) -> Any: ...
def soft_reset(*args, **kwargs) -> Any: ...
def time_pulse_us(*args, **kwargs) -> Any: ...
def unique_id(*args, **kwargs) -> Any: ...
