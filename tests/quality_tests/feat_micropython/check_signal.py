"""Test for the Signal class, verify that it is callable"""

from machine import Pin, Signal

s = Signal(2, Signal.IN, invert=True)
s(2)
s()


p15 = Pin(15, Pin.OUT)
p15(1)
p15()
