import asyncio
from typing import Any, List, TypedDict, Union, cast

import js
from pyscript import fetch, ffi, js_modules, window


class SQLExecResult(TypedDict):
    """Type for individual SQL.js exec result object"""

    columns: List[str]  # Column names
    values: List[List[Any]]  # Rows of data (each row is a list of values)


# The exec method returns a list of these result objects
SQLExecResults = List[SQLExecResult]


class SQLite:
    """Wrapper to make SQL.js object accessible with dot notation and handle initialization"""

    _init_error = RuntimeError("SQL.js not initialized. Use SQLWrapper.initialize() first.")

    def __init__(self, sql_obj=None):
        self._sql = sql_obj
        self._initialized = sql_obj is not None

    @classmethod
    async def initialize(cls, version="1.13.0", cdn="cdnjs"):
        """Initialize SQL.js and return a wrapped instance"""
        # https://sql.js.org/documentation/global.html#initSqlJs

        # Use the already imported modules

        if not hasattr(window, "initSqlJs"):
            raise RuntimeError("initSqlJs not found on window. Make sure sql-wasm.js script tag is in the HTML page.")

        # Create locateFile function for WASM loading
        # also requires SQL.js UMD module in the HTML page
        # <script src="https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.13.0/sql-wasm.js"></script>
        def locate_file(file, *args):
            if cdn == "cdnjs":
                return f"https://cdnjs.cloudflare.com/ajax/libs/sql.js/{version}/{file}"
            # # TODO: TEST with jsdelivr and unpkg
            # elif cdn == "jsdelivr":
            #     return f"https://cdn.jsdelivr.net/npm/sql.js@{version}/dist/{file}"
            # else:
            #     return f"https://unpkg.com/sql.js@{version}/dist/{file}"

        # Convert to JS function
        locate_file_js = ffi.to_js(locate_file)

        # Initialize SQL.js
        sql_obj = await window.initSqlJs({"locateFile": locate_file_js})

        if not sql_obj:
            raise RuntimeError("Failed to initialize SQL.js")

        return cls(sql_obj)

    def __getattr__(self, name):
        # Allow dot notation access to SQL.js members
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
        """Check if SQL.js is initialized"""
        return self._initialized


# API : https://sql.js.org/documentation/Database.html


async def main():
    print("Hello, Structured World!")

    try:
        # Initialize SQL.js using the wrapper class
        print("- Initializing SQLite-wasm ...")
        SQL = await SQLite.initialize(version="1.13.0", cdn="cdnjs")
        print("- ✅ SQLite-wasm initialized successfully")

    except Exception as e:
        print(f"- ❌ Error initializing SQLite-wasm: {e}")
        print(f"- ❌ Error type: {type(e).__name__}")
        return

    # Test creating a database - now you can use dot notation!
    try:
        # Now this works with dot notation
        db = SQL.Database.new()
        print("- ✅ Created SQLite database instance via SQL.Database.new()")

        # Test a simple query
        db.run("CREATE TABLE test (id INTEGER, name TEXT);")
        db.run("INSERT INTO test VALUES (1, 'Hello from SQL.js!');")
        db.run("INSERT INTO test VALUES (2, 'Second row data');")
        db.run("INSERT INTO test VALUES (3, 'Third row entry');")
        result = db.exec("SELECT * FROM test;")
        result = cast(SQLExecResults, result)
        for row in result[0]["values"]:
            print(f"  - Row: id={row[0]}, name={row[1]}")
        db.close()
    except Exception as db_error:
        print(f"- ❌ Database error: {db_error}")
        print(f"- ❌ Database error type: {type(db_error).__name__}")
        return

    print("- Test Loading database file from the server...")
    # https://sql.js.org/#/?id=using-fetch
    try:
        # Fetch database file
        response = await fetch("data.sqlite")
        buffer = await response.arrayBuffer()
        print(f"- loaded: {len(buffer)} bytes")
        # Create database instance
        db_array = js.Uint8Array.new(buffer)

        # Create database instance from file
        print("- Creating database from file...")
        db_from_file = SQL.Database.new(db_array)
        print("- Database loaded from file successfully.")
    except Exception as file_error:
        print(f"- ❌ Error loading database file: {file_error}")
        print(f"- ❌ Error type: {type(file_error).__name__}")
        return
    print(f"dir(db_from_file): {dir(db_from_file)}")
    print(f"help(db_from_file): {help(db_from_file)}")

    # Test a simple query on loaded database
    result = db_from_file.exec("SELECT * FROM users;")
    result = cast(SQLExecResults, result)
    for row in result[0]["values"]:
        print(f"  - Row: id={row[0]}, name={row[1]}")


# Start the application
asyncio.create_task(main())
