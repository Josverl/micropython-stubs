import network


# ref : https://github.com/Josverl/micropython-stubber/issues/338
wlan = network.WLAN(network.STA_IF)

wlan.config(pm = 0xa11140) # set power mode to get WiFi power-saving off (if needed)