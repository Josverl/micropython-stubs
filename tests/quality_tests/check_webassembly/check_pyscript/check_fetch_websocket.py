from pyscript import WebSocket, fetch
from pyscript.websocket import WebSocketEvent


async def check_fetch():
    response = await fetch("https://example.com")
    text = await response.text()
    data = await fetch("https://example.com/data.json").json()
    print(text, data)


def on_message(event: WebSocketEvent):
    if isinstance(event.data, str):
        print(event.data)
    else:
        print(len(event.data))


socket = WebSocket("wss://example.com/socket", onmessage=on_message)
socket.send(bytearray((1, 2, 3)))
socket.close()
