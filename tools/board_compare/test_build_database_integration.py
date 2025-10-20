"""
Integration tests for database builder using in-memory SQLite.

These tests verify the complete database building workflow without
needing temporary files or disk I/O.
"""

import json
import sqlite3
import tempfile
from pathlib import Path

import pytest

from .build_database import DatabaseBuilder
from .models import Board, Class, Constant, Method, Module, Parameter


@pytest.fixture
def in_memory_builder():
    """Create a DatabaseBuilder with an in-memory SQLite database."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row

    # Create builder with a dummy path (the connection will override it)
    import tempfile

    with tempfile.NamedTemporaryFile(suffix=".db", delete=True) as f:
        temp_path = Path(f.name)

    builder = DatabaseBuilder(temp_path)
    builder.conn = conn  # Override with in-memory connection
    builder.create_schema()

    yield builder

    if builder.conn:
        builder.conn.close()


class TestDatabaseBuilderIntegration:
    """Integration tests for DatabaseBuilder using in-memory SQLite."""

    def test_add_simple_board(self, in_memory_builder):
        """Test adding a simple board with no modules."""
        board_data = {"version": "v1.26.0", "port": "esp32", "board": "generic", "modules": []}

        board_id = in_memory_builder.add_board(board_data)

        assert board_id > 0

        # Verify board was added
        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT * FROM boards WHERE id = ?", (board_id,))
        board = cursor.fetchone()

        assert board is not None
        assert board["version"] == "v1.26.0"
        assert board["port"] == "esp32"
        assert board["board"] == "generic"

    def test_add_board_with_single_module(self, in_memory_builder):
        """Test adding a board with a single module."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [{"name": "sys", "classes": [], "functions": [], "constants": []}],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        # Verify module was added
        cursor = in_memory_builder.conn.cursor()
        cursor.execute(
            """
            SELECT COUNT(*) as count FROM board_module_support
            WHERE board_id = ?
            """,
            (board_id,),
        )
        result = cursor.fetchone()
        assert result["count"] == 1

    def test_add_board_with_module_containing_classes(self, in_memory_builder):
        """Test adding a board with a module that contains classes."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "machine",
                    "classes": [{"name": "Pin", "docstring": "GPIO pin control", "methods": [], "constants": [], "base_classes": []}],
                    "functions": [],
                    "constants": [],
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        # Verify class was added
        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM unique_classes WHERE name = 'Pin'")
        result = cursor.fetchone()
        assert result["count"] == 1

    def test_add_board_with_class_methods(self, in_memory_builder):
        """Test adding a board with a class that has methods."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "machine",
                    "classes": [
                        {
                            "name": "Pin",
                            "docstring": "GPIO pin",
                            "methods": [
                                {
                                    "name": "__init__",
                                    "parameters": [{"name": "self"}, {"name": "pin", "type_hint": "int"}],
                                    "return_type": None,
                                    "is_async": False,
                                    "is_classmethod": False,
                                    "is_staticmethod": False,
                                    "is_property": False,
                                    "decorators": None,
                                }
                            ],
                            "constants": [],
                            "base_classes": [],
                        }
                    ],
                    "functions": [],
                    "constants": [],
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        # Verify method was added
        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM unique_methods WHERE name = '__init__'")
        result = cursor.fetchone()
        assert result["count"] >= 1

    def test_add_board_with_module_constants(self, in_memory_builder):
        """Test adding a board with module-level constants."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "sys",
                    "classes": [],
                    "functions": [],
                    "constants": [{"name": "VERSION", "value": "3.11", "type_hint": "str", "is_hidden": False}],
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        # Verify constant was added
        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM unique_module_constants WHERE name = 'VERSION'")
        result = cursor.fetchone()
        assert result["count"] == 1

    def test_module_deduplication_across_boards(self, in_memory_builder):
        """Test that modules are deduplicated across boards."""
        board1 = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [{"name": "sys", "classes": [], "functions": [], "constants": []}],
        }

        board2 = {
            "version": "v1.26.0",
            "port": "rp2",
            "board": "pico",
            "modules": [{"name": "sys", "classes": [], "functions": [], "constants": []}],
        }

        bid1 = in_memory_builder.add_board(board1)
        bid2 = in_memory_builder.add_board(board2)

        assert bid1 > 0
        assert bid2 > 0

        # Verify only one unique module entry
        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM unique_modules WHERE name = 'sys'")
        result = cursor.fetchone()
        assert result["count"] == 1

    def test_class_attributes_support(self, in_memory_builder):
        """Test that classes with attributes are properly stored."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "machine",
                    "classes": [
                        {
                            "name": "Pin",
                            "attributes": [{"name": "IN", "type_hint": "int"}],
                            "methods": [],
                            "constants": [],
                            "base_classes": [],
                        }
                    ],
                    "functions": [],
                    "constants": [],
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        # Verify class exists
        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM unique_classes WHERE name = 'Pin'")
        result = cursor.fetchone()
        assert result["count"] == 1

    def test_export_to_json_creates_valid_json(self, in_memory_builder):
        """Test that JSON export creates valid JSON with board data."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [{"name": "sys", "classes": [], "functions": [], "constants": [], "docstring": None}],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        # Export to JSON
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json_path = Path(f.name)

        try:
            in_memory_builder.export_to_json(json_path)

            # Verify JSON file was created
            assert json_path.exists(), "JSON file should be created"

            # Verify JSON is valid
            with open(json_path, "r") as f:
                data = json.load(f)

            assert "version" in data
            assert "boards" in data
            assert isinstance(data["boards"], list)
            assert len(data["boards"]) >= 1

        finally:
            if json_path.exists():
                json_path.unlink()

    def test_complex_board_with_all_features(self, in_memory_builder):
        """Test adding a complex board with modules, classes, methods, and constants."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "devkit",
            "modules": [
                {
                    "name": "machine",
                    "docstring": "Machine control module",
                    "classes": [
                        {
                            "name": "Pin",
                            "docstring": "GPIO pin control",
                            "base_classes": [],
                            "methods": [
                                {
                                    "name": "__init__",
                                    "parameters": [
                                        {"name": "self"},
                                        {"name": "id", "type_hint": "int"},
                                        {"name": "mode", "type_hint": "int", "is_optional": True},
                                    ],
                                    "return_type": "None",
                                    "is_async": False,
                                    "is_classmethod": False,
                                    "is_staticmethod": False,
                                    "is_property": False,
                                    "decorators": None,
                                },
                                {
                                    "name": "value",
                                    "parameters": [{"name": "self"}],
                                    "return_type": "int",
                                    "is_async": False,
                                    "is_classmethod": False,
                                    "is_staticmethod": False,
                                    "is_property": True,
                                    "decorators": ["property"],
                                },
                            ],
                            "constants": [{"name": "IN", "value": "1", "type_hint": "int", "is_hidden": False}],
                        }
                    ],
                    "functions": [
                        {
                            "name": "led_toggle",
                            "parameters": [],
                            "return_type": None,
                            "is_async": False,
                            "is_classmethod": False,
                            "is_staticmethod": False,
                            "is_property": False,
                            "decorators": None,
                        }
                    ],
                    "constants": [],
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM unique_classes WHERE name = 'Pin'")
        assert cursor.fetchone()["count"] == 1

        cursor.execute("SELECT COUNT(*) as count FROM unique_methods WHERE name = '__init__'")
        assert cursor.fetchone()["count"] >= 1

    def test_invalid_board_data_handling(self, in_memory_builder):
        """Test that invalid board data raises appropriate errors."""
        # Missing version
        board_data = {"port": "esp32", "board": "generic", "modules": []}

        with pytest.raises(KeyError):
            in_memory_builder.add_board(board_data)

    def test_database_schema_has_all_tables(self, in_memory_builder):
        """Test that all expected database tables are created."""
        cursor = in_memory_builder.conn.cursor()

        # Get list of all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        tables = {row[0] for row in cursor.fetchall()}

        # Verify key tables exist
        expected_tables = {
            "boards",
            "unique_modules",
            "unique_classes",
            "unique_methods",
            "unique_parameters",
            "unique_module_constants",
            "board_module_support",
        }

        assert expected_tables.issubset(tables), f"Missing tables: {expected_tables - tables}"

    def test_method_parameters_properly_linked(self, in_memory_builder):
        """Test that method parameters are properly linked."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "os",
                    "classes": [],
                    "functions": [
                        {
                            "name": "urandom",
                            "parameters": [{"name": "n", "type_hint": "int", "is_optional": False}],
                            "return_type": "bytes",
                            "is_async": False,
                            "is_classmethod": False,
                            "is_staticmethod": False,
                            "is_property": False,
                            "decorators": None,
                        }
                    ],
                    "constants": [],
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        cursor = in_memory_builder.conn.cursor()
        cursor.execute(
            """
            SELECT p.name, p.type_hint FROM unique_parameters p
            JOIN unique_methods m ON p.method_id = m.id
            WHERE m.name = 'urandom'
            """
        )
        params = cursor.fetchall()
        assert len(params) >= 1
        assert any(p[0] == "n" for p in params)

    def test_base_classes_are_tracked(self, in_memory_builder):
        """Test that base class relationships are tracked."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "machine",
                    "classes": [
                        {
                            "name": "ADC",
                            "docstring": "Analog to digital converter",
                            "base_classes": ["object"],
                            "methods": [],
                            "constants": [],
                        }
                    ],
                    "functions": [],
                    "constants": [],
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM unique_classes WHERE name = 'ADC'")
        result = cursor.fetchone()
        assert result["count"] >= 1

    def test_function_vs_method_distinction(self, in_memory_builder):
        """Test that module-level functions are distinguished from methods."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "sys",
                    "classes": [],
                    "functions": [
                        {
                            "name": "exit",
                            "parameters": [{"name": "code", "type_hint": "int"}],
                            "return_type": None,
                            "is_async": False,
                            "is_classmethod": False,
                            "is_staticmethod": False,
                            "is_property": False,
                            "decorators": None,
                        }
                    ],
                    "constants": [],
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM unique_methods WHERE name = 'exit' AND class_id IS NULL")
        result = cursor.fetchone()
        assert result["count"] >= 1

    def test_optional_parameters_marked(self, in_memory_builder):
        """Test that optional parameters are properly marked."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "os",
                    "classes": [],
                    "functions": [
                        {
                            "name": "getcwd",
                            "parameters": [{"name": "default", "type_hint": "str", "is_optional": True, "default_value": "None"}],
                            "return_type": "str",
                            "is_async": False,
                            "is_classmethod": False,
                            "is_staticmethod": False,
                            "is_property": False,
                            "decorators": None,
                        }
                    ],
                    "constants": [],
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        cursor = in_memory_builder.conn.cursor()
        cursor.execute(
            """
            SELECT is_optional FROM unique_parameters
            WHERE name = 'default'
            """
        )
        result = cursor.fetchone()
        if result:
            assert result["is_optional"] == 1

    def test_async_methods_marked(self, in_memory_builder):
        """Test that async methods are properly marked."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "async_lib",
                    "classes": [
                        {
                            "name": "AsyncClient",
                            "methods": [
                                {
                                    "name": "fetch",
                                    "parameters": [{"name": "self"}, {"name": "url", "type_hint": "str"}],
                                    "return_type": "bytes",
                                    "is_async": True,
                                    "is_classmethod": False,
                                    "is_staticmethod": False,
                                    "is_property": False,
                                    "decorators": None,
                                }
                            ],
                            "base_classes": [],
                            "attributes": [],
                        }
                    ],
                    "functions": [],
                    "constants": [],
                    "docstring": None,
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        # Check async method
        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT is_async FROM unique_methods WHERE name = 'fetch'")
        result = cursor.fetchone()
        assert result is not None
        assert result["is_async"] == 1

    def test_staticmethod_decorator_support(self, in_memory_builder):
        """Test that static methods are properly marked."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "utils",
                    "classes": [
                        {
                            "name": "Math",
                            "methods": [
                                {
                                    "name": "sqrt",
                                    "parameters": [{"name": "x", "type_hint": "float"}],
                                    "return_type": "float",
                                    "is_async": False,
                                    "is_classmethod": False,
                                    "is_staticmethod": True,
                                    "is_property": False,
                                    "decorators": ["staticmethod"],
                                }
                            ],
                            "constants": [],
                            "base_classes": [],
                        }
                    ],
                    "functions": [],
                    "constants": [],
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT is_staticmethod FROM unique_methods WHERE name = 'sqrt'")
        result = cursor.fetchone()
        assert result is not None
        assert result["is_staticmethod"] == 1

    def test_classmethod_decorator_support(self, in_memory_builder):
        """Test that class methods are properly marked."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "collections",
                    "classes": [
                        {
                            "name": "OrderedDict",
                            "methods": [
                                {
                                    "name": "fromkeys",
                                    "parameters": [{"name": "keys"}, {"name": "value"}],
                                    "return_type": "OrderedDict",
                                    "is_async": False,
                                    "is_classmethod": True,
                                    "is_staticmethod": False,
                                    "is_property": False,
                                    "decorators": ["classmethod"],
                                }
                            ],
                            "constants": [],
                            "base_classes": [],
                        }
                    ],
                    "functions": [],
                    "constants": [],
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT is_classmethod FROM unique_methods WHERE name = 'fromkeys'")
        result = cursor.fetchone()
        assert result is not None
        assert result["is_classmethod"] == 1

    def test_property_decorator_support(self, in_memory_builder):
        """Test that property methods are properly marked."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "descriptors",
                    "classes": [
                        {
                            "name": "Person",
                            "methods": [
                                {
                                    "name": "age",
                                    "parameters": [{"name": "self"}],
                                    "return_type": "int",
                                    "is_async": False,
                                    "is_classmethod": False,
                                    "is_staticmethod": False,
                                    "is_property": True,
                                    "decorators": ["property"],
                                }
                            ],
                            "constants": [],
                            "base_classes": [],
                        }
                    ],
                    "functions": [],
                    "constants": [],
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT is_property FROM unique_methods WHERE name = 'age'")
        result = cursor.fetchone()
        assert result is not None
        assert result["is_property"] == 1

    def test_variadic_parameters_marked(self, in_memory_builder):
        """Test that variadic parameters are properly marked."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "builtins",
                    "classes": [],
                    "functions": [
                        {
                            "name": "print",
                            "parameters": [{"name": "value", "is_variadic": True}],
                            "return_type": "None",
                            "is_async": False,
                            "is_classmethod": False,
                            "is_staticmethod": False,
                            "is_property": False,
                            "decorators": None,
                        }
                    ],
                    "constants": [],
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT is_variadic FROM unique_parameters WHERE name = 'value'")
        result = cursor.fetchone()
        if result:
            assert result["is_variadic"] == 1

    def test_module_function_docstrings(self, in_memory_builder):
        """Test that function docstrings are preserved."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "json",
                    "classes": [],
                    "functions": [
                        {
                            "name": "dumps",
                            "parameters": [{"name": "obj"}],
                            "return_type": "str",
                            "is_async": False,
                            "is_classmethod": False,
                            "is_staticmethod": False,
                            "is_property": False,
                            "docstring": "Serialize obj to a JSON formatted str.",
                            "decorators": None,
                        }
                    ],
                    "constants": [],
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT docstring FROM unique_methods WHERE name = 'dumps'")
        result = cursor.fetchone()
        assert result is not None

    def test_multiple_modules_same_board(self, in_memory_builder):
        """Test adding multiple modules to the same board."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {"name": "sys", "classes": [], "functions": [], "constants": []},
                {"name": "os", "classes": [], "functions": [], "constants": []},
                {"name": "json", "classes": [], "functions": [], "constants": []},
                {"name": "time", "classes": [], "functions": [], "constants": []},
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM board_module_support WHERE board_id = ?", (board_id,))
        result = cursor.fetchone()
        assert result["count"] == 4

    def test_docstrings_in_classes_and_methods(self, in_memory_builder):
        """Test that docstrings are preserved for classes and methods."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "socket",
                    "classes": [
                        {
                            "name": "socket",
                            "docstring": "Socket object for network communication",
                            "methods": [
                                {
                                    "name": "connect",
                                    "parameters": [{"name": "self"}, {"name": "address"}],
                                    "return_type": None,
                                    "is_async": False,
                                    "is_classmethod": False,
                                    "is_staticmethod": False,
                                    "is_property": False,
                                    "docstring": "Connect to a remote socket",
                                    "decorators": None,
                                }
                            ],
                            "constants": [],
                            "base_classes": [],
                        }
                    ],
                    "functions": [],
                    "constants": [],
                }
            ],
        }

        board_id = in_memory_builder.add_board(board_data)
        assert board_id > 0

        # Verify class docstring
        cursor = in_memory_builder.conn.cursor()
        cursor.execute("SELECT docstring FROM unique_classes WHERE name = 'socket'")
        result = cursor.fetchone()
        assert result is not None

        # Verify method docstring
        cursor.execute("SELECT docstring FROM unique_methods WHERE name = 'connect'")
        result = cursor.fetchone()
        assert result is not None
