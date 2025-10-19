import asyncio
import json

import board_utils
import js
from pyscript import document, fetch, ffi, window
from sqlite_wasm import SQLDatabase, SQLExecResult, SQLExecResults, SQLite

# Global state
app_state = {
    "SQL": None,
    "db": None,
    "boards": [],
    "current_board": None,
}


def update_status(message, status_type="info"):
    """Update the status indicator."""
    status_elem = document.getElementById("status")
    status_text = document.getElementById("status-text")

    status_text.innerText = message

    # Reset classes
    status_elem.classList.remove("success", "error")

    # Add appropriate class
    if status_type == "success":
        status_elem.classList.add("success")
    elif status_type == "error":
        status_elem.classList.add("error")


async def load_database():
    """Load SQLite database using SQL.js."""
    try:
        update_status("SQLite.initialize ...", "info")
        SQL = await SQLite.initialize(version="1.13.0", cdn="cdnjs")
        window.console.log(f"SQLite-wasm wrapper created")
        app_state["SQL"] = SQL
        update_status("Loading database...", "info")
        await asyncio.sleep(0.1)  # Allow UI update
        window.console.log("Opening database 'board_comparison.db'...")
        app_state["db"] = await SQL.open_database("board_comparison.db")
        await asyncio.sleep(0.1)  # Allow UI update
        update_status("Database loaded successfully!", "success")

        # Test database connection
        stmt = app_state["db"].prepare("SELECT COUNT(*) as count FROM boards")
        stmt.step()
        row = stmt.getAsObject()
        stmt.free()

        board_count = row["count"]
        update_status(f"Database ready! Found {board_count} boards.", "success")

        return True

    except Exception as e:
        update_status(f"Error loading database: {str(e)}", "error")
        print(f"Database error: {e}")
        return False


async def load_board_list_from_db():
    """Load board list from database."""
    if not app_state["db"]:
        return False

    try:
        update_status("Loading board list from database...", "info")

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
        update_status(f"Loaded {len(boards)} boards from database", "success")

        return True

    except Exception as e:
        update_status(f"Error loading board list: {str(e)}", "error")
        print(f"Board list error: {e}")
        return False


def switch_page(page_id):
    """Switch between different pages."""
    # Hide all pages
    for page_name in ["explorer", "compare", "search"]:
        page = document.getElementById(f"{page_name}-page")
        tab = document.getElementById(f"tab-{page_name}")

        page.classList.remove("active")
        tab.classList.remove("active")

    # Show selected page
    page = document.getElementById(f"{page_id}-page")
    tab = document.getElementById(f"tab-{page_id}")

    page.classList.add("active")
    tab.classList.add("active")


def populate_board_selects():
    """Populate all board selection dropdowns."""
    if not app_state["boards"]:
        return

    # Get unique versions
    versions = list(set(board.get("version", "") for board in app_state["boards"]))
    versions.sort(reverse=True)

    # Populate version selects
    for select_id in ["explorer-version", "board1-version", "board2-version"]:
        select = document.getElementById(select_id)
        select.innerHTML = '<option value="">All versions</option>'

        for version in versions:
            option = document.createElement("option")
            option.value = version
            option.textContent = version
            select.appendChild(option)

    # Get unique board names (formatted)
    board_names = list(set(board_utils.format_board_name(board.get("port", ""), board.get("board", "")) for board in app_state["boards"]))
    board_names.sort()

    # Populate board selects
    for select_id in ["explorer-board", "board1", "board2"]:
        select = document.getElementById(select_id)
        select.innerHTML = '<option value="">Select a board...</option>'

        for board_name in board_names:
            option = document.createElement("option")
            option.value = board_name
            option.textContent = board_name
            select.appendChild(option)


def format_board_name(port, board):
    """Format board display name."""
    return board_utils.format_board_name(port, board)


# Set up event handlers
def setup_event_handlers():
    """Set up event listeners for the UI."""
    # Tab navigation
    document.getElementById("tab-explorer").onclick = lambda e: switch_page("explorer")
    document.getElementById("tab-compare").onclick = lambda e: switch_page("compare")
    document.getElementById("tab-search").onclick = lambda e: switch_page("search")

    # Compare button
    document.getElementById("compare-btn").onclick = lambda e: compare_boards()

    # Search button
    document.getElementById("search-btn").onclick = lambda e: search_apis()

    # Board selection change handlers
    def make_board_change_handler():
        async def handler(e):
            await load_board_details()

        return handler

    document.getElementById("explorer-version").onchange = make_board_change_handler()
    document.getElementById("explorer-board").onchange = make_board_change_handler()


def compare_boards():
    """Compare two selected boards."""
    results = document.getElementById("compare-results")
    results.innerHTML = """
    <div class="detail-view">
        <div class="detail-header">Board Comparison</div>
        <p style="color: #666;">Comparison functionality coming soon...</p>
        <p style="color: #666; margin-top: 10px;">
            This feature is under development.
        </p>
    </div>
    """


def search_apis():
    """Search for APIs across boards."""
    results = document.getElementById("search-results")
    results.innerHTML = """
    <div class="detail-view">
        <div class="detail-header">Search Results</div>
        <p style="color: #666;">Search functionality coming soon...</p>
        <p style="color: #666; margin-top: 10px;">
            This feature is under development.
        </p>
    </div>
    """


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
        # need to convert to js object
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
                    decorators_list = js.JSON.parse(row["decorators"])
                except:
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

            classes.append(
                {"id": class_id, "name": row["name"], "docstring": row["docstring"], "base_classes": base_classes, "methods": methods}
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
                    decorators_list = js.JSON.parse(row["decorators"])
                except:
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


def render_module_tree(module):
    """Render an expandable module tree."""
    classes = module.get("classes", [])
    functions = module.get("functions", [])
    constants = module.get("constants", [])

    class_count = len(classes)
    func_count = len(functions)
    const_count = len(constants)

    # Format summary
    summary = board_utils.format_module_summary(class_count, func_count, const_count, module["name"])

    module_id = f"module-{module['name']}"

    html = f"""
    <div class="tree-item" style="margin-bottom: 6px;">
        <div class="tree-node" onclick="toggleModule('{module_id}', event)" 
                style="padding: 12px; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #667eea; display: flex; align-items: center;">
            <i class="fas fa-cube fa-icon" style="color: #667eea;"></i>
            <strong style="font-size: 1.1em; color: #2c3e50;">{module["name"]}</strong>
            <span style="margin-left: auto; color: #6c757d; font-size: 0.9em; background: #e9ecef; padding: 4px 8px; border-radius: 12px;">
                {summary}
            </span>
        </div>
    """

    # Add children if module has content
    if class_count > 0 or func_count > 0 or const_count > 0:
        html += f'<div id="{module_id}" class="tree-children hidden">'

        # Render classes
        for cls in classes:
            html += render_class_tree(cls, module["name"])

        # Render module-level functions
        for func in functions:
            sig = format_function_signature(func)
            decorators_html = ""
            if func.get("decorators_list"):
                for dec in func["decorators_list"]:
                    decorators_html += f'<span style="color: #888; font-size: 0.85em;">@{dec}</span> '

            html += f"""
            <div class="tree-item">
                <div class="tree-node" style="padding: 8px; background: #fff; border-radius: 6px; margin-bottom: 4px;">
                    <i class="fas fa-bolt fa-icon" style="color: #f39c12;"></i>
                    {decorators_html}
                    <code style="font-family: 'Courier New', monospace; font-size: 0.9em;">{sig}</code>
                </div>
            </div>
            """

        # Render constants
        for const in constants:
            value_str = f" = {const['value']}" if const.get("value") else ""
            html += f"""
            <div class="tree-item">
                <div class="tree-node" style="padding: 8px; background: #fff; border-radius: 6px; margin-bottom: 4px;">
                    <i class="fas fa-circle fa-icon" style="color: #95a5a6; font-size: 0.6em;"></i>
                    <code style="font-family: 'Courier New', monospace; font-size: 0.9em;">{const["name"]}{value_str}</code>
                </div>
            </div>
            """

        html += "</div>"

    html += "</div>"
    return html


def render_class_tree(cls, module_name):
    """Render an expandable class tree."""
    methods = cls.get("methods", [])
    base_classes = cls.get("base_classes", [])

    base_str = ""
    if base_classes:
        base_str = f" <span style='color: #888; font-weight: normal;'>({', '.join(base_classes)})</span>"

    class_id = f"class-{module_name}-{cls['name']}"

    html = f"""
    <div class="tree-item">
        <div class="tree-node" onclick="toggleClass('{class_id}', event)"
                style="padding: 10px; background: #fff; border-radius: 6px; margin-bottom: 4px; border-left: 4px solid #e3f2fd; display: flex; align-items: center;">
            <i class="fas fa-object-group fa-icon" style="color: #3498db;"></i>
            <span style="font-weight: 600;">class {cls["name"]}{base_str}</span>
            <span style="margin-left: auto; color: #6c757d; font-size: 0.85em;">{len(methods)} methods</span>
        </div>
    """

    # Add methods if class has any
    if len(methods) > 0:
        html += f'<div id="{class_id}" class="tree-children hidden">'

        for method in methods:
            sig = format_function_signature(method)

            # Build decorator display
            decorators_html = ""
            if method.get("decorators_list"):
                for dec in method["decorators_list"]:
                    decorators_html += f'<span style="color: #888; font-size: 0.85em;">@{dec}</span> '
            elif method.get("is_property"):
                decorators_html = '<span style="color: #888; font-size: 0.85em;">@property</span> '
            elif method.get("is_classmethod"):
                decorators_html = '<span style="color: #888; font-size: 0.85em;">@classmethod</span> '
            elif method.get("is_staticmethod"):
                decorators_html = '<span style="color: #888; font-size: 0.85em;">@staticmethod</span> '

            html += f"""
            <div class="tree-item">
                <div class="tree-node" style="padding: 8px; background: #fafafa; border-radius: 6px; margin-bottom: 2px;">
                    <i class="fas fa-bolt fa-icon" style="color: #9b59b6; font-size: 0.8em;"></i>
                    {decorators_html}
                    <code style="font-family: 'Courier New', monospace; font-size: 0.85em;">{sig}</code>
                </div>
            </div>
            """

        html += "</div>"

    html += "</div>"
    return html


def format_function_signature(func):
    """Format a function/method signature with parameters."""
    # Build async prefix
    async_prefix = "async " if func.get("is_async") else ""

    # Build parameter list
    params = []
    for param in func.get("parameters", []):
        param_str = param["name"]

        # Add type hint
        if param.get("type_hint") and param["type_hint"] not in ("None", ""):
            param_str += f": {param['type_hint']}"

        # Add default value
        if param.get("default_value") and param["default_value"] not in ("None", ""):
            param_str += f" = {param['default_value']}"
        elif param.get("is_optional"):
            param_str += " = None"

        # Handle variadic
        if param.get("is_variadic"):
            if param["name"] == "kwargs":
                param_str = "**" + param_str
            else:
                param_str = "*" + param_str

        params.append(param_str)

    signature = f"{async_prefix}{func['name']}({', '.join(params)})"

    # Add return type
    if func.get("return_type") and func["return_type"] not in ("None", "", "Any"):
        signature += f" -> {func['return_type']}"

    return signature


async def load_board_details():
    """Load board details when a board is selected."""
    version_select = document.getElementById("explorer-version")
    board_select = document.getElementById("explorer-board")

    selected_version = version_select.value
    selected_board_name = board_select.value

    content = document.getElementById("explorer-content")

    if not selected_version or not selected_board_name:
        content.innerHTML = '<div class="loading"><p>Select both version and board to explore modules and APIs</p></div>'
        return

    # Show loading
    content.innerHTML = """
    <div class="loading">
        <div class="spinner"></div>
        <p>Loading board details...</p>
        <div class="progress-step">Fetching modules...</div>
    </div>
    """

    if not app_state["db"]:
        # Database is required
        content.innerHTML = f"""
        <div class="detail-view">
            <div class="detail-header">{selected_board_name} ({selected_version})</div>
            <p style="color: #dc3545; margin: 15px 0;">
                <strong>Error:</strong> Database not loaded.
            </p>
            <p style="color: #666;">
                Please refresh the page to retry loading the database.
            </p>
        </div>
        """
        return

    try:
        # Find the actual port/board from the board list
        board_info = board_utils.find_board_in_list(app_state["boards"], selected_version, selected_board_name)

        if not board_info:
            content.innerHTML = f"""
            <div class="detail-view">
                <h3 style="color: #dc3545;">Board Not Found</h3>
                <p style="color: #666;">Could not find board: {selected_board_name} ({selected_version})</p>
            </div>
            """
            return

        port, board = board_info

        # Store board context for queries
        board_context = {"version": selected_version, "port": port, "board": board}

        # Query database for modules
        stmt = app_state["db"].prepare("""
            SELECT um.id, um.name, um.docstring 
            FROM unique_modules um
            JOIN board_module_support bms ON um.id = bms.module_id
            JOIN boards b ON bms.board_id = b.id
            WHERE b.version = ? AND b.port = ? AND b.board = ?
            ORDER BY um.name
        """)

        stmt.bind(ffi.to_js([selected_version, port, board]))

        modules = []
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

        # Build expandable module tree
        html = f"""
        <div class="detail-view">
            <div class="detail-header">{selected_board_name} ({selected_version})</div>
            <div style="margin: 20px 0;">
                <h3 style="color: #667eea; margin-bottom: 15px;">
                    <i class="fas fa-cube"></i> Modules ({len(modules)})
                </h3>
                <div class="module-tree" style="background: white; border: 2px solid #e9ecef; border-radius: 8px; padding: 20px;">
        """

        # Render expandable module tree
        for module in modules:
            html += render_module_tree(module)

        html += """
                </div>
            </div>
        </div>
        """

        content.innerHTML = html

    except Exception as e:
        content.innerHTML = f"""
        <div class="detail-view">
            <h3 style="color: #dc3545;">⚠️ Error Loading Board</h3>
            <p style="color: #666; margin: 15px 0;">{str(e)}</p>
            <pre style="background: #f8f9fa; padding: 10px; border-radius: 4px; overflow-x: auto; font-size: 0.85em;">{type(e).__name__}: {str(e)}</pre>
        </div>
        """
        print(f"Error loading board details: {e}")
        import sys

        sys.print_exception(e)


# Main initialization
async def main():
    """Main entry point for the application."""
    update_status("Loading board utilities...", "info")

    # Set up event handlers
    setup_event_handlers()

    # Load database
    db_loaded = await load_database()

    if db_loaded:
        # Load board list from database
        await load_board_list_from_db()
        populate_board_selects()
        update_status("Loaded database. Application ready!", "success")
    else:
        # Database is required
        update_status("Failed to load database. Cannot continue.", "error")


# Start the application


asyncio.create_task(main())
