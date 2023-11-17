# Neopixel
from machine import Pin
from neopixel import NeoPixel

pin = Pin(2, Pin.OUT)  # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 8)  # create NeoPixel driver on GPIO0 for 8 pixels
np[0] = (255, 255, 255)  # stubs-ignore : version <= 1.19.1
np.write()  # 
r, g, b = np[0]  # stubs-ignore : version <= 1.19.1
