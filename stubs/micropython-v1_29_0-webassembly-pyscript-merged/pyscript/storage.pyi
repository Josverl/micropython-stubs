"""Persistent storage API documented by PyScript 2026.7.3."""
# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed

from typing import Any, TypeVar, overload

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

_StorageT = TypeVar("_StorageT", bound=Storage)

@overload
async def storage(name: str = "") -> Storage: ...
@overload
async def storage(name: str, storage_class: type[_StorageT]) -> _StorageT:
    """
    Create or access a named storage instance.

    A utility to instantiate a named idb-map (IndexedDB-backed storage)
    that can be consumed synchronously after initial async setup.

    Args:
          name: The required non-empty storage name. Different names create
              separate storage namespaces.
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
