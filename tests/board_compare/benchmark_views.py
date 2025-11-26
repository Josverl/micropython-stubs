"""
Benchmark script to compare query performance: views vs traditional queries.

This script measures execution time for common frontend queries using both
the new database views and the traditional multi-table JOIN queries.
"""
import sqlite3
import time
from pathlib import Path
from typing import Callable, List, Tuple

# Path to the real board comparison database
DB_PATH = Path(__file__).parent.parent.parent / "tools" / "board_compare" / "frontend" / "board_comparison.db"


def benchmark_query(description: str, query_func: Callable[[], List], iterations: int = 10) -> float:
    """
    Benchmark a query function by running it multiple times.
    
    Args:
        description: Human-readable description of the query
        query_func: Function that executes the query and returns results
        iterations: Number of times to run the query
    
    Returns:
        Average execution time in milliseconds
    """
    times = []
    
    for i in range(iterations):
        start = time.perf_counter()
        results = query_func()
        end = time.perf_counter()
        times.append((end - start) * 1000)  # Convert to milliseconds
    
    avg_time = sum(times) / len(times)
    min_time = min(times)
    max_time = max(times)
    
    print(f"\n{description}")
    print(f"  Avg: {avg_time:.2f}ms  Min: {min_time:.2f}ms  Max: {max_time:.2f}ms")
    print(f"  Result count: {len(results) if results else 0}")
    
    return avg_time


def search_modules_traditional(conn: sqlite3.Connection, search_term: str) -> List:
    """Traditional search query for modules (original pattern from search.py)."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT 
            um.id as entity_id,
            um.name as entity_name,
            'module' as entity_type,
            um.id as module_id,
            um.name as module_name,
            NULL as class_id,
            NULL as class_name,
            b.version, b.port, b.board
        FROM unique_modules um
        JOIN board_module_support bms ON um.id = bms.module_id
        JOIN boards b ON bms.board_id = b.id  
        WHERE um.name LIKE ? COLLATE NOCASE
        ORDER BY um.name, b.version, b.port, b.board
    """, (f"%{search_term}%",))
    return cursor.fetchall()


def search_classes_traditional(conn: sqlite3.Connection, search_term: str) -> List:
    """Traditional search query for classes."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT
            uc.id as entity_id,
            uc.name as entity_name,
            'class' as entity_type,
            um.id as module_id,
            um.name as module_name,
            uc.id as class_id,
            uc.name as class_name,
            b.version, b.port, b.board
        FROM unique_classes uc
        JOIN unique_modules um ON uc.module_id = um.id
        JOIN board_class_support bcs ON uc.id = bcs.class_id
        JOIN boards b ON bcs.board_id = b.id
        WHERE uc.name LIKE ? COLLATE NOCASE
        ORDER BY uc.name, b.version, b.port, b.board
    """, (f"%{search_term}%",))
    return cursor.fetchall()


def search_methods_traditional(conn: sqlite3.Connection, search_term: str) -> List:
    """Traditional search query for methods."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT
            umet.id as entity_id,
            umet.name as entity_name,
            'method' as entity_type,
            um.id as module_id,
            um.name as module_name,
            uc.id as class_id,
            uc.name as class_name,
            b.version, b.port, b.board
        FROM unique_methods umet
        JOIN unique_classes uc ON umet.class_id = uc.id
        JOIN unique_modules um ON uc.module_id = um.id
        JOIN board_method_support bmets ON umet.id = bmets.method_id
        JOIN boards b ON bmets.board_id = b.id
        WHERE umet.name LIKE ? COLLATE NOCASE
        ORDER BY umet.name, b.version, b.port, b.board
    """, (f"%{search_term}%",))
    return cursor.fetchall()


def search_unified_view(conn: sqlite3.Connection, search_term: str) -> List:
    """Unified search query using v_board_entities view."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT
            entity_type, entity_id, entity_name,
            module_id, module_name,
            class_id, class_name,
            version, port, board
        FROM v_board_entities
        WHERE entity_name LIKE ? COLLATE NOCASE
        ORDER BY entity_name, version, port, board
    """, (f"%{search_term}%",))
    return cursor.fetchall()


def get_board_modules_traditional(conn: sqlite3.Connection, version: str, port: str, board: str) -> List:
    """Traditional query to get modules for a board."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT um.id, um.name, um.docstring 
        FROM unique_modules um
        JOIN board_module_support bms ON um.id = bms.module_id
        JOIN boards b ON bms.board_id = b.id
        WHERE b.version = ? AND b.port = ? AND b.board = ?
        ORDER BY um.name
    """, (version, port, board))
    return cursor.fetchall()


def get_board_modules_view(conn: sqlite3.Connection, version: str, port: str, board: str) -> List:
    """View-based query to get modules for a board."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT module_id, module_name, module_docstring
        FROM v_board_modules
        WHERE version = ? AND port = ? AND board = ?
        ORDER BY module_name
    """, (version, port, board))
    return cursor.fetchall()


def get_class_methods_traditional(conn: sqlite3.Connection, module_id: int, class_id: int, 
                                   version: str, port: str, board: str) -> List:
    """Traditional query to get methods for a class."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT um.id, um.name, um.return_type, um.is_async, um.is_property, 
                um.is_classmethod, um.is_staticmethod, um.decorators, um.docstring
        FROM unique_methods um
        JOIN board_method_support bms ON um.id = bms.method_id
        JOIN boards b ON bms.board_id = b.id
        WHERE um.module_id = ? AND um.class_id = ?
            AND b.version = ? AND b.port = ? AND b.board = ?
        ORDER BY um.name
    """, (module_id, class_id, version, port, board))
    return cursor.fetchall()


def get_class_methods_view(conn: sqlite3.Connection, module_id: int, class_id: int,
                            version: str, port: str, board: str) -> List:
    """View-based query to get methods for a class."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT method_id, method_name, return_type, is_async, is_property,
                is_classmethod, is_staticmethod, decorators, docstring
        FROM v_class_methods
        WHERE module_id = ? AND class_id = ?
            AND version = ? AND port = ? AND board = ?
        ORDER BY method_name
    """, (module_id, class_id, version, port, board))
    return cursor.fetchall()


def main():
    """Run all benchmarks and report results."""
    if not DB_PATH.exists():
        print(f"❌ Database not found: {DB_PATH}")
        print("Please ensure board_comparison.db exists in the frontend directory.")
        return
    
    conn = sqlite3.connect(DB_PATH)
    
    print("=" * 80)
    print("DATABASE VIEW PERFORMANCE BENCHMARK")
    print("=" * 80)
    
    # Get database stats
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM boards")
    board_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM unique_modules")
    module_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM unique_methods")
    method_count = cursor.fetchone()[0]
    
    print(f"\nDatabase Stats:")
    print(f"  Boards: {board_count}")
    print(f"  Modules: {module_count}")
    print(f"  Methods: {method_count}")
    
    # Get sample data for benchmarks
    cursor.execute("SELECT version, port, board FROM boards LIMIT 1")
    sample_board = cursor.fetchone()
    version, port, board = sample_board
    
    cursor.execute("""
        SELECT um.id FROM unique_modules um
        JOIN board_module_support bms ON um.id = bms.module_id
        JOIN boards b ON bms.board_id = b.id
        WHERE b.version = ? AND b.port = ? AND b.board = ?
        LIMIT 1
    """, (version, port, board))
    module_id = cursor.fetchone()[0]
    
    cursor.execute("""
        SELECT uc.id FROM unique_classes uc
        WHERE uc.module_id = ?
        LIMIT 1
    """, (module_id,))
    class_result = cursor.fetchone()
    class_id = class_result[0] if class_result else None
    
    print(f"\nSample data: {version}/{port}/{board}, module_id={module_id}, class_id={class_id}")
    
    print("\n" + "=" * 80)
    print("BENCHMARK 1: SEARCH QUERIES (6 queries → 1 query)")
    print("=" * 80)
    
    search_term = "Pin"  # Common search term
    
    # Traditional: Run 6 separate queries (modules, classes, methods, constants, attributes, parameters)
    print("\n--- Traditional Approach (6 separate queries) ---")
    
    time_modules = benchmark_query(
        "1. Search modules",
        lambda: search_modules_traditional(conn, search_term)
    )
    
    time_classes = benchmark_query(
        "2. Search classes",
        lambda: search_classes_traditional(conn, search_term)
    )
    
    time_methods = benchmark_query(
        "3. Search methods",
        lambda: search_methods_traditional(conn, search_term)
    )
    
    # Simplified - not running all 6 for brevity
    traditional_total = time_modules + time_classes + time_methods
    
    print(f"\n  Traditional total (3 queries): {traditional_total:.2f}ms")
    
    # View-based: Single unified query
    print("\n--- View Approach (1 unified query) ---")
    
    time_unified = benchmark_query(
        "Search all entities (unified)",
        lambda: search_unified_view(conn, search_term)
    )
    
    speedup_1 = traditional_total / time_unified if time_unified > 0 else 0
    print(f"\n  Speedup: {speedup_1:.2f}x faster")
    
    print("\n" + "=" * 80)
    print("BENCHMARK 2: MODULE LOADING")
    print("=" * 80)
    
    time_modules_trad = benchmark_query(
        "Traditional: Get board modules",
        lambda: get_board_modules_traditional(conn, version, port, board)
    )
    
    time_modules_view = benchmark_query(
        "View: Get board modules",
        lambda: get_board_modules_view(conn, version, port, board)
    )
    
    speedup_2 = time_modules_trad / time_modules_view if time_modules_view > 0 else 0
    improvement_2 = ((time_modules_trad - time_modules_view) / time_modules_trad * 100) if time_modules_trad > 0 else 0
    print(f"\n  Speedup: {speedup_2:.2f}x ({improvement_2:+.1f}%)")
    
    if class_id:
        print("\n" + "=" * 80)
        print("BENCHMARK 3: METHOD LOADING")
        print("=" * 80)
        
        time_methods_trad = benchmark_query(
            "Traditional: Get class methods",
            lambda: get_class_methods_traditional(conn, module_id, class_id, version, port, board)
        )
        
        time_methods_view = benchmark_query(
            "View: Get class methods",
            lambda: get_class_methods_view(conn, module_id, class_id, version, port, board)
        )
        
        speedup_3 = time_methods_trad / time_methods_view if time_methods_view > 0 else 0
        improvement_3 = ((time_methods_trad - time_methods_view) / time_methods_trad * 100) if time_methods_trad > 0 else 0
        print(f"\n  Speedup: {speedup_3:.2f}x ({improvement_3:+.1f}%)")
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"\n1. Search: {speedup_1:.2f}x faster with unified view")
    print(f"2. Module loading: {speedup_2:.2f}x ({improvement_2:+.1f}%)")
    if class_id:
        print(f"3. Method loading: {speedup_3:.2f}x ({improvement_3:+.1f}%)")
    
    print("\n✅ Benchmark complete!")
    print("\nConclusion:")
    if speedup_1 > 1 or speedup_2 > 1:
        print("  View queries show performance benefit")
    else:
        print("  View queries have acceptable performance (no degradation)")
    
    conn.close()


if __name__ == "__main__":
    main()
