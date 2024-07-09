"""
Module: 'machine' on micropython-v1.22.2-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'build': '', 'ver': '1.22.2', 'version': '1.22.2', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'SAMD51P19A', 'arch': 'armv7emsp'}
# Stubber: v1.23.0
from __future__ import annotations
from _typeshed import Incomplete

PWRON_RESET: int = 1
HARD_RESET: int = 16
SOFT_RESET: int = 64
WDT_RESET: int = 32
DEEPSLEEP_RESET: int = 128

def dht_readinto(*args, **kwargs) -> Incomplete: ...
def enable_irq(*args, **kwargs) -> Incomplete: ...
def disable_irq(*args, **kwargs) -> Incomplete: ...
def bitstream(*args, **kwargs) -> Incomplete: ...
def deepsleep(*args, **kwargs) -> Incomplete: ...
def bootloader(*args, **kwargs) -> Incomplete: ...
def reset_cause(*args, **kwargs) -> Incomplete: ...
def soft_reset(*args, **kwargs) -> Incomplete: ...
def freq(*args, **kwargs) -> Incomplete: ...
def reset(*args, **kwargs) -> Incomplete: ...
def time_pulse_us(*args, **kwargs) -> Incomplete: ...
def lightsleep(*args, **kwargs) -> Incomplete: ...
def idle(*args, **kwargs) -> Incomplete: ...
def unique_id(*args, **kwargs) -> Incomplete: ...

class WDT:
    def timeout_ms(self, *args, **kwargs) -> Incomplete: ...
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
    def read_u16(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class DAC:
    def write(self, *args, **kwargs) -> Incomplete: ...
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

class Pin:
    OUT: int = 1
    OPEN_DRAIN: int = 2
    LOW_POWER: int = 0
    PULL_DOWN: int = 2
    PULL_OFF: int = 0
    PULL_UP: int = 1
    IRQ_RISING: int = 1
    HIGH_POWER: int = 1
    IN: int = 0
    IRQ_FALLING: int = 2
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def toggle(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def on(self, *args, **kwargs) -> Incomplete: ...
    def low(self, *args, **kwargs) -> Incomplete: ...
    def off(self, *args, **kwargs) -> Incomplete: ...
    def high(self, *args, **kwargs) -> Incomplete: ...
    def value(self, *args, **kwargs) -> Incomplete: ...
    def disable(self, *args, **kwargs) -> Incomplete: ...
    def drive(self, *args, **kwargs) -> Incomplete: ...

    class board:
        SDA0: Pin  ## = Pin(Pin.cpu.PA13, mode=IN, pull=PULL_OFF)
        QSPI_SCK: Pin  ## = Pin(Pin.cpu.PB10, mode=IN, pull=PULL_OFF)
        QSPI_D3: Pin  ## = Pin(Pin.cpu.PA11, mode=IN, pull=PULL_OFF)
        QSPI_D2: Pin  ## = Pin(Pin.cpu.PA10, mode=IN, pull=PULL_OFF)
        RX: Pin  ## = Pin(Pin.cpu.PB27, mode=IN, pull=PULL_OFF)
        SCL1: Pin  ## = Pin(Pin.cpu.PA16, mode=IN, pull=PULL_OFF)
        SCL0: Pin  ## = Pin(Pin.cpu.PA12, mode=IN, pull=PULL_OFF)
        SCK: Pin  ## = Pin(Pin.cpu.PB03, mode=IN, pull=PULL_OFF)
        QSPI_D1: Pin  ## = Pin(Pin.cpu.PA09, mode=IN, pull=PULL_OFF)
        MIC: Pin  ## = Pin(Pin.cpu.PC30, mode=IN, pull=PULL_OFF)
        LED_LCD: Pin  ## = Pin(Pin.cpu.PC05, mode=IN, pull=PULL_OFF)
        LED_BLUE: Pin  ## = Pin(Pin.cpu.PA15, mode=OUT, pull=PULL_OFF)
        MISO: Pin  ## = Pin(Pin.cpu.PB00, mode=IN, pull=PULL_OFF)
        QSPI_D0: Pin  ## = Pin(Pin.cpu.PA08, mode=IN, pull=PULL_OFF)
        QSPI_CS: Pin  ## = Pin(Pin.cpu.PB11, mode=IN, pull=PULL_OFF)
        MOSI: Pin  ## = Pin(Pin.cpu.PB02, mode=IN, pull=PULL_OFF)
        LCD_YU: Pin  ## = Pin(Pin.cpu.PC11, mode=IN, pull=PULL_OFF)
        SDA1: Pin  ## = Pin(Pin.cpu.PA17, mode=IN, pull=PULL_OFF)
        SWITCH_Y: Pin  ## = Pin(Pin.cpu.PD09, mode=IN, pull=PULL_OFF)
        SWITCH_X: Pin  ## = Pin(Pin.cpu.PD08, mode=IN, pull=PULL_OFF)
        SWITCH_U: Pin  ## = Pin(Pin.cpu.PD20, mode=IN, pull=PULL_OFF)
        SWITCH_Z: Pin  ## = Pin(Pin.cpu.PD10, mode=IN, pull=PULL_OFF)
        USB_DP: Pin  ## = Pin(Pin.cpu.PA25, mode=OUT, pull=PULL_OFF)
        USB_DM: Pin  ## = Pin(Pin.cpu.PA24, mode=OUT, pull=PULL_OFF)
        TX: Pin  ## = Pin(Pin.cpu.PB26, mode=IN, pull=PULL_OFF)
        SWITCH_B: Pin  ## = Pin(Pin.cpu.PD12, mode=IN, pull=PULL_OFF)
        SD_MISO: Pin  ## = Pin(Pin.cpu.PC18, mode=IN, pull=PULL_OFF)
        SD_DET: Pin  ## = Pin(Pin.cpu.PD21, mode=IN, pull=PULL_OFF)
        SD_CS: Pin  ## = Pin(Pin.cpu.PC19, mode=IN, pull=PULL_OFF)
        SD_MOSI: Pin  ## = Pin(Pin.cpu.PC16, mode=IN, pull=PULL_OFF)
        SWDIO: Pin  ## = Pin(Pin.cpu.PA31, mode=IN, pull=PULL_OFF)
        SWCLK: Pin  ## = Pin(Pin.cpu.PA30, mode=IN, pull=PULL_OFF)
        SD_SCK: Pin  ## = Pin(Pin.cpu.PC17, mode=IN, pull=PULL_OFF)
        USB_SOF: Pin  ## = Pin(Pin.cpu.PA23, mode=IN, pull=PULL_OFF)
        ENABLE_5V: Pin  ## = Pin(Pin.cpu.PC14, mode=IN, pull=PULL_OFF)
        BUTTON_2: Pin  ## = Pin(Pin.cpu.PC27, mode=IN, pull=PULL_OFF)
        BUTTON_1: Pin  ## = Pin(Pin.cpu.PC26, mode=IN, pull=PULL_OFF)
        A8_D8: Pin  ## = Pin(Pin.cpu.PA06, mode=IN, pull=PULL_OFF)
        BUTTON_3: Pin  ## = Pin(Pin.cpu.PC28, mode=IN, pull=PULL_OFF)
        ENABLE_3V3: Pin  ## = Pin(Pin.cpu.PC15, mode=IN, pull=PULL_OFF)
        CS: Pin  ## = Pin(Pin.cpu.PB01, mode=IN, pull=PULL_OFF)
        BUZZER: Pin  ## = Pin(Pin.cpu.PD11, mode=IN, pull=PULL_OFF)
        A7_D7: Pin  ## = Pin(Pin.cpu.PB07, mode=IN, pull=PULL_OFF)
        A2_D2: Pin  ## = Pin(Pin.cpu.PA07, mode=IN, pull=PULL_OFF)
        A1_D1: Pin  ## = Pin(Pin.cpu.PB09, mode=IN, pull=PULL_OFF)
        A0_D0: Pin  ## = Pin(Pin.cpu.PB08, mode=IN, pull=PULL_OFF)
        A3_D3: Pin  ## = Pin(Pin.cpu.PB04, mode=IN, pull=PULL_OFF)
        A6_D6: Pin  ## = Pin(Pin.cpu.PA04, mode=IN, pull=PULL_OFF)
        A5_D5: Pin  ## = Pin(Pin.cpu.PB06, mode=IN, pull=PULL_OFF)
        A4_D4: Pin  ## = Pin(Pin.cpu.PB05, mode=IN, pull=PULL_OFF)
        LCD_YD: Pin  ## = Pin(Pin.cpu.PC13, mode=IN, pull=PULL_OFF)
        GPCLK0: Pin  ## = Pin(Pin.cpu.PB15, mode=IN, pull=PULL_OFF)
        LCD_MOSI: Pin  ## = Pin(Pin.cpu.PB19, mode=IN, pull=PULL_OFF)
        LCD_MISO: Pin  ## = Pin(Pin.cpu.PB18, mode=IN, pull=PULL_OFF)
        LCD_D_C: Pin  ## = Pin(Pin.cpu.PC06, mode=IN, pull=PULL_OFF)
        LCD_RESET: Pin  ## = Pin(Pin.cpu.PC07, mode=IN, pull=PULL_OFF)
        LCD_XR: Pin  ## = Pin(Pin.cpu.PC12, mode=IN, pull=PULL_OFF)
        LCD_XL: Pin  ## = Pin(Pin.cpu.PC10, mode=IN, pull=PULL_OFF)
        LCD_SCK: Pin  ## = Pin(Pin.cpu.PB20, mode=IN, pull=PULL_OFF)
        LCD_CS: Pin  ## = Pin(Pin.cpu.PB21, mode=IN, pull=PULL_OFF)
        I2C_BCLK: Pin  ## = Pin(Pin.cpu.PB16, mode=IN, pull=PULL_OFF)
        GPCLK2: Pin  ## = Pin(Pin.cpu.PB13, mode=IN, pull=PULL_OFF)
        GPCLK1: Pin  ## = Pin(Pin.cpu.PB12, mode=IN, pull=PULL_OFF)
        I2S_LRCLK: Pin  ## = Pin(Pin.cpu.PA20, mode=IN, pull=PULL_OFF)
        LCD_BACKLIGHT: Pin  ## = Pin(Pin.cpu.PC05, mode=IN, pull=PULL_OFF)
        I2S_SDOUT: Pin  ## = Pin(Pin.cpu.PA22, mode=IN, pull=PULL_OFF)
        I2S_SDIN: Pin  ## = Pin(Pin.cpu.PA21, mode=IN, pull=PULL_OFF)
        def __init__(self, *argv, **kwargs) -> None: ...

    class cpu:
        PC04: Pin  ## = Pin(Pin.cpu.PC04, mode=IN, pull=PULL_OFF)
        PC14: Pin  ## = Pin(Pin.cpu.PC14, mode=IN, pull=PULL_OFF)
        PC05: Pin  ## = Pin(Pin.cpu.PC05, mode=IN, pull=PULL_OFF)
        PC01: Pin  ## = Pin(Pin.cpu.PC01, mode=IN, pull=PULL_OFF)
        PC03: Pin  ## = Pin(Pin.cpu.PC03, mode=IN, pull=PULL_OFF)
        PC02: Pin  ## = Pin(Pin.cpu.PC02, mode=IN, pull=PULL_OFF)
        PC12: Pin  ## = Pin(Pin.cpu.PC12, mode=IN, pull=PULL_OFF)
        PC06: Pin  ## = Pin(Pin.cpu.PC06, mode=IN, pull=PULL_OFF)
        PC13: Pin  ## = Pin(Pin.cpu.PC13, mode=IN, pull=PULL_OFF)
        PC07: Pin  ## = Pin(Pin.cpu.PC07, mode=IN, pull=PULL_OFF)
        PC11: Pin  ## = Pin(Pin.cpu.PC11, mode=IN, pull=PULL_OFF)
        PC10: Pin  ## = Pin(Pin.cpu.PC10, mode=IN, pull=PULL_OFF)
        PB24: Pin  ## = Pin(Pin.cpu.PB24, mode=IN, pull=PULL_OFF)
        PC00: Pin  ## = Pin(Pin.cpu.PC00, mode=IN, pull=PULL_OFF)
        PB25: Pin  ## = Pin(Pin.cpu.PB25, mode=IN, pull=PULL_OFF)
        PB21: Pin  ## = Pin(Pin.cpu.PB21, mode=IN, pull=PULL_OFF)
        PB23: Pin  ## = Pin(Pin.cpu.PB23, mode=IN, pull=PULL_OFF)
        PB22: Pin  ## = Pin(Pin.cpu.PB22, mode=IN, pull=PULL_OFF)
        PB30: Pin  ## = Pin(Pin.cpu.PB30, mode=IN, pull=PULL_OFF)
        PB26: Pin  ## = Pin(Pin.cpu.PB26, mode=IN, pull=PULL_OFF)
        PB31: Pin  ## = Pin(Pin.cpu.PB31, mode=IN, pull=PULL_OFF)
        PB27: Pin  ## = Pin(Pin.cpu.PB27, mode=IN, pull=PULL_OFF)
        PB29: Pin  ## = Pin(Pin.cpu.PB29, mode=IN, pull=PULL_OFF)
        PB28: Pin  ## = Pin(Pin.cpu.PB28, mode=IN, pull=PULL_OFF)
        PB20: Pin  ## = Pin(Pin.cpu.PB20, mode=IN, pull=PULL_OFF)
        PD00: Pin  ## = Pin(Pin.cpu.PD00, mode=IN, pull=PULL_OFF)
        PC15: Pin  ## = Pin(Pin.cpu.PC15, mode=IN, pull=PULL_OFF)
        PD01: Pin  ## = Pin(Pin.cpu.PD01, mode=IN, pull=PULL_OFF)
        PC28: Pin  ## = Pin(Pin.cpu.PC28, mode=IN, pull=PULL_OFF)
        PC31: Pin  ## = Pin(Pin.cpu.PC31, mode=IN, pull=PULL_OFF)
        PC30: Pin  ## = Pin(Pin.cpu.PC30, mode=IN, pull=PULL_OFF)
        PD12: Pin  ## = Pin(Pin.cpu.PD12, mode=IN, pull=PULL_OFF)
        PD08: Pin  ## = Pin(Pin.cpu.PD08, mode=IN, pull=PULL_OFF)
        PD20: Pin  ## = Pin(Pin.cpu.PD20, mode=IN, pull=PULL_OFF)
        PD09: Pin  ## = Pin(Pin.cpu.PD09, mode=IN, pull=PULL_OFF)
        PD11: Pin  ## = Pin(Pin.cpu.PD11, mode=IN, pull=PULL_OFF)
        PD10: Pin  ## = Pin(Pin.cpu.PD10, mode=IN, pull=PULL_OFF)
        PC19: Pin  ## = Pin(Pin.cpu.PC19, mode=IN, pull=PULL_OFF)
        PC27: Pin  ## = Pin(Pin.cpu.PC27, mode=IN, pull=PULL_OFF)
        PC20: Pin  ## = Pin(Pin.cpu.PC20, mode=IN, pull=PULL_OFF)
        PC16: Pin  ## = Pin(Pin.cpu.PC16, mode=IN, pull=PULL_OFF)
        PC18: Pin  ## = Pin(Pin.cpu.PC18, mode=IN, pull=PULL_OFF)
        PC17: Pin  ## = Pin(Pin.cpu.PC17, mode=IN, pull=PULL_OFF)
        PC25: Pin  ## = Pin(Pin.cpu.PC25, mode=IN, pull=PULL_OFF)
        PC21: Pin  ## = Pin(Pin.cpu.PC21, mode=IN, pull=PULL_OFF)
        PC26: Pin  ## = Pin(Pin.cpu.PC26, mode=IN, pull=PULL_OFF)
        PC22: Pin  ## = Pin(Pin.cpu.PC22, mode=IN, pull=PULL_OFF)
        PC24: Pin  ## = Pin(Pin.cpu.PC24, mode=IN, pull=PULL_OFF)
        PC23: Pin  ## = Pin(Pin.cpu.PC23, mode=IN, pull=PULL_OFF)
        PD21: Pin  ## = Pin(Pin.cpu.PD21, mode=IN, pull=PULL_OFF)
        PA15: Pin  ## = Pin(Pin.cpu.PA15, mode=OUT, pull=PULL_OFF)
        PA23: Pin  ## = Pin(Pin.cpu.PA23, mode=IN, pull=PULL_OFF)
        PA16: Pin  ## = Pin(Pin.cpu.PA16, mode=IN, pull=PULL_OFF)
        PA12: Pin  ## = Pin(Pin.cpu.PA12, mode=IN, pull=PULL_OFF)
        PA14: Pin  ## = Pin(Pin.cpu.PA14, mode=IN, pull=PULL_OFF)
        PA13: Pin  ## = Pin(Pin.cpu.PA13, mode=IN, pull=PULL_OFF)
        PA21: Pin  ## = Pin(Pin.cpu.PA21, mode=IN, pull=PULL_OFF)
        PA17: Pin  ## = Pin(Pin.cpu.PA17, mode=IN, pull=PULL_OFF)
        PA22: Pin  ## = Pin(Pin.cpu.PA22, mode=IN, pull=PULL_OFF)
        PA18: Pin  ## = Pin(Pin.cpu.PA18, mode=IN, pull=PULL_OFF)
        PA20: Pin  ## = Pin(Pin.cpu.PA20, mode=IN, pull=PULL_OFF)
        PA19: Pin  ## = Pin(Pin.cpu.PA19, mode=IN, pull=PULL_OFF)
        PA03: Pin  ## = Pin(Pin.cpu.PA03, mode=IN, pull=PULL_OFF)
        PA11: Pin  ## = Pin(Pin.cpu.PA11, mode=IN, pull=PULL_OFF)
        PA04: Pin  ## = Pin(Pin.cpu.PA04, mode=IN, pull=PULL_OFF)
        PA00: Pin  ## = Pin(Pin.cpu.PA00, mode=IN, pull=PULL_OFF)
        PA02: Pin  ## = Pin(Pin.cpu.PA02, mode=IN, pull=PULL_OFF)
        PA01: Pin  ## = Pin(Pin.cpu.PA01, mode=IN, pull=PULL_OFF)
        PA09: Pin  ## = Pin(Pin.cpu.PA09, mode=IN, pull=PULL_OFF)
        PA05: Pin  ## = Pin(Pin.cpu.PA05, mode=IN, pull=PULL_OFF)
        PA10: Pin  ## = Pin(Pin.cpu.PA10, mode=IN, pull=PULL_OFF)
        PA06: Pin  ## = Pin(Pin.cpu.PA06, mode=IN, pull=PULL_OFF)
        PA08: Pin  ## = Pin(Pin.cpu.PA08, mode=IN, pull=PULL_OFF)
        PA07: Pin  ## = Pin(Pin.cpu.PA07, mode=IN, pull=PULL_OFF)
        PB19: Pin  ## = Pin(Pin.cpu.PB19, mode=IN, pull=PULL_OFF)
        PB11: Pin  ## = Pin(Pin.cpu.PB11, mode=IN, pull=PULL_OFF)
        PA24: Pin  ## = Pin(Pin.cpu.PA24, mode=OUT, pull=PULL_OFF)
        PB12: Pin  ## = Pin(Pin.cpu.PB12, mode=IN, pull=PULL_OFF)
        PB08: Pin  ## = Pin(Pin.cpu.PB08, mode=IN, pull=PULL_OFF)
        PB10: Pin  ## = Pin(Pin.cpu.PB10, mode=IN, pull=PULL_OFF)
        PB09: Pin  ## = Pin(Pin.cpu.PB09, mode=IN, pull=PULL_OFF)
        PB17: Pin  ## = Pin(Pin.cpu.PB17, mode=IN, pull=PULL_OFF)
        PB13: Pin  ## = Pin(Pin.cpu.PB13, mode=IN, pull=PULL_OFF)
        PB18: Pin  ## = Pin(Pin.cpu.PB18, mode=IN, pull=PULL_OFF)
        PB14: Pin  ## = Pin(Pin.cpu.PB14, mode=IN, pull=PULL_OFF)
        PB16: Pin  ## = Pin(Pin.cpu.PB16, mode=IN, pull=PULL_OFF)
        PB15: Pin  ## = Pin(Pin.cpu.PB15, mode=IN, pull=PULL_OFF)
        PA31: Pin  ## = Pin(Pin.cpu.PA31, mode=IN, pull=PULL_OFF)
        PB07: Pin  ## = Pin(Pin.cpu.PB07, mode=IN, pull=PULL_OFF)
        PB00: Pin  ## = Pin(Pin.cpu.PB00, mode=IN, pull=PULL_OFF)
        PA25: Pin  ## = Pin(Pin.cpu.PA25, mode=OUT, pull=PULL_OFF)
        PA30: Pin  ## = Pin(Pin.cpu.PA30, mode=IN, pull=PULL_OFF)
        PA27: Pin  ## = Pin(Pin.cpu.PA27, mode=IN, pull=PULL_OFF)
        PB05: Pin  ## = Pin(Pin.cpu.PB05, mode=IN, pull=PULL_OFF)
        PB01: Pin  ## = Pin(Pin.cpu.PB01, mode=IN, pull=PULL_OFF)
        PB06: Pin  ## = Pin(Pin.cpu.PB06, mode=IN, pull=PULL_OFF)
        PB02: Pin  ## = Pin(Pin.cpu.PB02, mode=IN, pull=PULL_OFF)
        PB04: Pin  ## = Pin(Pin.cpu.PB04, mode=IN, pull=PULL_OFF)
        PB03: Pin  ## = Pin(Pin.cpu.PB03, mode=IN, pull=PULL_OFF)
        def __init__(self, *argv, **kwargs) -> None: ...

    def __init__(self, *argv, **kwargs) -> None: ...

class SoftSPI:
    LSB: int = 1
    MSB: int = 0
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def write_readinto(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Timer:
    PERIODIC: int = 2
    ONE_SHOT: int = 1
    def init(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class UART:
    def flush(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def txdone(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def sendbreak(self, *args, **kwargs) -> Incomplete: ...
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
    def init(self, *args, **kwargs) -> Incomplete: ...
    def calibration(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class SPI:
    LSB: int = 1
    MSB: int = 0
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
