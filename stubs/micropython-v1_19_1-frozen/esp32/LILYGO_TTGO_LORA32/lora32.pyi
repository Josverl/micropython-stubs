# Micropython 1.19.1 frozen stubs
from _typeshed import Incomplete
from machine import Signal as Signal

class Lora32Base:
    LORA_MOSI: Incomplete
    LORA_MISO: Incomplete
    LORA_SCLK: Incomplete
    LORA_CS: Incomplete
    LORA_DIO: Incomplete
    LORA_RST: Incomplete
    DAC1: Incomplete
    LED: Incomplete
    OLED_SDA: Incomplete
    OLED_SCL: Incomplete
    def __init__(self, define_helpers: bool = ...) -> None: ...
    led: Incomplete
    i2c: Incomplete
    oled: Incomplete
    def create_helpers(self) -> None: ...

class Lora32v1_0(Lora32Base):
    LORA_RST: Incomplete
    OLED_SDA: Incomplete
    OLED_SCL: Incomplete
    OLED_RST: Incomplete
    def __init__(self) -> None: ...

class Lora32v1_2(Lora32Base):
    DS3231_SDA: Incomplete
    DS3231_SCL: Incomplete
    def __init__(self) -> None: ...

class Lora32(Lora32Base):
    SD_CS: Incomplete
    SD_MOSI: Incomplete
    SD_MISO: Incomplete
    SD_SCLK: Incomplete
    def __init__(self) -> None: ...
