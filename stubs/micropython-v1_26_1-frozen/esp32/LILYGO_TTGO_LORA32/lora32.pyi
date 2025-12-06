from _typeshed import Incomplete
from machine import Signal as Signal
from micropython import const as const

class Lora32Base:
    """Base class defining common pins."""

    LORA_MOSI: int
    LORA_MISO: int
    LORA_SCLK: int
    LORA_CS: int
    LORA_DIO: int
    LORA_RST: int
    DAC1: int
    LED: int
    OLED_SDA: int
    OLED_SCL: int
    OLED_RST: Incomplete
    def __init__(self, define_helpers: bool = True) -> None: ...
    led: Incomplete
    i2c: Incomplete
    oled: Incomplete
    def create_helpers(self) -> None: ...

class Lora32v1_0(Lora32Base):
    """Device Support for LILYGO TTGO LoRa32 v1.0."""

    LORA_RST: int
    OLED_SDA: int
    OLED_SCL: int
    OLED_RST: int
    def __init__(self) -> None: ...

class Lora32v1_2(Lora32Base):
    """Device Support for LILYGO TTGO LoRa32 v1.2 (T-Fox)."""

    DS3231_SDA: int
    DS3231_SCL: int
    def __init__(self) -> None: ...

class Lora32(Lora32Base):
    """Device Support for LILYGO TTGO LoRa32 v1.6 and v2.0."""

    SD_CS: int
    SD_MOSI: int
    SD_MISO: int
    SD_SCLK: int
    def __init__(self) -> None: ...
