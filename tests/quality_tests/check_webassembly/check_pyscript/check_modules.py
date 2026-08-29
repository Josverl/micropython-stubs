# PyScript 2026.7.3: events, Flatted JSON, display, and utility contracts.
from pyscript import Event, HTML, display, when
from pyscript import flatted
from pyscript import window
from pyscript.util import NotSupported, as_bytearray, is_awaitable

event = Event()


def listener(value: object) -> None:
    print(value)


event.add_listener(listener)
when([event])(listener)
event.remove_listener(listener)

serialized: str = flatted.stringify({"name": "PyScript"}, indent=2)
restored: object = flatted.parse(serialized)
html = HTML("<strong>PyScript</strong>")
display(html)

unsupported = NotSupported("feature", "not available")
converted: bytearray = as_bytearray(window.ArrayBuffer.new(0))
awaitable: bool = is_awaitable(listener)
print(restored, unsupported, converted, awaitable)
