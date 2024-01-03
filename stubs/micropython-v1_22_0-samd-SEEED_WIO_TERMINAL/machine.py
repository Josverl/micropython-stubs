"""
Module: 'machine' on micropython-v1.22.0-samd-SEEED_WIO_TERMINAL
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'cpu': 'SAMD51P19A', 'mpy': 'v6.2', 'arch': 'armv7emsp'}
# Stubber: v1.16.2
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
        SDA0: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA13, mode=IN, pull=PULL_OFF)
        QSPI_SCK: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB10, mode=IN, pull=PULL_OFF)
        QSPI_D3: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA11, mode=IN, pull=PULL_OFF)
        QSPI_D2: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA10, mode=IN, pull=PULL_OFF)
        RX: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB27, mode=IN, pull=PULL_OFF)
        SCL1: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA16, mode=IN, pull=PULL_OFF)
        SCL0: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA12, mode=IN, pull=PULL_OFF)
        SCK: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB03, mode=IN, pull=PULL_OFF)
        QSPI_D1: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA09, mode=IN, pull=PULL_OFF)
        MIC: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC30, mode=IN, pull=PULL_OFF)
        LED_LCD: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC05, mode=IN, pull=PULL_OFF)
        LED_BLUE: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA15, mode=OUT, pull=PULL_OFF)
        MISO: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB00, mode=IN, pull=PULL_OFF)
        QSPI_D0: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA08, mode=IN, pull=PULL_OFF)
        QSPI_CS: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB11, mode=IN, pull=PULL_OFF)
        MOSI: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB02, mode=IN, pull=PULL_OFF)
        LCD_YU: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC11, mode=IN, pull=PULL_OFF)
        SDA1: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA17, mode=IN, pull=PULL_OFF)
        SWITCH_Y: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD09, mode=IN, pull=PULL_OFF)
        SWITCH_X: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD08, mode=IN, pull=PULL_OFF)
        SWITCH_U: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD20, mode=IN, pull=PULL_OFF)
        SWITCH_Z: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD10, mode=IN, pull=PULL_OFF)
        USB_DP: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA25, mode=OUT, pull=PULL_OFF)
        USB_DM: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA24, mode=OUT, pull=PULL_OFF)
        TX: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB26, mode=IN, pull=PULL_OFF)
        SWITCH_B: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD12, mode=IN, pull=PULL_OFF)
        SD_MISO: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC18, mode=IN, pull=PULL_OFF)
        SD_DET: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD21, mode=IN, pull=PULL_OFF)
        SD_CS: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC19, mode=IN, pull=PULL_OFF)
        SD_MOSI: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC16, mode=IN, pull=PULL_OFF)
        SWDIO: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA31, mode=IN, pull=PULL_OFF)
        SWCLK: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA30, mode=IN, pull=PULL_OFF)
        SD_SCK: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC17, mode=IN, pull=PULL_OFF)
        USB_SOF: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA23, mode=IN, pull=PULL_OFF)
        ENABLE_5V: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC14, mode=IN, pull=PULL_OFF)
        BUTTON_2: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC27, mode=IN, pull=PULL_OFF)
        BUTTON_1: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC26, mode=IN, pull=PULL_OFF)
        A8_D8: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA06, mode=IN, pull=PULL_OFF)
        BUTTON_3: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC28, mode=IN, pull=PULL_OFF)
        ENABLE_3V3: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC15, mode=IN, pull=PULL_OFF)
        CS: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB01, mode=IN, pull=PULL_OFF)
        BUZZER: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD11, mode=IN, pull=PULL_OFF)
        A7_D7: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB07, mode=IN, pull=PULL_OFF)
        A2_D2: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA07, mode=IN, pull=PULL_OFF)
        A1_D1: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB09, mode=IN, pull=PULL_OFF)
        A0_D0: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB08, mode=IN, pull=PULL_OFF)
        A3_D3: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB04, mode=IN, pull=PULL_OFF)
        A6_D6: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA04, mode=IN, pull=PULL_OFF)
        A5_D5: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB06, mode=IN, pull=PULL_OFF)
        A4_D4: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB05, mode=IN, pull=PULL_OFF)
        LCD_YD: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC13, mode=IN, pull=PULL_OFF)
        GPCLK0: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB15, mode=IN, pull=PULL_OFF)
        LCD_MOSI: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB19, mode=IN, pull=PULL_OFF)
        LCD_MISO: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB18, mode=IN, pull=PULL_OFF)
        LCD_D_C: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC06, mode=IN, pull=PULL_OFF)
        LCD_RESET: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC07, mode=IN, pull=PULL_OFF)
        LCD_XR: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC12, mode=IN, pull=PULL_OFF)
        LCD_XL: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC10, mode=IN, pull=PULL_OFF)
        LCD_SCK: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB20, mode=IN, pull=PULL_OFF)
        LCD_CS: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB21, mode=IN, pull=PULL_OFF)
        I2C_BCLK: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB16, mode=IN, pull=PULL_OFF)
        GPCLK2: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB13, mode=IN, pull=PULL_OFF)
        GPCLK1: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB12, mode=IN, pull=PULL_OFF)
        I2S_LRCLK: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA20, mode=IN, pull=PULL_OFF)
        LCD_BACKLIGHT: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC05, mode=IN, pull=PULL_OFF)
        I2S_SDOUT: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA22, mode=IN, pull=PULL_OFF)
        I2S_SDIN: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA21, mode=IN, pull=PULL_OFF)

        def __init__(self, *argv, **kwargs) -> None:
            ...

    class cpu:
        PC04: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC04, mode=IN, pull=PULL_OFF)
        PC14: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC14, mode=IN, pull=PULL_OFF)
        PC05: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC05, mode=IN, pull=PULL_OFF)
        PC01: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC01, mode=IN, pull=PULL_OFF)
        PC03: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC03, mode=IN, pull=PULL_OFF)
        PC02: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC02, mode=IN, pull=PULL_OFF)
        PC12: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC12, mode=IN, pull=PULL_OFF)
        PC06: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC06, mode=IN, pull=PULL_OFF)
        PC13: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC13, mode=IN, pull=PULL_OFF)
        PC07: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC07, mode=IN, pull=PULL_OFF)
        PC11: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC11, mode=IN, pull=PULL_OFF)
        PC10: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC10, mode=IN, pull=PULL_OFF)
        PB24: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB24, mode=IN, pull=PULL_OFF)
        PC00: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC00, mode=IN, pull=PULL_OFF)
        PB25: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB25, mode=IN, pull=PULL_OFF)
        PB21: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB21, mode=IN, pull=PULL_OFF)
        PB23: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB23, mode=IN, pull=PULL_OFF)
        PB22: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB22, mode=IN, pull=PULL_OFF)
        PB30: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB30, mode=IN, pull=PULL_OFF)
        PB26: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB26, mode=IN, pull=PULL_OFF)
        PB31: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB31, mode=IN, pull=PULL_OFF)
        PB27: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB27, mode=IN, pull=PULL_OFF)
        PB29: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB29, mode=IN, pull=PULL_OFF)
        PB28: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB28, mode=IN, pull=PULL_OFF)
        PB20: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB20, mode=IN, pull=PULL_OFF)
        PD00: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD00, mode=IN, pull=PULL_OFF)
        PC15: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC15, mode=IN, pull=PULL_OFF)
        PD01: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD01, mode=IN, pull=PULL_OFF)
        PC28: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC28, mode=IN, pull=PULL_OFF)
        PC31: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC31, mode=IN, pull=PULL_OFF)
        PC30: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC30, mode=IN, pull=PULL_OFF)
        PD12: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD12, mode=IN, pull=PULL_OFF)
        PD08: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD08, mode=IN, pull=PULL_OFF)
        PD20: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD20, mode=IN, pull=PULL_OFF)
        PD09: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD09, mode=IN, pull=PULL_OFF)
        PD11: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD11, mode=IN, pull=PULL_OFF)
        PD10: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD10, mode=IN, pull=PULL_OFF)
        PC19: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC19, mode=IN, pull=PULL_OFF)
        PC27: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC27, mode=IN, pull=PULL_OFF)
        PC20: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC20, mode=IN, pull=PULL_OFF)
        PC16: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC16, mode=IN, pull=PULL_OFF)
        PC18: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC18, mode=IN, pull=PULL_OFF)
        PC17: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC17, mode=IN, pull=PULL_OFF)
        PC25: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC25, mode=IN, pull=PULL_OFF)
        PC21: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC21, mode=IN, pull=PULL_OFF)
        PC26: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC26, mode=IN, pull=PULL_OFF)
        PC22: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC22, mode=IN, pull=PULL_OFF)
        PC24: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC24, mode=IN, pull=PULL_OFF)
        PC23: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PC23, mode=IN, pull=PULL_OFF)
        PD21: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PD21, mode=IN, pull=PULL_OFF)
        PA15: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA15, mode=OUT, pull=PULL_OFF)
        PA23: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA23, mode=IN, pull=PULL_OFF)
        PA16: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA16, mode=IN, pull=PULL_OFF)
        PA12: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA12, mode=IN, pull=PULL_OFF)
        PA14: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA14, mode=IN, pull=PULL_OFF)
        PA13: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA13, mode=IN, pull=PULL_OFF)
        PA21: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA21, mode=IN, pull=PULL_OFF)
        PA17: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA17, mode=IN, pull=PULL_OFF)
        PA22: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA22, mode=IN, pull=PULL_OFF)
        PA18: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA18, mode=IN, pull=PULL_OFF)
        PA20: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA20, mode=IN, pull=PULL_OFF)
        PA19: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA19, mode=IN, pull=PULL_OFF)
        PA03: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA03, mode=IN, pull=PULL_OFF)
        PA11: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA11, mode=IN, pull=PULL_OFF)
        PA04: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA04, mode=IN, pull=PULL_OFF)
        PA00: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA00, mode=IN, pull=PULL_OFF)
        PA02: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA02, mode=IN, pull=PULL_OFF)
        PA01: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA01, mode=IN, pull=PULL_OFF)
        PA09: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA09, mode=IN, pull=PULL_OFF)
        PA05: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA05, mode=IN, pull=PULL_OFF)
        PA10: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA10, mode=IN, pull=PULL_OFF)
        PA06: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA06, mode=IN, pull=PULL_OFF)
        PA08: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA08, mode=IN, pull=PULL_OFF)
        PA07: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA07, mode=IN, pull=PULL_OFF)
        PB19: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB19, mode=IN, pull=PULL_OFF)
        PB11: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB11, mode=IN, pull=PULL_OFF)
        PA24: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA24, mode=OUT, pull=PULL_OFF)
        PB12: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB12, mode=IN, pull=PULL_OFF)
        PB08: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB08, mode=IN, pull=PULL_OFF)
        PB10: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB10, mode=IN, pull=PULL_OFF)
        PB09: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB09, mode=IN, pull=PULL_OFF)
        PB17: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB17, mode=IN, pull=PULL_OFF)
        PB13: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB13, mode=IN, pull=PULL_OFF)
        PB18: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB18, mode=IN, pull=PULL_OFF)
        PB14: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB14, mode=IN, pull=PULL_OFF)
        PB16: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB16, mode=IN, pull=PULL_OFF)
        PB15: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB15, mode=IN, pull=PULL_OFF)
        PA31: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA31, mode=IN, pull=PULL_OFF)
        PB07: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB07, mode=IN, pull=PULL_OFF)
        PB00: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB00, mode=IN, pull=PULL_OFF)
        PA25: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA25, mode=OUT, pull=PULL_OFF)
        PA30: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA30, mode=IN, pull=PULL_OFF)
        PA27: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PA27, mode=IN, pull=PULL_OFF)
        PB05: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB05, mode=IN, pull=PULL_OFF)
        PB01: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB01, mode=IN, pull=PULL_OFF)
        PB06: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB06, mode=IN, pull=PULL_OFF)
        PB02: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB02, mode=IN, pull=PULL_OFF)
        PB04: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB04, mode=IN, pull=PULL_OFF)
        PB03: Incomplete  ## <class 'Pin'> = Pin(Pin.cpu.PB03, mode=IN, pull=PULL_OFF)

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
