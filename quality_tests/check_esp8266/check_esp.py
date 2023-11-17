# ref: https://docs.micropython.org/en/latest/esp8266/quickref.html
# The esp module:
import esp
from machine import Pin

esp.osdebug(None)  # turn off vendor O/S debugging messages
esp.osdebug(0)  # redirect vendor O/S debugging messages to UART(0)


sector_no = 1  # Placeholders
byte_offset = 0
buffer = b"0000"

# low level methods to interact with flash storage
esp.flash_size()
esp.flash_user_start()
esp.flash_erase(sector_no)
esp.flash_write(byte_offset, buffer)
esp.flash_read(byte_offset, len(buffer))

# Neopixel
# Note: ESP8266 only
# For low-level driving of a NeoPixel:
pin = Pin(18)
grb_buf = (1, 20, 2, 40)
is800khz = False
esp.neopixel_write(pin, grb_buf, is800khz)  # stubs-ignore: version<=1.19.1 

