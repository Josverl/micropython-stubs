# Capacitive touch

from machine import TouchPad, Pin

t = TouchPad(Pin(14))
t.read()  # Returns a smaller number when touched
