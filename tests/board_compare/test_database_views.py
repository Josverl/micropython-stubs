"""
Comprehensive validation tests for database views.

This test suite validates that the SQLite views produce correct data
by comparing view results with equivalent queries on base tables.
"""
import os
import sqlite3

# Add parent directories to path
import sys
import tempfile
from pathlib import Path
from typing import List, Tuple

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "tools" / "board_compare"))

from build_database import DatabaseBuilder
from models import Board, Class, Method, Module, Parameter


@pytest.fixture(scope="module")
def test_db():
    """Create a test database with sample data."""
    tf = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
    tf.close()
    test_db_path = tf.name
    
    # Create database with schema and views
    builder = DatabaseBuilder(test_db_path)
    builder.connect()
    builder.create_schema()
    builder.create_views()
    
    # Add sample board
    board_data = {
        "version": "v1.26.0",
        "port": "esp32",
        "board": "generic",
        "package_name": "micropython-esp32-generic-stubs",
        "package_version": "1.26.0.post1",
        "modules": [
            {
                "name": "machine",
                "docstring": "Hardware control module",
                "classes": [
                    {
                        "name": "Pin",
                        "docstring": "GPIO Pin class",
                        "base_classes": ["object"],
                        "methods": [
                            {
                                "name": "__init__",
                                "parameters": [
                                    {"name": "self", "position": 0},
                                    {"name": "id", "position": 1, "type_hint": "int"},
                                    {"name": "mode", "position": 2, "type_hint": "int", "default_value": "IN"}
                                ],
                                "return_type": "None"
                            },
                            {
                                "name": "value",
                                "parameters": [
                                    {"name": "self", "position": 0},
                                    {"name": "val", "position": 1, "type_hint": "int", "is_optional": True}
                                ],
                                "return_type": "int | None",
                                "is_property": True
                            }
                        ],
                        "attributes": [
                            {"name": "IN", "type_hint": "int", "value": "0"},
                            {"name": "OUT", "type_hint": "int", "value": "1"}
                        ]
                    }
                ],
                "functions": [
                    {
                        "name": "reset",
                        "parameters": [],
                        "return_type": "None",
                        "docstring": "Reset the device"
                    }
                ],
                "constants": [
                    {"name": "FREQ_20MHZ", "value": "20000000", "type_hint": "int"}
                ]
            },
            {
                "name": "sys",
                "docstring": "System-specific functions",
                "classes": [],
                "functions": [
                    {
                        "name": "exit",
                        "parameters": [{"name": "code", "position": 0, "type_hint": "int", "default_value": "0"}],
                        "return_type": "None"
                    }
                ],
                "constants": []
            }
        ]
    }
    
    board_id = builder.add_board(board_data)
    builder.close()
    
    yield test_db_path
    
    # Cleanup
    if os.path.exists(test_db_path):
        os.unlink(test_db_path)


def test_all_views_exist(test_db):
    """Test that all expected views are created."""
    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='view' ORDER BY name")
    views = [row[0] for row in cursor.fetchall()]
    
    expected_views = [
        'v_board_entities',
        'v_board_modules',
        'v_class_methods',
        'v_entity_hierarchy',
        'v_module_classes'
    ]
    
    for view_name in expected_views:
        assert view_name in views, f"View {view_name} not found in database"
    
    conn.close()


def test_v_board_entities_completeness(test_db):
    """
    Test that v_board_entities view includes all entities from base tables.
    
    This test verifies that every module, class, method, constant, attribute,
    and parameter in the base tables appears in the unified view.
    """
    conn = sqlite3.connect(test_db)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Count entities from base tables
    cursor.execute("""
        SELECT COUNT(*) as count FROM unique_modules um
        JOIN board_module_support bms ON um.id = bms.module_id
    """)
    module_count_base = cursor.fetchone()['count']
    
    cursor.execute("""
        SELECT COUNT(*) as count FROM unique_classes uc
        JOIN board_class_support bcs ON uc.id = bcs.class_id
    """)
    class_count_base = cursor.fetchone()['count']
    
    cursor.execute("""
        SELECT COUNT(*) as count FROM unique_methods umet
        JOIN board_method_support bmets ON umet.id = bmets.method_id
    """)
    method_count_base = cursor.fetchone()['count']
    
    cursor.execute("""
        SELECT COUNT(*) as count FROM unique_module_constants umc
        JOIN board_module_constant_support bmcs ON umc.id = bmcs.constant_id
    """)
    constant_count_base = cursor.fetchone()['count']
    
    cursor.execute("""
        SELECT COUNT(*) as count FROM unique_class_attributes uca
        JOIN board_class_attribute_support bcas ON uca.id = bcas.attribute_id
    """)
    attribute_count_base = cursor.fetchone()['count']
    
    cursor.execute("""
        SELECT COUNT(*) as count FROM unique_parameters up
        JOIN unique_methods umet ON up.method_id = umet.id
        JOIN board_method_support bmets ON umet.id = bmets.method_id
    """)
    parameter_count_base = cursor.fetchone()['count']
    
    # Count entities from view
    cursor.execute("SELECT COUNT(*) as count FROM v_board_entities WHERE entity_type = 'module'")
    module_count_view = cursor.fetchone()['count']
    
    cursor.execute("SELECT COUNT(*) as count FROM v_board_entities WHERE entity_type = 'class'")
    class_count_view = cursor.fetchone()['count']
    
    cursor.execute("SELECT COUNT(*) as count FROM v_board_entities WHERE entity_type = 'method'")
    method_count_view = cursor.fetchone()['count']
    
    cursor.execute("SELECT COUNT(*) as count FROM v_board_entities WHERE entity_type = 'constant'")
    constant_count_view = cursor.fetchone()['count']
    
    cursor.execute("SELECT COUNT(*) as count FROM v_board_entities WHERE entity_type = 'attribute'")
    attribute_count_view = cursor.fetchone()['count']
    
    cursor.execute("SELECT COUNT(*) as count FROM v_board_entities WHERE entity_type = 'parameter'")
    parameter_count_view = cursor.fetchone()['count']
    
    # Verify counts match
    assert module_count_view == module_count_base, f"Module count mismatch: view={module_count_view}, base={module_count_base}"
    assert class_count_view == class_count_base, f"Class count mismatch: view={class_count_view}, base={class_count_base}"
    assert method_count_view == method_count_base, f"Method count mismatch: view={method_count_view}, base={method_count_base}"
    assert constant_count_view == constant_count_base, f"Constant count mismatch: view={constant_count_view}, base={constant_count_base}"
    assert attribute_count_view == attribute_count_base, f"Attribute count mismatch: view={attribute_count_view}, base={attribute_count_base}"
    assert parameter_count_view == parameter_count_base, f"Parameter count mismatch: view={parameter_count_view}, base={parameter_count_base}"
    
    # Verify expected test data counts
    assert module_count_view == 2, "Expected 2 modules (machine, sys)"
    assert class_count_view == 1, "Expected 1 class (Pin)"
    assert method_count_view == 4, "Expected 4 methods (Pin.__init__, Pin.value, machine.reset, sys.exit)"
    assert constant_count_view == 1, "Expected 1 constant (FREQ_20MHZ)"
    assert attribute_count_view == 2, "Expected 2 attributes (Pin.IN, Pin.OUT)"
    assert parameter_count_view == 6, "Expected 6 parameters across all methods"
    
    conn.close()


def test_v_board_entities_search(test_db):
    """
    Test that LIKE queries on v_board_entities return expected results.
    
    This simulates the search functionality in the frontend.
    """
    conn = sqlite3.connect(test_db)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Search for "Pin" - should find the class
    cursor.execute("""
        SELECT DISTINCT entity_type, entity_name
        FROM v_board_entities
        WHERE entity_name LIKE '%Pin%' COLLATE NOCASE
        ORDER BY entity_name
    """)
    pin_results = cursor.fetchall()
    
    assert len(pin_results) >= 1, "Should find at least the Pin class"
    entity_names = [r['entity_name'] for r in pin_results]
    assert 'Pin' in entity_names, "Pin class should be in search results"
    
    # Search for "value" - should find the method
    cursor.execute("""
        SELECT DISTINCT entity_type, entity_name, class_name
        FROM v_board_entities
        WHERE entity_name LIKE '%value%' COLLATE NOCASE
        ORDER BY entity_name
    """)
    value_results = cursor.fetchall()
    
    assert len(value_results) >= 1, "Should find the value method"
    method_found = any(r['entity_name'] == 'value' and r['class_name'] == 'Pin' for r in value_results)
    assert method_found, "Pin.value method should be in search results"
    
    # Search for "FREQ" - should find the constant
    cursor.execute("""
        SELECT DISTINCT entity_type, entity_name, module_name
        FROM v_board_entities
        WHERE entity_name LIKE '%FREQ%' COLLATE NOCASE
        ORDER BY entity_name
    """)
    freq_results = cursor.fetchall()
    
    assert len(freq_results) >= 1, "Should find the FREQ_20MHZ constant"
    constant_found = any(r['entity_name'] == 'FREQ_20MHZ' and r['module_name'] == 'machine' for r in freq_results)
    assert constant_found, "FREQ_20MHZ constant should be in search results"
    
    conn.close()


def test_v_board_modules_structure(test_db):
    """
    Test that v_board_modules view returns correct board-module associations.
    """
    conn = sqlite3.connect(test_db)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Get modules for the test board
    cursor.execute("""
        SELECT module_name, version, port, board
        FROM v_board_modules
        WHERE version = 'v1.26.0' AND port = 'esp32' AND board = 'generic'
        ORDER BY module_name
    """)
    modules = cursor.fetchall()
    
    assert len(modules) == 2, "Should have 2 modules (machine, sys)"
    
    module_names = [m['module_name'] for m in modules]
    assert 'machine' in module_names, "machine module should be present"
    assert 'sys' in module_names, "sys module should be present"
    
    # Verify board context is correct
    for module in modules:
        assert module['version'] == 'v1.26.0'
        assert module['port'] == 'esp32'
        assert module['board'] == 'generic'
    
    conn.close()


def test_v_module_classes_bases(test_db):
    """
    Test that v_module_classes correctly concatenates base classes.
    """
    conn = sqlite3.connect(test_db)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Get Pin class
    cursor.execute("""
        SELECT class_name, module_name, base_classes
        FROM v_module_classes
        WHERE class_name = 'Pin'
    """)
    pin_class = cursor.fetchone()
    
    assert pin_class is not None, "Pin class should exist in view"
    assert pin_class['class_name'] == 'Pin'
    assert pin_class['module_name'] == 'machine'
    assert pin_class['base_classes'] == 'object', "Base classes should be 'object'"
    
    conn.close()


def test_v_class_methods_context(test_db):
    """
    Test that v_class_methods provides complete context (module, class, board).
    """
    conn = sqlite3.connect(test_db)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Get __init__ method for Pin class
    cursor.execute("""
        SELECT method_name, class_name, module_name, version, port, board
        FROM v_class_methods
        WHERE method_name = '__init__' AND class_name = 'Pin'
    """)
    init_method = cursor.fetchone()
    
    assert init_method is not None, "__init__ method should exist"
    assert init_method['method_name'] == '__init__'
    assert init_method['class_name'] == 'Pin'
    assert init_method['module_name'] == 'machine'
    assert init_method['version'] == 'v1.26.0'
    assert init_method['port'] == 'esp32'
    assert init_method['board'] == 'generic'
    
    # Get value property for Pin class
    cursor.execute("""
        SELECT method_name, is_property
        FROM v_class_methods
        WHERE method_name = 'value' AND class_name = 'Pin'
    """)
    value_method = cursor.fetchone()
    
    assert value_method is not None, "value property should exist"
    assert value_method['is_property'] == 1, "value should be marked as property"
    
    conn.close()


def test_v_entity_hierarchy_parent_child(test_db):
    """
    Test that v_entity_hierarchy correctly represents parent-child relationships.
    """
    conn = sqlite3.connect(test_db)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Get machine module (root entity)
    cursor.execute("""
        SELECT entity_id, entity_type, parent_id, parent_type
        FROM v_entity_hierarchy
        WHERE entity_name = 'machine' AND entity_type = 'module'
    """)
    machine_module = cursor.fetchone()
    
    assert machine_module is not None, "machine module should exist"
    assert machine_module['parent_id'] is None, "Modules should have no parent"
    assert machine_module['parent_type'] is None
    
    machine_module_id = machine_module['entity_id']
    
    # Get Pin class (child of machine module)
    cursor.execute("""
        SELECT entity_id, entity_type, parent_id, parent_type
        FROM v_entity_hierarchy
        WHERE entity_name = 'Pin' AND entity_type = 'class'
    """)
    pin_class = cursor.fetchone()
    
    assert pin_class is not None, "Pin class should exist"
    assert pin_class['parent_id'] == machine_module_id, "Pin should be child of machine module"
    assert pin_class['parent_type'] == 'module'
    
    pin_class_id = pin_class['entity_id']
    
    # Get __init__ method (child of Pin class)
    cursor.execute("""
        SELECT entity_id, entity_type, parent_id, parent_type
        FROM v_entity_hierarchy
        WHERE entity_name = '__init__' AND entity_type = 'method'
    """)
    init_method = cursor.fetchone()
    
    assert init_method is not None, "__init__ method should exist"
    assert init_method['parent_id'] == pin_class_id, "__init__ should be child of Pin class"
    assert init_method['parent_type'] == 'class'
    
    # Get FREQ_20MHZ constant (child of machine module)
    cursor.execute("""
        SELECT entity_id, entity_type, parent_id, parent_type
        FROM v_entity_hierarchy
        WHERE entity_name = 'FREQ_20MHZ' AND entity_type = 'constant'
    """)
    constant = cursor.fetchone()
    
    assert constant is not None, "FREQ_20MHZ constant should exist"
    assert constant['parent_id'] == machine_module_id, "Constant should be child of machine module"
    assert constant['parent_type'] == 'module'
    
    # Get Pin attribute (child of Pin class)
    cursor.execute("""
        SELECT entity_id, entity_type, parent_id, parent_type
        FROM v_entity_hierarchy
        WHERE entity_name = 'IN' AND entity_type = 'attribute'
    """)
    attribute = cursor.fetchone()
    
    assert attribute is not None, "IN attribute should exist"
    assert attribute['parent_id'] == pin_class_id, "Attribute should be child of Pin class"
    assert attribute['parent_type'] == 'class'
    
    conn.close()


def test_view_query_performance_structure(test_db):
    """
    Test that views have the expected column structure for frontend queries.
    
    This doesn't test performance directly but validates that all expected
    columns are present and have the correct data types.
    """
    conn = sqlite3.connect(test_db)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Test v_board_entities columns
    cursor.execute("SELECT * FROM v_board_entities LIMIT 1")
    entity_row = cursor.fetchone()
    assert entity_row is not None, "View should return at least one row"
    
    expected_entity_columns = [
        'entity_type', 'entity_id', 'entity_name',
        'module_id', 'module_name',
        'class_id', 'class_name',
        'method_id', 'method_name',
        'board_id', 'version', 'port', 'board'
    ]
    
    for col in expected_entity_columns:
        assert col in entity_row.keys(), f"Column {col} missing from v_board_entities"
    
    # Test v_board_modules columns
    cursor.execute("SELECT * FROM v_board_modules LIMIT 1")
    module_row = cursor.fetchone()
    
    expected_module_columns = [
        'module_id', 'module_name', 'module_docstring',
        'board_id', 'version', 'port', 'board'
    ]
    
    for col in expected_module_columns:
        assert col in module_row.keys(), f"Column {col} missing from v_board_modules"
    
    conn.close()


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])
