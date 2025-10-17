#!/usr/bin/env python3
"""Test suite to verify decorator parsing works correctly."""

from pathlib import Path

import pytest

from .scan_stubs import StubScanner


class TestDecoratorParsing:
    """Tests for decorator parsing in stub files."""

    @pytest.fixture
    def stdlib_stub_dir(self):
        """Get the stdlib stub directory."""
        stub_dir = Path(__file__).parent.parent.parent / "publish" / "micropython-stdlib-stubs" / "stdlib"
        if stub_dir.exists():
            return stub_dir
        pytest.skip(f"Stdlib stub directory not found at {stub_dir}")

    def test_array_module_has_decorators(self, stdlib_stub_dir):
        """Test that array module classes and methods are parsed with decorators."""
        scanner = StubScanner(stdlib_stub_dir)
        modules = scanner.scan_all_modules()
        
        # Find the array module
        array_module = next((m for m in modules if m.name == "array"), None)
        assert array_module is not None, "array module should be found"
        
        # Should have classes (array class contains all methods)
        assert len(array_module.classes) > 0, "array module should have classes"

    def test_overload_decorator_captured(self, stdlib_stub_dir):
        """Test that @overload decorators are captured in class methods."""
        scanner = StubScanner(stdlib_stub_dir)
        modules = scanner.scan_all_modules()
        
        # Find the array module
        array_module = next((m for m in modules if m.name == "array"), None)
        assert array_module is not None, "array module should be found"
        
        # Find a class with methods
        array_class = next((c for c in array_module.classes if c.name == "array"), None)
        assert array_class is not None, "array class should be found"
        
        # Check if we found overload decorators in methods
        overload_count = sum(1 for method in array_class.methods if method.decorators and "overload" in method.decorators)
        
        assert overload_count > 0, "array class should have methods with @overload decorator"

    def test_decorator_attribute_exists(self, stdlib_stub_dir):
        """Test that Method objects have decorators attribute."""
        scanner = StubScanner(stdlib_stub_dir)
        modules = scanner.scan_all_modules()
        
        # Find a module with functions
        for module in modules:
            if module.functions:
                func = module.functions[0]
                assert hasattr(func, "decorators"), "Method should have decorators attribute"
                # decorators should be a list or None
                assert func.decorators is None or isinstance(func.decorators, list), \
                    "decorators should be a list or None"
                break
        else:
            pytest.skip("No modules with functions found")
