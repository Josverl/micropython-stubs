#!/usr/bin/env python3
"""
Compare ESP32 vs STM32 boards (v1.26.0) at all 3 levels using SQL queries.
Pure CPython script - demonstrates complete SQL-based comparison implementation.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "board_comparison.db"

def get_board_id(conn, version, port, board):
    """Get board ID for version/port/board combination."""
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM boards WHERE version = ? AND port = ? AND board = ?",
        (version, port, board)
    )
    result = cursor.fetchone()
    return result[0] if result else None


def compare_boards(conn, board1_id, board2_id, board1_name, board2_name):
    """Compare two boards at all 3 levels using SQL queries."""
    cursor = conn.cursor()
    
    print(f"\n{'=' * 80}")
    print(f"Comparing: {board1_name} vs {board2_name}")
    print(f"{'=' * 80}")
    
    # Level 1: Module comparison
    print("\n" + "=" * 40)
    print("LEVEL 1: Module Comparison")
    print("=" * 40)
    
    cursor.execute("""
        WITH board1_modules AS (
            SELECT DISTINCT module_name
            FROM v_board_comparison_modules
            WHERE board_id = ?1
        ),
        board2_modules AS (
            SELECT DISTINCT module_name
            FROM v_board_comparison_modules
            WHERE board_id = ?2
        )
        SELECT 
            (SELECT COUNT(*) FROM board1_modules) as total1,
            (SELECT COUNT(*) FROM board2_modules) as total2,
            (SELECT COUNT(DISTINCT b1.module_name) 
             FROM board1_modules b1
             WHERE b1.module_name NOT IN (SELECT module_name FROM board2_modules)) as unique1,
            (SELECT COUNT(DISTINCT b2.module_name) 
             FROM board2_modules b2
             WHERE b2.module_name NOT IN (SELECT module_name FROM board1_modules)) as unique2,
            (SELECT COUNT(DISTINCT b1.module_name) 
             FROM board1_modules b1
             INNER JOIN board2_modules b2 ON b1.module_name = b2.module_name) as common
    """, (board1_id, board2_id))
    
    result = cursor.fetchone()
    print(f"\nTotal Modules:")
    print(f"  {board1_name}: {result[0]}")
    print(f"  {board2_name}: {result[1]}")
    print(f"\nUnique to {board1_name}: {result[2]}")
    print(f"Unique to {board2_name}: {result[3]}")
    print(f"Common modules: {result[4]}")
    
    # Show unique modules
    cursor.execute("""
        WITH board1_modules AS (
            SELECT DISTINCT module_name FROM v_board_comparison_modules WHERE board_id = ?1
        ),
        board2_modules AS (
            SELECT DISTINCT module_name FROM v_board_comparison_modules WHERE board_id = ?2
        )
        SELECT DISTINCT b1.module_name
        FROM board1_modules b1
        WHERE b1.module_name NOT IN (SELECT module_name FROM board2_modules)
        ORDER BY b1.module_name
    """, (board1_id, board2_id))
    
    unique1 = [row[0] for row in cursor.fetchall()]
    if unique1:
        print(f"\nModules unique to {board1_name}:")
        for mod in unique1:
            print(f"  - {mod}")
    
    cursor.execute("""
        WITH board1_modules AS (
            SELECT DISTINCT module_name FROM v_board_comparison_modules WHERE board_id = ?1
        ),
        board2_modules AS (
            SELECT DISTINCT module_name FROM v_board_comparison_modules WHERE board_id = ?2
        )
        SELECT DISTINCT b2.module_name
        FROM board2_modules b2
        WHERE b2.module_name NOT IN (SELECT module_name FROM board1_modules)
        ORDER BY b2.module_name
    """, (board1_id, board2_id))
    
    unique2 = [row[0] for row in cursor.fetchall()]
    if unique2:
        print(f"\nModules unique to {board2_name}:")
        for mod in unique2:
            print(f"  - {mod}")
    
    # Level 2: Classes, functions, constants comparison
    print("\n" + "=" * 40)
    print("LEVEL 2: Classes, Functions, Constants")
    print("=" * 40)
    
    cursor.execute("""
        WITH board1_modules AS (
            SELECT module_name FROM v_board_comparison_modules WHERE board_id = ?1
        ),
        board2_modules AS (
            SELECT module_name FROM v_board_comparison_modules WHERE board_id = ?2
        ),
        unique_modules1 AS (
            SELECT module_name FROM board1_modules 
            WHERE module_name NOT IN (SELECT module_name FROM board2_modules)
        ),
        unique_modules2 AS (
            SELECT module_name FROM board2_modules 
            WHERE module_name NOT IN (SELECT module_name FROM board1_modules)
        ),
        common_modules AS (
            SELECT b1.module_name FROM board1_modules b1 
            INNER JOIN board2_modules b2 ON b1.module_name = b2.module_name
        ),
        classes_unique1 AS (
            SELECT c.class_id FROM v_board_comparison_classes c
            INNER JOIN unique_modules1 u ON c.module_name = u.module_name
            WHERE c.board_id = ?1
        ),
        classes_unique2 AS (
            SELECT c.class_id FROM v_board_comparison_classes c
            INNER JOIN unique_modules2 u ON c.module_name = u.module_name
            WHERE c.board_id = ?2
        ),
        classes_in_common1 AS (
            SELECT c.class_id, c.class_name, c.module_name FROM v_board_comparison_classes c
            INNER JOIN common_modules cm ON c.module_name = cm.module_name
            WHERE c.board_id = ?1
        ),
        classes_in_common2 AS (
            SELECT c.class_id, c.class_name, c.module_name FROM v_board_comparison_classes c
            INNER JOIN common_modules cm ON c.module_name = cm.module_name
            WHERE c.board_id = ?2
        ),
        funcs_in_common1 AS (
            SELECT m.method_id, m.method_name, m.module_name FROM v_board_comparison_methods m
            INNER JOIN common_modules cm ON m.module_name = cm.module_name
            WHERE m.board_id = ?1 AND m.class_name IS NULL
        ),
        funcs_in_common2 AS (
            SELECT m.method_id, m.method_name, m.module_name FROM v_board_comparison_methods m
            INNER JOIN common_modules cm ON m.module_name = cm.module_name
            WHERE m.board_id = ?2 AND m.class_name IS NULL
        ),
        consts_in_common1 AS (
            SELECT c.constant_id, c.constant_name, c.module_name FROM v_board_comparison_constants c
            INNER JOIN common_modules cm ON c.module_name = cm.module_name
            WHERE c.board_id = ?1
        ),
        consts_in_common2 AS (
            SELECT c.constant_id, c.constant_name, c.module_name FROM v_board_comparison_constants c
            INNER JOIN common_modules cm ON c.module_name = cm.module_name
            WHERE c.board_id = ?2
        )
        SELECT 
            (SELECT COUNT(*) FROM classes_unique1) as classes1_unique,
            (SELECT COUNT(*) FROM classes_unique2) as classes2_unique,
            (SELECT COUNT(*) FROM classes_in_common1 c1 
             WHERE c1.class_name NOT IN (SELECT class_name FROM classes_in_common2 c2 
                                          WHERE c2.module_name = c1.module_name)) as classes1_diff,
            (SELECT COUNT(*) FROM classes_in_common2 c2 
             WHERE c2.class_name NOT IN (SELECT class_name FROM classes_in_common1 c1 
                                          WHERE c1.module_name = c2.module_name)) as classes2_diff,
            (SELECT COUNT(*) FROM funcs_in_common1 f1 
             WHERE f1.method_name NOT IN (SELECT method_name FROM funcs_in_common2 f2 
                                           WHERE f2.module_name = f1.module_name)) as functions1_unique,
            (SELECT COUNT(*) FROM funcs_in_common2 f2 
             WHERE f2.method_name NOT IN (SELECT method_name FROM funcs_in_common1 f1 
                                           WHERE f1.module_name = f2.module_name)) as functions2_unique,
            (SELECT COUNT(*) FROM consts_in_common1 c1 
             WHERE c1.constant_name NOT IN (SELECT constant_name FROM consts_in_common2 c2 
                                             WHERE c2.module_name = c1.module_name)) as constants1_unique,
            (SELECT COUNT(*) FROM consts_in_common2 c2 
             WHERE c2.constant_name NOT IN (SELECT constant_name FROM consts_in_common1 c1 
                                             WHERE c1.module_name = c2.module_name)) as constants2_unique
    """, (board1_id, board2_id))
    
    result = cursor.fetchone()
    print(f"\nClasses:")
    print(f"  Unique to {board1_name}: {result[0] + result[2]}")
    print(f"  Unique to {board2_name}: {result[1] + result[3]}")
    
    print(f"\nFunctions:")
    print(f"  Unique to {board1_name}: {result[4]}")
    print(f"  Unique to {board2_name}: {result[5]}")
    
    print(f"\nConstants:")
    print(f"  Unique to {board1_name}: {result[6]}")
    print(f"  Unique to {board2_name}: {result[7]}")
    
    # Level 3: Methods and attributes comparison
    print("\n" + "=" * 40)
    print("LEVEL 3: Methods and Attributes")
    print("=" * 40)
    
    cursor.execute("""
        WITH board1_modules AS (
            SELECT module_name FROM v_board_comparison_modules WHERE board_id = ?1
        ),
        board2_modules AS (
            SELECT module_name FROM v_board_comparison_modules WHERE board_id = ?2
        ),
        common_modules AS (
            SELECT b1.module_name FROM board1_modules b1 
            INNER JOIN board2_modules b2 ON b1.module_name = b2.module_name
        ),
        common_classes AS (
            SELECT c1.class_id as class_id1, c2.class_id as class_id2, 
                   c1.class_name, c1.module_name
            FROM v_board_comparison_classes c1
            INNER JOIN v_board_comparison_classes c2 
                ON c1.class_name = c2.class_name AND c1.module_name = c2.module_name
            INNER JOIN common_modules cm ON c1.module_name = cm.module_name
            WHERE c1.board_id = ?1 AND c2.board_id = ?2
        ),
        methods1 AS (
            SELECT m.method_id, m.method_name, m.class_id, cc.class_name, cc.module_name
            FROM v_board_comparison_methods m
            INNER JOIN common_classes cc ON m.class_id = cc.class_id1
            WHERE m.board_id = ?1
        ),
        methods2 AS (
            SELECT m.method_id, m.method_name, m.class_id, cc.class_name, cc.module_name
            FROM v_board_comparison_methods m
            INNER JOIN common_classes cc ON m.class_id = cc.class_id2
            WHERE m.board_id = ?2
        ),
        attrs1 AS (
            SELECT a.attribute_id, a.attribute_name, a.class_id, cc.class_name, cc.module_name
            FROM v_board_comparison_attributes a
            INNER JOIN common_classes cc ON a.class_id = cc.class_id1
            WHERE a.board_id = ?1
        ),
        attrs2 AS (
            SELECT a.attribute_id, a.attribute_name, a.class_id, cc.class_name, cc.module_name
            FROM v_board_comparison_attributes a
            INNER JOIN common_classes cc ON a.class_id = cc.class_id2
            WHERE a.board_id = ?2
        ),
        unique_modules1 AS (
            SELECT module_name FROM board1_modules 
            WHERE module_name NOT IN (SELECT module_name FROM board2_modules)
        ),
        unique_modules2 AS (
            SELECT module_name FROM board2_modules 
            WHERE module_name NOT IN (SELECT module_name FROM board1_modules)
        ),
        unique_classes1 AS (
            SELECT c.class_id FROM v_board_comparison_classes c
            INNER JOIN unique_modules1 u ON c.module_name = u.module_name
            WHERE c.board_id = ?1
        ),
        unique_classes2 AS (
            SELECT c.class_id FROM v_board_comparison_classes c
            INNER JOIN unique_modules2 u ON c.module_name = u.module_name
            WHERE c.board_id = ?2
        ),
        methods_unique_modules1 AS (
            SELECT m.method_id FROM v_board_comparison_methods m
            INNER JOIN unique_classes1 uc ON m.class_id = uc.class_id
            WHERE m.board_id = ?1
        ),
        methods_unique_modules2 AS (
            SELECT m.method_id FROM v_board_comparison_methods m
            INNER JOIN unique_classes2 uc ON m.class_id = uc.class_id
            WHERE m.board_id = ?2
        ),
        attrs_unique_modules1 AS (
            SELECT a.attribute_id FROM v_board_comparison_attributes a
            INNER JOIN unique_classes1 uc ON a.class_id = uc.class_id
            WHERE a.board_id = ?1
        ),
        attrs_unique_modules2 AS (
            SELECT a.attribute_id FROM v_board_comparison_attributes a
            INNER JOIN unique_classes2 uc ON a.class_id = uc.class_id
            WHERE a.board_id = ?2
        )
        SELECT 
            (SELECT COUNT(*) FROM methods1 m1 
             WHERE NOT EXISTS (SELECT 1 FROM methods2 m2 
                               WHERE m2.method_name = m1.method_name 
                               AND m2.class_name = m1.class_name 
                               AND m2.module_name = m1.module_name)) 
            + (SELECT COUNT(*) FROM methods_unique_modules1) as methods1_unique,
            (SELECT COUNT(*) FROM methods2 m2 
             WHERE NOT EXISTS (SELECT 1 FROM methods1 m1 
                               WHERE m1.method_name = m2.method_name 
                               AND m1.class_name = m2.class_name 
                               AND m1.module_name = m2.module_name))
            + (SELECT COUNT(*) FROM methods_unique_modules2) as methods2_unique,
            (SELECT COUNT(*) FROM attrs1 a1 
             WHERE NOT EXISTS (SELECT 1 FROM attrs2 a2 
                               WHERE a2.attribute_name = a1.attribute_name 
                               AND a2.class_name = a1.class_name 
                               AND a2.module_name = a1.module_name))
            + (SELECT COUNT(*) FROM attrs_unique_modules1) as attributes1_unique,
            (SELECT COUNT(*) FROM attrs2 a2 
             WHERE NOT EXISTS (SELECT 1 FROM attrs1 a1 
                               WHERE a1.attribute_name = a2.attribute_name 
                               AND a1.class_name = a2.class_name 
                               AND a1.module_name = a2.module_name))
            + (SELECT COUNT(*) FROM attrs_unique_modules2) as attributes2_unique,
            (SELECT COUNT(DISTINCT class_name || ':' || module_name) 
             FROM (SELECT m1.class_name, m1.module_name FROM methods1 m1 
                   WHERE NOT EXISTS (SELECT 1 FROM methods2 m2 
                                     WHERE m2.method_name = m1.method_name 
                                     AND m2.class_name = m1.class_name 
                                     AND m2.module_name = m1.module_name)
                   UNION
                   SELECT m2.class_name, m2.module_name FROM methods2 m2 
                   WHERE NOT EXISTS (SELECT 1 FROM methods1 m1 
                                     WHERE m1.method_name = m2.method_name 
                                     AND m1.class_name = m2.class_name 
                                     AND m1.module_name = m2.module_name))) as methods_different,
            (SELECT COUNT(DISTINCT class_name || ':' || module_name) 
             FROM (SELECT a1.class_name, a1.module_name FROM attrs1 a1 
                   WHERE NOT EXISTS (SELECT 1 FROM attrs2 a2 
                                     WHERE a2.attribute_name = a1.attribute_name 
                                     AND a2.class_name = a1.class_name 
                                     AND a2.module_name = a1.module_name)
                   UNION
                   SELECT a2.class_name, a2.module_name FROM attrs2 a2 
                   WHERE NOT EXISTS (SELECT 1 FROM attrs1 a1 
                                     WHERE a1.attribute_name = a2.attribute_name 
                                     AND a1.class_name = a2.class_name 
                                     AND a1.module_name = a2.module_name))) as attributes_different
    """, (board1_id, board2_id))
    
    result = cursor.fetchone()
    print(f"\nMethods:")
    print(f"  Unique to {board1_name}: {result[0]}")
    print(f"  Unique to {board2_name}: {result[1]}")
    print(f"  Classes with different methods: {result[4]}")
    
    print(f"\nAttributes:")
    print(f"  Unique to {board1_name}: {result[2]}")
    print(f"  Unique to {board2_name}: {result[3]}")
    print(f"  Classes with different attributes: {result[5]}")


def main():
    """Main entry point."""
    print("MicroPython v1.26.0 Board Comparison: ESP32 vs STM32")
    print("=" * 80)
    
    if not DB_PATH.exists():
        print(f"ERROR: Database not found: {DB_PATH}")
        return 1
    
    print(f"\nDatabase: {DB_PATH}")
    print(f"Size: {DB_PATH.stat().st_size / (1024*1024):.1f} MB")
    
    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    # Get board IDs
    esp32_id = get_board_id(conn, "v1.26.0", "esp32", "esp32_generic")
    stm32_id = get_board_id(conn, "v1.26.0", "stm32", "pybv11")
    
    if not esp32_id:
        print("ERROR: ESP32 board not found (v1.26.0 / esp32 / esp32_generic)")
        return 1
    
    if not stm32_id:
        print("ERROR: STM32 board not found (v1.26.0 / stm32 / pybv11)")
        return 1
    
    print(f"\nBoard IDs:")
    print(f"  ESP32:  {esp32_id}")
    print(f"  STM32:  {stm32_id}")
    
    # Perform comparison
    compare_boards(conn, esp32_id, stm32_id, "ESP32", "STM32")
    
    conn.close()
    print("\n" + "=" * 80)
    print("Comparison complete!")
    print("=" * 80)
    
    return 0


if __name__ == "__main__":
    exit(main())
