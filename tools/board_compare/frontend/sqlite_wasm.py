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

import time
from typing import Any, Dict, List, Optional, Protocol, Self, Sequence, TypedDict

import js
from pyscript import fetch, ffi, window

__version__ = "0.3.0"

# Database loading uses IndexedDB caching (previously Option 4)


def _timestamp() -> str:
    """Get current timestamp as string for logging"""
    return time.strftime("%H:%M:%S", time.localtime())


def _performance_now() -> float:
    """Get high-resolution timing from JavaScript performance API"""
    try:
        return float(js.window.dbOptimizer.performanceNow())
    except Exception:
        return time.time() * 1000.0  # Fallback to Python time in milliseconds


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
        window.console.log(f"SQLite-wasm wrapper created (version={version}, cdn={cdn})")
        self._sql = sql_obj
        self._initialized = sql_obj is not None
        self._version = version
        self._cdn = cdn

    @classmethod
    async def initialize(cls, version="1.13.0", cdn="cdnjs") -> Self:
        """Initialize SQLite-wasm and return a wrapped instance (Factory Method)"""
        window.console.log(f"Initializing SQLite-wasm (version={version}, cdn={cdn})")
        instance = cls(version=version, cdn=cdn)
        await instance._perform_initialization()
        return instance

    async def _perform_initialization(self):
        """Internal method to perform the actual initialization"""
        # https://sql.js.org/documentation/global.html#initSqlJs
        window.console.log("_Performing SQLite-wasm initialization...")
        if not hasattr(window, "initSqlJs"):
            raise RuntimeError("initSqlJs not found on window. Make sure sql-wasm.js script tag is in the HTML page.")

        # Create locateFile function for WASM loading
        def locate_file(file, *args):
            if self._cdn == "cdnjs":
                return f"https://cdnjs.cloudflare.com/ajax/libs/sql.js/{self._version}/{file}"
            # elif self._cdn == "jsdelivr":
            #     return f"https://cdn.jsdelivr.net/npm/sql.js@{self._version}/dist/{file}"
            # else:
            #     return f"https://unpkg.com/sql.js@{self._version}/dist/{file}"

        # Convert to JS function
        locate_file_js = ffi.to_js(locate_file)

        # Initialize SQLite-wasm
        window.console.log("Calling window.initSqlJs...")
        sql_obj = await window.initSqlJs({"locateFile": locate_file_js})

        if not sql_obj:
            raise RuntimeError("Failed to initialize SQLite-wasm")
        self._sql = sql_obj
        self._initialized = True
        window.console.log("SQLite-wasm initialized successfully.")

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
        """Load a SQLite database from a url using IndexedDB caching

        Args:
            url: URL to the SQLite database file, if no protocol is provided, assumes local server

        Returns:
            SQLDatabase instance loaded from the file

        Raises:
            RuntimeError: If SQLite not initialized or database access fails
            OSError: If file doesn't exist or cannot be read
            ValueError: If file is empty or invalid
        """
        if not self._initialized or self._sql is None:
            raise self._init_error

        # Convert filename to URL (assume local server)
        if not url.startswith("http"):
            # Use the current page's base URL and preserve the path
            base_url = str(js.window.location.href).rsplit('/', 1)[0]
            url = f"{base_url}/{url}"

        window.console.log(f"{_timestamp()} Starting database open with IndexedDB caching")
        start_time = _performance_now()

        return await self._open_database_cached(url, start_time)

    async def _open_database_cached(self, file_path: str, start_time: float) -> SQLDatabase:
        """IndexedDB caching implementation"""
        try:
            window.console.log(f"{_timestamp()} [IndexedDB] Loading database with IndexedDB caching...")

            # Use JavaScript function with caching, passing our SQL.js instance
            result = await js.window.dbOptimizer.loadDatabaseWithCache(file_path, "board_comparison_db", self._sql)

            total_time = _performance_now() - start_time
            window.console.log(f"{_timestamp()} [IndexedDB] Python wrapper total time: {total_time:.2f}ms")

            return result.database

        except Exception as e:
            window.console.log(f"{_timestamp()} [IndexedDB] Failed: {e}")
            raise RuntimeError(f"Failed to load database with IndexedDB caching: {e}") from e

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

    # async def load_database_data_url(self, url: str) -> bytes:
    #     """Load raw database data from a URL without creating multiple database instance
    #     This allows for parallel loading of multiple databases.

    #     Args:
    #         url: URL to the SQLite database file

    #     Returns:
    #         Raw bytes data of the database file

    #     Raises:
    #         ValueError: If URL is invalid or response is empty
    #         RuntimeError: If fetch fails
    #     """
    #     try:
    #         response = await fetch(url)
    #         if not response.ok:
    #             raise ValueError(f"Failed to fetch database from {url}: HTTP {response.status}")
    #         buffer = await response.arrayBuffer()
    #         if not buffer:
    #             raise ValueError(f"Empty or invalid database file from {url}")
    #         # Convert to bytes for Python use
    #         uint8_array = js.Uint8Array.new(buffer)
    #         return bytes(uint8_array.to_py())
    #     except Exception as e:
    #         if isinstance(e, (ValueError, RuntimeError)):
    #             raise
    #         raise RuntimeError(f"Failed to load database data from URL '{url}': {e}") from e

    # def create_database_from_data(self, data: bytes) -> SQLDatabase:
    #     """Create a SQLite database instance from raw bytes data

    #     This allows creating multiple databases in parallel after loading data.

    #     Args:
    #         data: Raw bytes data of the SQLite database

    #     Returns:
    #         New SQLDatabase instance

    #     Raises:
    #         RuntimeError: If SQLite not initialized
    #     """
    #     if not self._initialized or self._sql is None:
    #         raise self._init_error

    #     # Convert Python bytes to JavaScript Uint8Array
    #     db_array = js.Uint8Array.new(len(data))
    #     for i in range(len(data)):
    #         db_array[i] = data[i]

    #     return self._sql["Database"].new(db_array)

    # async def load_database_data(self, file_path: str) -> bytes:
    #     """Load raw database data from a file path using IndexedDB caching

    #     This allows for parallel loading of multiple databases.

    #     Args:
    #         file_path: Path to the SQLite database file

    #     Returns:
    #         Raw bytes data of the database file

    #     Raises:
    #         OSError: If file doesn't exist or cannot be read
    #         ValueError: If file is empty or invalid
    #         RuntimeError: If loading fails
    #     """
    #     if not self._initialized or self._sql is None:
    #         raise self._init_error

    #     window.console.log(f"{_timestamp()} Loading database data with IndexedDB caching...")
    #     start_time = _performance_now()

    #     return await self._load_database_data_cached(file_path, start_time)

    # async def _load_database_data_cached(self, file_path: str, start_time: float) -> bytes:
    #     """IndexedDB caching for data only"""
    #     try:
    #         window.console.log(f"{_timestamp()} [IndexedDB] Loading database data with IndexedDB caching...")

    #         # Use JavaScript function with caching, passing our SQL.js instance
    #         result = await js.window.dbOptimizer.loadDatabaseWithCache(file_path, "board_comparison_db", self._sql)

    #         # Export the database to get raw bytes
    #         db_data = result.database.export()

    #         total_time = _performance_now() - start_time
    #         window.console.log(f"{_timestamp()} [IndexedDB] Data loaded in: {total_time:.2f}ms")

    #         # Convert to Python bytes
    #         return bytes(db_data.to_py())

    #     except Exception as e:
    #         window.console.log(f"{_timestamp()} [IndexedDB] Failed: {e}")
    #         raise RuntimeError(f"Failed to load database data with IndexedDB caching: {e}") from e
