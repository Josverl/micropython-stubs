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


def print_query_results(title: str, result: Any) -> None:
    """Helper function to print query results in a nice format"""
    print(f"\n🔍 {title}")
    print("=" * (len(title) + 4))
    
    # Handle JavaScript result objects
    if not result:
        print("  No result found.")
        return
    
    # Check if result is a JavaScript array
    result_length = 0
    if hasattr(result, 'length'):  # JS Array
        result_length = int(result.length)
    else:
        try:
            result_length = len(result)
        except TypeError:
            print("  Cannot determine result length.")
            return
    
    if result_length == 0:
        print("  No result sets found.")
        return
    
    first_result = result[0]
    if not first_result["values"]:
        print("  No results found.")
        return
    
    columns = first_result["columns"]
    values = first_result["values"]
    
    # Convert JavaScript arrays to Python lists
    if hasattr(columns, 'length'):  # JS Array
        columns = [columns[i] for i in range(int(columns.length))]
    if hasattr(values, 'length'):  # JS Array
        values = [values[i] for i in range(int(values.length))]
    
    # Print column headers
    header_line = "  " + " | ".join(f"{col:<15}" for col in columns)
    print(header_line)
    print("  " + "-" * (len(columns) * 18 - 3))
    
    # Print rows
    for row in values:
        # Convert row to Python list if it's a JS array
        if hasattr(row, 'length'):  # JS Array
            row = [row[i] for i in range(int(row.length))]
            
        formatted_row = []
        for value in row:
            if value is None:
                formatted_row.append("NULL")
            elif isinstance(value, float):
                formatted_row.append(f"{value:.2f}")
            else:
                formatted_row.append(str(value))
        print("  " + " | ".join(f"{val:<15}" for val in formatted_row))


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

    # Demonstrate various SQL queries
    try:
        print("\n" + "="*60)
        print("🗃️  COMPLEX QUERY DEMONSTRATIONS")
        print("="*60)

        # 1. Basic table queries
        result = db_from_file.exec("SELECT * FROM users;")
        print_query_results("All Users", result)

        result = db_from_file.exec("SELECT * FROM user_profiles;")
        print_query_results("User Profiles", result)

        result = db_from_file.exec("SELECT * FROM orders;")
        print_query_results("All Orders", result)

        # 2. JOIN queries - Users with their profiles
        result = db_from_file.exec("""
            SELECT u.id, u.name, up.email, up.age, up.city, up.is_active
            FROM users u
            LEFT JOIN user_profiles up ON u.id = up.user_id
            ORDER BY u.id;
        """)
        print_query_results("Users with Profiles", result)

        # 3. Complex JOIN - Users with their total orders and spending
        result = db_from_file.exec("""
            SELECT 
                u.name,
                up.email,
                up.city,
                COUNT(o.id) as total_orders,
                ROUND(SUM(o.price * o.quantity), 2) as total_spent,
                ROUND(AVG(o.price), 2) as avg_order_value
            FROM users u
            LEFT JOIN user_profiles up ON u.id = up.user_id
            LEFT JOIN orders o ON u.id = o.user_id
            GROUP BY u.id, u.name, up.email, up.city
            ORDER BY total_spent DESC;
        """)
        print_query_results("User Spending Summary", result)

        # 4. Subquery - Most expensive order per user
        result = db_from_file.exec("""
            SELECT 
                u.name,
                o.product_name,
                o.quantity,
                o.price,
                (o.quantity * o.price) as total_cost
            FROM users u
            INNER JOIN orders o ON u.id = o.user_id
            WHERE (o.quantity * o.price) = (
                SELECT MAX(o2.quantity * o2.price)
                FROM orders o2
                WHERE o2.user_id = u.id
            )
            ORDER BY total_cost DESC;
        """)
        print_query_results("Most Expensive Order Per User", result)

        # 5. Aggregate with HAVING clause
        result = db_from_file.exec("""
            SELECT 
                up.city,
                COUNT(*) as user_count,
                ROUND(AVG(up.age), 1) as avg_age,
                ROUND(SUM(o.price * o.quantity), 2) as city_total_spending
            FROM user_profiles up
            LEFT JOIN orders o ON up.user_id = o.user_id
            GROUP BY up.city
            HAVING user_count > 0
            ORDER BY city_total_spending DESC;
        """)
        print_query_results("Spending by City", result)

        # 6. Window function simulation (since SQLite has limited window functions)
        result = db_from_file.exec("""
            SELECT 
                u.name,
                o.product_name,
                o.price,
                o.quantity,
                (SELECT COUNT(*) FROM orders o2 WHERE o2.user_id = o.user_id AND o2.id <= o.id) as order_sequence
            FROM users u
            INNER JOIN orders o ON u.id = o.user_id
            ORDER BY u.id, o.id;
        """)
        print_query_results("Orders with Sequence Numbers", result)

        # 7. Complex filtering and CASE statements
        result = db_from_file.exec("""
            SELECT 
                u.name,
                up.age,
                CASE 
                    WHEN up.age < 25 THEN 'Young'
                    WHEN up.age BETWEEN 25 AND 35 THEN 'Adult'
                    ELSE 'Senior'
                END as age_group,
                COUNT(o.id) as order_count,
                CASE 
                    WHEN COUNT(o.id) = 0 THEN 'No Orders'
                    WHEN COUNT(o.id) <= 2 THEN 'Light Buyer'
                    ELSE 'Heavy Buyer'
                END as buyer_type
            FROM users u
            LEFT JOIN user_profiles up ON u.id = up.user_id
            LEFT JOIN orders o ON u.id = o.user_id
            GROUP BY u.id, u.name, up.age
            ORDER BY up.age;
        """)
        print_query_results("User Demographics & Behavior", result)

        print("\n✅ Successfully demonstrated complex SQL queries with SQL.js!")
        
        # Count users safely from JavaScript result
        user_count = 0
        if result and hasattr(result, 'length') and int(result.length) > 0:
            values = result[0]['values']
            if hasattr(values, 'length'):
                user_count = int(values.length)
            else:
                try:
                    user_count = len(values)
                except TypeError:
                    user_count = 0
        
        print(f"📊 Database contains {user_count} users with full relational data.")

    except Exception as query_error:
        print(f"- ❌ Query error: {query_error}")
        print(f"- ❌ Error type: {type(query_error).__name__}")

    finally:
        # Clean up
        try:
            db_from_file.close()
            print("\n🔒 Database connection closed.")
        except Exception:
            pass

    
# Start the application
asyncio.create_task(main())
