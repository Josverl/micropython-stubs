# lazyespnow module for MicroPython on ESP32
# MIT license; Copyright (c) 2022 Glenn Moloney @glenn20

import time
import network
import espnow


def _handle_esperror(self, err, peer):
    if len(err.args) < 2:
        raise err

    esperr = err.args[1]
    if esperr == 'ESP_ERR_ESPNOW_NOT_INIT':
        if self.debug:
            print("LazyESPNow: init()")
        self.active(True)

    elif esperr == 'ESP_ERR_ESPNOW_NOT_FOUND':
        if self.debug:
            print("LazyESPNow: add_peer()")
        # Restore the saved options for this peer - if we have it
        args = self._saved_peers.get(peer, [])
        self.add_peer(peer, *args)

    elif esperr == 'ESP_ERR_ESPNOW_EXIST':
        if self.debug: print("LazyESPNow: del_peer()")
        self.del_peer(peer)

    elif esperr == 'ESP_ERR_ESPNOW_FULL':
        if self.debug: print("LazyESPNow: del_peer()")
        # Peers are listed in the order they were registered
        peers = self.get_peers()
        n_tot, _n_enc = self.peer_count()
        # If less than the max peers(20) are registered, assume we hit the limit
        # on encrypted peers(6) and delete an encrypted peer, otherwise an
        # unencrypted peer.
        is_encrypted = n_tot < espnow.MAX_TOTAL_PEER_NUM
        # We will try removing the first encrypted/unencrypted host
        peer, *args = next((p for p in peers if p[4] == is_encrypted))
        self._saved_peers[peer] = args  # Save options for deleted peer
        self.del_peer(peer)

    elif esperr == 'ESP_ERR_ESPNOW_IF':
        channel, if_idx = self.get_peer(peer)[2:3] if peer else 0, self.default_if
        if self.debug: print("LazyESPNow: activating", ('STA_IF','AP_IF')[if_idx])
        wlan = network.WLAN(if_idx)
        wlan.active(True)
        if if_idx == network.STA_IF:
            wlan.disconnect()         # ESP8266 may auto-connect to last AP.
        if channel:
            wlan.config(channel=channel)
        wlan.config(ps_mode=self.ps_mode)

    else:
        raise err

# A wrapper for methods which catches esp errors and tries to fix them
# Eg: if device is not initialised, call active(True)
#     if wifi interface is not active(), set it active(True)
#     if peer is not registered, register it.
def _catch_esperror(method):
    def wrapper(*args, **kwargs):
        for _ in range(5):
            try:
                return method(*args, **kwargs)
            except OSError as err:
                # Correct any esp errors
                peer = args[1] if len(args) > 1 else None
                _handle_esperror(args[0], err, peer)
        raise RuntimeError("_handle_OSError(): ESP Exception handling failed.")

    return wrapper


class LazyESPNow(espnow.ESPNow):
    default_if = network.STA_IF
    debug = None
    _saved_peers = {}
    wlans = [network.WLAN(i) for i in [network.STA_IF, network.AP_IF]]

    def __init__(self, default_if=network.STA_IF):
        self.default_if = default_if
        super().__init__()

    def _check_init(self):
        if not any((w.active() for w in self.wlans)):
            wlan = network.WLAN(self.default_if)
            wlan.active(True)
            if self.default_if == network.STA_IF:
                wlan.disconnect()   # ESP8266 may auto-connect to last AP.

    @_catch_esperror
    def irecv(self, t=None):
        self._check_init()
        return super().irecv(t)

    @_catch_esperror
    def recv(self, t=None):
        self._check_init()
        return super().recv(t)

    @_catch_esperror
    def send(self, mac, msg=None, sync=True):
        if msg is None:
            msg, mac = mac, None  # If msg is None: swap mac and msg
        return self.send(mac, msg, sync)

    @_catch_esperror
    def __next__(self):
        self._check_init()
        return super().__next__()

    @_catch_esperror
    def get_peer(self, mac):
        return super().get_peer(mac)

    @_catch_esperror
    def add_peer(self, mac, *args, **kwargs):
        return super().add_peer(mac, *args, **kwargs)

    def find_peer(self, mac, msg, lmk=None, ifidx=-1, encrypt=None):
        try:
            _ = super().get_peer(mac)
        except OSError:
            self.add_peer(
                mac, lmk, 0, ifidx,
                encrypt if encrypt is not None else bool(lmk))
        for num_tries in (0, 10):
            for chan in range(14):
                super().mod_peer(mac, channel=chan)
                for _ in range(num_tries):
                    if super().send(mac, msg):
                        return True
                    time.sleep(0.10)
        return False
