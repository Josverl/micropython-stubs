"""
Stub scanner tool to extract API information from MicroPython .pyi stub files.

This tool uses libcst to parse stub files and extract information about modules,
classes, methods, functions, and parameters.
"""

import ast
from pathlib import Path
from typing import List, Optional, Dict
import logging

from models import Module, Class, Method, Parameter

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
        Scan a single .pyi file and extract module information.

        Args:
            pyi_file: Path to the .pyi file

        Returns:
            Module object or None if parsing failed
        """
        try:
            with open(pyi_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Parse using ast (more reliable than libcst for stub files)
            tree = ast.parse(content, filename=str(pyi_file))

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
            docstring = ast.get_docstring(tree)

            # Extract classes and functions
            classes = []
            functions = []
            constants = []

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    # Only process top-level classes
                    if self._is_top_level(node, tree):
                        class_obj = self._extract_class(node)
                        if class_obj:
                            classes.append(class_obj)

                elif isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                    # Only process top-level functions
                    if self._is_top_level(node, tree):
                        func = self._extract_function(node)
                        if func:
                            functions.append(func)

                elif isinstance(node, ast.AnnAssign) and self._is_top_level(node, tree):
                    # Extract annotated constants
                    if isinstance(node.target, ast.Name):
                        constants.append(node.target.id)

                elif isinstance(node, ast.Assign) and self._is_top_level(node, tree):
                    # Extract simple assignments (constants)
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            constants.append(target.id)

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

    def _is_top_level(self, node: ast.AST, tree: ast.Module) -> bool:
        """Check if a node is at the top level of the module."""
        return node in tree.body

    def _extract_class(self, node: ast.ClassDef) -> Optional[Class]:
        """Extract class information from an AST ClassDef node."""
        try:
            # Extract base classes
            base_classes = []
            for base in node.bases:
                if isinstance(base, ast.Name):
                    base_classes.append(base.id)
                elif isinstance(base, ast.Attribute):
                    base_classes.append(self._get_full_name(base))

            # Extract methods and attributes
            methods = []
            attributes = []

            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    method = self._extract_function(item)
                    if method:
                        methods.append(method)

                elif isinstance(item, ast.AnnAssign):
                    if isinstance(item.target, ast.Name):
                        attributes.append(item.target.id)

                elif isinstance(item, ast.Assign):
                    for target in item.targets:
                        if isinstance(target, ast.Name):
                            attributes.append(target.id)

            docstring = ast.get_docstring(node)

            return Class(
                name=node.name,
                base_classes=base_classes,
                methods=methods,
                attributes=attributes,
                docstring=docstring,
            )
        except Exception as e:
            logger.error(f"Error extracting class {node.name}: {e}")
            return None

    def _extract_function(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> Optional[Method]:
        """Extract function/method information from an AST FunctionDef node."""
        try:
            # Extract parameters
            parameters = []
            args = node.args

            # Process regular arguments
            for i, arg in enumerate(args.args):
                param = self._extract_parameter(arg, args.defaults, i, len(args.args))
                parameters.append(param)

            # Process *args
            if args.vararg:
                parameters.append(
                    Parameter(
                        name=args.vararg.arg,
                        type_hint=self._get_annotation(args.vararg),
                        is_variadic=True,
                    )
                )

            # Process keyword-only arguments
            for i, arg in enumerate(args.kwonlyargs):
                default = args.kw_defaults[i] if i < len(args.kw_defaults) else None
                param = Parameter(
                    name=arg.arg,
                    type_hint=self._get_annotation(arg),
                    default_value=self._get_default_value(default) if default else None,
                    is_optional=default is not None,
                )
                parameters.append(param)

            # Process **kwargs
            if args.kwarg:
                parameters.append(
                    Parameter(
                        name=args.kwarg.arg,
                        type_hint=self._get_annotation(args.kwarg),
                        is_variadic=True,
                    )
                )

            # Extract return type
            return_type = self._get_annotation(node.returns) if node.returns else None

            # Check for decorators
            is_classmethod = any(
                (isinstance(d, ast.Name) and d.id == "classmethod") for d in node.decorator_list
            )
            is_staticmethod = any(
                (isinstance(d, ast.Name) and d.id == "staticmethod") for d in node.decorator_list
            )
            is_property = any(
                (isinstance(d, ast.Name) and d.id == "property") for d in node.decorator_list
            )

            # Check if overloaded
            is_overload = any(
                (isinstance(d, ast.Name) and d.id == "overload") for d in node.decorator_list
            )

            docstring = ast.get_docstring(node)

            return Method(
                name=node.name,
                parameters=parameters,
                return_type=return_type,
                is_async=isinstance(node, ast.AsyncFunctionDef),
                is_classmethod=is_classmethod,
                is_staticmethod=is_staticmethod,
                is_property=is_property,
                docstring=docstring,
                overloads=1 if is_overload else 0,
            )
        except Exception as e:
            logger.error(f"Error extracting function {node.name}: {e}")
            return None

    def _extract_parameter(
        self, arg: ast.arg, defaults: List, index: int, total_args: int
    ) -> Parameter:
        """Extract parameter information."""
        # Calculate if this parameter has a default value
        num_defaults = len(defaults)
        default_offset = total_args - num_defaults
        has_default = index >= default_offset
        default_value = None

        if has_default:
            default_idx = index - default_offset
            if default_idx < len(defaults):
                default_value = self._get_default_value(defaults[default_idx])

        return Parameter(
            name=arg.arg,
            type_hint=self._get_annotation(arg),
            default_value=default_value,
            is_optional=has_default,
        )

    def _get_annotation(self, node) -> Optional[str]:
        """Get type annotation as a string."""
        if not hasattr(node, "annotation") or node.annotation is None:
            return None

        try:
            return ast.unparse(node.annotation)
        except Exception:
            return None

    def _get_default_value(self, node) -> Optional[str]:
        """Get default value as a string."""
        if node is None:
            return None

        try:
            return ast.unparse(node)
        except Exception:
            return "..."

    def _get_full_name(self, node: ast.Attribute) -> str:
        """Get full name from an Attribute node."""
        parts = []
        current = node

        while isinstance(current, ast.Attribute):
            parts.insert(0, current.attr)
            current = current.value

        if isinstance(current, ast.Name):
            parts.insert(0, current.id)

        return ".".join(parts)


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
