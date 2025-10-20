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

# Database loading optimization options
LOAD_OPTION = 4  # 0=current, 1=js-fetch, 2=filesystem, 3=worker, 4=storage


def set_load_option(option: int):
    """Set the database loading option for testing"""
    global LOAD_OPTION
    LOAD_OPTION = option
    window.console.log(f"{_timestamp()} Database loading option set to: {option}")


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

    async def load_database_data_url(self, url: str) -> bytes:
        """Load raw database data from a URL without creating database instance

        This allows for parallel loading of multiple databases.

        Args:
            url: URL to the SQLite database file

        Returns:
            Raw bytes data of the database file

        Raises:
            ValueError: If URL is invalid or response is empty
            RuntimeError: If fetch fails
        """
        try:
            response = await fetch(url)
            if not response.ok:
                raise ValueError(f"Failed to fetch database from {url}: HTTP {response.status}")

            buffer = await response.arrayBuffer()
            if not buffer:
                raise ValueError(f"Empty or invalid database file from {url}")

            # Convert to bytes for Python use
            uint8_array = js.Uint8Array.new(buffer)
            return bytes(uint8_array.to_py())

        except Exception as e:
            if isinstance(e, (ValueError, RuntimeError)):
                raise
            raise RuntimeError(f"Failed to load database data from URL '{url}': {e}") from e

    def create_database_from_data(self, data: bytes) -> SQLDatabase:
        """Create a SQLite database instance from raw bytes data

        This allows creating multiple databases in parallel after loading data.

        Args:
            data: Raw bytes data of the SQLite database

        Returns:
            New SQLDatabase instance

        Raises:
            RuntimeError: If SQLite not initialized
        """
        if not self._initialized or self._sql is None:
            raise self._init_error

        # Convert Python bytes to JavaScript Uint8Array
        db_array = js.Uint8Array.new(len(data))
        for i in range(len(data)):
            db_array[i] = data[i]

        return self._sql["Database"].new(db_array)

    async def load_database_data(self, file_path: str) -> bytes:
        """Load raw database data from a file path without creating database instance

        This allows for parallel loading of multiple databases using the current optimization options.

        Args:
            file_path: Path to the SQLite database file

        Returns:
            Raw bytes data of the database file

        Raises:
            OSError: If file doesn't exist or cannot be read
            ValueError: If file is empty or invalid
            RuntimeError: If loading fails
        """
        if not self._initialized or self._sql is None:
            raise self._init_error

        window.console.log(f"{_timestamp()} Loading database data with LOAD_OPTION={LOAD_OPTION}")
        start_time = _performance_now()

        if LOAD_OPTION == 1:
            return await self._load_database_data_js_direct(file_path, start_time)
        elif LOAD_OPTION == 4:
            return await self._load_database_data_cached(file_path, start_time)
        else:
            # Fallback to current method for other options
            return await self._load_database_data_current(file_path, start_time)

    async def _load_database_data_js_direct(self, file_path: str, start_time: float) -> bytes:
        """Option 1: Direct JavaScript fetch for data only"""
        try:
            window.console.log(f"{_timestamp()} [Option 1 Data] Loading database data using JavaScript fetch...")

            # Use JavaScript function to fetch data, passing our SQL.js instance
            result = await js.window.dbOptimizer.loadDatabaseFromUrl(file_path, self._sql)

            # Export the database to get raw bytes
            db_data = result.database.export()

            total_time = _performance_now() - start_time
            window.console.log(f"{_timestamp()} [Option 1 Data] Data loaded in: {total_time:.2f}ms")

            # Convert to Python bytes
            return bytes(db_data.to_py())

        except Exception as e:
            window.console.log(f"{_timestamp()} [Option 1 Data] Failed, falling back to current method: {e}")
            return await self._load_database_data_current(file_path, start_time)

    async def _load_database_data_cached(self, file_path: str, start_time: float) -> bytes:
        """Option 4: JavaScript IndexedDB caching for data only"""
        try:
            window.console.log(f"{_timestamp()} [Option 4 Data] Loading database data with IndexedDB caching...")

            # Use JavaScript function with caching, passing our SQL.js instance
            result = await js.window.dbOptimizer.loadDatabaseWithCache(file_path, "board_comparison_db", self._sql)

            # Export the database to get raw bytes
            db_data = result.database.export()

            total_time = _performance_now() - start_time
            window.console.log(f"{_timestamp()} [Option 4 Data] Data loaded in: {total_time:.2f}ms")

            # Convert to Python bytes
            return bytes(db_data.to_py())

        except Exception as e:
            window.console.log(f"{_timestamp()} [Option 4 Data] Failed, falling back to current method: {e}")
            return await self._load_database_data_current(file_path, start_time)

    async def _load_database_data_current(self, file_path: str, start_time: float) -> bytes:
        """Current implementation for data loading"""
        try:
            window.console.log(f"{_timestamp()} [Option 0 Data] Loading database data using current method...")

            with open(file_path, "rb") as f:
                file_data = f.read()

            total_time = _performance_now() - start_time
            window.console.log(f"{_timestamp()} [Option 0 Data] Data loaded in: {total_time:.2f}ms")

            return file_data

        except OSError as e:
            window.console.log(f"{_timestamp()} [Option 0 Data] File error: {e}")
            raise OSError(f"Failed to read database file '{file_path}': {e}") from e

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

        window.console.log(f"{_timestamp()} Starting database open with LOAD_OPTION={LOAD_OPTION}")
        start_time = _performance_now()

        if LOAD_OPTION == 1:
            return await self._open_database_js_direct(file_path, start_time)
        elif LOAD_OPTION == 2:
            raise NotImplementedError("LOAD_OPTION 2 (filesystem) is not implemented.")
            # return await self._open_database_filesystem(file_path, start_time)
        elif LOAD_OPTION == 3:
            return await self._open_database_worker(file_path, start_time)
        elif LOAD_OPTION == 4:
            return await self._open_database_cached(file_path, start_time)
        else:
            return await self._open_database_current(file_path, start_time)

    async def _open_database_current(self, file_path: str, start_time: float) -> SQLDatabase:
        """Current implementation (Option 0) with timing measurements"""
        try:
            window.console.log(f"{_timestamp()} [Option 0] reading file_data from '{file_path}'...")
            read_start = _performance_now()

            with open(file_path, "rb") as f:
                file_data = f.read()

            if not file_data:
                raise ValueError(f"Database file '{file_path}' is empty")

            read_time = _performance_now()
            window.console.log(f"{_timestamp()} [Option 0] File read completed in {(read_time - read_start):.2f}ms")

            # Create Uint8Array from file data
            window.console.log(f"{_timestamp()} [Option 0] creating db_array from file_data...")
            array_start = _performance_now()
            db_array = js.Uint8Array.new(file_data)
            array_time = _performance_now()
            window.console.log(f"{_timestamp()} [Option 0] Uint8Array created in {(array_time - array_start):.2f}ms")

            window.console.log(f"{_timestamp()} [Option 0] creating Database instance from db_array...")
            db_start = _performance_now()
            db = self._sql["Database"].new(db_array)
            db_time = _performance_now()

            total_time = db_time - start_time
            window.console.log(f"{_timestamp()} [Option 0] Database created in {(db_time - db_start):.2f}ms")
            window.console.log(f"{_timestamp()} [Option 0] Total time: {total_time:.2f}ms")
            return db

        except OSError as e:
            raise OSError(f"Database file not found or cannot be read: '{file_path}': {e}")
        except Exception as e:
            if isinstance(e, (ValueError, OSError)):
                raise
            raise RuntimeError(f"Failed to load database from file '{file_path}': {e}") from e

    async def _open_database_js_direct(self, file_path: str, start_time: float) -> SQLDatabase:
        """Option 1: Direct JavaScript fetch and database creation"""
        try:
            window.console.log(f"{_timestamp()} [Option 1] Loading database via JavaScript...")

            # Use JavaScript function to load database directly, passing our SQL.js instance
            result = await js.window.dbOptimizer.loadDatabaseFromUrl(file_path, self._sql)

            total_time = _performance_now() - start_time
            window.console.log(f"{_timestamp()} [Option 1] Python wrapper total time: {total_time:.2f}ms")

            # The database object is already created in JavaScript
            return result.database

        except Exception as e:
            window.console.log(f"{_timestamp()} [Option 1] Failed, falling back to current method: {e}")
            return await self._open_database_current(file_path, start_time)

    # async def _open_database_filesystem(self, file_path: str, start_time: float) -> SQLDatabase:
    #     """Option 2: PyScript filesystem access"""
    #     try:
    #         window.console.log(f"{_timestamp()} [Option 2] Using PyScript filesystem access...")

    #         # This would require mounting the database file to the virtual filesystem
    #         # For now, fallback to current method as this needs more investigation
    #         window.console.log(f"{_timestamp()} [Option 2] Not fully implemented, using current method")
    #         return await self._open_database_current(file_path, start_time)

    #     except Exception as e:
    #         window.console.log(f"{_timestamp()} [Option 2] Failed, falling back to current method: {e}")
    #         return await self._open_database_current(file_path, start_time)

    async def _open_database_worker(self, file_path: str, start_time: float) -> SQLDatabase:
        """Option 3: Web Worker implementation"""
        try:
            window.console.log(f"{_timestamp()} [Option 3] Using Web Worker for database loading...")

            # This would require creating a worker and message passing
            # For now, fallback to current method as this needs worker setup
            window.console.log(f"{_timestamp()} [Option 3] Not fully implemented, using current method")
            return await self._open_database_current(file_path, start_time)

        except Exception as e:
            window.console.log(f"{_timestamp()} [Option 3] Failed, falling back to current method: {e}")
            return await self._open_database_current(file_path, start_time)

    async def _open_database_cached(self, file_path: str, start_time: float) -> SQLDatabase:
        """Option 4: JavaScript IndexedDB caching"""
        try:
            window.console.log(f"{_timestamp()} [Option 4] Loading database with IndexedDB caching...")

            # Use JavaScript function with caching, passing our SQL.js instance
            result = await js.window.dbOptimizer.loadDatabaseWithCache(file_path, "board_comparison_db", self._sql)

            total_time = _performance_now() - start_time
            window.console.log(f"{_timestamp()} [Option 4] Python wrapper total time: {total_time:.2f}ms")

            return result.database

        except Exception as e:
            window.console.log(f"{_timestamp()} [Option 4] Failed, falling back to current method: {e}")
            return await self._open_database_current(file_path, start_time)

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
