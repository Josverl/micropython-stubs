import asyncio
from typing import Any, cast

from pyscript import ffi
from sqlite_wasm import SQLDatabase, SQLExecResult, SQLExecResults, SQLite

# API : https://sql.js.org/documentation/Database.html


def print_query_results(title: str, result: SQLExecResults) -> None:
    """Helper function to print query results in a nice format"""
    print(f"\n🔍 {title}")
    print("=" * (len(title) + 4))

    # Handle JavaScript result objects
    if not result:
        print("  No result found.")
        return

    # Check if result is a JavaScript array
    result_length = 0
    if hasattr(result, "length"):  # JS Array
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
    if hasattr(columns, "length"):  # JS Array
        columns = [columns[i] for i in range(int(columns.length))]  # type: ignore
    if hasattr(values, "length"):  # JS Array
        values = [values[i] for i in range(int(values.length))]  # type: ignore

    # Print column headers
    header_line = "  " + " | ".join(f"{col:<15}" for col in columns)
    print(header_line)
    print("  " + "-" * (len(columns) * 18 - 3))

    # Print rows
    for row in values:
        # Convert row to Python list if it's a JS array
        if hasattr(row, "length"):  # JS Array
            row = [row[i] for i in range(int(row.length))]  # type: ignore

        formatted_row = []
        for value in row:
            if value is None:
                formatted_row.append("NULL")
            elif isinstance(value, float):
                formatted_row.append(f"{value:.2f}")
            else:
                formatted_row.append(str(value))
        print("  " + " | ".join(f"{val:<15}" for val in formatted_row))


async def example_create_db(SQL) -> SQLDatabase:
    # Test creating a database
    db = None
    try:
        # Use the integrated method to create a new database
        db = SQL.create_database()
        print("- ✅ Created SQLite database instance via SQL.create_database()")

        # Test a simple query
        db.run("CREATE TABLE test (id INTEGER, name TEXT);")
        db.run("INSERT INTO test VALUES (1, 'Hello from SQLite-wasm!');")
        db.run("INSERT INTO test VALUES (2, 'Second row data');")
        db.run("INSERT INTO test VALUES (3, 'Third row entry');")
        # now

        tables = await get_table_row_counts(db)
        print_query_results("All Tables and Row Counts", tables)

        print("\n- Now querying the 'test' table:")
        # Now query some data
        result = db.exec("SELECT * FROM test;")
        result = cast(SQLExecResults, result)
        for row in result[0]["values"]:
            print(f"  - Row: id={row[0]}, name={row[1]}")
        return db

    except Exception as db_error:
        print(f"- ❌ Database error: {db_error}")
        print(f"- ❌ Database error type: {type(db_error).__name__}")
        raise db_error


async def get_table_row_counts(db: SQLDatabase) -> SQLExecResults:
    """Dynamically get all tables and their row counts without knowing schema upfront"""

    # Step 1: Get all user table names
    tables_query = """
        SELECT name 
        FROM sqlite_master 
        WHERE type='table' 
        AND name NOT LIKE 'sqlite_%'
        ORDER BY name;
    """

    tables_result = db.exec(tables_query)

    if not tables_result[0]["values"]:
        return [{"columns": ["message"], "values": [["No user tables found"]]}]  # type: ignore

    # Step 2: Build dynamic UNION query
    table_names = [row[0] for row in tables_result[0]["values"]]

    union_queries = []
    for table_name in table_names:
        # Escape table name in case it has special characters
        escaped_name = f'"{table_name}"'
        union_queries.append(f"SELECT '{table_name}' as table_name, COUNT(*) as row_count FROM {escaped_name}")

    # Combine all queries with UNION ALL
    combined_query = " UNION ALL ".join(union_queries) + " ORDER BY row_count DESC, table_name;"

    # Step 3: Execute the combined query
    result = db.exec(combined_query)
    return result  # type: ignore - could also cast to SQLExecResults


async def load_and_query_database(SQL):
    db_from_file = await SQL.open_database("demodata.sqlite.db")
    print("- ✅ Database loaded from file successfully")

    # Show database structure and row counts
    try:
        result = await get_table_row_counts(db_from_file)
        print_query_results("All Tables and Row Counts", result)
    except Exception as e:
        print(f"- ❌ Error getting table row counts: {e}")

        # Demonstrate various SQL queries
    try:
        print("\n" + "=" * 60)
        print("🗃️  COMPLEX QUERY DEMONSTRATIONS")
        print("=" * 60)

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

        print("\n✅ Successfully demonstrated complex SQL queries with SQLite-wasm!")

        # Count users safely from JavaScript result
        user_count = 0
        if result and hasattr(result, "length") and int(result.length) > 0:
            values = result[0]["values"]
            if hasattr(values, "length"):
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


async def main():
    print("Hello, Structured World!")

    try:
        print("- Initializing SQLite-wasm ...")
        # Initialize SQLite-wasm using a context manager
        # - but this can also be done via factory method as below
        # SQL = await SQLite.initialize(version="1.13.0", cdn="cdnjs")
        async with SQLite() as SQL:
            print("- ✅ SQLite-wasm initialized successfully")

            # Run example to create a database and perform simple operations
            db = await example_create_db(SQL)

            print("\n- Testing binding queries...")
            stmt = db.prepare("SELECT * FROM test WHERE name LIKE ?")
            # Bindings to queries need to be converted to JS array
            stmt.bind(
                ffi.to_js(
                    [
                        r"%row%",
                    ]
                )
            )
            while stmt.step():
                row = stmt.getAsObject()
                print("What is a row?")
                print(f"{row=}")
                print(f"{type(row)=}")
                print(f"{repr(row)=}")
                print(f"{row.__class__=}")
                print(f"{dir(row)=}")
                # probably a dictionary-like object
                print(f"Found: {row['name']}")  # Should print results
                # or a named tuple maybe?
                print(f"Found: {row.name}")  # Should print results -

            db.close()

        # other db
        # await load_and_query_database(SQL)

    except Exception as e:
        print(f"- ❌ Error initializing SQLite-wasm: {e}")
        print(f"- ❌ Error type: {type(e).__name__}")
        return

    print("\n🎉 All done!")


# Start the application
asyncio.create_task(main())
