from machine import Signal as Signal
from typing import Any

class Lora32Base:
    LORA_MOSI: Any
    LORA_MISO: Any
    LORA_SCLK: Any
    LORA_CS: Any
    LORA_DIO: Any
    LORA_RST: Any
    DAC1: Any
    LED: Any
    OLED_SDA: Any
    OLED_SCL: Any
    def __init__(self, define_helpers: bool = ...) -> None: ...
    led: Any
    i2c: Any
    oled: Any
    def create_helpers(self) -> None: ...

class Lora32v1_0(Lora32Base):
    LORA_RST: Any
    OLED_SDA: Any
    OLED_SCL: Any
    OLED_RST: Any
    def __init__(self) -> None: ...

class Lora32v1_2(Lora32Base):
    DS3231_SDA: Any
    DS3231_SCL: Any
    def __init__(self) -> None: ...

class Lora32(Lora32Base):
    SD_CS: Any
    SD_MOSI: Any
    SD_MISO: Any
    SD_SCLK: Any
    def __init__(self) -> None: ...
