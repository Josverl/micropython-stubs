# DS18S20 and DS18B20 devices:
import time

import ds18x20
import onewire
from machine import Pin

ow = onewire.OneWire(Pin(12))
ds = ds18x20.DS18X20(ow)
roms = ds.scan()
ds.convert_temp()
time.sleep_ms(750)
for rom in roms:
    print(ds.read_temp(rom))
