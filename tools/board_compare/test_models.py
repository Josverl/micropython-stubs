#!/usr/bin/env python3
"""
Unit tests for Pydantic models in the board comparison tool.
"""

from typing import List

import pytest

from .models import Board, Class, Method, Module, Parameter


class TestParameter:
    """Tests for Parameter model."""
    
    def test_create_simple_parameter(self):
        """Test creating a simple parameter."""
        param = Parameter(name="x")
        assert param.name == "x"
        assert param.type_hint is None
        assert param.default_value is None
        assert param.is_optional is False
        assert param.is_variadic is False
    
    def test_create_parameter_with_type(self):
        """Test creating a parameter with type hint."""
        param = Parameter(name="x", type_hint="int")
        assert param.name == "x"
        assert param.type_hint == "int"
    
    def test_create_optional_parameter(self):
        """Test creating an optional parameter."""
        param = Parameter(name="x", default_value="0", is_optional=True)
        assert param.is_optional is True
        assert param.default_value == "0"
    
    def test_create_variadic_parameter(self):
        """Test creating a variadic parameter (*args, **kwargs)."""
        args_param = Parameter(name="args", is_variadic=True)
        assert args_param.is_variadic is True
        
        kwargs_param = Parameter(name="kwargs", is_variadic=True)
        assert kwargs_param.is_variadic is True
    
    def test_parameter_serialization(self):
        """Test parameter serialization to dict."""
        param = Parameter(name="x", type_hint="int", default_value="0", is_optional=True)
        data = param.model_dump()
        
        assert data["name"] == "x"
        assert data["type_hint"] == "int"
        assert data["default_value"] == "0"
        assert data["is_optional"] is True


class TestMethod:
    """Tests for Method model."""
    
    def test_create_simple_method(self):
        """Test creating a simple method."""
        method = Method(name="test_func")
        assert method.name == "test_func"
        assert len(method.parameters) == 0
        assert method.return_type is None
        assert method.is_async is False
    
    def test_create_method_with_parameters(self):
        """Test creating a method with parameters."""
        params = [
            Parameter(name="self"),
            Parameter(name="x", type_hint="int"),
            Parameter(name="y", type_hint="str", default_value="''", is_optional=True)
        ]
        method = Method(name="test_method", parameters=params, return_type="bool")
        
        assert method.name == "test_method"
        assert len(method.parameters) == 3
        assert method.return_type == "bool"
        assert method.parameters[0].name == "self"
        assert method.parameters[1].name == "x"
        assert method.parameters[2].is_optional is True
    
    def test_create_async_method(self):
        """Test creating an async method."""
        method = Method(name="async_func", is_async=True)
        assert method.is_async is True
    
    def test_create_property(self):
        """Test creating a property."""
        method = Method(name="value", is_property=True)
        assert method.is_property is True
    
    def test_create_classmethod(self):
        """Test creating a classmethod."""
        method = Method(name="from_string", is_classmethod=True)
        assert method.is_classmethod is True
    
    def test_create_staticmethod(self):
        """Test creating a staticmethod."""
        method = Method(name="helper", is_staticmethod=True)
        assert method.is_staticmethod is True
    
    def test_method_with_docstring(self):
        """Test method with docstring."""
        method = Method(
            name="test_func",
            docstring="This is a test function.\nIt does something."
        )
        assert "test function" in method.docstring
    
    def test_method_with_overloads(self):
        """Test method with overloads."""
        method = Method(name="test_func", overloads=2)
        assert method.overloads == 2


class TestClass:
    """Tests for Class model."""
    
    def test_create_simple_class(self):
        """Test creating a simple class."""
        cls = Class(name="TestClass")
        assert cls.name == "TestClass"
        assert len(cls.methods) == 0
        assert len(cls.base_classes) == 0
        assert len(cls.attributes) == 0
    
    def test_create_class_with_methods(self):
        """Test creating a class with methods."""
        methods = [
            Method(name="__init__", parameters=[Parameter(name="self")]),
            Method(name="test_method", parameters=[Parameter(name="self")])
        ]
        cls = Class(name="TestClass", methods=methods)
        
        assert cls.name == "TestClass"
        assert len(cls.methods) == 2
        assert cls.methods[0].name == "__init__"
        assert cls.methods[1].name == "test_method"
    
    def test_create_class_with_inheritance(self):
        """Test creating a class with base classes."""
        cls = Class(name="DerivedClass", base_classes=["BaseClass", "Mixin"])
        assert len(cls.base_classes) == 2
        assert "BaseClass" in cls.base_classes
        assert "Mixin" in cls.base_classes
    
    def test_create_class_with_attributes(self):
        """Test creating a class with attributes."""
        from .models import Attribute
        attrs = [
            Attribute(name="CONST1", value="1", type_hint="int"),
            Attribute(name="CONST2", value='"test"', type_hint="str"),
            Attribute(name="class_var", value=None, type_hint="int")
        ]
        cls = Class(
            name="TestClass",
            attributes=attrs,
            docstring=None
        )
        assert len(cls.attributes) == 3
        assert cls.attributes[0].name == "CONST1"
    
    def test_class_with_docstring(self):
        """Test class with docstring."""
        cls = Class(
            name="TestClass",
            docstring="This is a test class.\nIt represents something."
        )
        assert "test class" in cls.docstring


class TestModule:
    """Tests for Module model."""
    
    def test_create_simple_module(self):
        """Test creating a simple module."""
        module = Module(name="test_module")
        assert module.name == "test_module"
        assert len(module.classes) == 0
        assert len(module.functions) == 0
        assert len(module.constants) == 0
    
    def test_create_module_with_classes(self):
        """Test creating a module with classes."""
        classes = [
            Class(name="Class1"),
            Class(name="Class2")
        ]
        module = Module(name="test_module", classes=classes)
        
        assert module.name == "test_module"
        assert len(module.classes) == 2
        assert module.classes[0].name == "Class1"
    
    def test_create_module_with_functions(self):
        """Test creating a module with functions."""
        functions = [
            Method(name="func1"),
            Method(name="func2", parameters=[Parameter(name="x")])
        ]
        module = Module(name="test_module", functions=functions)
        
        assert module.name == "test_module"
        assert len(module.functions) == 2
    
    def test_create_module_with_constants(self):
        """Test creating a module with constants."""
        from .models import Constant
        constants = [
            Constant(name="CONST1", value="42", type_hint=None),
            Constant(name="CONST2", value="True", type_hint=None),
            Constant(name="VERSION", value='"1.0.0"', type_hint="str")
        ]
        module = Module(
            name="test_module",
            constants=constants,
            docstring=None
        )
        assert len(module.constants) == 3
        assert module.constants[0].name == "CONST1"
    
    def test_complex_module(self):
        """Test creating a complex module with all components."""
        from .models import Constant
        # Create methods for a class
        class_methods = [
            Method(name="__init__", parameters=[Parameter(name="self", type_hint=None, default_value=None, is_optional=False, is_variadic=False)], return_type=None, is_async=False, is_classmethod=False, is_staticmethod=False, is_property=False, docstring=None, overloads=0),
            Method(name="process", parameters=[
                Parameter(name="self", type_hint=None, default_value=None, is_optional=False, is_variadic=False),
                Parameter(name="data", type_hint="bytes", default_value=None, is_optional=False, is_variadic=False)
            ], return_type=None, is_async=False, is_classmethod=False, is_staticmethod=False, is_property=False, docstring=None, overloads=0)
        ]
        
        # Create a class
        test_class = Class(
            name="Processor",
            methods=class_methods,
            docstring="A data processor class."
        )
        
        # Create module-level functions
        module_functions = [
            Method(name="helper", parameters=[
                Parameter(name="x", type_hint="int", default_value=None, is_optional=False, is_variadic=False)
            ], return_type="str", is_async=False, is_classmethod=False, is_staticmethod=False, is_property=False, docstring=None, overloads=0)
        ]
        
        # Create constants
        constants = [
            Constant(name="VERSION", value="1.0.0", type_hint=None, is_hidden=False),
            Constant(name="MAX_SIZE", value="1000", type_hint=None, is_hidden=False)
        ]
        
        # Create module
        module = Module(
            name="processing",
            classes=[test_class],
            functions=module_functions,
            constants=constants,
            docstring="Data processing module."
        )
        
        assert module.name == "processing"
        assert len(module.classes) == 1
        assert len(module.functions) == 1
        assert len(module.constants) == 2
        assert module.classes[0].name == "Processor"
        assert len(module.classes[0].methods) == 2


class TestBoard:
    """Tests for Board model."""
    
    def test_create_simple_board(self):
        """Test creating a simple board."""
        board = Board(
            version="v1.26.0",
            port="esp32",
            board="esp32_generic",
            modules=[]
        )
        assert board.version == "v1.26.0"
        assert board.port == "esp32"
        assert board.board == "esp32_generic"
        assert len(board.modules) == 0
    
    def test_create_board_with_modules(self):
        """Test creating a board with modules."""
        modules = [
            Module(name="machine"),
            Module(name="time"),
            Module(name="gc")
        ]
        board = Board(
            version="v1.26.0",
            port="esp32",
            board="esp32_generic",
            modules=modules
        )
        
        assert len(board.modules) == 3
        assert board.modules[0].name == "machine"
    
    def test_board_serialization(self):
        """Test board serialization."""
        module = Module(
            name="test",
            functions=[Method(name="func1")]
        )
        board = Board(
            version="v1.26.0",
            port="test",
            board="test_board",
            modules=[module]
        )
        
        data = board.model_dump()
        assert data["version"] == "v1.26.0"
        assert data["port"] == "test"
        assert len(data["modules"]) == 1
        assert data["modules"][0]["name"] == "test"


class TestModelValidation:
    """Tests for model validation."""
    
    def test_parameter_name_required(self):
        """Test that parameter name is required."""
        with pytest.raises(Exception):  # Pydantic ValidationError
            Parameter()
    
    def test_method_name_required(self):
        """Test that method name is required."""
        with pytest.raises(Exception):  # Pydantic ValidationError
            Method()
    
    def test_class_name_required(self):
        """Test that class name is required."""
        with pytest.raises(Exception):  # Pydantic ValidationError
            Class()
    
    def test_module_name_required(self):
        """Test that module name is required."""
        with pytest.raises(Exception):  # Pydantic ValidationError
            Module()
    
    def test_board_fields_required(self):
        """Test that board required fields are enforced."""
        with pytest.raises(Exception):  # Pydantic ValidationError
            Board(version="v1.26.0")  # Missing port, board, modules


class TestModelEquality:
    """Tests for model equality and comparison."""
    
    def test_parameter_equality(self):
        """Test parameter equality."""
        param1 = Parameter(name="x", type_hint="int")
        param2 = Parameter(name="x", type_hint="int")
        param3 = Parameter(name="y", type_hint="int")
        
        assert param1.model_dump() == param2.model_dump()
        assert param1.model_dump() != param3.model_dump()
    
    def test_method_equality(self):
        """Test method equality."""
        method1 = Method(name="test", return_type="int")
        method2 = Method(name="test", return_type="int")
        method3 = Method(name="test", return_type="str")
        
        assert method1.model_dump() == method2.model_dump()
        assert method1.model_dump() != method3.model_dump()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
