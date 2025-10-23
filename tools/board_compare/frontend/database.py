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
    """Get detailed module information for a board using bulk queries to avoid N+1 problem.
    
    Strategy:
    1. Fetch all modules for board (1 query)
    2. Fetch ALL classes for board in bulk (1 query instead of N)
    3. Fetch ALL functions for board in bulk (1 query instead of N)
    4. Fetch ALL constants for board in bulk (1 query instead of N)
    5. Assemble hierarchy in memory
    
    This reduces queries from ~1,200+ to just 4 for a typical board with 100 modules.
    """
    if not app_state["db"]:
        return []

    try:
        version, port, board = board_info["version"], board_info["port"], board_info["board"]

        # Step 1: Get all modules for this board (using v_board_modules view)
        stmt = app_state["db"].prepare("""
            SELECT DISTINCT module_id, module_name, module_docstring
            FROM v_board_modules
            WHERE version = ? AND port = ? AND board = ?
            ORDER BY module_name
        """)
        stmt.bind(ffi.to_js([version, port, board]))

        # Build modules dict {module_id: module_data}
        modules_dict = {}
        while stmt.step():
            row = stmt.getAsObject()
            module_id = row["module_id"]
            modules_dict[module_id] = {
                "id": module_id,
                "name": row["module_name"],
                "docstring": row["module_docstring"],
                "classes": {},  # Will be dict first, then converted to list
                "functions": [],
                "constants": [],
            }
        stmt.free()

        if not modules_dict:
            return []

        # Step 2: Bulk fetch ALL classes for this board
        stmt = app_state["db"].prepare("""
            SELECT DISTINCT class_id, class_name, class_docstring, module_id, base_classes
            FROM v_module_classes
            WHERE version = ? AND port = ? AND board = ?
            ORDER BY class_name
        """)
        stmt.bind(ffi.to_js([version, port, board]))

        # Build classes dict {(module_id, class_id): class_data}
        classes_dict = {}
        while stmt.step():
            row = stmt.getAsObject()
            module_id = row["module_id"]
            class_id = row["class_id"]
            
            if module_id not in modules_dict:
                continue  # Skip classes for modules not in this board
            
            # Parse base_classes string
            base_classes_list = []
            if row["base_classes"]:
                base_classes_list = [b.strip() for b in row["base_classes"].split(",")]
            
            class_data = {
                "id": class_id,
                "name": row["class_name"],
                "docstring": row["class_docstring"],
                "base_classes": base_classes_list,
                "methods": [],
                "attributes": [],
            }
            
            modules_dict[module_id]["classes"][class_id] = class_data
            classes_dict[(module_id, class_id)] = class_data

        stmt.free()

        # Step 3: Bulk fetch ALL methods for this board
        stmt = app_state["db"].prepare("""
            SELECT method_id, method_name, docstring, return_type, 
                   is_async, decorators, module_id, class_id
            FROM v_class_methods
            WHERE version = ? AND port = ? AND board = ?
            ORDER BY method_name
        """)
        stmt.bind(ffi.to_js([version, port, board]))

        # Build methods dict to collect method IDs
        methods_dict = {}  # {method_id: method_data}
        method_to_location = {}  # {method_id: (module_id, class_id)}
        
        while stmt.step():
            row = stmt.getAsObject()
            module_id = row["module_id"]
            class_id = row["class_id"]
            method_id = row["method_id"]
            
            # Parse decorators
            decorators_list = []
            if row["decorators"]:
                try:
                    import js
                    decorators_list = js.JSON.parse(row["decorators"])
                except Exception:
                    pass
            
            method_data = {
                "id": method_id,
                "name": row["method_name"],
                "return_type": row["return_type"],
                "is_async": row["is_async"],
                "decorators_list": decorators_list,
                "parameters": [],  # Will be populated in Step 3b
                "docstring": row["docstring"],
            }
            
            methods_dict[method_id] = method_data
            method_to_location[method_id] = (module_id, class_id)

        stmt.free()

        # Step 3b: Bulk fetch ALL parameters for ALL methods
        # Get all method IDs as a list
        method_ids = list(methods_dict.keys())
        
        if method_ids:
            # Build SQL with IN clause for all method IDs
            placeholders = ",".join(["?" for _ in method_ids])
            query = f"""
                SELECT up.method_id, up.name, up.position, up.type_hint, up.default_value, 
                       up.is_optional, up.is_variadic
                FROM unique_parameters up
                WHERE up.method_id IN ({placeholders})
                ORDER BY up.method_id, up.position
            """
            stmt = app_state["db"].prepare(query)
            stmt.bind(ffi.to_js(method_ids))

            while stmt.step():
                row = stmt.getAsObject()
                method_id = row["method_id"]
                
                param_data = {
                    "name": row["name"],
                    "position": row["position"],
                    "type_hint": row["type_hint"],
                    "default_value": row["default_value"],
                    "is_optional": row["is_optional"],
                    "is_variadic": row["is_variadic"],
                }
                
                if method_id in methods_dict:
                    methods_dict[method_id]["parameters"].append(param_data)

            stmt.free()

        # Step 3c: Place methods in their respective modules/classes
        for method_id, method_data in methods_dict.items():
            module_id, class_id = method_to_location[method_id]
            
            if class_id:  # Class method
                key = (module_id, class_id)
                if key in classes_dict:
                    classes_dict[key]["methods"].append(method_data)
            else:  # Module-level function
                if module_id in modules_dict:
                    modules_dict[module_id]["functions"].append(method_data)

        # Step 4: Bulk fetch ALL attributes for this board's classes
        stmt = app_state["db"].prepare("""
            SELECT uca.id, uca.name, uca.type_hint, uca.value, uc.id as class_id, um.id as module_id
            FROM unique_class_attributes uca
            JOIN unique_classes uc ON uca.class_id = uc.id
            JOIN unique_modules um ON uc.module_id = um.id
            JOIN board_class_attribute_support bcas ON uca.id = bcas.attribute_id
            JOIN boards b ON bcas.board_id = b.id
            WHERE b.version = ? AND b.port = ? AND b.board = ?
            ORDER BY uca.name
        """)
        stmt.bind(ffi.to_js([version, port, board]))

        while stmt.step():
            row = stmt.getAsObject()
            module_id = row["module_id"]
            class_id = row["class_id"]
            
            attribute_data = {
                "id": row["id"],
                "name": row["name"],
                "type": row["type_hint"],
                "value": row["value"],
            }
            
            key = (module_id, class_id)
            if key in classes_dict:
                classes_dict[key]["attributes"].append(attribute_data)

        stmt.free()

        # Step 5: Bulk fetch ALL constants for this board's modules
        stmt = app_state["db"].prepare("""
            SELECT umc.name, umc.value, umc.type_hint, umc.module_id
            FROM unique_module_constants umc
            JOIN board_module_constant_support bmcs ON umc.id = bmcs.constant_id
            JOIN boards b ON bmcs.board_id = b.id
            WHERE b.version = ? AND b.port = ? AND b.board = ?
            ORDER BY umc.name
        """)
        stmt.bind(ffi.to_js([version, port, board]))

        while stmt.step():
            row = stmt.getAsObject()
            module_id = row["module_id"]
            
            constant_data = {
                "name": row["name"],
                "value": row["value"],
                "type": row["type_hint"],
            }
            
            if module_id in modules_dict:
                modules_dict[module_id]["constants"].append(constant_data)

        stmt.free()

        # Step 6: Convert classes dict to list for each module
        for module_id in modules_dict:
            modules_dict[module_id]["classes"] = list(modules_dict[module_id]["classes"].values())

        # Convert modules dict to sorted list
        modules = sorted(modules_dict.values(), key=lambda m: m["name"])
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


# ========================================
# Sprint 4.5: SQL-based Comparison Functions
# ========================================

def get_board_id(version, port, board):
    """Get board ID from version, port, and board name."""
    stmt = app_state["db"].prepare("""
        SELECT id FROM boards WHERE version = ? AND port = ? AND board = ?
    """)
    stmt.bind(ffi.to_js([version, port, board]))
    board_id = None
    if stmt.step():
        board_id = stmt.getAsObject()["id"]
    stmt.free()
    return board_id


def calculate_comparison_stats_sql(board_id_1, board_id_2):
    """
    Calculate comparison statistics using SQL views instead of Python iteration.
    Returns statistics at 3 levels: modules, direct children (classes/functions/constants), 
    and class members (methods/attributes).
    
    Sprint 4.5 Task 4.5.2: Replaces 300+ lines of nested Python loops with SQL queries.
    """
    
    # Level 1: Module comparison
    sql_modules = """
        WITH board1_modules AS (
            SELECT module_name, module_id FROM v_board_comparison_modules WHERE board_id = ?
        ),
        board2_modules AS (
            SELECT module_name, module_id FROM v_board_comparison_modules WHERE board_id = ?
        )
        SELECT 
            (SELECT COUNT(DISTINCT module_name) FROM board1_modules) as total1,
            (SELECT COUNT(DISTINCT module_name) FROM board2_modules) as total2,
            (SELECT COUNT(DISTINCT b1.module_name) FROM board1_modules b1 
             WHERE b1.module_name NOT IN (SELECT module_name FROM board2_modules)) as unique1,
            (SELECT COUNT(DISTINCT b2.module_name) FROM board2_modules b2 
             WHERE b2.module_name NOT IN (SELECT module_name FROM board1_modules)) as unique2,
            (SELECT COUNT(DISTINCT b1.module_name) FROM board1_modules b1 
             INNER JOIN board2_modules b2 ON b1.module_name = b2.module_name) as common
    """
    
    stmt = app_state["db"].prepare(sql_modules)
    stmt.bind(ffi.to_js([int(board_id_1), int(board_id_2)]))
    stmt.step()
    level1_data = stmt.getAsObject()
    stmt.free()
    
    level1 = {
        "total1": level1_data["total1"],
        "total2": level1_data["total2"],
        "unique1": level1_data["unique1"],
        "unique2": level1_data["unique2"],
        "common": level1_data["common"],
    }
    
    # Level 2: Classes, functions, constants comparison
    sql_level2 = """
        WITH board1_modules AS (
            SELECT module_name FROM v_board_comparison_modules WHERE board_id = ?1
        ),
        board2_modules AS (
            SELECT module_name FROM v_board_comparison_modules WHERE board_id = ?2
        ),
        unique_modules1 AS (
            SELECT module_name FROM board1_modules 
            WHERE module_name NOT IN (SELECT module_name FROM board2_modules)
        ),
        unique_modules2 AS (
            SELECT module_name FROM board2_modules 
            WHERE module_name NOT IN (SELECT module_name FROM board1_modules)
        ),
        common_modules AS (
            SELECT b1.module_name FROM board1_modules b1 
            INNER JOIN board2_modules b2 ON b1.module_name = b2.module_name
        ),
        -- Classes in unique modules
        classes_unique1 AS (
            SELECT c.class_id FROM v_board_comparison_classes c
            INNER JOIN unique_modules1 u ON c.module_name = u.module_name
            WHERE c.board_id = ?1
        ),
        classes_unique2 AS (
            SELECT c.class_id FROM v_board_comparison_classes c
            INNER JOIN unique_modules2 u ON c.module_name = u.module_name
            WHERE c.board_id = ?2
        ),
        -- Classes in common modules
        classes_in_common1 AS (
            SELECT c.class_id, c.class_name, c.module_name FROM v_board_comparison_classes c
            INNER JOIN common_modules cm ON c.module_name = cm.module_name
            WHERE c.board_id = ?1
        ),
        classes_in_common2 AS (
            SELECT c.class_id, c.class_name, c.module_name FROM v_board_comparison_classes c
            INNER JOIN common_modules cm ON c.module_name = cm.module_name
            WHERE c.board_id = ?2
        ),
        -- Functions and constants
        funcs_in_common1 AS (
            SELECT m.method_id, m.method_name, m.module_name FROM v_board_comparison_methods m
            INNER JOIN common_modules cm ON m.module_name = cm.module_name
            WHERE m.board_id = ?1 AND m.class_name IS NULL
        ),
        funcs_in_common2 AS (
            SELECT m.method_id, m.method_name, m.module_name FROM v_board_comparison_methods m
            INNER JOIN common_modules cm ON m.module_name = cm.module_name
            WHERE m.board_id = ?2 AND m.class_name IS NULL
        ),
        consts_in_common1 AS (
            SELECT c.constant_id, c.constant_name, c.module_name FROM v_board_comparison_constants c
            INNER JOIN common_modules cm ON c.module_name = cm.module_name
            WHERE c.board_id = ?1
        ),
        consts_in_common2 AS (
            SELECT c.constant_id, c.constant_name, c.module_name FROM v_board_comparison_constants c
            INNER JOIN common_modules cm ON c.module_name = cm.module_name
            WHERE c.board_id = ?2
        )
        SELECT 
            (SELECT COUNT(*) FROM classes_unique1) as classes1_unique,
            (SELECT COUNT(*) FROM classes_unique2) as classes2_unique,
            (SELECT COUNT(*) FROM classes_in_common1 c1 
             WHERE c1.class_name NOT IN (SELECT class_name FROM classes_in_common2 c2 
                                          WHERE c2.module_name = c1.module_name)) as classes1_diff,
            (SELECT COUNT(*) FROM classes_in_common2 c2 
             WHERE c2.class_name NOT IN (SELECT class_name FROM classes_in_common1 c1 
                                          WHERE c1.module_name = c2.module_name)) as classes2_diff,
            (SELECT COUNT(*) FROM funcs_in_common1 f1 
             WHERE f1.method_name NOT IN (SELECT method_name FROM funcs_in_common2 f2 
                                           WHERE f2.module_name = f1.module_name)) as functions1_unique,
            (SELECT COUNT(*) FROM funcs_in_common2 f2 
             WHERE f2.method_name NOT IN (SELECT method_name FROM funcs_in_common1 f1 
                                           WHERE f1.module_name = f2.module_name)) as functions2_unique,
            (SELECT COUNT(*) FROM consts_in_common1 c1 
             WHERE c1.constant_name NOT IN (SELECT constant_name FROM consts_in_common2 c2 
                                             WHERE c2.module_name = c1.module_name)) as constants1_unique,
            (SELECT COUNT(*) FROM consts_in_common2 c2 
             WHERE c2.constant_name NOT IN (SELECT constant_name FROM consts_in_common1 c1 
                                             WHERE c1.module_name = c2.module_name)) as constants2_unique
    """
    
    stmt = app_state["db"].prepare(sql_level2)
    # Bind: only 2 parameters now (was 10)
    stmt.bind(ffi.to_js([int(board_id_1), int(board_id_2)]))
    stmt.step()
    level2_data = stmt.getAsObject()
    stmt.free()
    
    level2 = {
        "classes1_unique": level2_data["classes1_unique"] + level2_data["classes1_diff"],
        "classes2_unique": level2_data["classes2_unique"] + level2_data["classes2_diff"],
        "functions1_unique": level2_data["functions1_unique"],
        "functions2_unique": level2_data["functions2_unique"],
        "constants1_unique": level2_data["constants1_unique"],
        "constants2_unique": level2_data["constants2_unique"],
        "classes_different": 0,  # Will be calculated in level 3
        "functions_different": 0,
        "constants_different": 0,
    }
    
    # Level 3: Methods and attributes comparison
    sql_level3 = """
        WITH board1_modules AS (
            SELECT module_name FROM v_board_comparison_modules WHERE board_id = ?1
        ),
        board2_modules AS (
            SELECT module_name FROM v_board_comparison_modules WHERE board_id = ?2
        ),
        common_modules AS (
            SELECT b1.module_name FROM board1_modules b1 
            INNER JOIN board2_modules b2 ON b1.module_name = b2.module_name
        ),
        common_classes AS (
            SELECT c1.class_id as class_id1, c2.class_id as class_id2, 
                   c1.class_name, c1.module_name
            FROM v_board_comparison_classes c1
            INNER JOIN v_board_comparison_classes c2 
                ON c1.class_name = c2.class_name AND c1.module_name = c2.module_name
            INNER JOIN common_modules cm ON c1.module_name = cm.module_name
            WHERE c1.board_id = ?1 AND c2.board_id = ?2
        ),
        methods1 AS (
            SELECT m.method_id, m.method_name, m.class_id, cc.class_name, cc.module_name
            FROM v_board_comparison_methods m
            INNER JOIN common_classes cc ON m.class_id = cc.class_id1
            WHERE m.board_id = ?1
        ),
        methods2 AS (
            SELECT m.method_id, m.method_name, m.class_id, cc.class_name, cc.module_name
            FROM v_board_comparison_methods m
            INNER JOIN common_classes cc ON m.class_id = cc.class_id2
            WHERE m.board_id = ?2
        ),
        attrs1 AS (
            SELECT a.attribute_id, a.attribute_name, a.class_id, cc.class_name, cc.module_name
            FROM v_board_comparison_attributes a
            INNER JOIN common_classes cc ON a.class_id = cc.class_id1
            WHERE a.board_id = ?1
        ),
        attrs2 AS (
            SELECT a.attribute_id, a.attribute_name, a.class_id, cc.class_name, cc.module_name
            FROM v_board_comparison_attributes a
            INNER JOIN common_classes cc ON a.class_id = cc.class_id2
            WHERE a.board_id = ?2
        ),
        -- Also count methods/attrs from unique classes in unique modules
        unique_modules1 AS (
            SELECT module_name FROM board1_modules 
            WHERE module_name NOT IN (SELECT module_name FROM board2_modules)
        ),
        unique_modules2 AS (
            SELECT module_name FROM board2_modules 
            WHERE module_name NOT IN (SELECT module_name FROM board1_modules)
        ),
        unique_classes1 AS (
            SELECT c.class_id FROM v_board_comparison_classes c
            INNER JOIN unique_modules1 u ON c.module_name = u.module_name
            WHERE c.board_id = ?1
        ),
        unique_classes2 AS (
            SELECT c.class_id FROM v_board_comparison_classes c
            INNER JOIN unique_modules2 u ON c.module_name = u.module_name
            WHERE c.board_id = ?2
        ),
        methods_unique_modules1 AS (
            SELECT m.method_id FROM v_board_comparison_methods m
            INNER JOIN unique_classes1 uc ON m.class_id = uc.class_id
            WHERE m.board_id = ?1
        ),
        methods_unique_modules2 AS (
            SELECT m.method_id FROM v_board_comparison_methods m
            INNER JOIN unique_classes2 uc ON m.class_id = uc.class_id
            WHERE m.board_id = ?2
        ),
        attrs_unique_modules1 AS (
            SELECT a.attribute_id FROM v_board_comparison_attributes a
            INNER JOIN unique_classes1 uc ON a.class_id = uc.class_id
            WHERE a.board_id = ?1
        ),
        attrs_unique_modules2 AS (
            SELECT a.attribute_id FROM v_board_comparison_attributes a
            INNER JOIN unique_classes2 uc ON a.class_id = uc.class_id
            WHERE a.board_id = ?2
        )
        SELECT 
            (SELECT COUNT(*) FROM methods1 m1 
             WHERE NOT EXISTS (SELECT 1 FROM methods2 m2 
                               WHERE m2.method_name = m1.method_name 
                               AND m2.class_name = m1.class_name 
                               AND m2.module_name = m1.module_name)) 
            + (SELECT COUNT(*) FROM methods_unique_modules1) as methods1_unique,
            (SELECT COUNT(*) FROM methods2 m2 
             WHERE NOT EXISTS (SELECT 1 FROM methods1 m1 
                               WHERE m1.method_name = m2.method_name 
                               AND m1.class_name = m2.class_name 
                               AND m1.module_name = m2.module_name))
            + (SELECT COUNT(*) FROM methods_unique_modules2) as methods2_unique,
            (SELECT COUNT(*) FROM attrs1 a1 
             WHERE NOT EXISTS (SELECT 1 FROM attrs2 a2 
                               WHERE a2.attribute_name = a1.attribute_name 
                               AND a2.class_name = a1.class_name 
                               AND a2.module_name = a1.module_name))
            + (SELECT COUNT(*) FROM attrs_unique_modules1) as attributes1_unique,
            (SELECT COUNT(*) FROM attrs2 a2 
             WHERE NOT EXISTS (SELECT 1 FROM attrs1 a1 
                               WHERE a1.attribute_name = a2.attribute_name 
                               AND a1.class_name = a2.class_name 
                               AND a1.module_name = a2.module_name))
            + (SELECT COUNT(*) FROM attrs_unique_modules2) as attributes2_unique,
            (SELECT COUNT(DISTINCT class_name || ':' || module_name) 
             FROM (SELECT m1.class_name, m1.module_name FROM methods1 m1 
                   WHERE NOT EXISTS (SELECT 1 FROM methods2 m2 
                                     WHERE m2.method_name = m1.method_name 
                                     AND m2.class_name = m1.class_name 
                                     AND m2.module_name = m1.module_name)
                   UNION
                   SELECT m2.class_name, m2.module_name FROM methods2 m2 
                   WHERE NOT EXISTS (SELECT 1 FROM methods1 m1 
                                     WHERE m1.method_name = m2.method_name 
                                     AND m1.class_name = m2.class_name 
                                     AND m1.module_name = m2.module_name))) as methods_different,
            (SELECT COUNT(DISTINCT class_name || ':' || module_name) 
             FROM (SELECT a1.class_name, a1.module_name FROM attrs1 a1 
                   WHERE NOT EXISTS (SELECT 1 FROM attrs2 a2 
                                     WHERE a2.attribute_name = a1.attribute_name 
                                     AND a2.class_name = a1.class_name 
                                     AND a2.module_name = a1.module_name)
                   UNION
                   SELECT a2.class_name, a2.module_name FROM attrs2 a2 
                   WHERE NOT EXISTS (SELECT 1 FROM attrs1 a1 
                                     WHERE a1.attribute_name = a2.attribute_name 
                                     AND a1.class_name = a2.class_name 
                                     AND a1.module_name = a2.module_name))) as attributes_different
    """
    
    stmt = app_state["db"].prepare(sql_level3)
    # Bind: only 2 parameters now (was 14)
    stmt.bind(ffi.to_js([int(board_id_1), int(board_id_2)]))
    stmt.step()
    level3_data = stmt.getAsObject()
    stmt.free()
    
    level3 = {
        "methods1_unique": level3_data["methods1_unique"],
        "methods2_unique": level3_data["methods2_unique"],
        "attributes1_unique": level3_data["attributes1_unique"],
        "attributes2_unique": level3_data["attributes2_unique"],
        "methods_different": level3_data["methods_different"],
        "attributes_different": level3_data["attributes_different"],
    }
    
    return {"level1": level1, "level2": level2, "level3": level3}