"""
Database builder tool to create and populate the SQLite database.

This tool scans published stubs for MicroPython boards and builds a normalized
database for comparison.
"""

import sqlite3
import json
from pathlib import Path
from typing import List, Dict, Optional
import logging
import re

from models import Board, Module, Class, Method, Parameter
from scan_stubs import scan_board_stubs

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatabaseBuilder:
    """Builds and populates the board comparison database."""

    def __init__(self, db_path: Path):
        """
        Initialize the database builder.

        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = Path(db_path)
        self.conn: Optional[sqlite3.Connection] = None

    def create_schema(self):
        """Create the database schema."""
        cursor = self.conn.cursor()

        # Boards table
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

        # Modules table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS modules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                docstring TEXT
            )
        """
        )

        # Board-Module relationship
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS board_modules (
                board_id INTEGER,
                module_id INTEGER,
                PRIMARY KEY (board_id, module_id),
                FOREIGN KEY (board_id) REFERENCES boards(id),
                FOREIGN KEY (module_id) REFERENCES modules(id)
            )
        """
        )

        # Classes table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS classes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                module_id INTEGER,
                name TEXT NOT NULL,
                docstring TEXT,
                FOREIGN KEY (module_id) REFERENCES modules(id),
                UNIQUE(module_id, name)
            )
        """
        )

        # Base classes relationship
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS class_bases (
                class_id INTEGER,
                base_name TEXT,
                FOREIGN KEY (class_id) REFERENCES classes(id)
            )
        """
        )

        # Class attributes
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS class_attributes (
                class_id INTEGER,
                name TEXT,
                FOREIGN KEY (class_id) REFERENCES classes(id)
            )
        """
        )

        # Methods/Functions table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS methods (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                module_id INTEGER,
                class_id INTEGER,
                name TEXT NOT NULL,
                return_type TEXT,
                is_async BOOLEAN,
                is_classmethod BOOLEAN,
                is_staticmethod BOOLEAN,
                is_property BOOLEAN,
                overloads INTEGER DEFAULT 0,
                docstring TEXT,
                FOREIGN KEY (module_id) REFERENCES modules(id),
                FOREIGN KEY (class_id) REFERENCES classes(id)
            )
        """
        )

        # Parameters table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS parameters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                method_id INTEGER,
                name TEXT NOT NULL,
                position INTEGER,
                type_hint TEXT,
                default_value TEXT,
                is_optional BOOLEAN,
                is_variadic BOOLEAN,
                FOREIGN KEY (method_id) REFERENCES methods(id)
            )
        """
        )

        # Module constants
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS module_constants (
                module_id INTEGER,
                name TEXT,
                FOREIGN KEY (module_id) REFERENCES modules(id)
            )
        """
        )

        # Create indexes for better query performance
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_boards_version ON boards(version)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_modules_name ON modules(name)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_classes_name ON classes(name)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_methods_name ON methods(name)")

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
        Add a board and its modules to the database.

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
        """Add a module and its contents to the database."""
        cursor = self.conn.cursor()

        # Insert or get module
        cursor.execute(
            """
            INSERT OR IGNORE INTO modules (name, docstring)
            VALUES (?, ?)
        """,
            (module_data["name"], module_data.get("docstring")),
        )

        cursor.execute("SELECT id FROM modules WHERE name = ?", (module_data["name"],))
        module_id = cursor.fetchone()[0]

        # Link board to module
        cursor.execute(
            """
            INSERT OR IGNORE INTO board_modules (board_id, module_id)
            VALUES (?, ?)
        """,
            (board_id, module_id),
        )

        # Add constants
        for const in module_data.get("constants", []):
            cursor.execute(
                """
                INSERT OR IGNORE INTO module_constants (module_id, name)
                VALUES (?, ?)
            """,
                (module_id, const),
            )

        # Add classes
        for class_data in module_data.get("classes", []):
            self._add_class(module_id, class_data)

        # Add module-level functions
        for func_data in module_data.get("functions", []):
            self._add_method(module_id, None, func_data)

    def _add_class(self, module_id: int, class_data: Dict):
        """Add a class and its contents to the database."""
        cursor = self.conn.cursor()

        # Insert or get class
        cursor.execute(
            """
            INSERT OR IGNORE INTO classes (module_id, name, docstring)
            VALUES (?, ?, ?)
        """,
            (module_id, class_data["name"], class_data.get("docstring")),
        )

        cursor.execute(
            "SELECT id FROM classes WHERE module_id = ? AND name = ?",
            (module_id, class_data["name"]),
        )
        class_id = cursor.fetchone()[0]

        # Add base classes
        for base in class_data.get("base_classes", []):
            cursor.execute(
                """
                INSERT OR IGNORE INTO class_bases (class_id, base_name)
                VALUES (?, ?)
            """,
                (class_id, base),
            )

        # Add attributes
        for attr in class_data.get("attributes", []):
            cursor.execute(
                """
                INSERT OR IGNORE INTO class_attributes (class_id, name)
                VALUES (?, ?)
            """,
                (class_id, attr),
            )

        # Add methods
        for method_data in class_data.get("methods", []):
            self._add_method(module_id, class_id, method_data)

    def _add_method(self, module_id: int, class_id: Optional[int], method_data: Dict):
        """Add a method/function to the database."""
        cursor = self.conn.cursor()

        cursor.execute(
            """
            INSERT INTO methods (
                module_id, class_id, name, return_type, is_async,
                is_classmethod, is_staticmethod, is_property, overloads, docstring
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
            ),
        )

        method_id = cursor.lastrowid

        # Add parameters
        for i, param_data in enumerate(method_data.get("parameters", [])):
            cursor.execute(
                """
                INSERT INTO parameters (
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

            # Get modules for this board
            cursor.execute(
                """
                SELECT m.name FROM modules m
                JOIN board_modules bm ON m.id = bm.module_id
                WHERE bm.board_id = ?
                ORDER BY m.name
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


def build_database_for_version(
    publish_dir: Path, version: str, db_path: Path, json_path: Optional[Path] = None
):
    """
    Build a database for all boards of a specific MicroPython version.

    Args:
        publish_dir: Path to the publish directory
        version: MicroPython version (e.g., 'v1_26_0')
        db_path: Path to output SQLite database
        json_path: Optional path to output JSON file
    """
    builder = DatabaseBuilder(db_path)
    builder.connect()
    builder.create_schema()

    # Find all stub directories for this version
    pattern = f"micropython-{version}-*-stubs"
    stub_dirs = sorted(publish_dir.glob(pattern))

    logger.info(f"Found {len(stub_dirs)} stub directories for version {version}")

    for stub_dir in stub_dirs:
        # Parse directory name to extract port and board
        # Format: micropython-v1_26_0-port-board-stubs
        parts = stub_dir.name.split("-")
        if len(parts) >= 4:
            version_str = parts[1]
            port = parts[2]
            board = "-".join(parts[3:-1])  # Everything between port and "stubs"

            logger.info(f"Processing {port}/{board}...")

            try:
                board_data = scan_board_stubs(stub_dir, version_str, port, board)
                builder.add_board(board_data)
                logger.info(
                    f"  Added {len(board_data['modules'])} modules for {port}/{board}"
                )
            except Exception as e:
                logger.error(f"  Error processing {stub_dir}: {e}")

    if json_path:
        logger.info(f"Exporting to JSON: {json_path}")
        builder.export_to_json(json_path)

    builder.close()
    logger.info(f"Database created at {db_path}")


if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(description="Build MicroPython board comparison database")
    parser.add_argument(
        "--publish-dir",
        type=Path,
        default=Path(__file__).parent.parent.parent / "publish",
        help="Path to publish directory",
    )
    parser.add_argument(
        "--version",
        type=str,
        default="v1_26_0",
        help="MicroPython version to process (e.g., v1_26_0)",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=Path(__file__).parent / "board_comparison.db",
        help="Output database path",
    )
    parser.add_argument(
        "--json", type=Path, help="Optional JSON output path for frontend"
    )

    args = parser.parse_args()

    build_database_for_version(args.publish_dir, args.version, args.db, args.json)
