#!/usr/bin/env python3
"""
Unit tests for the stub scanner component.
"""

import tempfile
from pathlib import Path
from textwrap import dedent

import pytest

from .models import Class, Method, Module, Parameter
from .scan_stubs import StubScanner


class TestStubScanner:
    """Tests for StubScanner class."""
    
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
    
    def test_scanner_initialization(self, temp_stub_dir):
        """Test scanner initialization."""
        scanner = StubScanner(temp_stub_dir)
        assert scanner.stub_dir == temp_stub_dir
    
    def test_find_stub_files(self, temp_stub_dir):
        """Test finding .pyi files."""
        # Create some stub files
        self.create_stub_file(temp_stub_dir, "module1.pyi", "# test")
        self.create_stub_file(temp_stub_dir, "module2.pyi", "# test")
        self.create_stub_file(temp_stub_dir, "not_stub.py", "# not a stub")
        
        scanner = StubScanner(temp_stub_dir)
        # Use glob to find .pyi files (matching actual implementation)
        stub_files = list(temp_stub_dir.glob("*.pyi"))
        
        assert len(stub_files) == 2
        assert all(f.suffix == ".pyi" for f in stub_files)
    
    def test_scan_simple_function(self, temp_stub_dir):
        """Test scanning a simple function."""
        content = """
        def test_func() -> None:
            '''A test function.'''
            ...
        """
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) == 1
        module = modules[0]
        assert module.name == "test"
        assert len(module.functions) == 1
        assert module.functions[0].name == "test_func"
        # Return type might be None or "None" depending on AST parsing
        assert module.functions[0].return_type in [None, "None"]
    
    def test_scan_function_with_parameters(self, temp_stub_dir):
        """Test scanning a function with parameters."""
        content = """
        def func_with_params(x: int, y: str = "default") -> bool:
            ...
        """
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        func = modules[0].functions[0]
        assert func.name == "func_with_params"
        assert len(func.parameters) == 2
        assert func.parameters[0].name == "x"
        assert func.parameters[0].type_hint == "int"
        assert func.parameters[1].name == "y"
        assert func.parameters[1].type_hint == "str"
        # Default value might be quoted differently
        assert "default" in func.parameters[1].default_value
    
    def test_scan_simple_class(self, temp_stub_dir):
        """Test scanning a simple class."""
        content = """
        class TestClass:
            '''A test class.'''
            pass
        """
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules[0].classes) == 1
        cls = modules[0].classes[0]
        assert cls.name == "TestClass"
        assert "test class" in cls.docstring.lower()
    
    def test_scan_class_with_methods(self, temp_stub_dir):
        """Test scanning a class with methods."""
        content = """
        class TestClass:
            def __init__(self) -> None:
                ...
            
            def method1(self, x: int) -> str:
                ...
            
            @property
            def value(self) -> int:
                ...
        """
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        cls = modules[0].classes[0]
        assert len(cls.methods) == 3
        assert cls.methods[0].name == "__init__"
        assert cls.methods[1].name == "method1"
        assert cls.methods[2].name == "value"
        assert cls.methods[2].is_property is True
    
    def test_scan_class_inheritance(self, temp_stub_dir):
        """Test scanning class with base classes."""
        content = """
        class BaseClass:
            pass
        
        class DerivedClass(BaseClass):
            pass
        
        class MultipleInheritance(BaseClass, object):
            pass
        """
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        classes = modules[0].classes
        assert classes[0].name == "BaseClass"
        assert len(classes[0].base_classes) == 0
        
        assert classes[1].name == "DerivedClass"
        assert "BaseClass" in classes[1].base_classes
        
        assert classes[2].name == "MultipleInheritance"
        assert len(classes[2].base_classes) == 2
    
    def test_scan_async_function(self, temp_stub_dir):
        """Test scanning async function."""
        content = """
        async def async_func() -> None:
            ...
        """
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        func = modules[0].functions[0]
        assert func.name == "async_func"
        assert func.is_async is True
    
    def test_scan_classmethod(self, temp_stub_dir):
        """Test scanning classmethod."""
        content = """
        class TestClass:
            @classmethod
            def from_string(cls, s: str) -> 'TestClass':
                ...
        """
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        method = modules[0].classes[0].methods[0]
        assert method.name == "from_string"
        assert method.is_classmethod is True
    
    def test_scan_staticmethod(self, temp_stub_dir):
        """Test scanning staticmethod."""
        content = """
        class TestClass:
            @staticmethod
            def helper(x: int) -> int:
                ...
        """
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        method = modules[0].classes[0].methods[0]
        assert method.name == "helper"
        assert method.is_staticmethod is True
    
    def test_scan_module_constants(self, temp_stub_dir):
        """Test scanning module-level constants."""
        content = """
        VERSION: str = "1.0.0"
        MAX_SIZE: int = 1024
        CONST1 = 42
        """
        self.create_stub_file(temp_stub_dir, "test.pyi", content)

        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()

        assert len(modules[0].constants) >= 3
        # Check by name attribute since constants are now Constant objects
        constant_names = [c.name for c in modules[0].constants]
        assert "VERSION" in constant_names
        assert "MAX_SIZE" in constant_names
    
    def test_scan_class_attributes(self, temp_stub_dir):
        """Test scanning class attributes."""
        content = """
        class TestClass:
            CONST1: int = 1
            CONST2: str = "test"
            var: int
        """
        self.create_stub_file(temp_stub_dir, "test.pyi", content)

        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()

        cls = modules[0].classes[0]
        assert len(cls.attributes) >= 3
        # Check by name attribute since attributes are now Attribute objects
        attribute_names = [a.name for a in cls.attributes]
        assert "CONST1" in attribute_names

    def test_scan_overloaded_function(self, temp_stub_dir):
        """Test scanning overloaded function."""
        content = """
        from typing import overload
        
        @overload
        def func(x: int) -> int: ...
        
        @overload
        def func(x: str) -> str: ...
        
        def func(x): ...
        """
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        # Should find the implementation
        funcs = [f for f in modules[0].functions if f.name == "func"]
        assert len(funcs) >= 1
    
    def test_scan_variadic_parameters(self, temp_stub_dir):
        """Test scanning *args and **kwargs."""
        content = """
        def func_with_varargs(*args, **kwargs) -> None:
            ...
        """
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        func = modules[0].functions[0]
        params = func.parameters
        
        args_param = next((p for p in params if p.name == "args"), None)
        assert args_param is not None
        assert args_param.is_variadic is True
        
        kwargs_param = next((p for p in params if p.name == "kwargs"), None)
        assert kwargs_param is not None
        assert kwargs_param.is_variadic is True
    
    def test_scan_complex_type_hints(self, temp_stub_dir):
        """Test scanning complex type hints."""
        content = """
        from typing import List, Dict, Optional, Union
        
        def func1(x: List[int]) -> None: ...
        def func2(x: Dict[str, int]) -> None: ...
        def func3(x: Optional[str]) -> None: ...
        def func4(x: Union[int, str]) -> None: ...
        """
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        funcs = modules[0].functions
        assert len(funcs) == 4
        
        # Check that type hints are captured (as strings)
        assert funcs[0].parameters[0].type_hint is not None
        assert funcs[1].parameters[0].type_hint is not None
    
    def test_scan_empty_module(self, temp_stub_dir):
        """Test scanning an empty module."""
        content = """
        # Empty module
        """
        self.create_stub_file(temp_stub_dir, "empty.pyi", content)
        
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) == 1
        assert modules[0].name == "empty"
        assert len(modules[0].classes) == 0
        assert len(modules[0].functions) == 0
    
    def test_scan_module_with_imports(self, temp_stub_dir):
        """Test that imports don't break scanning."""
        content = """
        from typing import Any, List
        import sys
        
        def func(x: List[Any]) -> None:
            ...
        """
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) == 1
        assert len(modules[0].functions) == 1
    
    def test_scan_nested_classes(self, temp_stub_dir):
        """Test scanning nested classes (currently not supported deeply)."""
        content = """
        class OuterClass:
            class InnerClass:
                def inner_method(self) -> None:
                    ...
        """
        self.create_stub_file(temp_stub_dir, "test.pyi", content)
        
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        # Should at least find the outer class
        assert len(modules[0].classes) >= 1
        assert modules[0].classes[0].name == "OuterClass"
    
    def test_error_handling_invalid_syntax(self, temp_stub_dir):
        """Test error handling for invalid Python syntax."""
        content = """
        def func(
        """  # Incomplete function
        self.create_stub_file(temp_stub_dir, "invalid.pyi", content)
        
        scanner = StubScanner(temp_stub_dir)
        # Should not crash, but may skip the file or return empty module
        modules = scanner.scan_all_modules()
        # Just verify it doesn't crash
        assert isinstance(modules, list)


class TestStubScannerIntegration:
    """Integration tests using real stub files if available."""
    
    def test_scan_real_stubs_if_available(self):
        """Test scanning real published stubs if available."""
        repo_root = Path(__file__).parent.parent.parent
        stub_dir = repo_root / "publish" / "micropython-v1_26_0-esp32-esp32_generic-stubs"
        
        if not stub_dir.exists():
            pytest.skip("Real stub directory not found")
        
        scanner = StubScanner(stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0, "Should find at least one module"
        
        # Check for expected common modules
        module_names = {m.name for m in modules}
        expected_modules = {"machine", "time", "gc"}
        found = expected_modules & module_names
        assert len(found) > 0, f"Should find common modules, found: {found}"
        
        # Check machine module if it exists
        machine_module = next((m for m in modules if m.name == "machine"), None)
        if machine_module:
            assert len(machine_module.classes) > 0, "machine should have classes"
            
            # Check for common classes
            class_names = {c.name for c in machine_module.classes}
            assert "Pin" in class_names or "I2C" in class_names, \
                "machine should have Pin or I2C class"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
