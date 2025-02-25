
# pyscript.PyWorker - https://docs.pyscript.net/2025.2.3/api/#pyscriptpyworker

from pyscript import RUNNING_IN_WORKER, display, sync

display("Hello World", target="output", append=True)

# will log into devtools console
print(RUNNING_IN_WORKER)  # True
print("sleeping")
sync.sleep(1)
print("awake")

from pyscript import PyWorker

# type MUST be either `micropython` or `pyodide`
# TODO: rewrite ## <class 'JsProxy'> = <JsProxy 15> to a class 

PyWorker("worker.py", type="micropython")

# pyscript.workers

# <script type="mpy" worker name="py-version">
import sys
def version():
    return sys.version
# define what to export to main consumers
__export__ = ["version"]
# </script>


from pyscript import workers

async def foo_1():
    pyworker = await workers["py-version"]

    # print the pyodide version
    print(await pyworker.version())


from pyscript import document, workers
async def foo_2():

    for el in document.querySelectorAll("[type='py'][worker][name]"):
        await workers[el.getAttribute('name')]

# ... rest of the code