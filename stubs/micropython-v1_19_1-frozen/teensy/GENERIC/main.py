# Micropython 1.19.1 frozen stubs
import pyb

print("Executing main.py")

led = pyb.LED(1)

led.on()
pyb.delay(100)
led.off()
pyb.delay(100)
led.on()
pyb.delay(100)
led.off()
