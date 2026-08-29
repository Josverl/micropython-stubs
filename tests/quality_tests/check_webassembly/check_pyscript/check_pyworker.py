# PyScript 2026.7.3: PyWorker, worker-context sync, and named-worker access.

from pyscript import RUNNING_IN_WORKER, display, sync

display("Hello World", target="output", append=True)

# will log into devtools console
print(RUNNING_IN_WORKER)  # True
print("sleeping")
sync.sleep(1)
print("awake")

from pyscript import PyWorker

PyWorker("worker.py", type="micropython")

from pyscript import workers


async def foo_1():
    pyworker = await workers["py-version"]

    print(await pyworker.version())


from pyscript import document, workers


async def foo_2():
    for el in document.querySelectorAll("[type='py'][worker][name]"):
        await workers[el.getAttribute("name")]
