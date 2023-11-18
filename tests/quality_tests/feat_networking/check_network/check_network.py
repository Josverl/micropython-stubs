# The network module:

import network

wlan = network.WLAN(network.STA_IF)  # create station interface
wlan.active(True)  # activate the interface
wlan.scan()  # scan for access points
wlan.isconnected()  # check if the station is connected to an AP
wlan.connect("essid", "password")  # connect to an AP
wlan.config("mac")  # get the interface's MAC address
wlan.ifconfig()  # get the interface's IP/netmask/gw/DNS addresses

ap = network.WLAN(network.AP_IF)  # create access-point interface
ap.config(essid="ESP-AP")  # set the ESSID of the access point
ap.config(max_clients=10)  # set how many clients can connect to the network
ap.active(True)  # activate the interface


# A useful function for connecting to your local WiFi network is:


def do_connect():
    import network

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting to network...")
        wlan.connect("essid", "password")
        while not wlan.isconnected():
            pass
    print("network config:", wlan.ifconfig())
