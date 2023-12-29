import sys

import espnow
import network

# SENDER CODE
# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()  # For ESP8266

reveal_type(espnow.ESPNow)
e = espnow.ESPNow()
e.active(True)
peer = b"\xbb\xbb\xbb\xbb\xbb\xbb"  # MAC address of peer's wifi interface
e.add_peer(peer)  # Must add_peer() before send()

e.send(peer, "Starting...")
for i in range(100):
    e.send(peer, str(i) * 20, True)
e.send(peer, b"end")

## Receiver:

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()  # Because ESP8266 auto-connects to last Access Point

e = espnow.ESPNow()
e.active(True)

while True:
    host, msg = e.recv()
    if msg:  # msg == None if timeout in recv()
        print(host, msg)
        if msg == b"end":
            break

import espnow

e = espnow.ESPNow()
e.active(True)
for mac, msg in e:
    print(mac, msg)
    if mac is None:  # mac, msg will equal (None, None) on timeout
        break

# Documented , but not detected by createstubs.py
print(e.peers_table)  # type: ignore # TODO: espnow ESPNow.peers_table - deal with undetectable attributes
# List of peers (MAC addresses) that have been added
# A reference to the peer device table: a dict of known peer devices and rssi values:

# Broadcast

bcast = b"\xff" * 6
e.add_peer(bcast)
e.send(bcast, "Hello World!")
