"""
Final targeted tests to push scan_stubs.py to 85%+ coverage.

Focuses on remaining edge cases and complex scenarios.
"""

import tempfile
from pathlib import Path

import pytest

from .scan_stubs import StubScanner


class TestScanStubsFinalCoverage:
    """Final tests to reach 85%+ coverage for scan_stubs."""

    @pytest.fixture
    def temp_stub_dir(self):
        """Create a temporary directory with test stub files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)

    def create_stub_file(self, stub_dir: Path, name: str, content: str) -> Path:
        """Helper to create a stub file."""
        stub_path = stub_dir / name
        stub_path.parent.mkdir(parents=True, exist_ok=True)
        stub_path.write_text(content)
        return stub_path

    def test_class_method_with_class_keyword(self, temp_stub_dir):
        """Test that classmethod keyword is captured."""
        content = """
class MyClass:
    @classmethod
    def create(cls, name: str):
        ...
"""
        self.create_stub_file(temp_stub_dir, "classmethod.pyi", content)
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0
        cls = modules[0].classes[0]
        method = cls.methods[0]
        assert method.is_classmethod is True

    def test_static_method_keyword(self, temp_stub_dir):
        """Test that staticmethod keyword is captured."""
        content = """
class Math:
    @staticmethod
    def add(a: int, b: int) -> int:
        ...
"""
        self.create_stub_file(temp_stub_dir, "staticmethod.pyi", content)
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0
        cls = modules[0].classes[0]
        method = cls.methods[0]
        assert method.is_staticmethod is True

    def test_async_function_and_method(self, temp_stub_dir):
        """Test async functions and methods are properly identified."""
        content = """
async def async_func() -> None: ...

class AsyncClass:
    async def async_method(self) -> None: ...
"""
        self.create_stub_file(temp_stub_dir, "async.pyi", content)
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0
        module = modules[0]
        
        # Check async function
        assert len(module.functions) > 0
        async_func = module.functions[0]
        assert async_func.is_async is True
        
        # Check async method
        cls = module.classes[0]
        async_method = cls.methods[0]
        assert async_method.is_async is True

    def test_property_decorator_keyword(self, temp_stub_dir):
        """Test that property decorator is recognized."""
        content = """
class Config:
    @property
    def timeout(self) -> int: ...
"""
        self.create_stub_file(temp_stub_dir, "property.pyi", content)
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0
        cls = modules[0].classes[0]
        prop = cls.methods[0]
        assert prop.is_property is True

    def test_parameter_positions_and_order(self, temp_stub_dir):
        """Test that parameter positions are preserved."""
        content = """
def func(a: int, b: str, c: float = 1.0, *args, **kwargs) -> None: ...
"""
        self.create_stub_file(temp_stub_dir, "params.pyi", content)
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0
        func = modules[0].functions[0]
        params = func.parameters
        
        # Should have all parameters
        assert len(params) >= 5
        
        # Check order
        assert params[0].name == "a"
        assert params[1].name == "b"
        assert params[2].name == "c"

    def test_overload_decorator_recognition(self, temp_stub_dir):
        """Test that @overload decorator is recognized."""
        content = """
from typing import overload

@overload
def process(x: int) -> str: ...

@overload
def process(x: str) -> int: ...

def process(x):
    ...
"""
        self.create_stub_file(temp_stub_dir, "overload.pyi", content)
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0
        # Should capture overloaded functions
        assert len(modules[0].functions) >= 3

    def test_class_with_no_methods(self, temp_stub_dir):
        """Test class with only attributes (no methods)."""
        content = """
class DataClass:
    name: str
    age: int
    active: bool = True
"""
        self.create_stub_file(temp_stub_dir, "dataclass.pyi", content)
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0
        cls = modules[0].classes[0]
        assert len(cls.attributes) >= 3
        assert len(cls.methods) == 0

    def test_function_with_many_parameters(self, temp_stub_dir):
        """Test function with many parameters."""
        content = """
def complex_func(
    p1: int,
    p2: str,
    p3: float,
    p4: bool,
    p5: list,
    p6: dict,
    p7: tuple,
    p8: set
) -> None: ...
"""
        self.create_stub_file(temp_stub_dir, "many_params.pyi", content)
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0
        func = modules[0].functions[0]
        assert len(func.parameters) == 8

    def test_class_inheritance_chain(self, temp_stub_dir):
        """Test class with multiple base classes."""
        content = """
class Base1: ...
class Base2: ...
class Derived(Base1, Base2): ...
"""
        self.create_stub_file(temp_stub_dir, "inheritance.pyi", content)
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0
        # Should have all classes
        assert len(modules[0].classes) >= 3

    def test_module_constants_with_various_types(self, temp_stub_dir):
        """Test module constants with various value types."""
        content = """
INT_CONST: int = 42
STR_CONST: str = "hello"
FLOAT_CONST: float = 3.14
BOOL_CONST: bool = True
LIST_CONST: list = []
DICT_CONST: dict = {}
NONE_CONST: None = None
EXPR_CONST = 1 + 2
"""
        self.create_stub_file(temp_stub_dir, "constants.pyi", content)
        scanner = StubScanner(temp_stub_dir)
        modules = scanner.scan_all_modules()
        
        assert len(modules) > 0
        # Should extract all constants
        constants = modules[0].constants
        assert len(constants) >= 8
