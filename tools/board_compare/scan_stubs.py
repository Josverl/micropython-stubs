"""
Stub scanner tool to extract API information from MicroPython .pyi stub files.

This tool uses libcst to parse stub files and extract information about modules,
classes, methods, functions, and parameters. libcst is used to maintain compatibility
with the micropython-stubber project and to preserve formatting/comments for future enhancements.
"""

import logging
from pathlib import Path
from typing import Dict, List, Optional, Union

import libcst as cst
from models import Attribute, Class, Constant, Method, Module, Parameter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class StubScanner:
    """Scans MicroPython stub files to extract API information."""

    def __init__(self, stub_dir: Path):
        """
        Initialize the scanner.

        Args:
            stub_dir: Path to the directory containing .pyi stub files
        """
        self.stub_dir = Path(stub_dir)

    def scan_all_modules(self) -> List[Module]:
        """
        Scan all .pyi files in the stub directory.

        Returns:
            List of Module objects containing extracted information
        """
        modules = []
        for pyi_file in self.stub_dir.glob("**/*.pyi"):
            if pyi_file.name.startswith("_") and pyi_file.name != "__builtins__.pyi":
                # Skip private modules except __builtins__
                continue

            try:
                module = self.scan_module(pyi_file)
                if module:
                    modules.append(module)
            except Exception as e:
                logger.error(f"Error scanning {pyi_file}: {e}")

        return modules

    def scan_module(self, pyi_file: Path) -> Optional[Module]:
        """
        Scan a single .pyi file and extract module information using libcst.

        Args:
            pyi_file: Path to the .pyi file

        Returns:
            Module object or None if parsing failed
        """
        try:
            with open(pyi_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Parse using libcst
            tree = cst.parse_module(content)

            # Extract module name from file path
            module_name = pyi_file.stem
            if pyi_file.parent.name not in ["", "."]:
                # Handle package modules like requests/__init__.pyi
                rel_path = pyi_file.relative_to(self.stub_dir)
                if rel_path.name == "__init__.pyi":
                    module_name = str(rel_path.parent).replace("/", ".")
                else:
                    module_name = str(rel_path.with_suffix("")).replace("/", ".")

            # Extract docstring
            docstring = self._get_docstring(tree)

            # Extract classes and functions
            classes = []
            functions = []
            constants = []

            for stmt in tree.body:
                if isinstance(stmt, cst.ClassDef):
                    class_obj = self._extract_class(stmt)
                    if class_obj:
                        classes.append(class_obj)

                elif isinstance(stmt, cst.FunctionDef):
                    func = self._extract_function(stmt)
                    if func:
                        functions.append(func)

                elif isinstance(stmt, cst.AnnAssign):
                    # Extract annotated constants
                    if isinstance(stmt.target, cst.Name):
                        const_name = stmt.target.value
                        type_hint = self._get_annotation_str(stmt.annotation) if stmt.annotation else None
                        value = self._get_value_str(stmt.value) if stmt.value else None
                        
                        constant = Constant(
                            name=const_name,
                            type_hint=type_hint,
                            value=value,
                            is_hidden=self._is_typing_related(const_name, type_hint, value)
                        )
                        constants.append(constant)

                elif isinstance(stmt, cst.SimpleStatementLine):
                    # Check for simple assignments (constants)
                    for item in stmt.body:
                        if isinstance(item, cst.Assign):
                            for target in item.targets:
                                if isinstance(target.target, cst.Name):
                                    const_name = target.target.value
                                    value = self._get_value_str(item.value) if item.value else None
                                    
                                    constant = Constant(
                                        name=const_name,
                                        value=value,
                                        type_hint=None,
                                        is_hidden=self._is_typing_related(const_name, None, value)
                                    )
                                    constants.append(constant)

            return Module(
                name=module_name,
                classes=classes,
                functions=functions,
                constants=constants,
                docstring=docstring,
            )

        except Exception as e:
            logger.error(f"Failed to parse {pyi_file}: {e}")
            return None

    def _get_docstring(self, node: Union[cst.Module, cst.ClassDef, cst.FunctionDef]) -> Optional[str]:
        """Extract docstring from a libcst node."""
        try:
            if isinstance(node, cst.Module):
                body = node.body
            else:
                body = node.body.body if isinstance(node.body, cst.IndentedBlock) else []
            
            if body and isinstance(body[0], cst.SimpleStatementLine):
                first_stmt = body[0].body[0]
                if isinstance(first_stmt, cst.Expr) and isinstance(first_stmt.value, cst.SimpleString):
                    # Remove quotes and handle escape sequences
                    docstring = first_stmt.value.value
                    if docstring.startswith('"""') or docstring.startswith("'''"):
                        return docstring[3:-3]
                    elif docstring.startswith('"') or docstring.startswith("'"):
                        return docstring[1:-1]
            return None
        except Exception:
            return None

    def _extract_class(self, node: cst.ClassDef) -> Optional[Class]:
        """Extract class information from a libcst ClassDef node."""
        try:
            # Extract base classes
            base_classes = []
            if node.bases:
                for arg in node.bases:
                    if isinstance(arg, cst.Arg):
                        base_classes.append(self._get_expression_str(arg.value))

            # Extract methods and attributes
            methods = []
            attributes = []

            if isinstance(node.body, cst.IndentedBlock):
                for item in node.body.body:
                    if isinstance(item, cst.FunctionDef):
                        method = self._extract_function(item)
                        if method:
                            methods.append(method)

                    elif isinstance(item, cst.SimpleStatementLine):
                        for stmt in item.body:
                            if isinstance(stmt, cst.AnnAssign) and isinstance(stmt.target, cst.Name):
                                attr_name = stmt.target.value
                                type_hint = self._get_annotation_str(stmt.annotation) if stmt.annotation else None
                                value = self._get_value_str(stmt.value) if stmt.value else None
                                
                                attribute = Attribute(
                                    name=attr_name,
                                    type_hint=type_hint,
                                    value=value,
                                    is_hidden=self._is_typing_related(attr_name, type_hint, value)
                                )
                                attributes.append(attribute)
                            elif isinstance(stmt, cst.Assign):
                                for target in stmt.targets:
                                    if isinstance(target.target, cst.Name):
                                        attr_name = target.target.value
                                        value = self._get_value_str(stmt.value) if stmt.value else None
                                        
                                        attribute = Attribute(
                                            name=attr_name,
                                            value=value,
                                            type_hint=None,
                                            is_hidden=self._is_typing_related(attr_name, None, value)
                                        )
                                        attributes.append(attribute)

            docstring = self._get_docstring(node)

            return Class(
                name=node.name.value,
                base_classes=base_classes,
                methods=methods,
                attributes=attributes,
                docstring=docstring,
            )
        except Exception as e:
            logger.error(f"Error extracting class {node.name.value if hasattr(node, 'name') else 'unknown'}: {e}")
            return None

    def _extract_function(self, node: cst.FunctionDef) -> Optional[Method]:
        """Extract function/method information from a libcst FunctionDef node."""
        try:
            # Extract parameters
            parameters = []
            params = node.params

            # Process regular arguments
            for param in params.params:
                parameters.append(self._extract_parameter_from_param(param))

            # Process *args
            if params.star_arg and isinstance(params.star_arg, cst.Param):
                parameters.append(
                    Parameter(
                        name=params.star_arg.name.value,
                        type_hint=self._get_annotation_str(params.star_arg.annotation) if params.star_arg.annotation else None,
                        is_variadic=True,
                    )
                )

            # Process keyword-only arguments
            for param in params.kwonly_params:
                parameters.append(self._extract_parameter_from_param(param))

            # Process **kwargs
            if params.star_kwarg:
                parameters.append(
                    Parameter(
                        name=params.star_kwarg.name.value,
                        type_hint=self._get_annotation_str(params.star_kwarg.annotation) if params.star_kwarg.annotation else None,
                        is_variadic=True,
                    )
                )

            # Extract return type
            return_type = self._get_annotation_str(node.returns) if node.returns else None

            # Check for decorators
            is_async = node.asynchronous is not None
            is_classmethod = False
            is_staticmethod = False
            is_property = False
            is_overload = False

            for decorator in node.decorators:
                dec_name = self._get_decorator_name(decorator)
                if dec_name == "classmethod":
                    is_classmethod = True
                elif dec_name == "staticmethod":
                    is_staticmethod = True
                elif dec_name == "property":
                    is_property = True
                elif dec_name == "overload":
                    is_overload = True

            docstring = self._get_docstring(node)

            return Method(
                name=node.name.value,
                parameters=parameters,
                return_type=return_type,
                is_async=is_async,
                is_classmethod=is_classmethod,
                is_staticmethod=is_staticmethod,
                is_property=is_property,
                docstring=docstring,
                overloads=1 if is_overload else 0,
            )
        except Exception as e:
            logger.error(f"Error extracting function {node.name.value if hasattr(node, 'name') else 'unknown'}: {e}")
            return None

    def _extract_parameter_from_param(self, param: cst.Param) -> Parameter:
        """Extract parameter information from a libcst Param node."""
        default_value = None
        is_optional = False

        if param.default:
            default_value = self._get_expression_str(param.default)
            is_optional = True

        return Parameter(
            name=param.name.value,
            type_hint=self._get_annotation_str(param.annotation) if param.annotation else None,
            default_value=default_value,
            is_optional=is_optional,
        )

    def _get_value_str(self, value: Union[cst.BaseExpression, None]) -> Optional[str]:
        """Get value as a string from libcst expression."""
        if value is None:
            return None
        try:
            return cst.Module([]).code_for_node(value)
        except Exception:
            return None

    def _is_typing_related(self, name: str, type_hint: Optional[str] = None, value: Optional[str] = None) -> bool:
        """
        Determine if a constant/attribute is typing-related and should be hidden.
        
        Args:
            name: The name of the constant/attribute
            type_hint: The type hint (if any)
            value: The value (if any)
            
        Returns:
            True if this is a typing-related constant that should be hidden
        """
        # Check for typing-specific type hints
        if type_hint:
            typing_indicators = [
                'TypeAlias', 'TypeVar', 'ParamSpec', 'Generic', 'Protocol',
                'ClassVar', 'Type[', 'Union[', 'Optional[', 'Literal[',
                'Callable[', 'Any', 'NoReturn', 'Never'
            ]
            if any(indicator in type_hint for indicator in typing_indicators):
                return True
        
        # Check for typing-specific value patterns
        if value:
            typing_value_patterns = [
                'TypeVar(', 'ParamSpec(', 'TypeAlias', 'Generic[',
                'Protocol[', 'Union[', 'Optional[', 'Literal[',
                'Callable[', 'Type[', 'ClassVar[', 'Final['
            ]
            if any(pattern in value for pattern in typing_value_patterns):
                return True
        
        # Check for common typing variable naming patterns
        # Variables starting with _ and containing type-related keywords
        if name.startswith('_') and any(keyword in name.lower() for keyword in [
            'type', 'var', 'param', 'spec', 'alias', 'generic', 'protocol'
        ]):
            return True
            
        # Common typing variable prefixes/suffixes
        typing_name_patterns = [
            '_T', '_F', '_P', '_R', '_Ret', '_Param', '_Args', '_Kwargs',
            'Const_T', '_TypeVar', '_ParamSpec', '_TypeAlias'
        ]
        if name in typing_name_patterns or any(name.endswith(pattern) for pattern in ['_T', '_F', '_P', '_R']):
            return True
            
        return False

    def _get_annotation_str(self, annotation: Union[cst.Annotation, None]) -> Optional[str]:
        """Get type annotation as a string from libcst annotation."""
        if annotation is None:
            return None

        try:
            if isinstance(annotation, cst.Annotation):
                return annotation.annotation.visit(cst.Module([]).code_for_node)
            return None
        except Exception:
            return None

    def _get_expression_str(self, expr: cst.BaseExpression) -> str:
        """Get expression as a string."""
        try:
            # Create a temporary module to get the code
            return cst.Module([]).code_for_node(expr)
        except Exception:
            return "..."

    def _get_decorator_name(self, decorator: cst.Decorator) -> Optional[str]:
        """Get decorator name from a Decorator node."""
        try:
            if isinstance(decorator.decorator, cst.Name):
                return decorator.decorator.value
            elif isinstance(decorator.decorator, cst.Attribute):
                return self._get_expression_str(decorator.decorator)
            return None
        except Exception:
            return None


def scan_board_stubs(stub_path: Path, version: str, port: str, board: str) -> Dict:
    """
    Scan all stubs for a specific board.

    Args:
        stub_path: Path to the stub directory
        version: MicroPython version
        port: Port name
        board: Board name

    Returns:
        Dictionary containing board information
    """
    scanner = StubScanner(stub_path)
    modules = scanner.scan_all_modules()

    # Extract version info from docstrings if available
    mpy_version = None
    arch = None

    if modules:
        for module in modules:
            if module.docstring and "MCU:" in module.docstring:
                # Try to extract MCU info from docstring
                try:
                    import re

                    mcu_match = re.search(r"MCU:\s*({[^}]+})", module.docstring)
                    if mcu_match:
                        mcu_info = eval(mcu_match.group(1))
                        mpy_version = mcu_info.get("mpy")
                        arch = mcu_info.get("arch")
                        break
                except Exception:
                    pass

    return {
        "version": version,
        "port": port,
        "board": board,
        "modules": [m.model_dump() for m in modules],
        "mpy_version": mpy_version,
        "arch": arch,
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python scan_stubs.py <stub_directory>")
        sys.exit(1)

    stub_dir = Path(sys.argv[1])
    if not stub_dir.exists():
        print(f"Error: Directory {stub_dir} does not exist")
        sys.exit(1)

    scanner = StubScanner(stub_dir)
    modules = scanner.scan_all_modules()

    print(f"Found {len(modules)} modules:")
    for module in modules:
        print(f"  - {module.name}: {len(module.classes)} classes, {len(module.functions)} functions")
