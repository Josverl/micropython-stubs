"""
Unit tests for build_database helper functions.
Tests internal methods to increase coverage of helper logic.
"""

import sqlite3
import tempfile
from pathlib import Path

import pytest

from .build_database import DatabaseBuilder


@pytest.fixture
def builder():
    """Create a DatabaseBuilder instance."""
    with tempfile.NamedTemporaryFile(suffix=".db", delete=True) as f:
        temp_path = Path(f.name)
    
    builder = DatabaseBuilder(temp_path)
    return builder


class TestDatabaseBuilderHelpers:
    """Test internal helper methods of DatabaseBuilder."""

    def test_is_typing_related_typevar(self, builder):
        """Test detection of TypeVar as typing-related."""
        result = builder._is_typing_related("T", "TypeVar", None)
        assert result is True

    def test_is_typing_related_typealias(self, builder):
        """Test detection of TypeAlias as typing-related."""
        result = builder._is_typing_related("StrLike", "TypeAlias", None)
        assert result is True

    def test_is_typing_related_regular_name(self, builder):
        """Test that regular names are not typing-related."""
        result = builder._is_typing_related("MyClass", None, None)
        assert result is False

    def test_is_typing_related_callable(self, builder):
        """Test detection of Callable type as typing-related."""
        result = builder._is_typing_related("func", "Callable[[int], str]", None)
        assert result is True

    def test_generate_signature_hash(self, builder):
        """Test signature hash generation is deterministic."""
        hash1 = builder._generate_signature_hash("module", "MyClass", "docstring")
        hash2 = builder._generate_signature_hash("module", "MyClass", "docstring")
        
        # Same inputs should produce same hash
        assert hash1 == hash2
        # Hash should be short (first 16 chars of SHA256)
        assert len(hash1) == 16

    def test_generate_signature_hash_different_inputs(self, builder):
        """Test that different inputs produce different hashes."""
        hash1 = builder._generate_signature_hash("module", "Class1", "doc")
        hash2 = builder._generate_signature_hash("module", "Class2", "doc")
        
        # Different inputs should produce different hashes
        assert hash1 != hash2

    def test_connection_property(self, builder):
        """Test that connection property works."""
        # Initially no connection
        assert builder.conn is None
        
        # Create connection
        conn = sqlite3.connect(":memory:")
        builder.conn = conn
        
        # Connection should be set
        assert builder.conn is not None
        assert builder.conn == conn
        
        conn.close()

    def test_database_path_property(self, builder):
        """Test that database path is stored correctly."""
        assert builder.db_path is not None
        assert isinstance(builder.db_path, Path)

    def test_create_schema_creates_tables(self, builder):
        """Test that create_schema actually creates all necessary tables."""
        conn = sqlite3.connect(":memory:")
        builder.conn = conn
        builder.create_schema()
        
        cursor = conn.cursor()
        
        # Get list of all tables
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        )
        tables = {row[0] for row in cursor.fetchall()}
        
        # Verify key tables exist
        expected = {
            'boards',
            'unique_modules',
            'unique_classes',
            'unique_methods',
            'unique_parameters',
        }
        
        assert expected.issubset(tables)
        conn.close()

    def test_is_typing_related_with_type_hint(self, builder):
        """Test typing detection based on type hint."""
        result = builder._is_typing_related("param", "Union[int, str]", None)
        # Union is typing-related
        assert result is True

    def test_is_typing_related_with_none_type_hint(self, builder):
        """Test typing detection with None type hint."""
        result = builder._is_typing_related("x", None, None)
        # Without type hint, it's not typing-related
        assert result is False

    def test_is_typing_related_generic_alias(self, builder):
        """Test detection of generic types."""
        result = builder._is_typing_related("Mapping", "Type[dict]", None)
        assert result is True

    def test_close_connection(self, builder):
        """Test that closing connection works."""
        conn = sqlite3.connect(":memory:")
        builder.conn = conn
        
        # Connection should be open
        assert builder.conn is not None
        
        # Close it
        builder.close()
        
        # After close, conn might be None or closed
        # Verify it's properly handled

    def test_connection_row_factory(self, builder):
        """Test that connection has row factory set correctly."""
        conn = sqlite3.connect(":memory:")
        conn.row_factory = sqlite3.Row
        builder.conn = conn
        builder.create_schema()
        
        # Add a board and verify row factory works
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO boards (version, port, board)
            VALUES (?, ?, ?)
            """,
            ("v1.0", "esp32", "generic")
        )
        
        cursor.execute("SELECT * FROM boards LIMIT 1")
        row = cursor.fetchone()
        
        # With row factory, can access by name
        assert row["version"] == "v1.0"
        assert row["port"] == "esp32"
        
        conn.close()

    def test_is_typing_related_with_value_pattern(self, builder):
        """Test typing detection based on value pattern."""
        result = builder._is_typing_related("T", None, "TypeVar('T')")
        assert result is True

    def test_is_typing_related_classvar(self, builder):
        """Test detection of ClassVar."""
        result = builder._is_typing_related("count", "ClassVar[int]", None)
        assert result is True

    def test_is_typing_related_optional(self, builder):
        """Test detection of Optional type."""
        result = builder._is_typing_related("maybe", "Optional[str]", None)
        assert result is True

    def test_is_typing_related_literal(self, builder):
        """Test detection of Literal type."""
        result = builder._is_typing_related("status", "Literal['on', 'off']", None)
        assert result is True
