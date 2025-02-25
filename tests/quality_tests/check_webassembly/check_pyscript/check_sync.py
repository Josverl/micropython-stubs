# pyscript.sync - https://docs.pyscript.net/2025.2.3/api/#pyscriptsync

from pyscript import PyWorker, display

def hello(name="world"):
    display(f"Hello, {name}")

worker = PyWorker("./worker.py")
worker.sync.hello = hello


from pyscript import sync

sync.hello("PyScript")
