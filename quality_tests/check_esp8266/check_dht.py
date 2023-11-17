# https://docs.micropython.org/en/latest/esp32/quickref.html#dht-driver
# DHT driver
# The DHT driver is implemented in software and works on all pins:

import dht
import machine

d = dht.DHT11(machine.Pin(4))
d.measure()
d.temperature()  # eg. 23 (°C)
d.humidity()  # eg. 41 (% RH)

d = dht.DHT22(machine.Pin(4))
d.measure()
d.temperature()  # eg. 23.6 (°C)
d.humidity()  # eg. 41.3 (% RH)
