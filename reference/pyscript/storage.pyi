"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/
"""

class Storage(dict):
    def __init__(self, store) -> None: ...
    def __delitem__(self, attr) -> None: ...
    def __setitem__(self, attr, value) -> None: ...
    def clear(self) -> None: ...
    async def sync(self) -> None: ...

async def storage(name=..., storage_class=...) -> Storage: 
    """
    a utility to instantiate a named idb-map that can be consumed synchronously.
    """
    ...
