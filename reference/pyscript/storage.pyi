"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/
"""
# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed


from typing import Any, Type

class Storage(dict[str, Any]):
    """
    Persistent storage interface backed by IndexedDB.

    Extends dict to provide a dictionary-like interface for storing
    and retrieving data that persists across browser sessions.
    Data is stored in the browser's IndexedDB.
    """

    def __init__(self, store: Any) -> None:
        """
        Initialize a Storage instance.

        Args:
            store: The underlying IndexedDB store object
        """
        ...

    def __delitem__(self, attr: str) -> None: ...

    def __setitem__(self, attr: str, value: Any) -> None: ...

    def clear(self) -> None:
        """
        Remove all items from storage.

        Clears all key-value pairs from the storage instance.
        """
        ...

    async def sync(self) -> None:
        """
        Synchronize storage with IndexedDB.

        Ensures all pending writes are committed to the underlying
        IndexedDB store. Call this after making changes to persist them.

        Example:
            store = await storage("my_data")
            store["key"] = "value"
            await store.sync()  # Persist changes
        """
        ...

async def storage(
    name: str = "pyscript",
    storage_class: Type[Storage] = Storage,
) -> Storage:
    """
    Create or access a named storage instance.

    A utility to instantiate a named idb-map (IndexedDB-backed storage)
    that can be consumed synchronously after initial async setup.

    Args:
        name: The name of the storage instance. Different names create
              separate storage namespaces. Default is "pyscript".
        storage_class: The Storage class to instantiate. Default is Storage.
                      Can be a custom subclass for specialized behavior.

    Returns:
        A Storage instance that acts like a dict but persists data
        to IndexedDB

    Example:
        # Create/access storage
        store = await storage("my_app_data")

        # Use like a dict
        store["username"] = "alice"
        store["settings"] = {"theme": "dark"}

        # Persist changes
        await store.sync()

        # Later, access the same data
        store = await storage("my_app_data")
        print(store["username"])  # "alice"
    """
    ...
