# Capacitive touch

from machine import TouchPad, Pin  # stubs-ignore : board.endswith("_c6" )

t = TouchPad(Pin(14))
t.read()  # Returns a smaller number when touched
