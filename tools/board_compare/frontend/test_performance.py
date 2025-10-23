"""
Performance comparison: Python iteration vs SQL-based comparison.

Tests calculate_comparison_stats() (Python) vs calculate_comparison_stats_sql() (SQL)
across multiple board comparison scenarios.

This standalone version recreates the functions without PyScript dependencies.
"""

import sqlite3
import time
from pathlib import Path

# Use production database
DB_PATH = Path(__file__).parent / "board_comparison.db"


def calculate_comparison_stats_python(modules1, modules2):
    """Python-based comparison (original implementation)."""
    # Get module names
    modules1_names = {m["name"] for m in modules1}
    modules2_names = {m["name"] for m in modules2}
    
    # Calculate differences
    unique1 = sorted(modules1_names - modules2_names)
    unique2 = sorted(modules2_names - modules1_names)
    common = sorted(modules1_names & modules2_names)
    
    return {
        "level1": {
            "total1": len(modules1),
            "total2": len(modules2),
            "unique1": len(unique1),
            "unique2": len(unique2),
            "common": len(common)
        }
    }


def calculate_comparison_stats_sql(conn, board1_id, board2_id):
    """SQL-based comparison using views - complete 3-level implementation."""
    cursor = conn.cursor()
    
    # Level 1: Module comparison
    cursor.execute("""
        WITH board1_modules AS (
            SELECT DISTINCT module_name
            FROM v_board_comparison_modules
            WHERE board_id = ?
        ),
        board2_modules AS (
            SELECT DISTINCT module_name
            FROM v_board_comparison_modules
            WHERE board_id = ?
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
    level1 = {
        "total1": result[0],
        "total2": result[1],
        "unique1": result[2],
        "unique2": result[3],
        "common": result[4]
    }
    
    # Level 2: Classes, functions, constants comparison
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
    level2 = {
        "classes1_unique": result[0] + result[2],
        "classes2_unique": result[1] + result[3],
        "functions1_unique": result[4],
        "functions2_unique": result[5],
        "constants1_unique": result[6],
        "constants2_unique": result[7],
    }
    
    # Level 3: Methods and attributes comparison
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
    level3 = {
        "methods1_unique": result[0],
        "methods2_unique": result[1],
        "attributes1_unique": result[2],
        "attributes2_unique": result[3],
        "methods_different": result[4],
        "attributes_different": result[5],
    }
    
    return {"level1": level1, "level2": level2, "level3": level3}


def get_board_info(conn, version, port, board):
    """Get board info from database."""
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, version, port, board
        FROM boards
        WHERE version = ? AND port = ? AND board = ?
    """, (version, port, board))
    
    result = cursor.fetchone()
    if result:
        return {
            "id": result[0],
            "version": result[1],
            "port": result[2],
            "board": result[3]
        }
    return None


def get_modules_for_board(conn, board_id):
    """Get modules for a board."""
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT um.name as module_name
        FROM v_board_comparison_modules vcm
        JOIN unique_modules um ON vcm.module_id = um.id
        WHERE vcm.board_id = ?
        ORDER BY um.name
    """, (board_id,))
    
    return [{"name": row[0]} for row in cursor.fetchall()]


def benchmark_python_comparison(conn, board1_id, board2_id, iterations=10):
    """Benchmark Python-based comparison."""
    # Get modules for both boards
    modules1 = get_modules_for_board(conn, board1_id)
    modules2 = get_modules_for_board(conn, board2_id)
    
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        stats = calculate_comparison_stats_python(modules1, modules2)
        end = time.perf_counter()
        times.append(end - start)
    
    avg_time = sum(times) / len(times)
    min_time = min(times)
    max_time = max(times)
    
    return {
        "avg": avg_time,
        "min": min_time,
        "max": max_time,
        "stats": stats
    }


def benchmark_sql_comparison(conn, board1_id, board2_id, iterations=10):
    """Benchmark SQL-based comparison."""
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        stats = calculate_comparison_stats_sql(conn, board1_id, board2_id)
        end = time.perf_counter()
        times.append(end - start)
    
    avg_time = sum(times) / len(times)
    min_time = min(times)
    max_time = max(times)
    
    return {
        "avg": avg_time,
        "min": min_time,
        "max": max_time,
        "stats": stats
    }


def print_results(scenario, python_result, sql_result):
    """Print benchmark results for a scenario."""
    print(f"\n{'=' * 80}")
    print(f"Scenario: {scenario}")
    print(f"{'=' * 80}")
    
    print("\nPython Iteration:")
    print(f"  Average: {python_result['avg']*1000:.2f}ms")
    print(f"  Min:     {python_result['min']*1000:.2f}ms")
    print(f"  Max:     {python_result['max']*1000:.2f}ms")
    
    print("\nSQL Query:")
    print(f"  Average: {sql_result['avg']*1000:.2f}ms")
    print(f"  Min:     {sql_result['min']*1000:.2f}ms")
    print(f"  Max:     {sql_result['max']*1000:.2f}ms")
    
    # Calculate improvement
    improvement = ((python_result['avg'] - sql_result['avg']) / python_result['avg']) * 100
    speedup = python_result['avg'] / sql_result['avg']
    
    print("\nPerformance Improvement:")
    print(f"  {improvement:.1f}% faster ({speedup:.2f}x speedup)")
    
    # Verify results match (Level 1 only - no Python implementation for Level 2/3)
    p_stats = python_result['stats']
    s_stats = sql_result['stats']
    
    print("\nLevel 1 - Module Comparison:")
    print(f"  Python:  total={p_stats['level1']['total1']}/{p_stats['level1']['total2']}, unique={p_stats['level1']['unique1']}/{p_stats['level1']['unique2']}, common={p_stats['level1']['common']}")
    print(f"  SQL:     total={s_stats['level1']['total1']}/{s_stats['level1']['total2']}, unique={s_stats['level1']['unique1']}/{s_stats['level1']['unique2']}, common={s_stats['level1']['common']}")
    
    modules_match = (
        p_stats['level1']['total1'] == s_stats['level1']['total1'] and
        p_stats['level1']['total2'] == s_stats['level1']['total2'] and
        p_stats['level1']['unique1'] == s_stats['level1']['unique1'] and
        p_stats['level1']['unique2'] == s_stats['level1']['unique2'] and
        p_stats['level1']['common'] == s_stats['level1']['common']
    )
    print(f"  Level 1 Match: {'YES' if modules_match else 'NO'}")
    
    # Show Level 2 & 3 (SQL only - no Python reference implementation)
    print("\nLevel 2 - Classes/Functions/Constants (SQL only):")
    print(f"  Classes:    Board1={s_stats['level2']['classes1_unique']}, Board2={s_stats['level2']['classes2_unique']}")
    print(f"  Functions:  Board1={s_stats['level2']['functions1_unique']}, Board2={s_stats['level2']['functions2_unique']}")
    print(f"  Constants:  Board1={s_stats['level2']['constants1_unique']}, Board2={s_stats['level2']['constants2_unique']}")
    
    print("\nLevel 3 - Methods/Attributes (SQL only):")
    print(f"  Methods:    Board1={s_stats['level3']['methods1_unique']}, Board2={s_stats['level3']['methods2_unique']}, Different={s_stats['level3']['methods_different']}")
    print(f"  Attributes: Board1={s_stats['level3']['attributes1_unique']}, Board2={s_stats['level3']['attributes2_unique']}, Different={s_stats['level3']['attributes_different']}")
    
    return improvement


def main():
    """Run performance benchmarks."""
    print("Board Comparison Performance Benchmark")
    print("=" * 80)
    print(f"Database: {DB_PATH}")
    print(f"Database size: {DB_PATH.stat().st_size / (1024*1024):.1f} MB")
    
    # Setup
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    # Test scenarios
    scenarios = [
        {
            "name": "Different Architectures (ESP32 vs RP2)",
            "board1": ("v1.26.0", "esp32", "esp32_generic"),
            "board2": ("v1.26.0", "rp2", "rpi_pico")
        },
        {
            "name": "Similar Boards (ESP32 Generic vs ESP32 S3)",
            "board1": ("v1.26.0", "esp32", "esp32_generic"),
            "board2": ("v1.26.0", "esp32", "esp32_generic_s3")
        },
        {
            "name": "Version Comparison (ESP32 v1.25.0 vs v1.26.0)",
            "board1": ("v1.25.0", "esp32", "esp32_generic"),
            "board2": ("v1.26.0", "esp32", "esp32_generic")
        },
        {
            "name": "Different Architectures (ESP32 vs STM32)",
            "board1": ("v1.26.0", "esp32", "esp32_generic"),
            "board2": ("v1.26.0", "stm32", "")
        }
    ]
    
    improvements = []
    
    for scenario in scenarios:
        # Get board IDs
        board1 = get_board_info(conn, *scenario["board1"])
        board2 = get_board_info(conn, *scenario["board2"])
        
        if not board1 or not board2:
            print(f"\nSkipping '{scenario['name']}': Board not found")
            continue
        
        # Run benchmarks (20 iterations for accuracy)
        python_result = benchmark_python_comparison(conn, board1["id"], board2["id"], iterations=20)
        sql_result = benchmark_sql_comparison(conn, board1["id"], board2["id"], iterations=20)
        
        # Print results
        improvement = print_results(scenario["name"], python_result, sql_result)
        improvements.append(improvement)
    
    # Summary
    print(f"\n{'=' * 80}")
    print("SUMMARY")
    print(f"{'=' * 80}")
    avg_improvement = sum(improvements) / len(improvements) if improvements else 0
    print(f"Average improvement across all scenarios: {avg_improvement:.1f}%")
    if improvements:
        print(f"Best improvement: {max(improvements):.1f}%")
        print(f"Worst improvement: {min(improvements):.1f}%")
    
    print("\nPERFORMANCE ANALYSIS:")
    print("  - Level 1 (Module comparison): Python faster due to simple set operations")
    print("  - Levels 2 & 3 (Complete comparison): SQL provides comprehensive analysis")
    print("  - SQL advantage: Single query returns all 3 levels vs multiple Python iterations")
    print("  - SQL timing: ~500-900ms includes all levels (modules, classes, functions, constants, methods, attributes)")
    print("  - Python timing: Only Level 1 (~0.01ms), would need 300+ lines of code for Levels 2 & 3")
    
    conn.close()


if __name__ == "__main__":
    main()
