#!/usr/bin/env python3
"""
Unit tests for the database builder component.
"""

import pytest
import tempfile
import json
import sqlite3
from pathlib import Path

from build_database import DatabaseBuilder
from models import Module, Class, Method, Parameter


class TestDatabaseBuilder:
    """Tests for DatabaseBuilder class."""
    
    @pytest.fixture
    def temp_db(self):
        """Create a temporary database file."""
        with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
            db_path = Path(f.name)
        yield db_path
        # Cleanup
        if db_path.exists():
            db_path.unlink()
    
    @pytest.fixture
    def builder(self, temp_db):
        """Create a DatabaseBuilder instance with temp database."""
        builder = DatabaseBuilder(temp_db)
        builder.connect()
        builder.create_schema()
        yield builder
        builder.close()
    
    def test_builder_initialization(self, temp_db):
        """Test database builder initialization."""
        builder = DatabaseBuilder(temp_db)
        assert builder.db_path == temp_db
        assert builder.conn is None
        builder.close()
    
    def test_connect_creates_database(self, temp_db):
        """Test that connect creates the database file."""
        builder = DatabaseBuilder(temp_db)
        builder.connect()
        
        assert temp_db.exists()
        assert builder.conn is not None
        builder.close()
    
    def test_create_schema(self, temp_db):
        """Test schema creation."""
        builder = DatabaseBuilder(temp_db)
        builder.connect()
        builder.create_schema()
        
        # Check that tables were created
        cursor = builder.conn.cursor()
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name NOT LIKE 'sqlite_%'
        """)
        tables = {row[0] for row in cursor.fetchall()}
        
        expected_tables = {
            'boards', 'modules', 'board_modules', 'classes', 
            'methods', 'parameters', 'module_constants', 
            'class_attributes', 'class_bases'
        }
        assert expected_tables.issubset(tables)
        builder.close()
    
    def test_add_simple_board(self, builder):
        """Test adding a simple board."""
        board_data = {
            "version": "v1.26.0",
            "port": "test",
            "board": "test_board",
            "modules": []
        }
        
        board_id = builder.add_board(board_data)
        assert board_id > 0
        
        # Verify board was added
        cursor = builder.conn.cursor()
        cursor.execute("SELECT version, port, board FROM boards WHERE id = ?", (board_id,))
        row = cursor.fetchone()
        assert row is not None
        assert row[0] == "v1.26.0"
        assert row[1] == "test"
        assert row[2] == "test_board"
    
    def test_add_board_with_module(self, builder):
        """Test adding a board with a module."""
        board_data = {
            "version": "v1.26.0",
            "port": "test",
            "board": "test_board",
            "modules": [
                {
                    "name": "test_module",
                    "docstring": "A test module",
                    "classes": [],
                    "functions": [],
                    "constants": []
                }
            ]
        }
        
        board_id = builder.add_board(board_data)
        assert board_id > 0
        
        # Verify module was added
        cursor = builder.conn.cursor()
        cursor.execute("""
            SELECT m.name FROM modules m
            JOIN board_modules bm ON m.id = bm.module_id
            WHERE bm.board_id = ?
        """, (board_id,))
        
        modules = [row[0] for row in cursor.fetchall()]
        assert "test_module" in modules
    
    def test_add_board_with_class(self, builder):
        """Test adding a board with a class."""
        board_data = {
            "version": "v1.26.0",
            "port": "test",
            "board": "test_board",
            "modules": [
                {
                    "name": "test_module",
                    "classes": [
                        {
                            "name": "TestClass",
                            "docstring": "A test class",
                            "base_classes": [],
                            "methods": [],
                            "attributes": []
                        }
                    ],
                    "functions": [],
                    "constants": []
                }
            ]
        }
        
        board_id = builder.add_board(board_data)
        
        # Verify class was added
        cursor = builder.conn.cursor()
        cursor.execute("""
            SELECT c.name FROM classes c
            JOIN modules m ON c.module_id = m.id
            JOIN board_modules bm ON m.id = bm.module_id
            WHERE bm.board_id = ?
        """, (board_id,))
        
        classes = [row[0] for row in cursor.fetchall()]
        assert "TestClass" in classes
    
    def test_add_board_with_method(self, builder):
        """Test adding a board with methods."""
        board_data = {
            "version": "v1.26.0",
            "port": "test",
            "board": "test_board",
            "modules": [
                {
                    "name": "test_module",
                    "classes": [
                        {
                            "name": "TestClass",
                            "methods": [
                                {
                                    "name": "test_method",
                                    "parameters": [
                                        {"name": "self"},
                                        {"name": "x", "type_hint": "int"}
                                    ],
                                    "return_type": "None"
                                }
                            ],
                            "base_classes": [],
                            "attributes": []
                        }
                    ],
                    "functions": [],
                    "constants": []
                }
            ]
        }
        
        board_id = builder.add_board(board_data)
        
        # Verify method was added
        cursor = builder.conn.cursor()
        cursor.execute("""
            SELECT mt.name FROM methods mt
            JOIN classes c ON mt.class_id = c.id
            WHERE c.name = 'TestClass'
        """)
        
        methods = [row[0] for row in cursor.fetchall()]
        assert "test_method" in methods
    
    def test_add_board_with_parameters(self, builder):
        """Test adding a board with method parameters."""
        board_data = {
            "version": "v1.26.0",
            "port": "test",
            "board": "test_board",
            "modules": [
                {
                    "name": "test_module",
                    "functions": [
                        {
                            "name": "test_func",
                            "parameters": [
                                {"name": "x", "type_hint": "int"},
                                {"name": "y", "type_hint": "str", "default_value": "''", "is_optional": True}
                            ],
                            "return_type": "bool"
                        }
                    ],
                    "classes": [],
                    "constants": []
                }
            ]
        }
        
        board_id = builder.add_board(board_data)
        
        # Verify parameters were added
        cursor = builder.conn.cursor()
        cursor.execute("""
            SELECT p.name, p.type_hint, p.is_optional FROM parameters p
            JOIN methods m ON p.method_id = m.id
            WHERE m.name = 'test_func'
            ORDER BY p.position
        """)
        
        params = cursor.fetchall()
        assert len(params) == 2
        assert params[0][0] == "x"
        assert params[0][1] == "int"
        assert params[1][0] == "y"
        assert params[1][2] == 1  # is_optional
    
    def test_add_module_constants(self, builder):
        """Test adding module constants."""
        board_data = {
            "version": "v1.26.0",
            "port": "test",
            "board": "test_board",
            "modules": [
                {
                    "name": "test_module",
                    "constants": ["CONST1", "CONST2", "VERSION"],
                    "classes": [],
                    "functions": []
                }
            ]
        }
        
        board_id = builder.add_board(board_data)
        
        # Verify constants were added
        cursor = builder.conn.cursor()
        cursor.execute("""
            SELECT mc.name FROM module_constants mc
            JOIN modules m ON mc.module_id = m.id
            WHERE m.name = 'test_module'
        """)
        
        constants = {row[0] for row in cursor.fetchall()}
        assert "CONST1" in constants
        assert "VERSION" in constants
    
    def test_add_class_attributes(self, builder):
        """Test adding class attributes."""
        board_data = {
            "version": "v1.26.0",
            "port": "test",
            "board": "test_board",
            "modules": [
                {
                    "name": "test_module",
                    "classes": [
                        {
                            "name": "TestClass",
                            "attributes": ["CONST1", "CONST2"],
                            "methods": [],
                            "base_classes": []
                        }
                    ],
                    "functions": [],
                    "constants": []
                }
            ]
        }
        
        board_id = builder.add_board(board_data)
        
        # Verify attributes were added
        cursor = builder.conn.cursor()
        cursor.execute("""
            SELECT ca.name FROM class_attributes ca
            JOIN classes c ON ca.class_id = c.id
            WHERE c.name = 'TestClass'
        """)
        
        attributes = {row[0] for row in cursor.fetchall()}
        assert "CONST1" in attributes
        assert "CONST2" in attributes
    
    def test_add_base_classes(self, builder):
        """Test adding base classes."""
        board_data = {
            "version": "v1.26.0",
            "port": "test",
            "board": "test_board",
            "modules": [
                {
                    "name": "test_module",
                    "classes": [
                        {
                            "name": "DerivedClass",
                            "base_classes": ["BaseClass", "Mixin"],
                            "methods": [],
                            "attributes": []
                        }
                    ],
                    "functions": [],
                    "constants": []
                }
            ]
        }
        
        board_id = builder.add_board(board_data)
        
        # Verify base classes were added
        cursor = builder.conn.cursor()
        cursor.execute("""
            SELECT cb.base_name FROM class_bases cb
            JOIN classes c ON cb.class_id = c.id
            WHERE c.name = 'DerivedClass'
        """)
        
        bases = {row[0] for row in cursor.fetchall()}
        assert "BaseClass" in bases
        assert "Mixin" in bases
    
    def test_module_deduplication(self, builder):
        """Test that modules are deduplicated across boards."""
        # Add two boards with the same module
        board1_data = {
            "version": "v1.26.0",
            "port": "test1",
            "board": "board1",
            "modules": [{"name": "shared_module", "classes": [], "functions": [], "constants": []}]
        }
        
        board2_data = {
            "version": "v1.26.0",
            "port": "test2",
            "board": "board2",
            "modules": [{"name": "shared_module", "classes": [], "functions": [], "constants": []}]
        }
        
        builder.add_board(board1_data)
        builder.add_board(board2_data)
        
        # Verify only one module was created
        cursor = builder.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM modules WHERE name = 'shared_module'")
        count = cursor.fetchone()[0]
        assert count == 1
        
        # Verify both boards are linked to it
        cursor.execute("""
            SELECT COUNT(DISTINCT b.id) FROM boards b
            JOIN board_modules bm ON b.id = bm.board_id
            JOIN modules m ON bm.module_id = m.id
            WHERE m.name = 'shared_module'
        """)
        board_count = cursor.fetchone()[0]
        assert board_count == 2
    
    def test_export_to_json(self, builder, temp_db):
        """Test exporting database to JSON."""
        # Add a board with data
        board_data = {
            "version": "v1.26.0",
            "port": "test",
            "board": "test_board",
            "modules": [
                {"name": "module1", "classes": [], "functions": [], "constants": []},
                {"name": "module2", "classes": [], "functions": [], "constants": []}
            ]
        }
        
        builder.add_board(board_data)
        
        # Export to JSON
        json_path = temp_db.with_suffix(".json")
        builder.export_to_json(json_path)
        
        # Verify JSON file was created
        assert json_path.exists()
        
        # Read and verify JSON content
        with open(json_path) as f:
            data = json.load(f)
        
        assert "version" in data
        assert "boards" in data
        assert len(data["boards"]) == 1
        assert data["boards"][0]["port"] == "test"
        assert len(data["boards"][0]["modules"]) == 2
        
        # Cleanup
        json_path.unlink()
    
    def test_export_detailed_to_json(self, builder, temp_db):
        """Test exporting detailed database to JSON."""
        # Add a board with complex data
        board_data = {
            "version": "v1.26.0",
            "port": "test",
            "board": "test_board",
            "modules": [
                {
                    "name": "test_module",
                    "classes": [
                        {
                            "name": "TestClass",
                            "methods": [
                                {
                                    "name": "test_method",
                                    "parameters": [{"name": "self"}],
                                    "return_type": "None"
                                }
                            ],
                            "base_classes": [],
                            "attributes": []
                        }
                    ],
                    "functions": [],
                    "constants": []
                }
            ]
        }
        
        builder.add_board(board_data)
        
        # Export detailed JSON
        json_path = temp_db.parent / (temp_db.stem + "_detailed.json")
        builder.export_detailed_to_json(json_path)
        
        # Verify JSON file was created
        assert json_path.exists()
        
        # Read and verify JSON content
        with open(json_path) as f:
            data = json.load(f)
        
        assert "boards" in data
        board = data["boards"][0]
        assert "modules" in board
        assert len(board["modules"]) == 1
        assert "classes" in board["modules"][0]
        assert len(board["modules"][0]["classes"]) == 1
        assert "methods" in board["modules"][0]["classes"][0]
        
        # Cleanup
        json_path.unlink()
    
    def test_database_integrity(self, builder):
        """Test database foreign key integrity."""
        # This test verifies that foreign key constraints work
        # Note: SQLite needs foreign keys enabled explicitly
        cursor = builder.conn.cursor()
        
        # Enable foreign keys for this test
        cursor.execute("PRAGMA foreign_keys = ON")
        
        # Try to insert a board_module with non-existent board_id
        # This should fail due to foreign key constraint
        with pytest.raises(sqlite3.IntegrityError):
            cursor.execute("""
                INSERT INTO board_modules (board_id, module_id)
                VALUES (99999, 1)
            """)
            builder.conn.commit()
    
    def test_complex_board_data(self, builder):
        """Test adding a complex board with all features."""
        board_data = {
            "version": "v1.26.0",
            "port": "complex",
            "board": "complex_board",
            "modules": [
                {
                    "name": "complex_module",
                    "docstring": "A complex module for testing",
                    "classes": [
                        {
                            "name": "ComplexClass",
                            "docstring": "A complex class",
                            "base_classes": ["BaseClass"],
                            "methods": [
                                {
                                    "name": "__init__",
                                    "parameters": [{"name": "self"}],
                                    "return_type": "None"
                                },
                                {
                                    "name": "process",
                                    "parameters": [
                                        {"name": "self"},
                                        {"name": "data", "type_hint": "bytes"},
                                        {"name": "size", "type_hint": "int", "default_value": "1024", "is_optional": True}
                                    ],
                                    "return_type": "bool",
                                    "is_async": True
                                },
                                {
                                    "name": "value",
                                    "parameters": [{"name": "self"}],
                                    "return_type": "int",
                                    "is_property": True
                                }
                            ],
                            "attributes": ["VERSION", "MAX_SIZE"]
                        }
                    ],
                    "functions": [
                        {
                            "name": "helper_func",
                            "parameters": [{"name": "x", "type_hint": "int"}],
                            "return_type": "str"
                        }
                    ],
                    "constants": ["CONST1", "CONST2"]
                }
            ]
        }
        
        board_id = builder.add_board(board_data)
        assert board_id > 0
        
        # Verify all components were added
        cursor = builder.conn.cursor()
        
        # Check classes
        cursor.execute("SELECT COUNT(*) FROM classes WHERE name = 'ComplexClass'")
        assert cursor.fetchone()[0] == 1
        
        # Check methods
        cursor.execute("SELECT COUNT(*) FROM methods WHERE name IN ('__init__', 'process', 'value')")
        assert cursor.fetchone()[0] == 3
        
        # Check functions
        cursor.execute("SELECT COUNT(*) FROM methods WHERE name = 'helper_func' AND class_id IS NULL")
        assert cursor.fetchone()[0] == 1
        
        # Check parameters
        cursor.execute("""
            SELECT COUNT(*) FROM parameters p
            JOIN methods m ON p.method_id = m.id
            WHERE m.name = 'process'
        """)
        assert cursor.fetchone()[0] == 3  # self, data, size


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
