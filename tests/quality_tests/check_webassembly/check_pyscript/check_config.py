
#pyscript.config
from pyscript import config


# It's just a dict.
print(config.get("files"))
# This will be either "mpy" or "py" depending on the current interpreter.
print(config["type"])


# pyscript.current_target
from pyscript import display, current_target
display(f"current_target(): {current_target()}")

# pyscript.display

from pyscript import display
display("PyScript", append=False)

display("PyScript", target="my-h2", append=False)

# pyscript.document

# pyscript.fetch
# https://docs.pyscript.net/2025.2.3/api/#pyscriptfetch
from pyscript import fetch

async def foo():
    # TODO: change .pyi to async def 
    response = await fetch("https://example.com")
    if response.ok:
        data = await response.text()
    else:
        print(response.status)

    # TODO: returns 'JavaScript response object'
    result = await fetch("https://example.com", method="POST", body="HELLO").text()

# pyscript.ffi


# pyscript.js_modules




#
#