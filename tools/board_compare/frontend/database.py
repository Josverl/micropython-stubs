"""
Database operations, application state management, and board utilities.
Consolidates all database-related functionality for the MicroPython Board Explorer.
"""

import asyncio
from pyscript import document, ffi, window
from sqlite_wasm import SQLDatabase, SQLExecResult, SQLExecResults, SQLite


# Global application state
app_state = {
    "SQL": None,
    "db": None,
    "boards": [],
    "current_board": None,
}

# Global comparison state
comparison_data = {
    "board1": None,
    "board2": None,
    "modules1": [],
    "modules2": [],
}

# MicroPython deprecated u-modules
U_MODULES = [
    "array",
    "asyncio",
    "binascii",
    "bluetooth",
    "cryptolib",
    "errno",
    "hashlib",
    "heapq",
    "io",
    "json",
    "machine",
    "os",
    "platform",
    "random",
    "re",
    "select",
    "ssl",
    "struct",
    "socket",
    "sys",
    "time",
    "websocket",
    "zlib",
]


# === BOARD UTILITY FUNCTIONS ===
# Consolidated from board_utils.py and main.py to eliminate duplication

def format_board_name(port, board):
    """Format board display name consistently."""
    if not board or board == "":
        return port.rstrip("-")
    # FIXME: Is too port specific
    if board.startswith("esp-"):
        return board[4:]  # Remove "esp-" prefix
    return board


def find_board_in_list(boards, version, board_name):
    """
    Find a board in the list matching version and formatted name.
    Returns tuple (port, board) or None if not found.
    """
    for b in boards:
        if b["version"] == version:
            formatted = format_board_name(b["port"], b["board"])
            if formatted == board_name:
                return (b["port"], b["board"])
    return None


def get_icon_class(entity_type):
    """Get Font Awesome icon class for different entity types."""
    icons = {
        "module": "fas fa-cube",
        "class": "fas fa-object-group",
        "function": "fas fa-bolt",
        "method": "fas fa-bolt",
        "property": "fas fa-ellipsis",
        "constant": "fas fa-circle",
        "variable": "fas fa-circle-dot",
        "attribute": "fas fa-tag",
        "parameter": "fas fa-list",
    }
    return icons.get(entity_type, "fas fa-cube")


# === DATABASE INITIALIZATION ===

async def load_database():
    """Load SQLite database using SQL.js."""
    try:
        window.console.log("SQLite.initialize ...")
        SQL = await SQLite.initialize(version="1.13.0", cdn="cdnjs")
        window.console.log("SQLite-wasm wrapper created")
        app_state["SQL"] = SQL
        window.console.log("Loading database...")
        await asyncio.sleep(0.1)  # Allow UI update
        window.console.log("Opening database 'board_comparison.db'...")
        app_state["db"] = await SQL.open_database_url("board_comparison.db")
        await asyncio.sleep(0.1)  # Allow UI update
        window.console.log("Database loaded successfully!")

        # Test database connection
        stmt = app_state["db"].prepare("SELECT COUNT(*) as count FROM boards")
        stmt.step()
        row = stmt.getAsObject()
        stmt.free()

        board_count = row["count"]
        window.console.log(f"Database ready! Found {board_count} boards.")

        return True

    except Exception as e:
        window.console.log(f"Error loading database: {str(e)}")
        print(f"Database error: {e}")
        return False


async def load_board_list_from_db():
    """Load board list from database."""
    if not app_state["db"]:
        return False

    try:
        window.console.log("Loading board list from database...")

        stmt = app_state["db"].prepare("""
            SELECT DISTINCT version, port, board
            FROM boards
            ORDER BY version DESC, port, board
        """)

        boards = []
        while stmt.step():
            row = stmt.getAsObject()
            boards.append({"version": row["version"], "port": row["port"], "board": row["board"]})

        stmt.free()

        app_state["boards"] = boards
        window.console.log(f"Loaded {len(boards)} boards from database")

        return True

    except Exception as e:
        window.console.log(f"Error loading board list: {str(e)}")
        print(f"Board list error: {e}")
        return False


# === DATABASE QUERY FUNCTIONS ===

def get_class_bases(class_id):
    """Get base classes for a class."""
    if not app_state["db"]:
        return []

    try:
        stmt = app_state["db"].prepare("""
            SELECT ucb.base_name
            FROM unique_class_bases ucb
            WHERE ucb.class_id = ?
            ORDER BY ucb.base_name
        """)
        stmt.bind(ffi.to_js([class_id]))

        bases = []
        while stmt.step():
            row = stmt.getAsObject()
            bases.append(row["base_name"])

        stmt.free()
        return bases
    except Exception as e:
        print(f"Error getting base classes: {e}")
        return []


def get_method_parameters(method_id):
    """Get parameters for a method/function."""
    if not app_state["db"]:
        return []

    try:
        stmt = app_state["db"].prepare("""
            SELECT up.name, up.position, up.type_hint, up.default_value, 
                    up.is_optional, up.is_variadic
            FROM unique_parameters up
            WHERE up.method_id = ?
            ORDER BY up.position
        """)
        stmt.bind(ffi.to_js([method_id]))

        params = []
        while stmt.step():
            row = stmt.getAsObject()
            params.append(
                {
                    "name": row["name"],
                    "position": row["position"],
                    "type_hint": row["type_hint"],
                    "default_value": row["default_value"],
                    "is_optional": row["is_optional"],
                    "is_variadic": row["is_variadic"],
                }
            )

        stmt.free()
        return params
    except Exception as e:
        print(f"Error getting parameters: {e}")
        return []


def get_class_methods(module_id, class_id, board_context):
    """Get methods for a class."""
    if not app_state["db"]:
        return []

    try:
        stmt = app_state["db"].prepare("""
            SELECT um.id, um.name, um.return_type, um.is_async, um.is_property, 
                    um.is_classmethod, um.is_staticmethod, um.decorators, um.docstring
            FROM unique_methods um
            JOIN board_method_support bms ON um.id = bms.method_id
            JOIN boards b ON bms.board_id = b.id
            WHERE um.module_id = ? AND um.class_id = ?
                AND b.version = ? AND b.port = ? AND b.board = ?
            ORDER BY um.name
        """)
        stmt.bind(
            ffi.to_js(
                [
                    module_id,
                    class_id,
                    board_context["version"],
                    board_context["port"],
                    board_context["board"],
                ]
            )
        )

        methods = []
        while stmt.step():
            row = stmt.getAsObject()
            method_id = row["id"]

            # Get parameters
            parameters = get_method_parameters(method_id)

            # Parse decorators
            decorators_list = []
            if row["decorators"]:
                try:
                    import js
                    decorators_list = js.JSON.parse(row["decorators"])
                except Exception:
                    pass

            methods.append(
                {
                    "id": method_id,
                    "name": row["name"],
                    "return_type": row["return_type"],
                    "is_async": row["is_async"],
                    "is_property": row["is_property"],
                    "is_classmethod": row["is_classmethod"],
                    "is_staticmethod": row["is_staticmethod"],
                    "decorators_list": decorators_list,
                    "parameters": parameters,
                    "docstring": row["docstring"],
                }
            )

        stmt.free()
        return methods
    except Exception as e:
        print(f"Error getting class methods: {e}")
        return []


def get_class_attributes(class_id):
    """Get attributes for a class."""
    if not app_state["db"]:
        return []

    try:
        stmt = app_state["db"].prepare("""
            SELECT uca.name, uca.type_hint, uca.value
            FROM unique_class_attributes uca
            WHERE uca.class_id = ? AND (uca.is_hidden = 0 OR uca.is_hidden IS NULL)
            ORDER BY uca.name
        """)
        stmt.bind(ffi.to_js([class_id]))

        attributes = []
        while stmt.step():
            row = stmt.getAsObject()
            attributes.append({"name": row["name"], "type_hint": row["type_hint"], "value": row["value"]})

        stmt.free()
        return attributes
    except Exception as e:
        print(f"Error getting class attributes: {e}")
        return []


def get_module_classes(module_id, board_context):
    """Get classes for a module."""
    if not app_state["db"]:
        return []

    try:
        stmt = app_state["db"].prepare("""
            SELECT uc.id, uc.name, uc.docstring
            FROM unique_classes uc
            WHERE uc.module_id = ?
            ORDER BY uc.name
        """)
        stmt.bind(ffi.to_js([module_id]))

        classes = []
        while stmt.step():
            row = stmt.getAsObject()
            class_id = row["id"]

            # Get base classes
            base_classes = get_class_bases(class_id)

            # Get methods
            methods = get_class_methods(module_id, class_id, board_context)

            # Get attributes
            attributes = get_class_attributes(class_id)

            classes.append(
                {
                    "id": class_id,
                    "name": row["name"],
                    "docstring": row["docstring"],
                    "base_classes": base_classes,
                    "methods": methods,
                    "attributes": attributes,
                }
            )

        stmt.free()
        return classes
    except Exception as e:
        print(f"Error getting module classes: {e}")
        return []


def get_module_functions(module_id, board_context):
    """Get module-level functions."""
    if not app_state["db"]:
        return []

    try:
        stmt = app_state["db"].prepare("""
            SELECT um.id, um.name, um.return_type, um.is_async, um.decorators, um.docstring
            FROM unique_methods um
            JOIN board_method_support bms ON um.id = bms.method_id
            JOIN boards b ON bms.board_id = b.id
            WHERE um.module_id = ? AND um.class_id IS NULL
                AND b.version = ? AND b.port = ? AND b.board = ?
            ORDER BY um.name
        """)
        stmt.bind(
            ffi.to_js(
                [
                    module_id,
                    board_context["version"],
                    board_context["port"],
                    board_context["board"],
                ]
            )
        )

        functions = []
        while stmt.step():
            row = stmt.getAsObject()
            func_id = row["id"]

            # Get parameters
            parameters = get_method_parameters(func_id)

            # Parse decorators
            decorators_list = []
            if row["decorators"]:
                try:
                    import js
                    decorators_list = js.JSON.parse(row["decorators"])
                except Exception:
                    pass

            functions.append(
                {
                    "id": func_id,
                    "name": row["name"],
                    "return_type": row["return_type"],
                    "is_async": row["is_async"],
                    "decorators_list": decorators_list,
                    "parameters": parameters,
                    "docstring": row["docstring"],
                }
            )

        stmt.free()
        return functions
    except Exception as e:
        print(f"Error getting module functions: {e}")
        return []


def get_module_constants(module_id):
    """Get module constants."""
    if not app_state["db"]:
        return []

    try:
        stmt = app_state["db"].prepare("""
            SELECT umc.name, umc.value, umc.type_hint
            FROM unique_module_constants umc
            WHERE umc.module_id = ?
            ORDER BY umc.name
        """)
        stmt.bind(ffi.to_js([module_id]))

        constants = []
        while stmt.step():
            row = stmt.getAsObject()
            constants.append({"name": row["name"], "value": row["value"], "type": row["type"]})

        stmt.free()
        return constants
    except Exception as e:
        print(f"Error getting constants: {e}")
        return []


def get_board_modules(board_info):
    """Get detailed module information for a board (for comparison purposes)."""
    if not app_state["db"]:
        return []

    try:
        version, port, board = board_info["version"], board_info["port"], board_info["board"]

        # Query database for modules
        stmt = app_state["db"].prepare("""
            SELECT um.id, um.name, um.docstring 
            FROM unique_modules um
            JOIN board_module_support bms ON um.id = bms.module_id
            JOIN boards b ON bms.board_id = b.id
            WHERE b.version = ? AND b.port = ? AND b.board = ?
            ORDER BY um.name
        """)

        stmt.bind(ffi.to_js([version, port, board]))

        modules = []
        board_context = {"version": version, "port": port, "board": board}

        while stmt.step():
            row = stmt.getAsObject()
            module_id = row["id"]

            # Get classes with full details
            classes = get_module_classes(module_id, board_context)

            # Get functions with full details
            functions = get_module_functions(module_id, board_context)

            # Get constants
            constants = get_module_constants(module_id)

            modules.append(
                {
                    "id": module_id,
                    "name": row["name"],
                    "docstring": row["docstring"],
                    "classes": classes,
                    "functions": functions,
                    "constants": constants,
                }
            )

        stmt.free()
        return modules

    except Exception as e:
        print(f"Error getting board modules: {e}")
        return []


# === SEARCH-SPECIFIC DATABASE QUERIES ===

def get_basic_class_info_for_search(class_id, board_context):
    """Get basic class info (name, base classes) without all methods - for search results."""
    if not app_state["db"]:
        return None
    
    try:
        # Get basic class info
        stmt = app_state["db"].prepare("""
            SELECT uc.id, uc.name, uc.docstring
            FROM unique_classes uc
            WHERE uc.id = ?
        """)
        stmt.bind(ffi.to_js([class_id]))
        
        if not stmt.step():
            stmt.free()
            return None
            
        row = stmt.getAsObject()
        class_name = row["name"]
        class_docstring = row["docstring"]
        stmt.free()
        
        # Get base classes
        base_classes = get_class_bases(class_id)
        
        result = {
            "id": class_id,
            "name": class_name,
            "docstring": class_docstring,
            "base_classes": base_classes,
            "methods": [],  # Will be populated by caller with search results
            "attributes": [],  # Will be populated by caller with search results
        }
        
        return result
        
    except Exception as e:
        print(f"ERROR: Getting basic class {class_id}: {e}")
        return None


def get_complete_class_for_search(class_id, board_context):
    """Get complete class definition for search results."""
    if not app_state["db"]:
        return None
    
    try:
        # Get basic class info
        stmt = app_state["db"].prepare("""
            SELECT uc.id, uc.name, uc.docstring
            FROM unique_classes uc
            WHERE uc.id = ?
        """)
        stmt.bind(ffi.to_js([class_id]))
        
        if not stmt.step():
            stmt.free()
            return None
            
        row = stmt.getAsObject()
        class_name = row["name"]
        class_docstring = row["docstring"]
        stmt.free()
        
        # Get base classes
        base_classes = get_class_bases(class_id)
        
        # Get methods using existing function
        methods = get_class_methods(board_context["module_id"], class_id, board_context)
        
        # Get attributes using existing function  
        attributes = get_class_attributes(class_id)
        
        result = {
            "id": class_id,
            "name": class_name,
            "docstring": class_docstring,
            "base_classes": base_classes,
            "methods": methods,
            "attributes": attributes,
        }
        
        return result
        
    except Exception as e:
        print(f"Error getting complete class {class_id}: {e}")
        return None


# === SEARCH HELPER FUNCTIONS ===

def get_search_result_classes(module_id, parent_result):
    """Get classes for a module in search result format."""
    classes = []
    stmt = app_state["db"].prepare("SELECT id, name FROM unique_classes WHERE module_id = ?")
    stmt.bind(ffi.to_js([int(module_id)]))
    
    while stmt.step():
        class_data = stmt.getAsObject()
        # Create new dict without spread operator for PyScript compatibility
        class_result = dict(parent_result)  # Copy parent data
        class_result.update({
            "entity_type": "class",
            "entity_name": class_data["name"],
            "class_id": class_data["id"],
        })
        classes.append(class_result)
    
    stmt.free()
    return classes


def get_search_result_constants(module_id, parent_result):
    """Get constants for a module in search result format."""
    constants = []
    stmt = app_state["db"].prepare("SELECT id, name FROM unique_module_constants WHERE module_id = ?")
    stmt.bind(ffi.to_js([int(module_id)]))
    
    while stmt.step():
        const_data = stmt.getAsObject()
        # Create new dict without spread operator for PyScript compatibility
        const_result = dict(parent_result)  # Copy parent data
        const_result.update({
            "entity_type": "constant",
            "entity_name": const_data["name"], 
            "constant_id": const_data["id"],
        })
        constants.append(const_result)
    
    stmt.free()
    return constants


def get_search_result_methods(class_id, parent_result):
    """Get methods for a class in search result format."""
    methods = []
    stmt = app_state["db"].prepare("SELECT id, name FROM unique_methods WHERE class_id = ?")
    stmt.bind(ffi.to_js([int(class_id)]))
    
    while stmt.step():
        method_data = stmt.getAsObject()
        # Create new dict without spread operator for PyScript compatibility
        method_result = dict(parent_result)  # Copy parent data
        method_result.update({
            "entity_type": "method",
            "entity_name": method_data["name"],
            "method_id": method_data["id"],
        })
        methods.append(method_result)
    
    stmt.free()  
    return methods


def get_search_result_attributes(class_id, parent_result):
    """Get attributes for a class in search result format."""
    attributes = []
    stmt = app_state["db"].prepare("SELECT id, name FROM unique_class_attributes WHERE class_id = ?")
    stmt.bind(ffi.to_js([int(class_id)]))
    
    while stmt.step():
        attr_data = stmt.getAsObject()
        # Create new dict without spread operator for PyScript compatibility
        attr_result = dict(parent_result)  # Copy parent data
        attr_result.update({
            "entity_type": "attribute",
            "entity_name": attr_data["name"],
            "attribute_id": attr_data["id"],
        })
        attributes.append(attr_result)
    
    stmt.free()
    return attributes