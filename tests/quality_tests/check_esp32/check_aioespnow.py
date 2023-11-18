# typed: ignore
# Async
# TODO : how is aioespnow documented / detected
# Todo : add inheritance to table

import asyncio

import aioespnow  # type: ignore
import network

# A WLAN interface must be active to send()/recv()
network.WLAN(network.STA_IF).active(True)

e = aioespnow.AIOESPNow()  # Returns AIOESPNow enhanced with async support
e.active(True)
peer = b"\xbb\xbb\xbb\xbb\xbb\xbb"
e.add_peer(peer)


# Send a periodic ping to a peer
async def heartbeat(e, peer, period=30):
    while True:
        if not await e.asend(peer, b"ping"):
            print("Heartbeat: peer not responding:", peer)
        else:
            print("Heartbeat: ping", peer)
        await asyncio.sleep(period)


# Echo any received messages back to the sender
async def echo_server(e):
    async for mac, msg in e:
        print("Echo:", msg)
        try:
            await e.asend(mac, msg)
        except OSError as err:
            if len(err.args) > 1 and err.args[1] == "ESP_ERR_ESPNOW_NOT_FOUND":
                e.add_peer(mac)
                await e.asend(mac, msg)


async def main(e, peer, timeout, period):
    asyncio.create_task(heartbeat(e, peer, period))
    asyncio.create_task(echo_server(e))
    await asyncio.sleep(timeout)


asyncio.run(main(e, peer, 120, 10))
