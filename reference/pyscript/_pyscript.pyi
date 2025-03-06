from typing import Any, Callable
from _typeshed import  Incomplete

def js_import(name: str) -> JSModule:
    """Module level __getattr__ that returns an JSModule object for any requested attribute."""
    ...


class JSModule:
    def __init__(self, name) -> None: ...
    def __getattr__(self, field) -> Any | None: ...



class Worker:
    async def sync(self) -> Callable: ...

class XWorker(Worker):
    # https://pyscript.github.io/polyscript/#xworker-options

    polyfill:bool = False
    window: Incomplete = ...

    def __init__(self, 
                 file:str, 
                 a_sync:bool=True,
                 config:str = "",
                 type:str='pyodide', #  pyodide, micropython, ruby-wasm-wasi, wasmoon, webr
                 version:str=...,
                 serviceWorker:str=...,
                 ) -> None: ...
    
    # def isWindowProxy(self, ref:Incomplete) -> bool: ...



class PyWorker(XWorker):
    def __init__(self, name) -> None: ...    


xworker:XWorker = ...



