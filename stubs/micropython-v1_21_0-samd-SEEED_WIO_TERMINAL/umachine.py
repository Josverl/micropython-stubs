"""
Module: 'umachine' on micropython-v1.21.0-samd-SEEED_WIO_TERMINAL
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51P19A', 'arch': 'armv7emsp'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

PWRON_RESET = 1  # type: int
HARD_RESET = 16  # type: int
SOFT_RESET = 64  # type: int
WDT_RESET = 32  # type: int
DEEPSLEEP_RESET = 128  # type: int


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


def reset_cause(*args, **kwargs) -> Incomplete:
    ...


def soft_reset(*args, **kwargs) -> Incomplete:
    ...


def freq(*args, **kwargs) -> Incomplete:
    ...


def reset(*args, **kwargs) -> Incomplete:
    ...


def time_pulse_us(*args, **kwargs) -> Incomplete:
    ...


def lightsleep(*args, **kwargs) -> Incomplete:
    ...


def idle(*args, **kwargs) -> Incomplete:
    ...


def unique_id(*args, **kwargs) -> Incomplete:
    ...


class WDT:
    def timeout_ms(self, *args, **kwargs) -> Incomplete:
        ...

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
    def read_u16(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class DAC:
    def write(self, *args, **kwargs) -> Incomplete:
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

    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def toggle(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def on(self, *args, **kwargs) -> Incomplete:
        ...

    def low(self, *args, **kwargs) -> Incomplete:
        ...

    def off(self, *args, **kwargs) -> Incomplete:
        ...

    def high(self, *args, **kwargs) -> Incomplete:
        ...

    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def disable(self, *args, **kwargs) -> Incomplete:
        ...

    def drive(self, *args, **kwargs) -> Incomplete:
        ...

    class board:
        LCD_YU: Incomplete  ## <class 'Pin'> = Pin("LCD_YU", mode=IN, pull=PULL_OFF, GPIO=PC11)
        QSPI_SCK: Incomplete  ## <class 'Pin'> = Pin("QSPI_SCK", mode=IN, pull=PULL_OFF, GPIO=PB10)
        QSPI_D3: Incomplete  ## <class 'Pin'> = Pin("QSPI_D3", mode=IN, pull=PULL_OFF, GPIO=PA11)
        QSPI_D2: Incomplete  ## <class 'Pin'> = Pin("QSPI_D2", mode=IN, pull=PULL_OFF, GPIO=PA10)
        RX: Incomplete  ## <class 'Pin'> = Pin("RX", mode=IN, pull=PULL_OFF, GPIO=PB27)
        SCL1: Incomplete  ## <class 'Pin'> = Pin("SCL1", mode=IN, pull=PULL_OFF, GPIO=PA16)
        SCL0: Incomplete  ## <class 'Pin'> = Pin("SCL0", mode=IN, pull=PULL_OFF, GPIO=PA12)
        SCK: Incomplete  ## <class 'Pin'> = Pin("SCK", mode=IN, pull=PULL_OFF, GPIO=PB03)
        QSPI_D1: Incomplete  ## <class 'Pin'> = Pin("QSPI_D1", mode=IN, pull=PULL_OFF, GPIO=PA09)
        MIC: Incomplete  ## <class 'Pin'> = Pin("MIC", mode=IN, pull=PULL_OFF, GPIO=PC30)
        LED_LCD: Incomplete  ## <class 'Pin'> = Pin("LED_LCD", mode=IN, pull=PULL_OFF, GPIO=PC05)
        LED_BLUE: Incomplete  ## <class 'Pin'> = Pin("LED_BLUE", mode=OUT, pull=PULL_OFF, GPIO=PA15)
        MISO: Incomplete  ## <class 'Pin'> = Pin("MISO", mode=IN, pull=PULL_OFF, GPIO=PB00)
        QSPI_D0: Incomplete  ## <class 'Pin'> = Pin("QSPI_D0", mode=IN, pull=PULL_OFF, GPIO=PA08)
        QSPI_CS: Incomplete  ## <class 'Pin'> = Pin("QSPI_CS", mode=IN, pull=PULL_OFF, GPIO=PB11)
        MOSI: Incomplete  ## <class 'Pin'> = Pin("MOSI", mode=IN, pull=PULL_OFF, GPIO=PB02)
        SDA0: Incomplete  ## <class 'Pin'> = Pin("SDA0", mode=IN, pull=PULL_OFF, GPIO=PA13)
        SWITCH_X: Incomplete  ## <class 'Pin'> = Pin("SWITCH_X", mode=IN, pull=PULL_OFF, GPIO=PD08)
        SWITCH_U: Incomplete  ## <class 'Pin'> = Pin("SWITCH_U", mode=IN, pull=PULL_OFF, GPIO=PD20)
        SWITCH_B: Incomplete  ## <class 'Pin'> = Pin("SWITCH_B", mode=IN, pull=PULL_OFF, GPIO=PD12)
        SWITCH_Y: Incomplete  ## <class 'Pin'> = Pin("SWITCH_Y", mode=IN, pull=PULL_OFF, GPIO=PD09)
        USB_DM: Incomplete  ## <class 'Pin'> = Pin("USB_DM", mode=OUT, pull=PULL_OFF, GPIO=PA24)
        TX: Incomplete  ## <class 'Pin'> = Pin("TX", mode=IN, pull=PULL_OFF, GPIO=PB26)
        SWITCH_Z: Incomplete  ## <class 'Pin'> = Pin("SWITCH_Z", mode=IN, pull=PULL_OFF, GPIO=PD10)
        SWDIO: Incomplete  ## <class 'Pin'> = Pin("SWDIO", mode=IN, pull=PULL_OFF, GPIO=PA31)
        SD_DET: Incomplete  ## <class 'Pin'> = Pin("SD_DET", mode=IN, pull=PULL_OFF, GPIO=PD21)
        SD_CS: Incomplete  ## <class 'Pin'> = Pin("SD_CS", mode=IN, pull=PULL_OFF, GPIO=PC19)
        SDA1: Incomplete  ## <class 'Pin'> = Pin("SDA1", mode=IN, pull=PULL_OFF, GPIO=PA17)
        SD_MISO: Incomplete  ## <class 'Pin'> = Pin("SD_MISO", mode=IN, pull=PULL_OFF, GPIO=PC18)
        SWCLK: Incomplete  ## <class 'Pin'> = Pin("SWCLK", mode=IN, pull=PULL_OFF, GPIO=PA30)
        SD_SCK: Incomplete  ## <class 'Pin'> = Pin("SD_SCK", mode=IN, pull=PULL_OFF, GPIO=PC17)
        SD_MOSI: Incomplete  ## <class 'Pin'> = Pin("SD_MOSI", mode=IN, pull=PULL_OFF, GPIO=PC16)
        USB_DP: Incomplete  ## <class 'Pin'> = Pin("USB_DP", mode=OUT, pull=PULL_OFF, GPIO=PA25)
        LCD_YD: Incomplete  ## <class 'Pin'> = Pin("LCD_YD", mode=IN, pull=PULL_OFF, GPIO=PC13)
        BUTTON_2: Incomplete  ## <class 'Pin'> = Pin("BUTTON_2", mode=IN, pull=PULL_OFF, GPIO=PC27)
        BUTTON_1: Incomplete  ## <class 'Pin'> = Pin("BUTTON_1", mode=IN, pull=PULL_OFF, GPIO=PC26)
        A8_D8: Incomplete  ## <class 'Pin'> = Pin("A8_D8", mode=IN, pull=PULL_OFF, GPIO=PA06)
        BUTTON_3: Incomplete  ## <class 'Pin'> = Pin("BUTTON_3", mode=IN, pull=PULL_OFF, GPIO=PC28)
        ENABLE_3V3: Incomplete  ## <class 'Pin'> = Pin("ENABLE_3V3", mode=IN, pull=PULL_OFF, GPIO=PC15)
        CS: Incomplete  ## <class 'Pin'> = Pin("CS", mode=IN, pull=PULL_OFF, GPIO=PB01)
        BUZZER: Incomplete  ## <class 'Pin'> = Pin("BUZZER", mode=IN, pull=PULL_OFF, GPIO=PD11)
        A7_D7: Incomplete  ## <class 'Pin'> = Pin("A7_D7", mode=IN, pull=PULL_OFF, GPIO=PB07)
        A2_D2: Incomplete  ## <class 'Pin'> = Pin("A2_D2", mode=IN, pull=PULL_OFF, GPIO=PA07)
        A1_D1: Incomplete  ## <class 'Pin'> = Pin("A1_D1", mode=IN, pull=PULL_OFF, GPIO=PB09)
        A0_D0: Incomplete  ## <class 'Pin'> = Pin("A0_D0", mode=IN, pull=PULL_OFF, GPIO=PB08)
        A3_D3: Incomplete  ## <class 'Pin'> = Pin("A3_D3", mode=IN, pull=PULL_OFF, GPIO=PB04)
        A6_D6: Incomplete  ## <class 'Pin'> = Pin("A6_D6", mode=IN, pull=PULL_OFF, GPIO=PA04)
        A5_D5: Incomplete  ## <class 'Pin'> = Pin("A5_D5", mode=IN, pull=PULL_OFF, GPIO=PB06)
        A4_D4: Incomplete  ## <class 'Pin'> = Pin("A4_D4", mode=IN, pull=PULL_OFF, GPIO=PB05)
        ENABLE_5V: Incomplete  ## <class 'Pin'> = Pin("ENABLE_5V", mode=IN, pull=PULL_OFF, GPIO=PC14)
        LCD_MOSI: Incomplete  ## <class 'Pin'> = Pin("LCD_MOSI", mode=IN, pull=PULL_OFF, GPIO=PB19)
        LCD_MISO: Incomplete  ## <class 'Pin'> = Pin("LCD_MISO", mode=IN, pull=PULL_OFF, GPIO=PB18)
        LCD_D_C: Incomplete  ## <class 'Pin'> = Pin("LCD_D_C", mode=IN, pull=PULL_OFF, GPIO=PC06)
        LCD_RESET: Incomplete  ## <class 'Pin'> = Pin("LCD_RESET", mode=IN, pull=PULL_OFF, GPIO=PC07)
        LCD_XR: Incomplete  ## <class 'Pin'> = Pin("LCD_XR", mode=IN, pull=PULL_OFF, GPIO=PC12)
        LCD_XL: Incomplete  ## <class 'Pin'> = Pin("LCD_XL", mode=IN, pull=PULL_OFF, GPIO=PC10)
        LCD_SCK: Incomplete  ## <class 'Pin'> = Pin("LCD_SCK", mode=IN, pull=PULL_OFF, GPIO=PB20)
        LCD_CS: Incomplete  ## <class 'Pin'> = Pin("LCD_CS", mode=IN, pull=PULL_OFF, GPIO=PB21)
        GPCLK2: Incomplete  ## <class 'Pin'> = Pin("GPCLK2", mode=IN, pull=PULL_OFF, GPIO=PB13)
        GPCLK1: Incomplete  ## <class 'Pin'> = Pin("GPCLK1", mode=IN, pull=PULL_OFF, GPIO=PB12)
        GPCLK0: Incomplete  ## <class 'Pin'> = Pin("GPCLK0", mode=IN, pull=PULL_OFF, GPIO=PB15)
        I2C_BCLK: Incomplete  ## <class 'Pin'> = Pin("I2C_BCLK", mode=IN, pull=PULL_OFF, GPIO=PB16)
        I2S_SDOUT: Incomplete  ## <class 'Pin'> = Pin("I2S_SDOUT", mode=IN, pull=PULL_OFF, GPIO=PA22)
        I2S_SDIN: Incomplete  ## <class 'Pin'> = Pin("I2S_SDIN", mode=IN, pull=PULL_OFF, GPIO=PA21)
        I2S_LRCLK: Incomplete  ## <class 'Pin'> = Pin("I2S_LRCLK", mode=IN, pull=PULL_OFF, GPIO=PA20)

        def __init__(self, *argv, **kwargs) -> None:
            ...

    class cpu:
        PC04: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC04)
        PC14: Incomplete  ## <class 'Pin'> = Pin("ENABLE_5V", mode=IN, pull=PULL_OFF, GPIO=PC14)
        PC05: Incomplete  ## <class 'Pin'> = Pin("LED_LCD", mode=IN, pull=PULL_OFF, GPIO=PC05)
        PC01: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC01)
        PC03: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC03)
        PC02: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC02)
        PC12: Incomplete  ## <class 'Pin'> = Pin("LCD_XR", mode=IN, pull=PULL_OFF, GPIO=PC12)
        PC06: Incomplete  ## <class 'Pin'> = Pin("LCD_D_C", mode=IN, pull=PULL_OFF, GPIO=PC06)
        PC13: Incomplete  ## <class 'Pin'> = Pin("LCD_YD", mode=IN, pull=PULL_OFF, GPIO=PC13)
        PC07: Incomplete  ## <class 'Pin'> = Pin("LCD_RESET", mode=IN, pull=PULL_OFF, GPIO=PC07)
        PC11: Incomplete  ## <class 'Pin'> = Pin("LCD_YU", mode=IN, pull=PULL_OFF, GPIO=PC11)
        PC10: Incomplete  ## <class 'Pin'> = Pin("LCD_XL", mode=IN, pull=PULL_OFF, GPIO=PC10)
        PB24: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB24)
        PC00: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC00)
        PB25: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB25)
        PB21: Incomplete  ## <class 'Pin'> = Pin("LCD_CS", mode=IN, pull=PULL_OFF, GPIO=PB21)
        PB23: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB23)
        PB22: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB22)
        PB30: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB30)
        PB26: Incomplete  ## <class 'Pin'> = Pin("TX", mode=IN, pull=PULL_OFF, GPIO=PB26)
        PB31: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB31)
        PB27: Incomplete  ## <class 'Pin'> = Pin("RX", mode=IN, pull=PULL_OFF, GPIO=PB27)
        PB29: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB29)
        PB28: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB28)
        PB20: Incomplete  ## <class 'Pin'> = Pin("LCD_SCK", mode=IN, pull=PULL_OFF, GPIO=PB20)
        PD00: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PD00)
        PC15: Incomplete  ## <class 'Pin'> = Pin("ENABLE_3V3", mode=IN, pull=PULL_OFF, GPIO=PC15)
        PD01: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PD01)
        PC28: Incomplete  ## <class 'Pin'> = Pin("BUTTON_3", mode=IN, pull=PULL_OFF, GPIO=PC28)
        PC31: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC31)
        PC30: Incomplete  ## <class 'Pin'> = Pin("MIC", mode=IN, pull=PULL_OFF, GPIO=PC30)
        PD12: Incomplete  ## <class 'Pin'> = Pin("SWITCH_B", mode=IN, pull=PULL_OFF, GPIO=PD12)
        PD08: Incomplete  ## <class 'Pin'> = Pin("SWITCH_X", mode=IN, pull=PULL_OFF, GPIO=PD08)
        PD20: Incomplete  ## <class 'Pin'> = Pin("SWITCH_U", mode=IN, pull=PULL_OFF, GPIO=PD20)
        PD09: Incomplete  ## <class 'Pin'> = Pin("SWITCH_Y", mode=IN, pull=PULL_OFF, GPIO=PD09)
        PD11: Incomplete  ## <class 'Pin'> = Pin("BUZZER", mode=IN, pull=PULL_OFF, GPIO=PD11)
        PD10: Incomplete  ## <class 'Pin'> = Pin("SWITCH_Z", mode=IN, pull=PULL_OFF, GPIO=PD10)
        PC19: Incomplete  ## <class 'Pin'> = Pin("SD_CS", mode=IN, pull=PULL_OFF, GPIO=PC19)
        PC27: Incomplete  ## <class 'Pin'> = Pin("BUTTON_2", mode=IN, pull=PULL_OFF, GPIO=PC27)
        PC20: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC20)
        PC16: Incomplete  ## <class 'Pin'> = Pin("SD_MOSI", mode=IN, pull=PULL_OFF, GPIO=PC16)
        PC18: Incomplete  ## <class 'Pin'> = Pin("SD_MISO", mode=IN, pull=PULL_OFF, GPIO=PC18)
        PC17: Incomplete  ## <class 'Pin'> = Pin("SD_SCK", mode=IN, pull=PULL_OFF, GPIO=PC17)
        PC25: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC25)
        PC21: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC21)
        PC26: Incomplete  ## <class 'Pin'> = Pin("BUTTON_1", mode=IN, pull=PULL_OFF, GPIO=PC26)
        PC22: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC22)
        PC24: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC24)
        PC23: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC23)
        PD21: Incomplete  ## <class 'Pin'> = Pin("SD_DET", mode=IN, pull=PULL_OFF, GPIO=PD21)
        PA15: Incomplete  ## <class 'Pin'> = Pin("LED_BLUE", mode=OUT, pull=PULL_OFF, GPIO=PA15)
        PA23: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA23)
        PA16: Incomplete  ## <class 'Pin'> = Pin("SCL1", mode=IN, pull=PULL_OFF, GPIO=PA16)
        PA12: Incomplete  ## <class 'Pin'> = Pin("SCL0", mode=IN, pull=PULL_OFF, GPIO=PA12)
        PA14: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA14)
        PA13: Incomplete  ## <class 'Pin'> = Pin("SDA0", mode=IN, pull=PULL_OFF, GPIO=PA13)
        PA21: Incomplete  ## <class 'Pin'> = Pin("I2S_SDIN", mode=IN, pull=PULL_OFF, GPIO=PA21)
        PA17: Incomplete  ## <class 'Pin'> = Pin("SDA1", mode=IN, pull=PULL_OFF, GPIO=PA17)
        PA22: Incomplete  ## <class 'Pin'> = Pin("I2S_SDOUT", mode=IN, pull=PULL_OFF, GPIO=PA22)
        PA18: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA18)
        PA20: Incomplete  ## <class 'Pin'> = Pin("I2S_LRCLK", mode=IN, pull=PULL_OFF, GPIO=PA20)
        PA19: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA19)
        PA03: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA03)
        PA11: Incomplete  ## <class 'Pin'> = Pin("QSPI_D3", mode=IN, pull=PULL_OFF, GPIO=PA11)
        PA04: Incomplete  ## <class 'Pin'> = Pin("A6_D6", mode=IN, pull=PULL_OFF, GPIO=PA04)
        PA00: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA00)
        PA02: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA02)
        PA01: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA01)
        PA09: Incomplete  ## <class 'Pin'> = Pin("QSPI_D1", mode=IN, pull=PULL_OFF, GPIO=PA09)
        PA05: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA05)
        PA10: Incomplete  ## <class 'Pin'> = Pin("QSPI_D2", mode=IN, pull=PULL_OFF, GPIO=PA10)
        PA06: Incomplete  ## <class 'Pin'> = Pin("A8_D8", mode=IN, pull=PULL_OFF, GPIO=PA06)
        PA08: Incomplete  ## <class 'Pin'> = Pin("QSPI_D0", mode=IN, pull=PULL_OFF, GPIO=PA08)
        PA07: Incomplete  ## <class 'Pin'> = Pin("A2_D2", mode=IN, pull=PULL_OFF, GPIO=PA07)
        PB19: Incomplete  ## <class 'Pin'> = Pin("LCD_MOSI", mode=IN, pull=PULL_OFF, GPIO=PB19)
        PB11: Incomplete  ## <class 'Pin'> = Pin("QSPI_CS", mode=IN, pull=PULL_OFF, GPIO=PB11)
        PA24: Incomplete  ## <class 'Pin'> = Pin("USB_DM", mode=OUT, pull=PULL_OFF, GPIO=PA24)
        PB12: Incomplete  ## <class 'Pin'> = Pin("GPCLK1", mode=IN, pull=PULL_OFF, GPIO=PB12)
        PB08: Incomplete  ## <class 'Pin'> = Pin("A0_D0", mode=IN, pull=PULL_OFF, GPIO=PB08)
        PB10: Incomplete  ## <class 'Pin'> = Pin("QSPI_SCK", mode=IN, pull=PULL_OFF, GPIO=PB10)
        PB09: Incomplete  ## <class 'Pin'> = Pin("A1_D1", mode=IN, pull=PULL_OFF, GPIO=PB09)
        PB17: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB17)
        PB13: Incomplete  ## <class 'Pin'> = Pin("GPCLK2", mode=IN, pull=PULL_OFF, GPIO=PB13)
        PB18: Incomplete  ## <class 'Pin'> = Pin("LCD_MISO", mode=IN, pull=PULL_OFF, GPIO=PB18)
        PB14: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB14)
        PB16: Incomplete  ## <class 'Pin'> = Pin("I2C_BCLK", mode=IN, pull=PULL_OFF, GPIO=PB16)
        PB15: Incomplete  ## <class 'Pin'> = Pin("GPCLK0", mode=IN, pull=PULL_OFF, GPIO=PB15)
        PA31: Incomplete  ## <class 'Pin'> = Pin("SWDIO", mode=IN, pull=PULL_OFF, GPIO=PA31)
        PB07: Incomplete  ## <class 'Pin'> = Pin("A7_D7", mode=IN, pull=PULL_OFF, GPIO=PB07)
        PB00: Incomplete  ## <class 'Pin'> = Pin("MISO", mode=IN, pull=PULL_OFF, GPIO=PB00)
        PA25: Incomplete  ## <class 'Pin'> = Pin("USB_DP", mode=OUT, pull=PULL_OFF, GPIO=PA25)
        PA30: Incomplete  ## <class 'Pin'> = Pin("SWCLK", mode=IN, pull=PULL_OFF, GPIO=PA30)
        PA27: Incomplete  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA27)
        PB05: Incomplete  ## <class 'Pin'> = Pin("A4_D4", mode=IN, pull=PULL_OFF, GPIO=PB05)
        PB01: Incomplete  ## <class 'Pin'> = Pin("CS", mode=IN, pull=PULL_OFF, GPIO=PB01)
        PB06: Incomplete  ## <class 'Pin'> = Pin("A5_D5", mode=IN, pull=PULL_OFF, GPIO=PB06)
        PB02: Incomplete  ## <class 'Pin'> = Pin("MOSI", mode=IN, pull=PULL_OFF, GPIO=PB02)
        PB04: Incomplete  ## <class 'Pin'> = Pin("A3_D3", mode=IN, pull=PULL_OFF, GPIO=PB04)
        PB03: Incomplete  ## <class 'Pin'> = Pin("SCK", mode=IN, pull=PULL_OFF, GPIO=PB03)

        def __init__(self, *argv, **kwargs) -> None:
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
    PERIODIC = 2  # type: int
    ONE_SHOT = 1  # type: int

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class UART:
    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def txdone(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def sendbreak(self, *args, **kwargs) -> Incomplete:
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

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def calibration(self, *args, **kwargs) -> Incomplete:
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
