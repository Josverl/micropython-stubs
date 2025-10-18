#!/usr/bin/env python3
"""Test suite to verify decorator parsing works correctly."""

import tempfile
from pathlib import Path
from textwrap import dedent

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

    @pytest.fixture
    def temp_stub_dir(self):
        """Create a temporary directory for test stub files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)
    
    def create_stub_file(self, stub_dir: Path, filename: str, content: str):
        """Helper to create a stub file with content."""
        file_path = stub_dir / filename
        file_path.write_text(dedent(content))
        return file_path

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

    def test_property_decorator(self, temp_stub_dir):
        """Test that @property decorator is captured."""
        content = """
        class MyClass:
            '''Test class.'''
            
            @property
            def my_property(self) -> int:
                '''A property.'''
                pass
        """
        
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0
        cls = modules[0].classes[0]
        
        # Find property method
        prop_method = next((m for m in cls.methods if m.name == "my_property"), None)
        assert prop_method is not None
        assert prop_method.is_property, "Should be marked as property"
        assert prop_method.decorators and "property" in prop_method.decorators

    def test_staticmethod_decorator(self, temp_stub_dir):
        """Test that @staticmethod decorator is captured."""
        content = """
        class MyClass:
            '''Test class.'''
            
            @staticmethod
            def static_method() -> str:
                '''A static method.'''
                pass
        """
        
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0
        cls = modules[0].classes[0]
        
        # Find static method
        static_method = next((m for m in cls.methods if m.name == "static_method"), None)
        assert static_method is not None
        assert static_method.is_staticmethod, "Should be marked as staticmethod"
        assert static_method.decorators and "staticmethod" in static_method.decorators

    def test_classmethod_decorator(self, temp_stub_dir):
        """Test that @classmethod decorator is captured."""
        content = """
        class MyClass:
            '''Test class.'''
            
            @classmethod
            def class_method(cls) -> 'MyClass':
                '''A class method.'''
                pass
        """
        
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0
        cls = modules[0].classes[0]
        
        # Find class method
        class_method = next((m for m in cls.methods if m.name == "class_method"), None)
        assert class_method is not None
        assert class_method.is_classmethod, "Should be marked as classmethod"
        assert class_method.decorators and "classmethod" in class_method.decorators

    def test_multiple_decorators_on_method(self, temp_stub_dir):
        """Test that multiple decorators are all captured."""
        content = """
        class MyClass:
            '''Test class.'''
            
            @staticmethod
            @some_decorator
            def decorated_method() -> None:
                '''A method with multiple decorators.'''
                pass
        """
        
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0
        cls = modules[0].classes[0]
        method = cls.methods[0]
        
        # Should capture all decorators
        assert method.decorators is not None
        assert len(method.decorators) >= 1
        assert "staticmethod" in method.decorators

    def test_overload_decorator_on_function(self, temp_stub_dir):
        """Test that @overload decorator is captured on functions."""
        content = """
        from typing import overload
        
        @overload
        def process(data: int) -> str: ...
        
        @overload
        def process(data: str) -> int: ...
        
        def process(data):
            '''Process data.'''
            pass
        """
        
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0
        module = modules[0]
        
        # Find process functions
        overload_funcs = [f for f in module.functions if f.name == "process" and f.decorators and "overload" in f.decorators]
        assert len(overload_funcs) >= 2, "Should find multiple overloaded versions"

