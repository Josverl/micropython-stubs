from pyscript import storage
from pyscript.ffi import assign, create_proxy, direct, is_none, to_js


def callback(value):
    print(value)


proxy = create_proxy(callback)
js_value = to_js({"value": 1})
merged = assign(js_value, {"other": 2})
remote = direct(merged)
print(proxy, remote, is_none(None))


async def check_storage():
    preferences = await storage("preferences")
    preferences["theme"] = "dark"
    await preferences.sync()
