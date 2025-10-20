"""
Pydantic models for the MicroPython board comparison database.

This module defines the data models used to represent and store information
about MicroPython modules, classes, methods, and their parameters across
different boards and versions.
"""

from typing import List, Optional

from pydantic import BaseModel, Field


class Parameter(BaseModel):
    """Represents a function or method parameter."""

    name: str = Field(..., description="Parameter name")
    type_hint: Optional[str] = Field(None, description="Type annotation if available")
    default_value: Optional[str] = Field(None, description="Default value if any")
    is_optional: bool = Field(False, description="Whether the parameter is optional")
    is_variadic: bool = Field(False, description="Whether this is *args or **kwargs")


class Method(BaseModel):
    """Represents a method or function."""

    name: str = Field(..., description="Method/function name")
    parameters: List[Parameter] = Field(default_factory=list, description="List of parameters")
    return_type: Optional[str] = Field(None, description="Return type annotation if available")
    is_async: bool = Field(False, description="Whether the method is async")
    is_classmethod: bool = Field(False, description="Whether this is a classmethod")
    is_staticmethod: bool = Field(False, description="Whether this is a staticmethod")
    is_property: bool = Field(False, description="Whether this is a property")
    decorators: List[str] = Field(
        default_factory=list, description="List of all decorator names (e.g., ['property', 'classmethod', 'overload'])"
    )
    docstring: Optional[str] = Field(None, description="Method docstring")
    overloads: int = Field(0, description="Number of overloaded versions")


class Constant(BaseModel):
    """Represents a module or class constant/variable."""

    name: str = Field(..., description="Constant name")
    value: Optional[str] = Field(None, description="Constant value if available")
    type_hint: Optional[str] = Field(None, description="Type annotation if available")
    is_hidden: bool = Field(False, description="Whether this constant should be hidden (e.g., typing-related)")


class Attribute(BaseModel):
    """Represents a class attribute/variable."""

    name: str = Field(..., description="Attribute name")
    value: Optional[str] = Field(None, description="Attribute value if available")
    type_hint: Optional[str] = Field(None, description="Type annotation if available")
    is_hidden: bool = Field(False, description="Whether this attribute should be hidden (e.g., typing-related)")


class Class(BaseModel):
    """Represents a class definition."""

    name: str = Field(..., description="Class name")
    base_classes: List[str] = Field(default_factory=list, description="Base class names")
    methods: List[Method] = Field(default_factory=list, description="Class methods")
    attributes: List[Attribute] = Field(default_factory=list, description="Class attributes/constants")
    docstring: Optional[str] = Field(None, description="Class docstring")


class Module(BaseModel):
    """Represents a module."""

    name: str = Field(..., description="Module name")
    classes: List[Class] = Field(default_factory=list, description="Classes defined in module")
    functions: List[Method] = Field(default_factory=list, description="Module-level functions")
    constants: List[Constant] = Field(default_factory=list, description="Module-level constants")
    docstring: Optional[str] = Field(None, description="Module docstring")


class Board(BaseModel):
    """Represents a board/port combination."""

    version: str = Field(..., description="MicroPython version (e.g., 'v1.26.0')")
    port: str = Field(..., description="Port name (e.g., 'esp32', 'rp2')")
    board: str = Field(..., description="Board name (e.g., 'ESP32_GENERIC', 'RPI_PICO')")
    modules: List[Module] = Field(default_factory=list, description="Modules available on this board")
    mpy_version: Optional[str] = Field(None, description=".mpy version")
    arch: Optional[str] = Field(None, description="Architecture")


class DatabaseSchema(BaseModel):
    """Root schema for the entire database."""

    version: str = Field("1.0.0", description="Database schema version")
    boards: List[Board] = Field(default_factory=list, description="All boards in database")
