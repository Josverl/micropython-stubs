"""
Basic typing for polyscript

https://pyscript.github.io/polyscript/#the-polyscript-module
""" 
# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed


# https://github.com/pyscript/polyscript


# XWorker	from polyscript import XWorker	described in the XWorker part.
# config	from polyscript import config	custom only: the used config as object literal
# currentScript	from polyscript import currentScript	it’s an explicit, always correct, reference to the current node running the generic script code.
# js_modules	from polyscript import js_modules	described in the Extra config Features part.
# lazy_py_modules	from polyscript import lazy_py_modules	allows, only in Python related interpreters, and without needing static config entries, to import lazily any available module.
# storage	from polyscript import storage	a utility to instantiate a named idb-map that can be consumed synchronously.
# JSON	from polyscript import JSON	a utility to stringify/parse more complex or recursive data via


from typing import Tuple

# avoid name collisions
import storage as _storage

storage = _storage.storage



async def lazy_py_modules(*args: str) -> Tuple:
    """
    allows, only in Python related interpreters, and without needing static config entries, to import lazily any available module.

    Example: 
        from polyscript import lazy_py_modules
        matplotlib, regex, = await lazy_py_modules("matplotlib", "regex")
        print(matplotlib, regex)

    """

    ...

