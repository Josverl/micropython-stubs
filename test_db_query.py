import sqlite3

conn = sqlite3.connect('tools/board_compare/frontend/board_comparison.db')
cursor = conn.cursor()

# Test the exact query that search.py uses
cursor.execute("""
    SELECT DISTINCT
        entity_type,
        entity_name,
        entity_type_hint,
        entity_value,
        entity_return_type,
        entity_docstring,
        module_id,
        module_name,
        class_id,
        class_name,
        method_id,
        method_name,
        parent_name,
        board_id,
        version,
        port,
        board
    FROM v_board_entities
    WHERE entity_name LIKE ? COLLATE NOCASE
    LIMIT 100
""", ('%Pin%',))

results = cursor.fetchall()
print(f"Found {len(results)} results")

# Check if any result has issues
for i, row in enumerate(results[:10]):
    entity_type = row[0]
    entity_name = row[1]
    parent_name = row[12]
    print(f"{i+1}. {entity_type}: {entity_name}, parent={parent_name}")

conn.close()
print("\nQuery executed successfully!")
