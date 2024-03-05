"""LILYGO TTGO LoRa32 MicroPython Helper Library."""

from machine import Pin, SoftI2C, Signal

from lilygo_oled import OLED

from micropython import const


class Lora32Base:
    """Base class defining common pins."""

    def __init__(self, define_helpers=True):
        # LORA
        self.LORA_MOSI = 27
        self.LORA_MISO = 19
        self.LORA_SCLK = 5
        self.LORA_CS = 18
        self.LORA_DIO = 26
        self.LORA_RST = 23

        # DAC
        self.DAC1 = 26

        # LED
        self.LED = 25

        # OLED
        self.OLED_SDA = 21
        self.OLED_SCL = 22

        if define_helpers:
            self.create_helpers()

    def create_helpers(self):
        self.led = Pin(self.LED, Pin.OUT)
        self.i2c = SoftI2C(scl=Pin(self.OLED_SCL), sda=Pin(self.OLED_SDA))
        self.oled = OLED(self.i2c)


class Lora32v1_0(Lora32Base):
    """Device Support for LILYGO TTGO LoRa32 v1.0."""

    def __init__(self):
        super().__init__(define_helpers=False)

        # v1.0 has different pins for the following
        self.LORA_RST = 14
        self.OLED_SDA = 4
        self.OLED_SCL = 15

        # Also has a reset for the OLED that the others don't have
        self.OLED_RST = 16

        super().create_helpers()


class Lora32v1_2(Lora32Base):
    """Device Support for LILYGO TTGO LoRa32 v1.2 (T-Fox)."""

    def __init__(self):
        super().__init__()

        # v1.2 Has a DS3231 RTC
        self.DS3231_SDA = 21
        self.DS3231_SCL = 22


class Lora32(Lora32Base):
    """Device Support for LILYGO TTGO LoRa32 v1.6 and v2.0."""

    def __init__(self):
        super().__init__()

        # v1.6 and v2.0 support an SDCard
        self.SD_CS = 13
        self.SD_MOSI = 15
        self.SD_MISO = 2
        self.SD_SCLK = 14
