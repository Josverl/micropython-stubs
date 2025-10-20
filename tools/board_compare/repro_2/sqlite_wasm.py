"""
Wrapper for SQLite-wasm to provide Pythonic access and initialization handling

# Quick one-liner initialization
    SQL = await SQLite.initialize(version="1.13.0", cdn="cdnjs")
    db = SQL.Database.new()
    # ... use database
    # Manual cleanup if needed

or use as an async context manager

    async with SQLite(version="1.13.0", cdn="cdnjs") as SQL:
        db = SQL.Database.new()
        # ... use database
        # Automatic cleanup when exiting context

"""

from typing import Any, Dict, List, Optional, Protocol, Self, Sequence, TypedDict

import js
from pyscript import fetch, ffi, window

__version__ = "0.1.0"


# classess to define types for SQLite-wasm interactions
class SQLExecResult(TypedDict):
    """Type for individual SQLite-wasm exec result object"""

    columns: List[str]  # Column names
    values: List[List[Any]]  # Rows of data (each row is a list of values)


class SQLExecResults(List[SQLExecResult]):
    """List of SQLite-wasm exec result objects with length property"""

    @property
    def length(self) -> int: ...


class SQLDatabase(Protocol):
    """Protocol for SQLite-wasm Database instances"""

    def run(self, sql: str, params: Optional[Sequence] = None) -> None: ...
    def exec(self, sql: str, params: Optional[Sequence] = None) -> Sequence[Dict]: ...
    def prepare(self, sql: str) -> "SQLStatement": ...
    def close(self) -> None: ...


class SQLStatement(Protocol):
    """Protocol for SQLite-wasm prepared statements"""

    def step(self) -> bool: ...
    def get(self) -> list[Any]: ...
    def getAsObject(self) -> dict[str, Any]: ...
    def bind(self, params: list[Any]) -> None: ...
    def free(self) -> None: ...


# Wrapper to make SQLite-wasm object accessible with dot notation and handle initialization
class SQLite:
    """Wrapper to make SQLite-wasm object accessible with dot notation and handle initialization"""

    _init_error = RuntimeError("SQLite-wasm not initialized. Use SQLite.initialize() first.")

    def __init__(self, sql_obj=None, version="1.13.0", cdn="cdnjs"):
        self._sql = sql_obj
        self._initialized = sql_obj is not None
        self._version = version
        self._cdn = cdn

    @classmethod
    async def initialize(cls, version="1.13.0", cdn="cdnjs") -> Self:
        """Initialize SQLite-wasm and return a wrapped instance (Factory Method)"""
        instance = cls(version=version, cdn=cdn)
        await instance._perform_initialization()
        return instance

    async def _perform_initialization(self):
        """Internal method to perform the actual initialization"""
        # https://sql.js.org/documentation/global.html#initSqlJs

        if not hasattr(window, "initSqlJs"):
            raise RuntimeError("initSqlJs not found on window. Make sure sql-wasm.js script tag is in the HTML page.")

        # Create locateFile function for WASM loading
        def locate_file(file, *args):
            if self._cdn == "cdnjs":
                return f"https://cdnjs.cloudflare.com/ajax/libs/sql.js/{self._version}/{file}"
            elif self._cdn == "jsdelivr":
                return f"https://cdn.jsdelivr.net/npm/sql.js@{self._version}/dist/{file}"
            else:
                return f"https://unpkg.com/sql.js@{self._version}/dist/{file}"

        # Convert to JS function
        locate_file_js = ffi.to_js(locate_file)

        # Initialize SQLite-wasm
        sql_obj = await window.initSqlJs({"locateFile": locate_file_js})

        if not sql_obj:
            raise RuntimeError("Failed to initialize SQLite-wasm")

        self._sql = sql_obj
        self._initialized = True

    # Async Context Manager Support
    async def __aenter__(self):
        """Async context manager entry - auto-initialize if needed"""
        if not self._initialized:
            await self._perform_initialization()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit - auto-cleanup"""
        if self._sql and hasattr(self._sql, "close"):
            # Note: SQL.js doesn't actually have a close method on the main object
            # But individual databases do, so this is here for completeness
            pass
        return False  # Don't suppress exceptions

    def __getattr__(self, name):
        # Allow dot notation access to SQLite-wasm members
        if not self._initialized or self._sql is None:
            raise self._init_error

        if name in self._sql:
            return self._sql[name]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __getitem__(self, key):
        # Also keep bracket notation working
        if not self._initialized or self._sql is None:
            raise self._init_error
        return self._sql[key]

    def keys(self):
        if not self._initialized or self._sql is None:
            raise self._init_error
        return self._sql.keys()

    @property
    def initialized(self):
        """Check if SQLite-wasm is initialized"""
        return self._initialized

    async def open_database_url(self, url: str) -> SQLDatabase:
        """Load a SQLite database from a URL

        Args:
            url: URL to the SQLite database file

        Returns:
            SQLDatabase instance loaded from the URL

        Raises:
            RuntimeError: If SQLite not initialized or database loading fails
            ValueError: If URL is invalid or response is empty
        """
        if not self._initialized or self._sql is None:
            raise self._init_error

        try:
            response = await fetch(url)
            if not response.ok:
                raise ValueError(f"Failed to fetch database from {url}: HTTP {response.status}")

            buffer = await response.arrayBuffer()
            if not buffer:
                raise ValueError(f"Empty or invalid database file from {url}")

            # Create database instance from buffer
            return self._sql["Database"].new(js.Uint8Array.new(buffer))

        except Exception as e:
            if isinstance(e, (ValueError, RuntimeError)):
                raise
            raise RuntimeError(f"Failed to load database from URL '{url}': {e}") from e

    async def open_database(self, file_path: str) -> SQLDatabase:
        """Load a SQLite database from a local file path

        Args:
            file_path: Path to the SQLite database file

        Returns:
            SQLDatabase instance loaded from the file

        Raises:
            RuntimeError: If SQLite not initialized or database loading fails
            OSError: If file doesn't exist or cannot be read
            ValueError: If file is empty or invalid
        """
        if not self._initialized or self._sql is None:
            raise self._init_error

        try:
            with open(file_path, "rb") as f:
                file_data = f.read()

            if not file_data:
                raise ValueError(f"Database file '{file_path}' is empty")

            # Create Uint8Array from file data
            # db_array = js.Uint8Array.new(file_data)

            return self._sql["Database"].new(js.Uint8Array.new(file_data))

        except OSError as e:
            raise OSError(f"Database file not found or cannot be read: '{file_path}': {e}")
        except Exception as e:
            if isinstance(e, (ValueError, OSError)):
                raise
            raise RuntimeError(f"Failed to load database from file '{file_path}': {e}") from e

    def create_database(self, data: Optional[bytes] = None) -> SQLDatabase:
        """Create a new SQLite database instance

        Args:
            data: Optional bytes data to initialize the database with

        Returns:
            New SQLDatabase instance

        Raises:
            RuntimeError: If SQLite not initialized
        """
        if not self._initialized or self._sql is None:
            raise self._init_error

        if data is None:
            return self._sql["Database"].new()
        else:
            db_array = js.Uint8Array.new(len(data))
            for i in range(len(data)):
                db_array[i] = data[i]
            return self._sql["Database"].new(db_array)
