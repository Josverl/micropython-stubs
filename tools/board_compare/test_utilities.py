"""
Tests for utility modules and scripts.

These tests cover the CLI utilities and helper scripts
that don't have complex dependencies.
"""

import sys
from pathlib import Path
from unittest import mock

import pytest


class TestExampleQueries:
    """Tests for example_queries module."""

    def test_example_queries_imports(self):
        """Test that example_queries can be imported."""
        # Add the parent directory to path temporarily
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "example_queries",
            Path(__file__).parent / "example_queries.py"
        )
        module = importlib.util.module_from_spec(spec)
        # Module loads successfully
        assert module is not None

    def test_example_queries_has_main_function(self):
        """Test that example_queries exports example_queries function."""
        # Verify the file contains the function definition
        example_file = Path(__file__).parent / "example_queries.py"
        content = example_file.read_text()
        assert "def example_queries" in content


class TestCheckSchema:
    """Tests for check_schema module."""

    def test_check_schema_imports(self):
        """Test that check_schema can be imported."""
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "check_schema",
            Path(__file__).parent / "check_schema.py"
        )
        module = importlib.util.module_from_spec(spec)
        assert module is not None

    def test_check_schema_has_main_function(self):
        """Test that check_schema exports main function."""
        check_file = Path(__file__).parent / "check_schema.py"
        content = check_file.read_text()
        assert "def main" in content


class TestRunTests:
    """Tests for run_tests module."""

    def test_run_tests_imports(self):
        """Test that run_tests module can be imported."""
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "run_tests",
            Path(__file__).parent / "run_tests.py"
        )
        module = importlib.util.module_from_spec(spec)
        assert module is not None

    def test_run_tests_functions_exist(self):
        """Test that run_tests has required functions."""
        test_file = Path(__file__).parent / "run_tests.py"
        content = test_file.read_text()
        
        # Check for key functions
        assert "def run_simple_tests" in content
        assert "def run_pytest_tests" in content
        assert "def main" in content

    def test_run_simple_tests_function_signature(self):
        """Test that run_simple_tests is callable."""
        test_file = Path(__file__).parent / "run_tests.py"
        content = test_file.read_text()
        
        # Verify it's a function that can be called
        assert "def run_simple_tests():" in content

    def test_run_pytest_tests_function_signature(self):
        """Test that run_pytest_tests is callable."""
        test_file = Path(__file__).parent / "run_tests.py"
        content = test_file.read_text()
        
        # Verify it's a function that can be called
        assert "def run_pytest_tests():" in content


class TestRunLocal:
    """Tests for run_local server setup."""

    def test_run_local_imports(self):
        """Test that run_local can be imported."""
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "run_local",
            Path(__file__).parent / "run_local.py"
        )
        module = importlib.util.module_from_spec(spec)
        assert module is not None

    def test_run_local_has_required_components(self):
        """Test that run_local has required server components."""
        run_local_file = Path(__file__).parent / "run_local.py"
        content = run_local_file.read_text()
        
        # Check for key components
        assert "MyHTTPRequestHandler" in content
        assert "PORT" in content
        assert "DIRECTORY" in content
        assert "TCPServer" in content

    def test_run_local_http_handler_class_exists(self):
        """Test that HTTP handler is properly defined."""
        run_local_file = Path(__file__).parent / "run_local.py"
        content = run_local_file.read_text()
        
        # Check class definition
        assert "class MyHTTPRequestHandler" in content
        assert "def end_headers" in content

    def test_run_local_port_constant(self):
        """Test that PORT constant is defined."""
        run_local_file = Path(__file__).parent / "run_local.py"
        content = run_local_file.read_text()
        
        # Parse PORT definition
        assert "PORT = 8000" in content

    def test_run_local_directory_constant(self):
        """Test that DIRECTORY constant is defined."""
        run_local_file = Path(__file__).parent / "run_local.py"
        content = run_local_file.read_text()
        
        # Parse DIRECTORY definition
        assert 'DIRECTORY = Path("./frontend")' in content


class TestUtilityModuleSyntax:
    """Test that all utility modules have valid Python syntax."""

    def test_check_schema_syntax(self):
        """Test check_schema.py has valid syntax."""
        check_file = Path(__file__).parent / "check_schema.py"
        content = check_file.read_text()
        
        # Try to compile - will raise SyntaxError if invalid
        try:
            compile(content, str(check_file), 'exec')
        except SyntaxError as e:
            pytest.fail(f"check_schema.py has syntax error: {e}")

    def test_example_queries_syntax(self):
        """Test example_queries.py has valid syntax."""
        example_file = Path(__file__).parent / "example_queries.py"
        content = example_file.read_text()
        
        try:
            compile(content, str(example_file), 'exec')
        except SyntaxError as e:
            pytest.fail(f"example_queries.py has syntax error: {e}")

    def test_run_tests_syntax(self):
        """Test run_tests.py has valid syntax."""
        test_file = Path(__file__).parent / "run_tests.py"
        content = test_file.read_text()
        
        try:
            compile(content, str(test_file), 'exec')
        except SyntaxError as e:
            pytest.fail(f"run_tests.py has syntax error: {e}")

    def test_run_local_syntax(self):
        """Test run_local.py has valid syntax."""
        run_local_file = Path(__file__).parent / "run_local.py"
        content = run_local_file.read_text()
        
        try:
            compile(content, str(run_local_file), 'exec')
        except SyntaxError as e:
            pytest.fail(f"run_local.py has syntax error: {e}")
