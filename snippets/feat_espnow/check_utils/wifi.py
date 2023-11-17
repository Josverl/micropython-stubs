# """
# wifi.py: Useful functions for setting up wifi on ESP32 and ESP8266 devices

# These functions are designed to robustly and reliably account for differences
# between esp8266 and esp32 devices and to ensure the wifi is always in a fully
# known state (even after soft_reset).

# Examples:

#     import wifi

#     # Reset wifi to know state (STA is disconnected)
#     sta, ap = wifi.reset()               # STA on, AP off, channel=1
#     sta, ap = wifi.reset(sta=True, ap=True, channel=5)  # STA on, AP on, channel=5
#     sta, ap = wifi.reset(False, False)   # STA off, AP off, channel=1
#     sta, ap = wifi.reset(ap=True)        # STA on, AP on, channel=1
#     sta, ap = wifi.reset(channel=11)     # STA on, AP off, channel=11

#     # Set/get the channel
#     wifi.channel(11)
#     print(wifi.channel())

#     # Connect/disconnect from a wifi network
#     wifi.connect("ssid", "password")
#     wifi.connect()                       # Reconnect to last wifi network
#     wifi.disconnect()                    # Disconnect from wifi network

#     # Print verbose details of the device wifi config
#     wifi.status()

# Config:

#     # Power save mode used whenever connected() - default is WIFI_PS_NONE
#     wifi.ps_mode = network.WIFI_PS_MIN_MODEM
#     wifi.timeout = 30             # Timeout for connect to network (seconds)
#     wifi.sta    # The STA_IF wlan interface
#     wifi.ap     # The AP_IF wlan interface
# """

import sys
import time
import network


class TimeoutError(Exception):
    pass


this = sys.modules[__name__]  # A reference to this module

is_esp8266 = sys.platform == "esp8266"
wlans = [network.WLAN(w) for w in (network.STA_IF, network.AP_IF)]
sta, ap = wlans
_sta, _ap = wlans
timeout = 20  # (seconds) timeout on connect()
default_channel = 1
try:
    default_pm_mode = sta.PM_PERFORMANCE
except AttributeError:
    default_pm_mode = None
try:
    default_protocol = network.MODE_11B | network.MODE_11G | network.MODE_11N
except AttributeError:
    default_protocol = None


def channel(channel=0):
    if channel == 0:
        return _ap.config("channel")
    if _sta.isconnected():
        raise OSError("can not set channel when connected to wifi network.")
    if _ap.isconnected():
        raise OSError("can not set channel when clients are connected to AP.")
    if _sta.active() and not is_esp8266:
        _sta.config(channel=channel)  # On ESP32 use STA interface
        return _sta.config("channel")
    else:
        # On ESP8266, use the AP interface to set the channel
        ap_save = _ap.active()
        _ap.active(True)
        _ap.config(channel=channel)
        _ap.active(ap_save)
        return _ap.config("channel")


def wait_for(fun, timeout=timeout):
    start = time.time()
    while not fun():
        if time.time() - start > timeout:
            raise TimeoutError()
        time.sleep(0.1)


def disconnect():
    _sta.disconnect()
    wait_for(lambda: not _sta.isconnected(), 5)


def connect(*args, **kwargs):
    _sta.active(True)
    disconnect()
    _sta.connect(*args, **kwargs)
    wait_for(lambda: _sta.isconnected())
    ssid, chan = _sta.config("ssid"), channel()
    print('Connected to "{}" on wifi channel {}'.format(ssid, chan))


def reset(
    sta=True,
    ap=False,
    channel=default_channel,
    pm=default_pm_mode,
    protocol=default_protocol,
):
    "Reset wifi to STA_IF on, AP_IF off, channel=1 and disconnected"
    _sta.active(False)  # Force into known state by turning off radio
    _ap.active(False)
    _sta.active(sta)  # Now set to requested state
    _ap.active(ap)
    if sta:
        disconnect()  # For ESP8266
        try:
            _sta.config(pm=pm)
        except (ValueError):
            pass
    try:
        wlan = _sta if sta else _ap if ap else None
        if wlan and (protocol is not None):
            wlan.config(protocol=protocol)
    except (ValueError, RuntimeError):
        pass
    this.channel(channel)
    return _sta, _ap


def status():
    from binascii import hexlify

    for name, w in (("STA", _sta), ("AP", _ap)):
        active = "on," if w.active() else "off,"
        mac = w.config("mac")
        hex = hexlify(mac, ":").decode()
        print("{:3s}: {:4s} mac= {} ({})".format(name, active, hex, mac))
    if _sta.isconnected():
        print("     connected:", _sta.config("ssid"), end="")
    else:
        print("     disconnected", end="")
    print(", channel={:d}".format(_ap.config("channel")), end="")
    pm_mode = None
    try:
        pm_mode = _sta.config("pm")
        names = {
            _sta.PM_NONE: "PM_NONE",
            _sta.PM_PERFORMANCE: "PM_PERFORMANCE",
            _sta.PM_POWERSAVE: "PM_POWERSAVE",
            }
        print(", pm={:d} ({})".format(pm_mode, names[pm_mode]), end="")
    except (AttributeError, ValueError):
        print(", pm={}".format(pm_mode), end="")
    try:
        names = ("MODE_11B", "MODE_11G", "MODE_11N", "MODE_LR")
        protocol = _sta.config("protocol")
        try:
            p = "|".join((x for x in names if protocol & getattr(network, x)))
        except AttributeError:
            p = ""
        print(", protocol={:d} ({})".format(protocol, p), end="")
    except ValueError:
        pass
    print()
    if _sta.isconnected():
        print("     ifconfig:", _sta.ifconfig())
