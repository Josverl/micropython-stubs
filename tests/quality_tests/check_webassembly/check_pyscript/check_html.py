
# pyscript.html - https://docs.pyscript.net/2025.2.3/api/#pyscripthtml


from pyscript import display, HTML

# Escaped by default:
display("<em>em</em>")  # &lt;em&gt;em&lt;/em&gt;

from pyscript import display, HTML

# Un-escaped raw content inserted into the page:
display(HTML("<em>em</em>"))  # <em>em</em>


from pyscript import RUNNING_IN_WORKER

if RUNNING_IN_WORKER:
    from pyscript import display, HTML

    # Un-escaped raw content inserted into the page:
    display(HTML("<em>em</em>"))  # <em>em</em>

# pyscript.WebSocket - https://docs.pyscript.net/2025.2.3/api/#pyscriptwebsocket

from pyscript import WebSocket

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

# pyscript.js_import

# TODO: window is not defined in stub 
# from _pyscript import js_import
from pyscript import js_import, window

async def foo_4():
    escaper, = await js_import("https://esm.run/html-escaper")
    window.console.log(escaper)

# pyscript.py_import
from pyscript import py_import

async def foo_5():
    matplotlib, regex, = await py_import("matplotlib", "regex")
    print(matplotlib, regex)





# pyscript.
# pyscript.
# pyscript.
# pyscript.
