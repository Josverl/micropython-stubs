#!/usr/bin/env python3
"""
Example usage of the MicroPython Board Comparison Tool.

This script demonstrates how to:
1. Build a database from published stubs
2. Query the database for specific information
3. Export data for the web viewer
"""

import sys
from pathlib import Path

# Add the tool to the Python path
sys.path.insert(0, str(Path(__file__).parent))

from build_database import DatabaseBuilder


def example_queries():
    """Show example database queries."""

    # Connect to the database
    db_path = Path(__file__).parent / "board_comparison.db"

    if not db_path.exists():
        print(f"Database not found at {db_path}")
        print("Please run: python build_database.py --version v1_26_0")
        return

    builder = DatabaseBuilder(db_path)
    builder.connect()

    cursor = builder.conn.cursor()

    print("=" * 70)
    print("Example Queries - MicroPython Board Comparison Database")
    print("=" * 70)

    # Query 1: List all boards
    print("\n1. All boards in database:")
    print("-" * 70)
    cursor.execute("SELECT version, port, board FROM boards ORDER BY port, board")
    for row in cursor.fetchall():
        print(f"   {row[1]:15} {row[2]:30} (v{row[0]})")

    # Query 2: Find modules available on ESP32 but not RP2
    print("\n2. Modules unique to ESP32 (not on RP2):")
    print("-" * 70)
    cursor.execute("""
        SELECT DISTINCT m.name 
        FROM modules m
        JOIN board_modules bm ON m.id = bm.module_id
        JOIN boards b ON bm.board_id = b.id
        WHERE b.port = 'esp32' 
        AND m.name NOT IN (
            SELECT m2.name 
            FROM modules m2
            JOIN board_modules bm2 ON m2.id = bm2.module_id
            JOIN boards b2 ON bm2.board_id = b2.id
            WHERE b2.port = 'rp2'
        )
        ORDER BY m.name
        LIMIT 10
    """)
    for row in cursor.fetchall():
        print(f"   - {row[0]}")

    # Query 3: Find common modules across all boards
    print("\n3. Modules available on ALL boards:")
    print("-" * 70)
    cursor.execute("""
        SELECT m.name, COUNT(DISTINCT b.id) as board_count
        FROM modules m
        JOIN board_modules bm ON m.id = bm.module_id
        JOIN boards b ON bm.board_id = b.id
        GROUP BY m.name
        HAVING COUNT(DISTINCT b.id) = (SELECT COUNT(*) FROM boards)
        ORDER BY m.name
    """)
    common_modules = cursor.fetchall()
    if common_modules:
        for row in common_modules:
            print(f"   - {row[0]}")
    else:
        print("   (No modules are available on all boards)")

    # Query 4: Count classes in machine module by board
    print("\n4. Number of classes in 'machine' module by board:")
    print("-" * 70)
    cursor.execute("""
        SELECT b.port, b.board, COUNT(c.id) as class_count
        FROM boards b
        JOIN board_modules bm ON b.id = bm.board_id
        JOIN modules m ON bm.module_id = m.id
        LEFT JOIN classes c ON m.id = c.module_id
        WHERE m.name = 'machine'
        GROUP BY b.id
        ORDER BY class_count DESC, b.port
        LIMIT 10
    """)
    for row in cursor.fetchall():
        print(f"   {row[0]:15} {row[1]:30} {row[2]:3} classes")

    # Query 5: Find methods with most parameters
    print("\n5. Methods with most parameters:")
    print("-" * 70)
    cursor.execute("""
        SELECT m.name as module, c.name as class, meth.name as method, 
               COUNT(p.id) as param_count
        FROM methods meth
        JOIN modules m ON meth.module_id = m.id
        LEFT JOIN classes c ON meth.class_id = c.id
        LEFT JOIN parameters p ON meth.id = p.method_id
        GROUP BY meth.id
        ORDER BY param_count DESC
        LIMIT 10
    """)
    for row in cursor.fetchall():
        class_name = row[1] if row[1] else "(module-level)"
        print(f"   {row[0]}.{class_name}.{row[2]:30} ({row[3]} parameters)")

    # Query 6: Statistics
    print("\n6. Database Statistics:")
    print("-" * 70)
    cursor.execute("SELECT COUNT(*) FROM boards")
    print(f"   Total boards:     {cursor.fetchone()[0]}")

    cursor.execute("SELECT COUNT(*) FROM modules")
    print(f"   Unique modules:   {cursor.fetchone()[0]}")

    cursor.execute("SELECT COUNT(*) FROM classes")
    print(f"   Total classes:    {cursor.fetchone()[0]}")

    cursor.execute("SELECT COUNT(*) FROM methods")
    print(f"   Total methods:    {cursor.fetchone()[0]}")

    cursor.execute("SELECT COUNT(*) FROM parameters")
    print(f"   Total parameters: {cursor.fetchone()[0]}")

    print("\n" + "=" * 70)

    builder.close()


if __name__ == "__main__":
    example_queries()
