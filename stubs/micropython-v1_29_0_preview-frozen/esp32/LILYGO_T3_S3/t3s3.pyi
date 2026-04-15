# Micropython v1.29.0-preview frozen stubs
from _typeshed import Incomplete
from micropython import const as const

_pins: Incomplete
_OLED_ADDR: int
_VBAT_DIVIDER_RATIO: float

def get_battery_voltage():
    """Read battery voltage via ADC with voltage divider compensation.

    Returns voltage in volts (e.g. 3.85). Accuracy is approximate.
    """

def set_led(state) -> None:
    """Turn on-board LED on (True) or off (False). LED is active HIGH."""

def get_button():
    """Read boot button state. Returns True when pressed (active LOW)."""

def get_oled():
    """Create and return an SSD1306 128x64 OLED display instance."""

def get_lora(lora_cfg=None):
    """Create and return a configured SX1262 LoRa modem for the T3-S3.

    Optional lora_cfg dict, e.g.:
        {"freq_khz": 869500, "sf": 7, "bw": "125", "coding_rate": 5, "output_power": 14}
    """
