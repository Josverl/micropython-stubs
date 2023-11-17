# the hello world of IoT
# This short script serves as a sanity check.
# It makes the onboard LED blink

# ref: https://docs.micropython.org/en/latest/rp2/quickref.html

import utime as time
from machine import Pin


# Blink

# led = Pin()
led = Pin(1, value=2)
led = Pin(13, Pin.OUT)


for i in range(2):  # no infinite loop
    led.on()
    time.sleep_ms(250)
    led.off()
    time.sleep_ms(250)







