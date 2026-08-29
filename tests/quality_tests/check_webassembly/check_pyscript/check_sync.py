# PyScript 2026.7.3: context-dependent sync proxy contract.

from pyscript import PyWorker, display


def hello(name="world"):
    display(f"Hello, {name}")


worker = PyWorker("./worker.py")
worker.sync.hello = hello


from pyscript import sync

sync.hello("PyScript")
