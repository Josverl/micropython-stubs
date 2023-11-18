# ref : https://docs.micropython.org/en/latest/rp2/quickref.html

import network

# set your Wifi country code
network.country("NL")  # stubs-ignore: version <= 1.19.1 or port in ["esp8266"]
# esp8266 has no network.country() method
