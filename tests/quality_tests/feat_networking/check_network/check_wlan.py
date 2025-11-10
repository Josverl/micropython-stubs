import network


# ref : https://github.com/Josverl/micropython-stubber/issues/338
wlan = network.WLAN(network.STA_IF)

wlan.config(pm = 0xa11140) # set power mode to get WiFi power-saving off (if needed)

# Better: Use symbolic constants for portability across different MicroPython ports
wlan.config(pm=network.WLAN.PM_NONE)  # Disable power management
wlan.config(pm=network.WLAN.PM_PERFORMANCE)  # Balanced power/performance
wlan.config(pm=network.WLAN.PM_POWERSAVE)  # Maximum power saving