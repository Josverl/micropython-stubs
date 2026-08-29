# PyScript 2026.7.3: FFI and generic Storage subclass contracts.
from pyscript import Storage, storage
from pyscript.ffi import assign, create_proxy, direct, gather, is_none, query, to_js


def callback(value):
    print(value)


proxy = create_proxy(callback)
js_value = to_js({"value": 1})
merged = assign(js_value, {"other": 2})
remote = direct(merged)
print(proxy, remote, is_none(None))


class Preferences(Storage):
    pass


async def check_storage():
    preferences: Preferences = await storage("preferences", Preferences)
    preferences["theme"] = "dark"
    await preferences.sync()
    print(gather, query)
