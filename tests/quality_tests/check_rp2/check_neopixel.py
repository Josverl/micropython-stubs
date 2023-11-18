# NeoPixel

from machine import Pin
from neopixel import NeoPixel

pin = Pin(0, Pin.OUT)  # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 8)  # create NeoPixel driver on GPIO0 for 8 pixels

# below onlt correct for version 1.21.0 or later
np[0] = (255, 255, 255)  # stubs-ignore: version<1.21.0
np.write()  # write data to all pixels
r, g, b = np[0]  # stubs-ignore: version<1.21.0
