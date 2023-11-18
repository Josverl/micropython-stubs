# https://docs.micropython.org/en/latest/esp32/quickref.html#dht-driver
# DHT driver
# The DHT driver is implemented in software and works on all pins:

import dht
import machine

dht_11 = dht.DHT11(machine.Pin(4))
dht_11.measure()
dht_11.temperature()  # eg. 23 (°C)
dht_11.humidity()  # eg. 41 (% RH)

dht_12 = dht.DHT22(machine.Pin(5))
dht_12.measure()
dht_12.temperature()  # eg. 23.6 (°C)
dht_12.humidity()  # eg. 41.3 (% RH)
