"""
Module: 'machine' on micropython-v1.20.0-samd-SEEED_WIO_TERMINAL
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'cpu': 'SAMD51P19A', 'mpy': 'v6.1', 'arch': 'armv7emsp'})
# Stubber: v1.13.4
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
        RX: Any  ## <class 'Pin'> = Pin("RX", mode=IN, pull=PULL_OFF, GPIO=PB27)
        SCK: Any  ## <class 'Pin'> = Pin("SCK", mode=IN, pull=PULL_OFF, GPIO=PB03)
        MOSI: Any  ## <class 'Pin'> = Pin("MOSI", mode=IN, pull=PULL_OFF, GPIO=PB02)
        SDA1: Any  ## <class 'Pin'> = Pin("SDA1", mode=IN, pull=PULL_OFF, GPIO=PA17)
        SDA0: Any  ## <class 'Pin'> = Pin("SDA0", mode=IN, pull=PULL_OFF, GPIO=PA13)
        SCL0: Any  ## <class 'Pin'> = Pin("SCL0", mode=IN, pull=PULL_OFF, GPIO=PA12)
        SCL1: Any  ## <class 'Pin'> = Pin("SCL1", mode=IN, pull=PULL_OFF, GPIO=PA16)
        LCD_YD: Any  ## <class 'Pin'> = Pin("LCD_YD", mode=IN, pull=PULL_OFF, GPIO=PC13)
        LCD_YU: Any  ## <class 'Pin'> = Pin("LCD_YU", mode=IN, pull=PULL_OFF, GPIO=PC11)
        LCD_XR: Any  ## <class 'Pin'> = Pin("LCD_XR", mode=IN, pull=PULL_OFF, GPIO=PC12)
        MISO: Any  ## <class 'Pin'> = Pin("MISO", mode=IN, pull=PULL_OFF, GPIO=PB00)
        MIC: Any  ## <class 'Pin'> = Pin("MIC", mode=IN, pull=PULL_OFF, GPIO=PC30)
        LED_BLUE: Any  ## <class 'Pin'> = Pin("LED_BLUE", mode=OUT, pull=PULL_OFF, GPIO=PA15)
        LED_LCD: Any  ## <class 'Pin'> = Pin("LED_LCD", mode=IN, pull=PULL_OFF, GPIO=PC05)
        LCD_XL: Any  ## <class 'Pin'> = Pin("LCD_XL", mode=IN, pull=PULL_OFF, GPIO=PC10)
        SWITCH_X: Any  ## <class 'Pin'> = Pin("SWITCH_X", mode=IN, pull=PULL_OFF, GPIO=PD08)
        SWITCH_Y: Any  ## <class 'Pin'> = Pin("SWITCH_Y", mode=IN, pull=PULL_OFF, GPIO=PD09)
        SWITCH_U: Any  ## <class 'Pin'> = Pin("SWITCH_U", mode=IN, pull=PULL_OFF, GPIO=PD20)
        SD_CS: Any  ## <class 'Pin'> = Pin("SD_CS", mode=IN, pull=PULL_OFF, GPIO=PC19)
        USB_DM: Any  ## <class 'Pin'> = Pin("USB_DM", mode=OUT, pull=PULL_OFF, GPIO=PA24)
        SWITCH_Z: Any  ## <class 'Pin'> = Pin("SWITCH_Z", mode=IN, pull=PULL_OFF, GPIO=PD10)
        TX: Any  ## <class 'Pin'> = Pin("TX", mode=IN, pull=PULL_OFF, GPIO=PB26)
        SD_MISO: Any  ## <class 'Pin'> = Pin("SD_MISO", mode=IN, pull=PULL_OFF, GPIO=PC18)
        SD_MOSI: Any  ## <class 'Pin'> = Pin("SD_MOSI", mode=IN, pull=PULL_OFF, GPIO=PC16)
        SD_DET: Any  ## <class 'Pin'> = Pin("SD_DET", mode=IN, pull=PULL_OFF, GPIO=PD21)
        SWITCH_B: Any  ## <class 'Pin'> = Pin("SWITCH_B", mode=IN, pull=PULL_OFF, GPIO=PD12)
        SWDIO: Any  ## <class 'Pin'> = Pin("SWDIO", mode=IN, pull=PULL_OFF, GPIO=PA31)
        SD_SCK: Any  ## <class 'Pin'> = Pin("SD_SCK", mode=IN, pull=PULL_OFF, GPIO=PC17)
        SWCLK: Any  ## <class 'Pin'> = Pin("SWCLK", mode=IN, pull=PULL_OFF, GPIO=PA30)
        USB_DP: Any  ## <class 'Pin'> = Pin("USB_DP", mode=OUT, pull=PULL_OFF, GPIO=PA25)
        A6_D6: Any  ## <class 'Pin'> = Pin("A6_D6", mode=IN, pull=PULL_OFF, GPIO=PA04)
        A7_D7: Any  ## <class 'Pin'> = Pin("A7_D7", mode=IN, pull=PULL_OFF, GPIO=PB07)
        A5_D5: Any  ## <class 'Pin'> = Pin("A5_D5", mode=IN, pull=PULL_OFF, GPIO=PB06)
        BUTTON_3: Any  ## <class 'Pin'> = Pin("BUTTON_3", mode=IN, pull=PULL_OFF, GPIO=PC28)
        BUTTON_2: Any  ## <class 'Pin'> = Pin("BUTTON_2", mode=IN, pull=PULL_OFF, GPIO=PC27)
        A8_D8: Any  ## <class 'Pin'> = Pin("A8_D8", mode=IN, pull=PULL_OFF, GPIO=PA06)
        BUTTON_1: Any  ## <class 'Pin'> = Pin("BUTTON_1", mode=IN, pull=PULL_OFF, GPIO=PC26)
        A0_D0: Any  ## <class 'Pin'> = Pin("A0_D0", mode=IN, pull=PULL_OFF, GPIO=PB08)
        A4_D4: Any  ## <class 'Pin'> = Pin("A4_D4", mode=IN, pull=PULL_OFF, GPIO=PB05)
        A3_D3: Any  ## <class 'Pin'> = Pin("A3_D3", mode=IN, pull=PULL_OFF, GPIO=PB04)
        A1_D1: Any  ## <class 'Pin'> = Pin("A1_D1", mode=IN, pull=PULL_OFF, GPIO=PB09)
        A2_D2: Any  ## <class 'Pin'> = Pin("A2_D2", mode=IN, pull=PULL_OFF, GPIO=PA07)
        LCD_SCK: Any  ## <class 'Pin'> = Pin("LCD_SCK", mode=IN, pull=PULL_OFF, GPIO=PB20)
        LCD_CS: Any  ## <class 'Pin'> = Pin("LCD_CS", mode=IN, pull=PULL_OFF, GPIO=PB21)
        LCD_D_C: Any  ## <class 'Pin'> = Pin("LCD_D_C", mode=IN, pull=PULL_OFF, GPIO=PC06)
        I2S_SDOUT: Any  ## <class 'Pin'> = Pin("I2S_SDOUT", mode=IN, pull=PULL_OFF, GPIO=PA22)
        BUZZER: Any  ## <class 'Pin'> = Pin("BUZZER", mode=IN, pull=PULL_OFF, GPIO=PD11)
        LCD_RESET: Any  ## <class 'Pin'> = Pin("LCD_RESET", mode=IN, pull=PULL_OFF, GPIO=PC07)
        LCD_MISO: Any  ## <class 'Pin'> = Pin("LCD_MISO", mode=IN, pull=PULL_OFF, GPIO=PB18)
        LCD_MOSI: Any  ## <class 'Pin'> = Pin("LCD_MOSI", mode=IN, pull=PULL_OFF, GPIO=PB19)
        GPCLK0: Any  ## <class 'Pin'> = Pin("GPCLK0", mode=IN, pull=PULL_OFF, GPIO=PB15)
        GPCLK1: Any  ## <class 'Pin'> = Pin("GPCLK1", mode=IN, pull=PULL_OFF, GPIO=PB12)
        CS: Any  ## <class 'Pin'> = Pin("CS", mode=IN, pull=PULL_OFF, GPIO=PB01)
        I2S_SDIN: Any  ## <class 'Pin'> = Pin("I2S_SDIN", mode=IN, pull=PULL_OFF, GPIO=PA21)
        I2S_LRCLK: Any  ## <class 'Pin'> = Pin("I2S_LRCLK", mode=IN, pull=PULL_OFF, GPIO=PA20)
        GPCLK2: Any  ## <class 'Pin'> = Pin("GPCLK2", mode=IN, pull=PULL_OFF, GPIO=PB13)
        I2C_BCLK: Any  ## <class 'Pin'> = Pin("I2C_BCLK", mode=IN, pull=PULL_OFF, GPIO=PB16)

        def __init__(self, *argv, **kwargs) -> None:
            ...

    class cpu:
        PC04: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC04)
        PC14: Any  ## <class 'Pin'> = Pin("5V_ENABLE", mode=IN, pull=PULL_OFF, GPIO=PC14)
        PC05: Any  ## <class 'Pin'> = Pin("LED_LCD", mode=IN, pull=PULL_OFF, GPIO=PC05)
        PC01: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC01)
        PC03: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC03)
        PC02: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC02)
        PC12: Any  ## <class 'Pin'> = Pin("LCD_XR", mode=IN, pull=PULL_OFF, GPIO=PC12)
        PC06: Any  ## <class 'Pin'> = Pin("LCD_D_C", mode=IN, pull=PULL_OFF, GPIO=PC06)
        PC13: Any  ## <class 'Pin'> = Pin("LCD_YD", mode=IN, pull=PULL_OFF, GPIO=PC13)
        PC07: Any  ## <class 'Pin'> = Pin("LCD_RESET", mode=IN, pull=PULL_OFF, GPIO=PC07)
        PC11: Any  ## <class 'Pin'> = Pin("LCD_YU", mode=IN, pull=PULL_OFF, GPIO=PC11)
        PC10: Any  ## <class 'Pin'> = Pin("LCD_XL", mode=IN, pull=PULL_OFF, GPIO=PC10)
        PB24: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB24)
        PC00: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC00)
        PB25: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB25)
        PB21: Any  ## <class 'Pin'> = Pin("LCD_CS", mode=IN, pull=PULL_OFF, GPIO=PB21)
        PB23: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB23)
        PB22: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB22)
        PB30: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB30)
        PB26: Any  ## <class 'Pin'> = Pin("TX", mode=IN, pull=PULL_OFF, GPIO=PB26)
        PB31: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB31)
        PB27: Any  ## <class 'Pin'> = Pin("RX", mode=IN, pull=PULL_OFF, GPIO=PB27)
        PB29: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB29)
        PB28: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB28)
        PB20: Any  ## <class 'Pin'> = Pin("LCD_SCK", mode=IN, pull=PULL_OFF, GPIO=PB20)
        PD00: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PD00)
        PC15: Any  ## <class 'Pin'> = Pin("3V3_ENABLE", mode=IN, pull=PULL_OFF, GPIO=PC15)
        PD01: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PD01)
        PC28: Any  ## <class 'Pin'> = Pin("BUTTON_3", mode=IN, pull=PULL_OFF, GPIO=PC28)
        PC31: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC31)
        PC30: Any  ## <class 'Pin'> = Pin("MIC", mode=IN, pull=PULL_OFF, GPIO=PC30)
        PD12: Any  ## <class 'Pin'> = Pin("SWITCH_B", mode=IN, pull=PULL_OFF, GPIO=PD12)
        PD08: Any  ## <class 'Pin'> = Pin("SWITCH_X", mode=IN, pull=PULL_OFF, GPIO=PD08)
        PD20: Any  ## <class 'Pin'> = Pin("SWITCH_U", mode=IN, pull=PULL_OFF, GPIO=PD20)
        PD09: Any  ## <class 'Pin'> = Pin("SWITCH_Y", mode=IN, pull=PULL_OFF, GPIO=PD09)
        PD11: Any  ## <class 'Pin'> = Pin("BUZZER", mode=IN, pull=PULL_OFF, GPIO=PD11)
        PD10: Any  ## <class 'Pin'> = Pin("SWITCH_Z", mode=IN, pull=PULL_OFF, GPIO=PD10)
        PC19: Any  ## <class 'Pin'> = Pin("SD_CS", mode=IN, pull=PULL_OFF, GPIO=PC19)
        PC27: Any  ## <class 'Pin'> = Pin("BUTTON_2", mode=IN, pull=PULL_OFF, GPIO=PC27)
        PC20: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC20)
        PC16: Any  ## <class 'Pin'> = Pin("SD_MOSI", mode=IN, pull=PULL_OFF, GPIO=PC16)
        PC18: Any  ## <class 'Pin'> = Pin("SD_MISO", mode=IN, pull=PULL_OFF, GPIO=PC18)
        PC17: Any  ## <class 'Pin'> = Pin("SD_SCK", mode=IN, pull=PULL_OFF, GPIO=PC17)
        PC25: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC25)
        PC21: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC21)
        PC26: Any  ## <class 'Pin'> = Pin("BUTTON_1", mode=IN, pull=PULL_OFF, GPIO=PC26)
        PC22: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC22)
        PC24: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC24)
        PC23: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PC23)
        PD21: Any  ## <class 'Pin'> = Pin("SD_DET", mode=IN, pull=PULL_OFF, GPIO=PD21)
        PA15: Any  ## <class 'Pin'> = Pin("LED_BLUE", mode=OUT, pull=PULL_OFF, GPIO=PA15)
        PA23: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA23)
        PA16: Any  ## <class 'Pin'> = Pin("SCL1", mode=IN, pull=PULL_OFF, GPIO=PA16)
        PA12: Any  ## <class 'Pin'> = Pin("SCL0", mode=IN, pull=PULL_OFF, GPIO=PA12)
        PA14: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA14)
        PA13: Any  ## <class 'Pin'> = Pin("SDA0", mode=IN, pull=PULL_OFF, GPIO=PA13)
        PA21: Any  ## <class 'Pin'> = Pin("I2S_SDIN", mode=IN, pull=PULL_OFF, GPIO=PA21)
        PA17: Any  ## <class 'Pin'> = Pin("SDA1", mode=IN, pull=PULL_OFF, GPIO=PA17)
        PA22: Any  ## <class 'Pin'> = Pin("I2S_SDOUT", mode=IN, pull=PULL_OFF, GPIO=PA22)
        PA18: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA18)
        PA20: Any  ## <class 'Pin'> = Pin("I2S_LRCLK", mode=IN, pull=PULL_OFF, GPIO=PA20)
        PA19: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA19)
        PA03: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA03)
        PA11: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA11)
        PA04: Any  ## <class 'Pin'> = Pin("A6_D6", mode=IN, pull=PULL_OFF, GPIO=PA04)
        PA00: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA00)
        PA02: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA02)
        PA01: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA01)
        PA09: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA09)
        PA05: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA05)
        PA10: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA10)
        PA06: Any  ## <class 'Pin'> = Pin("A8_D8", mode=IN, pull=PULL_OFF, GPIO=PA06)
        PA08: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA08)
        PA07: Any  ## <class 'Pin'> = Pin("A2_D2", mode=IN, pull=PULL_OFF, GPIO=PA07)
        PB19: Any  ## <class 'Pin'> = Pin("LCD_MOSI", mode=IN, pull=PULL_OFF, GPIO=PB19)
        PB11: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB11)
        PA24: Any  ## <class 'Pin'> = Pin("USB_DM", mode=OUT, pull=PULL_OFF, GPIO=PA24)
        PB12: Any  ## <class 'Pin'> = Pin("GPCLK1", mode=IN, pull=PULL_OFF, GPIO=PB12)
        PB08: Any  ## <class 'Pin'> = Pin("A0_D0", mode=IN, pull=PULL_OFF, GPIO=PB08)
        PB10: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB10)
        PB09: Any  ## <class 'Pin'> = Pin("A1_D1", mode=IN, pull=PULL_OFF, GPIO=PB09)
        PB17: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB17)
        PB13: Any  ## <class 'Pin'> = Pin("GPCLK2", mode=IN, pull=PULL_OFF, GPIO=PB13)
        PB18: Any  ## <class 'Pin'> = Pin("LCD_MISO", mode=IN, pull=PULL_OFF, GPIO=PB18)
        PB14: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PB14)
        PB16: Any  ## <class 'Pin'> = Pin("I2C_BCLK", mode=IN, pull=PULL_OFF, GPIO=PB16)
        PB15: Any  ## <class 'Pin'> = Pin("GPCLK0", mode=IN, pull=PULL_OFF, GPIO=PB15)
        PA31: Any  ## <class 'Pin'> = Pin("SWDIO", mode=IN, pull=PULL_OFF, GPIO=PA31)
        PB07: Any  ## <class 'Pin'> = Pin("A7_D7", mode=IN, pull=PULL_OFF, GPIO=PB07)
        PB00: Any  ## <class 'Pin'> = Pin("MISO", mode=IN, pull=PULL_OFF, GPIO=PB00)
        PA25: Any  ## <class 'Pin'> = Pin("USB_DP", mode=OUT, pull=PULL_OFF, GPIO=PA25)
        PA30: Any  ## <class 'Pin'> = Pin("SWCLK", mode=IN, pull=PULL_OFF, GPIO=PA30)
        PA27: Any  ## <class 'Pin'> = Pin("", mode=IN, pull=PULL_OFF, GPIO=PA27)
        PB05: Any  ## <class 'Pin'> = Pin("A4_D4", mode=IN, pull=PULL_OFF, GPIO=PB05)
        PB01: Any  ## <class 'Pin'> = Pin("CS", mode=IN, pull=PULL_OFF, GPIO=PB01)
        PB06: Any  ## <class 'Pin'> = Pin("A5_D5", mode=IN, pull=PULL_OFF, GPIO=PB06)
        PB02: Any  ## <class 'Pin'> = Pin("MOSI", mode=IN, pull=PULL_OFF, GPIO=PB02)
        PB04: Any  ## <class 'Pin'> = Pin("A3_D3", mode=IN, pull=PULL_OFF, GPIO=PB04)
        PB03: Any  ## <class 'Pin'> = Pin("SCK", mode=IN, pull=PULL_OFF, GPIO=PB03)

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
