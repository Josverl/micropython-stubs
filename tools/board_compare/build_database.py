"""
Database builder tool to create and populate the SQLite database.

This tool scans published stubs for MicroPython boards and builds a normalized
database for comparison.
"""

import hashlib
import json
import logging
import re
import sqlite3
from pathlib import Path
from typing import Dict, List, Optional

from models import Board, Class, Method, Module, Parameter
from scan_stubs import scan_board_stubs

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatabaseBuilder:
    """Builds and populates the normalized board comparison database."""

    def __init__(self, db_path: Path):
        """
        Initialize the database builder.

        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = Path(db_path)
        self.conn: Optional[sqlite3.Connection] = None

    def _generate_signature_hash(self, *components) -> str:
        """Generate a signature hash from components."""
        # Convert all components to strings and join them
        signature_str = "|".join(str(comp) if comp is not None else "" for comp in components)
        return hashlib.sha256(signature_str.encode()).hexdigest()[:16]

    def _get_method_signature_hash(self, method_data: Dict, parameters: List[Dict]) -> str:
        """Generate a unique signature hash for a method including its parameters."""
        param_signature = "|".join([
            f"{p['name']}:{p.get('type_hint', '')}:{p.get('default_value', '')}:{p.get('is_optional', False)}:{p.get('is_variadic', False)}"
            for p in parameters
        ])
        
        return self._generate_signature_hash(
            method_data["name"],
            method_data.get("return_type"),
            method_data.get("is_async", False),
            method_data.get("is_classmethod", False),
            method_data.get("is_staticmethod", False),
            method_data.get("is_property", False),
            param_signature
        )

    def _is_typing_related(self, name: str, type_hint: str = None, value: str = None) -> bool:
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

    def create_schema(self):
        """Create the normalized database schema."""
        cursor = self.conn.cursor()

        # Boards table (unchanged)
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS boards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                version TEXT NOT NULL,
                port TEXT NOT NULL,
                board TEXT NOT NULL,
                mpy_version TEXT,
                arch TEXT,
                UNIQUE(version, port, board)
            )
        """
        )

        # Unique module definitions
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS unique_modules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                docstring TEXT,
                signature_hash TEXT NOT NULL UNIQUE
            )
        """
        )

        # Board-Module support relationship
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS board_module_support (
                board_id INTEGER NOT NULL,
                module_id INTEGER NOT NULL,
                PRIMARY KEY (board_id, module_id),
                FOREIGN KEY (board_id) REFERENCES boards(id),
                FOREIGN KEY (module_id) REFERENCES unique_modules(id)
            )
        """
        )

        # Unique class definitions
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS unique_classes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                module_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                docstring TEXT,
                signature_hash TEXT NOT NULL UNIQUE,
                FOREIGN KEY (module_id) REFERENCES unique_modules(id)
            )
        """
        )

        # Board-Class support relationship
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS board_class_support (
                board_id INTEGER NOT NULL,
                class_id INTEGER NOT NULL,
                PRIMARY KEY (board_id, class_id),
                FOREIGN KEY (board_id) REFERENCES boards(id),
                FOREIGN KEY (class_id) REFERENCES unique_classes(id)
            )
        """
        )

        # Unique class inheritance relationships
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS unique_class_bases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                class_id INTEGER NOT NULL,
                base_name TEXT NOT NULL,
                signature_hash TEXT NOT NULL UNIQUE,
                FOREIGN KEY (class_id) REFERENCES unique_classes(id)
            )
        """
        )

        # Unique class attributes
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS unique_class_attributes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                class_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                type_hint TEXT,
                value TEXT,
                is_hidden INTEGER DEFAULT 0,
                signature_hash TEXT NOT NULL UNIQUE,
                FOREIGN KEY (class_id) REFERENCES unique_classes(id)
            )
        """
        )

        # Board-Class Attribute support relationship
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS board_class_attribute_support (
                board_id INTEGER NOT NULL,
                attribute_id INTEGER NOT NULL,
                PRIMARY KEY (board_id, attribute_id),
                FOREIGN KEY (board_id) REFERENCES boards(id),
                FOREIGN KEY (attribute_id) REFERENCES unique_class_attributes(id)
            )
        """
        )

        # Unique method definitions
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS unique_methods (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                module_id INTEGER,
                class_id INTEGER,
                name TEXT NOT NULL,
                return_type TEXT,
                is_async INTEGER DEFAULT 0,
                is_classmethod INTEGER DEFAULT 0,
                is_staticmethod INTEGER DEFAULT 0,
                is_property INTEGER DEFAULT 0,
                overloads INTEGER DEFAULT 0,
                docstring TEXT,
                signature_hash TEXT NOT NULL UNIQUE,
                FOREIGN KEY (module_id) REFERENCES unique_modules(id),
                FOREIGN KEY (class_id) REFERENCES unique_classes(id)
            )
        """
        )

        # Board-Method support relationship
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS board_method_support (
                board_id INTEGER NOT NULL,
                method_id INTEGER NOT NULL,
                PRIMARY KEY (board_id, method_id),
                FOREIGN KEY (board_id) REFERENCES boards(id),
                FOREIGN KEY (method_id) REFERENCES unique_methods(id)
            )
        """
        )

        # Unique parameter definitions (linked to unique methods)
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS unique_parameters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                method_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                position INTEGER NOT NULL,
                type_hint TEXT,
                default_value TEXT,
                is_optional INTEGER DEFAULT 0,
                is_variadic INTEGER DEFAULT 0,
                FOREIGN KEY (method_id) REFERENCES unique_methods(id)
            )
        """
        )

        # Unique module constants
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS unique_module_constants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                module_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                value TEXT,
                type_hint TEXT,
                is_hidden INTEGER DEFAULT 0,
                signature_hash TEXT NOT NULL UNIQUE,
                FOREIGN KEY (module_id) REFERENCES unique_modules(id)
            )
        """
        )

        # Board-Module Constant support relationship
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS board_module_constant_support (
                board_id INTEGER NOT NULL,
                constant_id INTEGER NOT NULL,
                PRIMARY KEY (board_id, constant_id),
                FOREIGN KEY (board_id) REFERENCES boards(id),
                FOREIGN KEY (constant_id) REFERENCES unique_module_constants(id)
            )
        """
        )

        # Create indexes for performance
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_boards_version ON boards(version)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_unique_modules_signature ON unique_modules(signature_hash)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_unique_modules_name ON unique_modules(name)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_unique_classes_signature ON unique_classes(signature_hash)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_unique_classes_module ON unique_classes(module_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_unique_methods_signature ON unique_methods(signature_hash)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_unique_methods_module ON unique_methods(module_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_unique_methods_class ON unique_methods(class_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_unique_methods_name ON unique_methods(name)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_board_method_support_method ON board_method_support(method_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_board_method_support_board ON board_method_support(board_id)")

        # Create view for methods with board support information
        cursor.execute(
            """
            CREATE VIEW IF NOT EXISTS methods_with_board_support AS
            SELECT 
                um.id,
                um.name,
                um.return_type,
                um.is_async,
                um.is_classmethod,
                um.is_staticmethod,
                um.is_property,
                um.docstring,
                umod.name as module_name,
                uc.name as class_name,
                GROUP_CONCAT(b.port || '-' || COALESCE(b.board, '') || '-' || b.version, '; ') as supported_boards,
                COUNT(DISTINCT bms.board_id) as board_count
            FROM unique_methods um
            LEFT JOIN unique_modules umod ON um.module_id = umod.id
            LEFT JOIN unique_classes uc ON um.class_id = uc.id
            LEFT JOIN board_method_support bms ON um.id = bms.method_id
            LEFT JOIN boards b ON bms.board_id = b.id
            GROUP BY um.id
        """
        )

        self.conn.commit()

    def connect(self):
        """Connect to the database."""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def add_board(self, board_data: Dict) -> int:
        """
        Add a board and its modules to the normalized database.

        Args:
            board_data: Dictionary containing board information

        Returns:
            Board ID
        """
        cursor = self.conn.cursor()

        # Insert or get board
        cursor.execute(
            """
            INSERT OR IGNORE INTO boards (version, port, board, mpy_version, arch)
            VALUES (?, ?, ?, ?, ?)
        """,
            (
                board_data["version"],
                board_data["port"],
                board_data["board"],
                board_data.get("mpy_version"),
                board_data.get("arch"),
            ),
        )

        cursor.execute(
            """
            SELECT id FROM boards 
            WHERE version = ? AND port = ? AND board = ?
        """,
            (board_data["version"], board_data["port"], board_data["board"]),
        )

        board_id = cursor.fetchone()[0]

        # Add modules
        for module_data in board_data["modules"]:
            self._add_module(board_id, module_data)

        self.conn.commit()
        return board_id

    def _add_module(self, board_id: int, module_data: Dict):
        """Add a module and its contents to the normalized database."""
        cursor = self.conn.cursor()

        # Generate module signature hash
        module_hash = self._generate_signature_hash(
            module_data["name"],
            module_data.get("docstring", "")
        )

        # Insert or get unique module
        cursor.execute(
            """
            INSERT OR IGNORE INTO unique_modules (name, docstring, signature_hash)
            VALUES (?, ?, ?)
        """,
            (module_data["name"], module_data.get("docstring"), module_hash),
        )

        cursor.execute("SELECT id FROM unique_modules WHERE signature_hash = ?", (module_hash,))
        module_id = cursor.fetchone()[0]

        # Link board to module
        cursor.execute(
            """
            INSERT OR IGNORE INTO board_module_support (board_id, module_id)
            VALUES (?, ?)
        """,
            (board_id, module_id),
        )

        # Add constants
        for const in module_data.get("constants", []):
            self._add_module_constant(board_id, module_id, const)

        # Add classes
        for class_data in module_data.get("classes", []):
            self._add_class(board_id, module_id, class_data)

        # Add module-level functions
        for func_data in module_data.get("functions", []):
            self._add_method(board_id, module_id, None, func_data)

    def _add_module_constant(self, board_id: int, module_id: int, constant: Dict):
        """Add a module constant to the normalized database."""
        cursor = self.conn.cursor()

        # Extract constant information
        if isinstance(constant, dict):
            const_name = constant.get("name")
            const_value = constant.get("value")
            const_type_hint = constant.get("type_hint")
            const_is_hidden = constant.get("is_hidden", False)
        else:
            # Backward compatibility for string constants
            const_name = str(constant)
            const_value = None
            const_type_hint = None
            const_is_hidden = self._is_typing_related(const_name, None, None)

        # Generate constant signature hash
        const_hash = self._generate_signature_hash(module_id, const_name, const_type_hint, const_value)

        # Insert or get unique constant
        cursor.execute(
            """
            INSERT OR IGNORE INTO unique_module_constants (module_id, name, value, type_hint, is_hidden, signature_hash)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
            (module_id, const_name, const_value, const_type_hint, int(const_is_hidden), const_hash),
        )

        cursor.execute("SELECT id FROM unique_module_constants WHERE signature_hash = ?", (const_hash,))
        const_id = cursor.fetchone()[0]

        # Link board to constant
        cursor.execute(
            """
            INSERT OR IGNORE INTO board_module_constant_support (board_id, constant_id)
            VALUES (?, ?)
        """,
            (board_id, const_id),
        )

    def _add_class(self, board_id: int, module_id: int, class_data: Dict):
        """Add a class and its contents to the normalized database."""
        cursor = self.conn.cursor()

        # Generate class signature hash
        class_hash = self._generate_signature_hash(
            module_id,
            class_data["name"],
            class_data.get("docstring", "")
        )

        # Insert or get unique class
        cursor.execute(
            """
            INSERT OR IGNORE INTO unique_classes (module_id, name, docstring, signature_hash)
            VALUES (?, ?, ?, ?)
        """,
            (module_id, class_data["name"], class_data.get("docstring"), class_hash),
        )

        cursor.execute("SELECT id FROM unique_classes WHERE signature_hash = ?", (class_hash,))
        class_id = cursor.fetchone()[0]

        # Link board to class
        cursor.execute(
            """
            INSERT OR IGNORE INTO board_class_support (board_id, class_id)
            VALUES (?, ?)
        """,
            (board_id, class_id),
        )

        # Add base classes
        for base in class_data.get("base_classes", []):
            self._add_class_base(board_id, class_id, base)

        # Add attributes
        for attr in class_data.get("attributes", []):
            self._add_class_attribute(board_id, class_id, attr)

        # Add methods
        for method_data in class_data.get("methods", []):
            self._add_method(board_id, module_id, class_id, method_data)

    def _add_class_base(self, board_id: int, class_id: int, base_name: str):
        """Add a class base relationship to the normalized database."""
        cursor = self.conn.cursor()

        # Generate base signature hash
        base_hash = self._generate_signature_hash(class_id, base_name)

        # Insert or get unique base relationship
        cursor.execute(
            """
            INSERT OR IGNORE INTO unique_class_bases (class_id, base_name, signature_hash)
            VALUES (?, ?, ?)
        """,
            (class_id, base_name, base_hash),
        )

    def _add_class_attribute(self, board_id: int, class_id: int, attribute: Dict):
        """Add a class attribute to the normalized database."""
        cursor = self.conn.cursor()

        # Extract attribute information
        if isinstance(attribute, dict):
            attr_name = attribute.get("name")
            attr_value = attribute.get("value")
            attr_type_hint = attribute.get("type_hint")
            attr_is_hidden = attribute.get("is_hidden", False)
        else:
            # Backward compatibility for string attributes
            attr_name = str(attribute)
            attr_value = None
            attr_type_hint = None
            attr_is_hidden = self._is_typing_related(attr_name, None, None)

        # Generate attribute signature hash
        attr_hash = self._generate_signature_hash(class_id, attr_name, attr_type_hint, attr_value)

        # Insert or get unique attribute
        cursor.execute(
            """
            INSERT OR IGNORE INTO unique_class_attributes (class_id, name, value, type_hint, is_hidden, signature_hash)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
            (class_id, attr_name, attr_value, attr_type_hint, int(attr_is_hidden), attr_hash),
        )

        cursor.execute("SELECT id FROM unique_class_attributes WHERE signature_hash = ?", (attr_hash,))
        attr_id = cursor.fetchone()[0]

        # Link board to attribute
        cursor.execute(
            """
            INSERT OR IGNORE INTO board_class_attribute_support (board_id, attribute_id)
            VALUES (?, ?)
        """,
            (board_id, attr_id),
        )

    def _add_method(self, board_id: int, module_id: int, class_id: Optional[int], method_data: Dict):
        """Add a method/function to the normalized database."""
        cursor = self.conn.cursor()

        # Generate method signature hash including parameters
        parameters = method_data.get("parameters", [])
        method_hash = self._get_method_signature_hash(method_data, parameters)

        # Insert or get unique method
        cursor.execute(
            """
            INSERT OR IGNORE INTO unique_methods (
                module_id, class_id, name, return_type, is_async,
                is_classmethod, is_staticmethod, is_property, overloads, 
                docstring, signature_hash
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                module_id,
                class_id,
                method_data["name"],
                method_data.get("return_type"),
                method_data.get("is_async", False),
                method_data.get("is_classmethod", False),
                method_data.get("is_staticmethod", False),
                method_data.get("is_property", False),
                method_data.get("overloads", 0),
                method_data.get("docstring"),
                method_hash,
            ),
        )

        cursor.execute("SELECT id FROM unique_methods WHERE signature_hash = ?", (method_hash,))
        method_id = cursor.fetchone()[0]

        # Link board to method
        cursor.execute(
            """
            INSERT OR IGNORE INTO board_method_support (board_id, method_id)
            VALUES (?, ?)
        """,
            (board_id, method_id),
        )

        # Add parameters (only if this is the first time we see this method)
        cursor.execute("SELECT COUNT(*) FROM unique_parameters WHERE method_id = ?", (method_id,))
        param_count = cursor.fetchone()[0]
        
        if param_count == 0:  # Only add parameters if not already added
            for i, param_data in enumerate(parameters):
                cursor.execute(
                    """
                    INSERT INTO unique_parameters (
                        method_id, name, position, type_hint, default_value,
                        is_optional, is_variadic
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                    (
                        method_id,
                        param_data["name"],
                        i,
                        param_data.get("type_hint"),
                        param_data.get("default_value"),
                        param_data.get("is_optional", False),
                        param_data.get("is_variadic", False),
                    ),
                )

    def export_to_json(self, output_path: Path, include_docstrings: bool = False):
        """
        Export the database to a JSON file for the frontend.
        
        Args:
            output_path: Path to output JSON file
            include_docstrings: Whether to include docstrings (default: False to reduce size)
        """
        cursor = self.conn.cursor()

        # Get all boards
        cursor.execute("SELECT * FROM boards ORDER BY version, port, board")
        boards = []

        for board_row in cursor.fetchall():
            board_dict = dict(board_row)
            board_id = board_dict["id"]

            # Get modules for this board using the new schema
            cursor.execute(
                """
                SELECT um.name FROM unique_modules um
                JOIN board_module_support bms ON um.id = bms.module_id
                WHERE bms.board_id = ?
                ORDER BY um.name
            """,
                (board_id,),
            )

            modules = []
            for module_row in cursor.fetchall():
                module_name = module_row[0]
                modules.append(module_name)

            # Simplify board dict for frontend
            boards.append({
                "version": board_dict["version"],
                "port": board_dict["port"],
                "board": board_dict["board"],
                "modules": modules,
                "module_count": len(modules),
            })

        # Write to JSON
        with open(output_path, "w") as f:
            json.dump({"version": "1.0.0", "boards": boards}, f, indent=2)

    def _get_classes_for_module(self, module_id: int) -> List[Dict]:
        """Get all classes for a module."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM classes WHERE module_id = ?", (module_id,))

        classes = []
        for class_row in cursor.fetchall():
            class_dict = dict(class_row)
            class_dict["methods"] = self._get_methods_for_module(module_id, class_dict["id"])
            classes.append(class_dict)

        return classes

    def _get_methods_for_module(self, module_id: int, class_id: Optional[int]) -> List[Dict]:
        """Get all methods for a module/class."""
        cursor = self.conn.cursor()

        if class_id is None:
            cursor.execute(
                "SELECT * FROM methods WHERE module_id = ? AND class_id IS NULL", (module_id,)
            )
        else:
            cursor.execute(
                "SELECT * FROM methods WHERE module_id = ? AND class_id = ?",
                (module_id, class_id),
            )

        methods = []
        for method_row in cursor.fetchall():
            method_dict = dict(method_row)
            method_dict["parameters"] = self._get_parameters_for_method(method_dict["id"])
            methods.append(method_dict)

        return methods

    def _get_parameters_for_method(self, method_id: int) -> List[Dict]:
        """Get all parameters for a method."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM parameters WHERE method_id = ? ORDER BY position", (method_id,)
        )
        return [dict(row) for row in cursor.fetchall()]

    def export_detailed_to_json(self, output_path: Path):
        """
        Export detailed database to JSON file for advanced frontend features.
        Includes modules, classes, methods, and parameters.
        """
        cursor = self.conn.cursor()

        # Get all boards
        cursor.execute("SELECT * FROM boards ORDER BY version, port, board")
        boards = []

        for board_row in cursor.fetchall():
            board_dict = dict(board_row)
            board_id = board_dict["id"]

            # Get modules for this board with full details
            cursor.execute(
                """
                SELECT m.* FROM modules m
                JOIN board_modules bm ON m.id = bm.module_id
                WHERE bm.board_id = ?
                ORDER BY m.name
            """,
                (board_id,),
            )

            modules = []
            for module_row in cursor.fetchall():
                module_dict = dict(module_row)
                module_id = module_dict["id"]
                
                # Get classes
                cursor.execute("SELECT * FROM classes WHERE module_id = ?", (module_id,))
                classes = []
                for class_row in cursor.fetchall():
                    class_dict = dict(class_row)
                    class_id = class_dict["id"]
                    
                    # Get class methods
                    cursor.execute(
                        "SELECT * FROM methods WHERE module_id = ? AND class_id = ?",
                        (module_id, class_id)
                    )
                    methods = []
                    for method_row in cursor.fetchall():
                        method_dict = dict(method_row)
                        method_id = method_dict["id"]
                        
                        # Get parameters
                        cursor.execute(
                            "SELECT name, type_hint, default_value, is_optional, is_variadic FROM parameters WHERE method_id = ? ORDER BY position",
                            (method_id,)
                        )
                        params = [dict(row) for row in cursor.fetchall()]
                        method_dict["parameters"] = params
                        
                        # Remove internal IDs
                        method_dict.pop("id", None)
                        method_dict.pop("module_id", None)
                        method_dict.pop("class_id", None)
                        methods.append(method_dict)
                    
                    class_dict["methods"] = methods
                    class_dict.pop("id", None)
                    class_dict.pop("module_id", None)
                    classes.append(class_dict)
                
                # Get module-level functions
                cursor.execute(
                    "SELECT * FROM methods WHERE module_id = ? AND class_id IS NULL",
                    (module_id,)
                )
                functions = []
                for func_row in cursor.fetchall():
                    func_dict = dict(func_row)
                    func_id = func_dict["id"]
                    
                    # Get parameters
                    cursor.execute(
                        "SELECT name, type_hint, default_value, is_optional, is_variadic FROM parameters WHERE method_id = ? ORDER BY position",
                        (func_id,)
                    )
                    params = [dict(row) for row in cursor.fetchall()]
                    func_dict["parameters"] = params
                    
                    # Remove internal IDs
                    func_dict.pop("id", None)
                    func_dict.pop("module_id", None)
                    func_dict.pop("class_id", None)
                    functions.append(func_dict)
                
                # Get constants
                cursor.execute(
                    "SELECT name FROM module_constants WHERE module_id = ?",
                    (module_id,)
                )
                constants = [row[0] for row in cursor.fetchall()]
                
                module_dict["classes"] = classes
                module_dict["functions"] = functions
                module_dict["constants"] = constants
                module_dict.pop("id", None)
                modules.append(module_dict)

            board_dict["modules"] = modules
            board_dict.pop("id", None)
            boards.append(board_dict)

        # Write to JSON
        with open(output_path, "w") as f:
            json.dump({"version": "1.0.0", "boards": boards}, f, indent=2)

    def get_board_modules_detailed(self, version: str, port: str, board: str) -> Dict:
        """
        Get detailed module information for a specific board (for API endpoint).
        
        Args:
            version: MicroPython version
            port: Port name
            board: Board name
            
        Returns:
            Dictionary with detailed module information
        """
        cursor = self.conn.cursor()
        
        # Get board
        cursor.execute(
            "SELECT id FROM boards WHERE version = ? AND port = ? AND board = ?",
            (version, port, board)
        )
        result = cursor.fetchone()
        if not result:
            return None
            
        board_id = result[0]
        
        # Get modules for this board with details
        cursor.execute(
            """
            SELECT m.* FROM modules m
            JOIN board_modules bm ON m.id = bm.module_id
            WHERE bm.board_id = ?
            ORDER BY m.name
        """,
            (board_id,),
        )

        modules = []
        for module_row in cursor.fetchall():
            module_dict = dict(module_row)
            module_id = module_dict["id"]
            
            # Get class count
            cursor.execute("SELECT COUNT(*) FROM classes WHERE module_id = ?", (module_id,))
            class_count = cursor.fetchone()[0]
            
            # Get function count
            cursor.execute(
                "SELECT COUNT(*) FROM methods WHERE module_id = ? AND class_id IS NULL",
                (module_id,)
            )
            function_count = cursor.fetchone()[0]
            
            modules.append({
                "name": module_dict["name"],
                "class_count": class_count,
                "function_count": function_count,
            })

        return {
            "version": version,
            "port": port,
            "board": board,
            "modules": modules,
        }

    def clean_version(self, version: str):
        """
        Remove all records for a specific version from the database.
        
        Args:
            version: Version to clean (e.g., 'v1.26.0')
        """
        cursor = self.conn.cursor()
        
        logger.info(f"Cleaning database for version: {version}")
        
        # Get all board IDs for this version
        cursor.execute("SELECT id FROM boards WHERE version = ?", (version,))
        board_ids = [row[0] for row in cursor.fetchall()]
        
        if not board_ids:
            logger.info(f"No boards found for version {version}")
            return
        
        logger.info(f"Found {len(board_ids)} boards for version {version}")
        
        # Convert board IDs to comma-separated string for SQL IN clause
        board_ids_str = ','.join('?' * len(board_ids))
        
        # Delete all board support relationships
        cursor.execute(f"DELETE FROM board_module_support WHERE board_id IN ({board_ids_str})", board_ids)
        cursor.execute(f"DELETE FROM board_class_support WHERE board_id IN ({board_ids_str})", board_ids)
        cursor.execute(f"DELETE FROM board_method_support WHERE board_id IN ({board_ids_str})", board_ids)
        cursor.execute(f"DELETE FROM board_class_attribute_support WHERE board_id IN ({board_ids_str})", board_ids)
        cursor.execute(f"DELETE FROM board_module_constant_support WHERE board_id IN ({board_ids_str})", board_ids)
        
        # Delete boards
        cursor.execute(f"DELETE FROM boards WHERE id IN ({board_ids_str})", board_ids)
        deleted_boards = cursor.rowcount
        logger.info(f"Deleted {deleted_boards} boards for version {version}")
        
        # Clean up orphaned records
        self._cleanup_orphaned_records()
        
        self.conn.commit()
        logger.info(f"Cleanup completed for version {version}")

    def _cleanup_orphaned_records(self):
        """Clean up orphaned records that are no longer referenced by any board."""
        cursor = self.conn.cursor()
        
        # Find and delete orphaned modules
        cursor.execute("""
            DELETE FROM unique_modules 
            WHERE id NOT IN (SELECT DISTINCT module_id FROM board_module_support)
        """)
        deleted_modules = cursor.rowcount
        if deleted_modules > 0:
            logger.info(f"Deleted {deleted_modules} orphaned modules")
        
        # Find and delete orphaned classes
        cursor.execute("""
            DELETE FROM unique_classes 
            WHERE id NOT IN (SELECT DISTINCT class_id FROM board_class_support)
        """)
        deleted_classes = cursor.rowcount
        if deleted_classes > 0:
            logger.info(f"Deleted {deleted_classes} orphaned classes")
        
        # Find and delete orphaned methods
        cursor.execute("""
            DELETE FROM unique_methods 
            WHERE id NOT IN (SELECT DISTINCT method_id FROM board_method_support)
        """)
        deleted_methods = cursor.rowcount
        if deleted_methods > 0:
            logger.info(f"Deleted {deleted_methods} orphaned methods")
        
        # Delete parameters for orphaned methods
        cursor.execute("""
            DELETE FROM unique_parameters 
            WHERE method_id NOT IN (SELECT DISTINCT id FROM unique_methods)
        """)
        deleted_params = cursor.rowcount
        if deleted_params > 0:
            logger.info(f"Deleted {deleted_params} orphaned parameters")
        
        # Delete orphaned class attributes
        cursor.execute("""
            DELETE FROM unique_class_attributes 
            WHERE id NOT IN (SELECT DISTINCT attribute_id FROM board_class_attribute_support)
        """)
        deleted_attrs = cursor.rowcount
        if deleted_attrs > 0:
            logger.info(f"Deleted {deleted_attrs} orphaned class attributes")
        
        # Delete orphaned module constants
        cursor.execute("""
            DELETE FROM unique_module_constants 
            WHERE id NOT IN (SELECT DISTINCT constant_id FROM board_module_constant_support)
        """)
        deleted_constants = cursor.rowcount
        if deleted_constants > 0:
            logger.info(f"Deleted {deleted_constants} orphaned module constants")
        
        # Delete orphaned class bases (these should be cleaned up based on class existence)
        cursor.execute("""
            DELETE FROM unique_class_bases 
            WHERE class_id NOT IN (SELECT DISTINCT id FROM unique_classes)
        """)
        deleted_bases = cursor.rowcount
        if deleted_bases > 0:
            logger.info(f"Deleted {deleted_bases} orphaned class bases")

    def list_versions(self):
        """List all versions currently in the database."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT version FROM boards ORDER BY version")
        versions = [row[0] for row in cursor.fetchall()]
        
        if versions:
            logger.info(f"Versions currently in database: {versions}")
            
            # Show board counts per version
            for version in versions:
                cursor.execute("SELECT COUNT(*) FROM boards WHERE version = ?", (version,))
                count = cursor.fetchone()[0]
                logger.info(f"  {version}: {count} boards")
        else:
            logger.info("No versions found in database")
        
        return versions

    def reset_database(self):
        """Completely reset the database by dropping and recreating all tables."""
        cursor = self.conn.cursor()
        
        logger.info("Resetting entire database...")
        
        # Drop view first
        cursor.execute("DROP VIEW IF EXISTS methods_with_board_support")
        
        # Drop all tables in reverse order of dependencies
        tables = [
            'unique_parameters', 'board_method_support', 'board_class_attribute_support',
            'board_module_constant_support', 'board_class_support', 'board_module_support',
            'unique_methods', 'unique_class_attributes', 'unique_class_bases', 
            'unique_module_constants', 'unique_classes', 'unique_modules', 'boards'
        ]
        
        for table in tables:
            cursor.execute(f"DROP TABLE IF EXISTS {table}")
            logger.info(f"Dropped table: {table}")
        
        # Drop indexes
        indexes = [
            'idx_boards_version', 'idx_unique_modules_signature', 'idx_unique_modules_name',
            'idx_unique_classes_signature', 'idx_unique_classes_module',
            'idx_unique_methods_signature', 'idx_unique_methods_module', 
            'idx_unique_methods_class', 'idx_unique_methods_name',
            'idx_board_method_support_method', 'idx_board_method_support_board'
        ]
        
        for index in indexes:
            cursor.execute(f"DROP INDEX IF EXISTS {index}")
        
        self.conn.commit()
        logger.info("Database reset complete")
        
        # Recreate schema
        self.create_schema()
        logger.info("Database schema recreated")

def normalize_version_for_directory(version: str) -> str:
    """
    Normalize version format for directory matching.
    
    Args:
        version: Version in format like 'v1.26.0', '1.26.0', or 'v1_26_0'
        
    Returns:
        Version in directory format like 'v1_26_0'
    """
    # Remove 'v' prefix if present
    if version.startswith('v'):
        version = version[1:]
    
    # Replace dots with underscores
    version = version.replace('.', '_')
    
    # Add 'v' prefix back
    return f'v{version}'

def normalize_version_for_display(version: str) -> str:
    """
    Normalize version format for display and database storage.
    
    Args:
        version: Version in format like 'v1_26_0', 'v1.26.0', or '1.26.0'
        
    Returns:
        Version in display format like 'v1.26.0'
    """
    # Remove 'v' prefix if present
    if version.startswith('v'):
        version = version[1:]
    
    # Replace underscores with dots
    version = version.replace('_', '.')
    
    # Add 'v' prefix back
    return f'v{version}'

def build_database_for_version(
    publish_dir: Path, version: str, db_path: Path, json_path: Optional[Path] = None, detailed_json_path: Optional[Path] = None, no_clean: bool = False, clean_only: bool = False, reset_db: bool = False, list_versions: bool = False
):
    """
    Build a database for all boards of a specific MicroPython version.

    Args:
        publish_dir: Path to the publish directory
        version: MicroPython version (e.g., 'v1.26.0', '1.26.0', or 'v1_26_0')
        db_path: Path to output SQLite database
        json_path: Optional path to output simplified JSON file
        detailed_json_path: Optional path to output detailed JSON file with full data
        no_clean: Whether to skip cleaning existing records for this version (default: False, meaning clean by default)
        clean_only: Whether to only clean (don't process any stubs)
        reset_db: Whether to completely reset the database (removes ALL data)
        list_versions: Whether to list all versions currently in the database
    """
    builder = DatabaseBuilder(db_path)
    builder.connect()
    builder.create_schema()

    # List versions if requested
    if list_versions:
        builder.list_versions()
        if not (clean_only or reset_db):
            builder.close()
            return

    # Reset entire database if requested
    if reset_db:
        builder.reset_database()
        if not clean_only:
            logger.info("Database reset complete. Use without --reset-db to add data.")
        builder.close()
        return

    # Normalize version for directory pattern matching
    directory_version = normalize_version_for_directory(version)
    display_version = normalize_version_for_display(version)
    
    logger.info(f"Input version: {version}")
    logger.info(f"Directory pattern version: {directory_version}")
    logger.info(f"Display/storage version: {display_version}")

    # Show current versions before cleaning
    builder.list_versions()

    # Clean existing data by default (unless --no-clean specified)
    should_clean = not no_clean or clean_only
    if should_clean:
        logger.info(f"Cleaning existing data for version '{display_version}' (use --no-clean to skip)")
        builder.clean_version(display_version)
        
        # Show what's left after cleaning
        logger.info("After cleaning:")
        builder.list_versions()
    else:
        logger.warning("Skipping clean - this may result in duplicate methods/functions!")

    # If clean-only, stop here
    if clean_only:
        logger.info("Clean-only mode: skipping stub processing")
        builder.close()
        return

    # Find all stub directories for this version
    pattern = f"micropython-{directory_version}-*-stubs"
    stub_dirs = sorted(publish_dir.glob(pattern))

    logger.info(f"Found {len(stub_dirs)} stub directories for version {directory_version}")

    if not stub_dirs:
        logger.warning(f"No stub directories found matching pattern: {pattern}")
        logger.warning("Please check that --publish-dir points to the correct location")

    for stub_dir in stub_dirs:
        # Parse directory name to extract port and board
        # Format: micropython-v1_26_0-port-board-stubs
        parts = stub_dir.name.split("-")
        if len(parts) >= 4:
            port = parts[2]
            board = "-".join(parts[3:-1])  # Everything between port and "stubs"
            
            # Use the normalized display version for database storage
            logger.info(f"Processing {port}/{board} (version: {display_version})...")

            try:
                board_data = scan_board_stubs(stub_dir, display_version, port, board)
                builder.add_board(board_data)
                logger.info(
                    f"  Added {len(board_data['modules'])} modules for {port}/{board}"
                )
            except Exception as e:
                logger.error(f"  Error processing {stub_dir}: {e}")

    if json_path:
        logger.info(f"Exporting simplified JSON to: {json_path}")
        builder.export_to_json(json_path)
    
    if detailed_json_path:
        logger.info(f"Exporting detailed JSON to: {detailed_json_path}")
        builder.export_detailed_to_json(detailed_json_path)

    builder.close()
    logger.info(f"Database created at {db_path}")


if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description="Build MicroPython board comparison database",
        epilog="Version can be specified as v1.26.0, 1.26.0, or v1_26_0. By default, existing data for the version is cleaned before building."
    )
    parser.add_argument(
        "--publish-dir",
        type=Path,
        default=Path(__file__).parent.parent.parent / "publish",
        help="Path to publish directory containing micropython-*-stubs folders",
    )
    parser.add_argument(
        "--version",
        type=str,
        default="v1.26.0",
        help="MicroPython version to process (e.g., v1.26.0, 1.26.0, or v1_26_0)",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=Path(__file__).parent / "board_comparison.db",
        help="Output database path",
    )
    parser.add_argument(
        "--json", type=Path, help="Optional JSON output path for frontend (simplified)"
    )
    parser.add_argument(
        "--detailed-json", type=Path, help="Optional detailed JSON output path with full module/class/method info"
    )
    parser.add_argument(
        "--no-clean",
        action="store_true",
        help="Skip cleaning existing records for this version (WARNING: may create duplicates)"
    )
    parser.add_argument(
        "--clean-only",
        action="store_true",
        help="Only clean the database for this version (don't process any stubs)"
    )
    parser.add_argument(
        "--reset-db",
        action="store_true",
        help="Completely reset the database (removes ALL data for ALL versions)"
    )
    parser.add_argument(
        "--list-versions",
        action="store_true",
        help="List all versions currently in the database"
    )

    args = parser.parse_args()

    build_database_for_version(args.publish_dir, args.version, args.db, args.json, args.detailed_json, args.no_clean, args.clean_only, args.reset_db, args.list_versions)
