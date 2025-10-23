"""
Benchmark search performance using v_board_entities view.

Compares the new unified query approach against what the old 6-query approach would have done.
"""

import sqlite3
import time
from pathlib import Path
from statistics import mean, stdev

# Database path
DB_PATH = Path(__file__).parent.parent.parent / "tools" / "board_compare" / "frontend" / "board_comparison.db"

# Test search terms that should hit different entity types
TEST_SEARCHES = [
    "machine",  # Common module name
    "Pin",  # Common class name
    "init",  # Common method name
    "value",  # Mixed: method, attribute, parameter
    "TIME",  # Test case-insensitivity
    "i2c",  # Short term, many matches
]


def benchmark_view_search(conn: sqlite3.Connection, search_term: str, iterations: int = 10) -> dict:
    """
    Benchmark the new unified view query.
    
    Returns:
        dict with 'mean_ms', 'stdev_ms', 'result_count', 'entity_types'
    """
    cursor = conn.cursor()
    pattern = f"%{search_term}%"
    timings = []
    result_count = 0
    entity_types = set()
    
    for _ in range(iterations):
        start = time.perf_counter()
        
        cursor.execute("""
            SELECT DISTINCT
                entity_type,
                entity_name,
                version,
                port,
                board,
                module_id,
                class_id,
                class_name as parent_name
            FROM v_board_entities
            WHERE entity_name LIKE ? COLLATE NOCASE
            ORDER BY version DESC, port, board, module_id, entity_type, entity_name
        """, (pattern,))
        
        results = cursor.fetchall()
        
        end = time.perf_counter()
        timings.append((end - start) * 1000)  # Convert to ms
        
        if result_count == 0:  # Only count on first iteration
            result_count = len(results)
            entity_types = {row[0] for row in results}
    
    return {
        "mean_ms": mean(timings),
        "stdev_ms": stdev(timings) if len(timings) > 1 else 0,
        "result_count": result_count,
        "entity_types": sorted(entity_types),
    }


def benchmark_traditional_search(conn: sqlite3.Connection, search_term: str, iterations: int = 10) -> dict:
    """
    Benchmark what the old 6-query approach would have done.
    
    Note: This simulates the old approach by running 6 separate queries.
    """
    cursor = conn.cursor()
    pattern = f"%{search_term}%"
    timings = []
    result_count = 0
    
    queries = [
        # Modules
        """
        SELECT DISTINCT 
            um.name as entity_name,
            'module' as entity_type,
            b.version, b.port, b.board,
            um.id as module_id,
            NULL as class_id,
            NULL as parent_name
        FROM unique_modules um
        JOIN board_module_support bms ON um.id = bms.module_id
        JOIN boards b ON bms.board_id = b.id
        WHERE um.name LIKE ? COLLATE NOCASE
        ORDER BY b.version DESC, b.port, b.board, um.name
        """,
        # Classes
        """
        SELECT DISTINCT
            uc.name as entity_name,
            'class' as entity_type,
            b.version, b.port, b.board,
            um.id as module_id,
            uc.id as class_id,
            um.name as parent_name
        FROM unique_classes uc
        JOIN unique_modules um ON uc.module_id = um.id
        JOIN board_class_support bcs ON uc.id = bcs.class_id
        JOIN boards b ON bcs.board_id = b.id
        WHERE uc.name LIKE ? COLLATE NOCASE
        ORDER BY b.version DESC, b.port, b.board, um.name, uc.name
        """,
        # Methods
        """
        SELECT DISTINCT
            umet.name as entity_name,
            'method' as entity_type,
            b.version, b.port, b.board,
            um.id as module_id,
            uc.id as class_id,
            uc.name as parent_name
        FROM unique_methods umet
        JOIN unique_classes uc ON umet.class_id = uc.id
        JOIN unique_modules um ON uc.module_id = um.id
        JOIN board_method_support bmets ON umet.id = bmets.method_id
        JOIN boards b ON bmets.board_id = b.id
        WHERE umet.name LIKE ? COLLATE NOCASE
        ORDER BY b.version DESC, b.port, b.board, um.name, uc.name, umet.name
        """,
        # Constants
        """
        SELECT DISTINCT
            umc.name as entity_name,
            'constant' as entity_type,
            b.version, b.port, b.board,
            um.id as module_id,
            NULL as class_id,
            um.name as parent_name
        FROM unique_module_constants umc
        JOIN unique_modules um ON umc.module_id = um.id
        JOIN board_module_constant_support bmcs ON umc.id = bmcs.constant_id
        JOIN boards b ON bmcs.board_id = b.id
        WHERE umc.name LIKE ? COLLATE NOCASE
        ORDER BY b.version DESC, b.port, b.board, um.name, umc.name
        """,
        # Attributes
        """
        SELECT DISTINCT
            uca.name as entity_name,
            'attribute' as entity_type,
            b.version, b.port, b.board,
            um.id as module_id,
            uc.id as class_id,
            uc.name as parent_name
        FROM unique_class_attributes uca
        JOIN unique_classes uc ON uca.class_id = uc.id
        JOIN unique_modules um ON uc.module_id = um.id
        JOIN board_class_attribute_support bcas ON uca.id = bcas.attribute_id
        JOIN boards b ON bcas.board_id = b.id
        WHERE uca.name LIKE ? COLLATE NOCASE
        ORDER BY b.version DESC, b.port, b.board, um.name, uc.name, uca.name
        """,
        # Parameters
        """
        SELECT DISTINCT
            up.name as entity_name,
            'parameter' as entity_type,
            b.version, b.port, b.board,
            um.id as module_id,
            uc.id as class_id,
            umet.name as parent_name
        FROM unique_parameters up
        JOIN unique_methods umet ON up.method_id = umet.id
        JOIN unique_classes uc ON umet.class_id = uc.id
        JOIN unique_modules um ON uc.module_id = um.id
        JOIN board_method_support bmets ON umet.id = bmets.method_id
        JOIN boards b ON bmets.board_id = b.id
        WHERE up.name LIKE ? COLLATE NOCASE
        ORDER BY b.version DESC, b.port, b.board, um.name, uc.name, umet.name, up.name
        """
    ]
    
    for _ in range(iterations):
        start = time.perf_counter()
        
        all_results = []
        for query in queries:
            cursor.execute(query, (pattern,))
            all_results.extend(cursor.fetchall())
        
        end = time.perf_counter()
        timings.append((end - start) * 1000)  # Convert to ms
        
        if result_count == 0:  # Only count on first iteration
            result_count = len(all_results)
    
    return {
        "mean_ms": mean(timings),
        "stdev_ms": stdev(timings) if len(timings) > 1 else 0,
        "result_count": result_count,
        "query_count": len(queries),
    }


def main():
    """Run benchmarks and report results."""
    if not DB_PATH.exists():
        print(f"❌ Database not found at {DB_PATH}")
        print("   Run build_database.py first to create the database.")
        return
    
    print("🔍 Search Performance Benchmark")
    print("=" * 80)
    print(f"Database: {DB_PATH}")
    print(f"Test searches: {', '.join(TEST_SEARCHES)}")
    print()
    
    conn = sqlite3.connect(DB_PATH)
    
    # Run benchmarks for each search term
    for search_term in TEST_SEARCHES:
        print(f"\n📊 Search: '{search_term}'")
        print("-" * 80)
        
        # Traditional approach (6 queries)
        traditional = benchmark_traditional_search(conn, search_term)
        print(f"Traditional (6 queries):")
        print(f"  Time: {traditional['mean_ms']:.2f}ms ± {traditional['stdev_ms']:.2f}ms")
        print(f"  Results: {traditional['result_count']}")
        
        # View approach (1 query)
        view = benchmark_view_search(conn, search_term)
        print(f"\nView (1 query):")
        print(f"  Time: {view['mean_ms']:.2f}ms ± {view['stdev_ms']:.2f}ms")
        print(f"  Results: {view['result_count']}")
        print(f"  Entity types: {', '.join(view['entity_types'])}")
        
        # Performance comparison
        speedup = traditional['mean_ms'] / view['mean_ms']
        if speedup > 1:
            print(f"\n✅ View is {speedup:.2f}x faster ({traditional['mean_ms'] - view['mean_ms']:.2f}ms saved)")
        elif speedup < 1:
            print(f"\n⚠️ View is {1/speedup:.2f}x slower ({view['mean_ms'] - traditional['mean_ms']:.2f}ms penalty)")
        else:
            print(f"\n➖ Same performance")
    
    conn.close()
    
    print("\n" + "=" * 80)
    print("Summary:")
    print("- View consolidates 6 queries into 1")
    print("- Simpler code, easier maintenance")
    print("- Performance impact varies by search term")


if __name__ == "__main__":
    main()
