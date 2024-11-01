from __future__ import annotations
from typing import TypeVar, Text, TYPE_CHECKING

from machine import Pin

# Allow simple references to Pins by either Pin instance, pin name or pin number
AnyPin = TypeVar("AnyPin", Pin, str, int)
"""A machine.Pin instance, pin name or pin number"""
