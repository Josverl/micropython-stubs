# PyScript 2026.7.3: HTML display and JavaScript import contracts.
from pyscript import HTML, RUNNING_IN_WORKER, WebSocket, display, js_import, window

# Escaped by default:
display("<em>em</em>")  # &lt;em&gt;em&lt;/em&gt;

# Un-escaped raw content inserted into the page:
display(HTML("<em>em</em>"))  # <em>em</em>

if RUNNING_IN_WORKER:
    display(HTML("<em>worker</em>"), target="output")


def onopen(event):
    print(event.type)
    ws.send("hello")


def onmessage(event):
    print(event.type, event.data)
    ws.close()


def onclose(event):
    print(event.type)


ws = WebSocket(url="ws://localhost:5037/")
ws.onopen = onopen
ws.onmessage = onmessage
ws.onclose = onclose


async def foo_4():
    escaper = await js_import("https://esm.run/html-escaper")
    window.console.log(escaper)
