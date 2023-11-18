import espnow
import machine

enow = espnow.ESPNow()

def server():
    peers = []
    for peer, msg in enow:
        if peer is None:
            return
        if peer not in peers:
            peers.append(peer)
            try:
                enow.add_peer(peer)
            except OSError:
                pass

        #  Echo the MAC and message back to the sender
        if not enow.send(peer, msg):
            print("ERROR: send() failed to", peer)
            return

        if msg == b"!done":
            return
        elif msg == b"!reset":
            machine.reset()
