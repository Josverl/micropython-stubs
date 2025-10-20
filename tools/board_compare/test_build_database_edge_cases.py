"""
Additional integration tests for build_database module.
Focus on edge cases and specific data flows.
"""

import sqlite3
import tempfile
from pathlib import Path

import pytest

from .build_database import DatabaseBuilder


@pytest.fixture
def memory_db():
    """Create in-memory database for testing."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row

    with tempfile.NamedTemporaryFile(suffix=".db", delete=True) as f:
        temp_path = Path(f.name)

    builder = DatabaseBuilder(temp_path)
    builder.conn = conn
    builder.create_schema()

    yield builder

    conn.close()


class TestBuildDatabaseEdgeCases:
    """Test edge cases and specific data flows in build_database."""

    def test_board_with_many_decorators(self, memory_db):
        """Test method with many stacked decorators."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "decorators_lib",
                    "classes": [
                        {
                            "name": "Cache",
                            "methods": [
                                {
                                    "name": "memoize_expensive",
                                    "parameters": [{"name": "func"}],
                                    "return_type": "callable",
                                    "decorators": ["lru_cache", "timer", "logger"],
                                    "is_async": False,
                                    "is_classmethod": False,
                                    "is_staticmethod": False,
                                    "is_property": False,
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

        board_id = memory_db.add_board(board_data)
        assert board_id > 0

    def test_parameter_with_default_value_and_type_hint(self, memory_db):
        """Test parameters with both type hints and default values."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "defaults_lib",
                    "classes": [],
                    "functions": [
                        {
                            "name": "format_string",
                            "parameters": [
                                {
                                    "name": "value",
                                    "type_hint": "str | None",
                                    "default_value": "None",
                                    "is_optional": True,
                                },
                                {
                                    "name": "width",
                                    "type_hint": "int",
                                    "default_value": "10",
                                    "is_optional": True,
                                },
                            ],
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

        board_id = memory_db.add_board(board_data)
        assert board_id > 0

        cursor = memory_db.conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM unique_parameters WHERE name = 'width'")
        result = cursor.fetchone()
        assert result["count"] >= 1

    def test_constants_with_various_types(self, memory_db):
        """Test constants with different type hints."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "constants_lib",
                    "classes": [],
                    "functions": [],
                    "constants": [
                        {"name": "INT_CONSTANT", "value": "42", "type_hint": "int", "is_hidden": False},
                        {"name": "STR_CONSTANT", "value": "'hello'", "type_hint": "str", "is_hidden": False},
                        {"name": "BOOL_CONSTANT", "value": "True", "type_hint": "bool", "is_hidden": False},
                        {"name": "FLOAT_CONSTANT", "value": "3.14", "type_hint": "float", "is_hidden": False},
                    ],
                }
            ],
        }

        board_id = memory_db.add_board(board_data)
        assert board_id > 0

        cursor = memory_db.conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM unique_module_constants")
        result = cursor.fetchone()
        assert result["count"] >= 4

    def test_class_inheritance_chain(self, memory_db):
        """Test class with multiple base classes."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "inheritance_lib",
                    "classes": [{"name": "MyClass", "base_classes": ["Base", "Mixin", "object"], "methods": [], "constants": []}],
                    "functions": [],
                    "constants": [],
                }
            ],
        }

        board_id = memory_db.add_board(board_data)
        assert board_id > 0

    def test_mixed_async_and_sync_methods(self, memory_db):
        """Test class with both async and sync methods."""
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
                                    "name": "connect",
                                    "parameters": [{"name": "self"}],
                                    "return_type": None,
                                    "is_async": True,
                                    "is_classmethod": False,
                                    "is_staticmethod": False,
                                    "is_property": False,
                                    "decorators": None,
                                },
                                {
                                    "name": "get_status",
                                    "parameters": [{"name": "self"}],
                                    "return_type": "str",
                                    "is_async": False,
                                    "is_classmethod": False,
                                    "is_staticmethod": False,
                                    "is_property": False,
                                    "decorators": None,
                                },
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

        board_id = memory_db.add_board(board_data)
        assert board_id > 0

        cursor = memory_db.conn.cursor()
        cursor.execute("SELECT is_async FROM unique_methods WHERE name = 'connect'")
        result = cursor.fetchone()
        assert result is not None
        assert result["is_async"] == 1

        cursor.execute("SELECT is_async FROM unique_methods WHERE name = 'get_status'")
        result = cursor.fetchone()
        assert result is not None
        assert result["is_async"] == 0

    def test_hidden_typing_constants(self, memory_db):
        """Test that typing constants are marked as hidden."""
        board_data = {
            "version": "v1.26.0",
            "port": "esp32",
            "board": "generic",
            "modules": [
                {
                    "name": "typing_constants",
                    "classes": [],
                    "functions": [],
                    "constants": [{"name": "T", "value": "TypeVar('T')", "type_hint": None, "is_hidden": True}],
                }
            ],
        }

        board_id = memory_db.add_board(board_data)
        assert board_id > 0
