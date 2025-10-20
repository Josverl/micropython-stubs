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

# Template utilities
def get_template(template_id):
    """Get a clone of a template element."""
    template = document.getElementById(template_id)
    if template:
        return template.cloneNode(True)
    return None


def populate_template(element, data):
    """Populate template placeholders with data."""
    if not element:
        return element

    # Handle text content placeholders
    for key, value in data.items():
        # Find elements with data attributes
        target_elements = element.querySelectorAll(f"[data-{key}]")

        for target in target_elements:
            if key.endswith("-click") and value:
                target.setAttribute("onclick", value)
            elif key.endswith("-class") and value:
                target.className = value
            elif key.endswith("-id") and value:
                target.id = value
            elif key.endswith("-data") and value:
                target.setAttribute("data-module", value)
            elif key.endswith("-style") and value:
                if value == "hide":
                    target.style.display = "none"
                elif value == "show":
                    target.style.display = "block"
            elif key.endswith("-icon") and value:
                # Handle icon classes - set className instead of text content
                target.className = value
            else:
                # Set text content
                if hasattr(target, "textContent"):
                    target.textContent = str(value) if value is not None else ""
                elif hasattr(target, "innerText"):
                    target.innerText = str(value) if value is not None else ""

    return element


def show_loading(container_id, message="Loading...", progress=""):
    """Show loading state using template."""
    container = document.getElementById(container_id)
    if not container:
        return

    loading_element = get_template("loading-template")
    if loading_element:
        loading_element.style.display = "block"
        populate_template(loading_element, {"loading-message": message, "progress-step": progress})
        container.innerHTML = ""
        container.appendChild(loading_element)


def show_error(container_id, title="Error", message="An error occurred", show_retry=False):
    """Show error state using template."""
    container = document.getElementById(container_id)
    if not container:
        return

    error_element = get_template("error-template")
    if error_element:
        error_element.style.display = "block"
        populate_template(
            error_element, {"error-title": title, "error-message": message, "retry-button-style": "show" if show_retry else "hide"}
        )
        container.innerHTML = ""
        container.appendChild(error_element)


def show_message(container_id, title="Information", message=""):
    """Show simple message using template."""
    container = document.getElementById(container_id)
    if not container:
        return

    message_element = get_template("message-template")
    if message_element:
        message_element.style.display = "block"
        populate_template(message_element, {"message-title": title, "message-text": message})
        container.innerHTML = ""
        container.appendChild(message_element)


def create_module_item(module, options):
    """Create a module item using template."""
    module_prefix = options.get("module_prefix", "tree")
    get_badge_class = options.get("get_badge_class", lambda m: "")
    get_module_badge = options.get("get_module_badge", lambda m: "")
    
    classes = module.get("classes", [])
    functions = module.get("functions", [])
    constants = module.get("constants", [])
    
    # has_children = len(classes) > 0 or len(functions) > 0 or len(constants) > 0
    is_deprecated = module["name"].startswith("u") and len(module["name"]) != "uctypes"
    # FIXME: Why does in not work ?
    # is_deprecated =str(module['name']) in U_MODULES
    # if is_deprecated:
    #     print(f"{module['name']=}")
    #     window.console.log(ffi.to_js(module["name"]))
    #     window.console.log(ffi.to_js(module))

    badge_class = get_badge_class(module)
    module_badge = get_module_badge(module)
    module_tree_id = f"{module_prefix}-module-{module['name']}"
    
    # Format module summary
    summary_parts = []
    if len(classes) > 0:
        summary_parts.append(f"{len(classes)} classes")
    if len(functions) > 0:
        summary_parts.append(f"{len(functions)} functions")
    if len(constants) > 0:
        summary_parts.append(f"{len(constants)} constants")
    
    if summary_parts:
        module_summary = ", ".join(summary_parts)
    elif is_deprecated:
        base_module_name = module["name"][1:]  # Remove 'u' prefix
        module_summary = f"deprecated - use {base_module_name} instead"
    else:
        module_summary = "empty module"
    
    module_header_class = "module-header"
    if badge_class:
        module_header_class += " unique"
    if is_deprecated:
        module_header_class += " deprecated"
    
    # Get template and populate
    module_element = get_template("module-item-template")
    if module_element:
        populate_template(module_element, {
            "module-header-class": module_header_class,
            "module-click": f"toggleModule('{module_tree_id}', event)",
            "module-data": module["name"],
            "module-name": module["name"],
            "module-badge-style": "inline" if module_badge else "hide",
            "module-details": module_summary,
            "module-id": module_tree_id
        })
        
        # Show/hide badge
        badge_elem = module_element.querySelector("[data-module-badge]")
        if badge_elem:
            badge_elem.style.display = "inline" if module_badge else "none"
    
    return module_element


def create_class_item(cls, module_name, module_prefix):
    """Create a class item using template."""
    class_id = f"{module_prefix}-class-{module_name}-{cls['name']}"
    
    base_classes_str = ""
    if cls.get("base_classes") and len(cls["base_classes"]) > 0:
        base_classes_str = f"({', '.join(cls['base_classes'])})"
    
    # Format class summary
    method_count = len(cls.get("methods", []))
    attr_count = len(cls.get("attributes", []))
    
    class_summary_parts = []
    if method_count > 0:
        class_summary_parts.append(f"{method_count} methods")
    if attr_count > 0:
        class_summary_parts.append(f"{attr_count} attributes")
    
    class_summary = ", ".join(class_summary_parts) if class_summary_parts else "empty class"
    
    base_classes_span = f' {base_classes_str}' if base_classes_str else ""
    
    # Get template and populate
    class_element = get_template("class-item-template")
    if class_element:
        populate_template(class_element, {
            "class-click": f"toggleClass('{class_id}', event)",
            "class-signature": f"class {cls['name']}",
            "base-classes": base_classes_span,
            "class-summary": class_summary,
            "class-id": class_id
        })
    
    return class_element


def create_function_item(func):
    """Create a function item using template."""
    # Format function signature
    signature = func["name"]
    
    params = ""
    if func.get("parameters"):
        param_strs = []
        for param in func["parameters"]:
            param_str = param["name"]
            
            if param.get("type_hint") and param["type_hint"] not in ["None", ""]:
                param_str += f": {param['type_hint']}"
            
            if param.get("default_value") and param["default_value"] != "None":
                param_str += f" = {param['default_value']}"
            elif param.get("is_optional"):
                param_str += " = None"
            
            if param.get("is_variadic"):
                param_str = ("**" if param["name"] == "kwargs" else "*") + param_str
            
            param_strs.append(param_str)
        
        params = ", ".join(param_strs)
    
    signature += f"({params})"
    
    if func.get("return_type") and func["return_type"] not in ["None", "", "Any"]:
        signature += f" -> {func['return_type']}"
    
    decorators_list = func.get("decorators_list", [])
    decorator_strs = [f"@{d}" for d in decorators_list]
    async_marker = "async " if func.get("is_async") else ""
    
    function_decorator_span = f'{" ".join(decorator_strs)} ' if decorator_strs else ""
    
    # Get template and populate
    function_element = get_template("function-item-template")
    if function_element:
        populate_template(function_element, {
            "function-icon": "fas fa-ellipsis" if func.get("is_property") else "fas fa-bolt",
            "decorators": function_decorator_span,
            "signature": f"{async_marker}{signature}"
        })
    
    return function_element


def create_constant_item(const):
    """Create a constant item using template."""
    const_value = f" = {const['value']}" if const.get("value") else ""
    
    # Get template and populate
    constant_element = get_template("constant-item-template")
    if constant_element:
        populate_template(constant_element, {
            "constant-signature": f"{const['name']}{const_value}"
        })
    
    return constant_element


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
        window.console.log("SQLite-wasm wrapper created")
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
    tab_explorer = document.getElementById("tab-explorer")
    if tab_explorer:
        tab_explorer.onclick = lambda e: switch_page("explorer")

    tab_compare = document.getElementById("tab-compare")
    if tab_compare:
        tab_compare.onclick = lambda e: switch_page("compare")

    tab_search = document.getElementById("tab-search")
    if tab_search:
        tab_search.onclick = lambda e: switch_page("search")

    # Compare button - async handler
    def make_compare_handler():
        async def handler(e):
            await compare_boards()

        return handler

    compare_btn = document.getElementById("compare-btn")
    if compare_btn:
        compare_btn.onclick = make_compare_handler()

    # Search button - async handler
    def make_search_handler():
        async def handler(e):
            await search_apis()

        return handler

    search_btn = document.getElementById("search-btn")
    if search_btn:
        search_btn.onclick = make_search_handler()

    # Search input - Enter key handler (using JavaScript interop)
    search_input = document.getElementById("search-input")
    if search_input:
        # Use JavaScript to handle the keydown event properly
        js.eval("""
        document.getElementById('search-input').addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                window.micropython_search_enter();
            }
        });
        """)

        # Define the search function for JavaScript to call
        def search_enter():
            asyncio.create_task(search_apis())

        js.window["micropython_search_enter"] = search_enter

    # Board selection change handlers
    def make_board_change_handler():
        async def handler(e):
            await load_board_details()

        return handler

    explorer_version = document.getElementById("explorer-version")
    if explorer_version:
        explorer_version.onchange = make_board_change_handler()

    explorer_board = document.getElementById("explorer-board")
    if explorer_board:
        explorer_board.onchange = make_board_change_handler()

    # Comparison page event handlers
    def make_comparison_change_handler(version_id, board_id):
        def handler(e):
            update_board_options(version_id, board_id)
            update_comparison_url()

        return handler

    def make_board_change_handler_comparison(version_id, board_id):
        def handler(e):
            update_version_options(version_id, board_id)
            update_comparison_url()

        return handler

    # Board version and board selection handlers for comparison
    board1_version = document.getElementById("board1-version")
    if board1_version:
        board1_version.onchange = make_comparison_change_handler("board1-version", "board1")

    board1 = document.getElementById("board1")
    if board1:
        board1.onchange = make_board_change_handler_comparison("board1-version", "board1")

    board2_version = document.getElementById("board2-version")
    if board2_version:
        board2_version.onchange = make_comparison_change_handler("board2-version", "board2")

    board2 = document.getElementById("board2")
    if board2:
        board2.onchange = make_board_change_handler_comparison("board2-version", "board2")

    # Hide common checkbox
    hide_common = document.getElementById("hide-common")
    if hide_common:
        hide_common.onchange = lambda e: update_comparison()

    # Compare boards button
    compare_boards_btn = document.getElementById("compare-boards-btn")
    if compare_boards_btn:

        def make_async_compare_handler():
            async def handler(e):
                await compare_boards()

            return handler

        compare_boards_btn.onclick = make_async_compare_handler()

    # Share button
    share_btn = document.getElementById("share-btn")
    if share_btn:
        share_btn.onclick = lambda e: share_comparison()


# Global comparison state
comparison_data = {
    "board1": None,
    "board2": None,
    "modules1": [],
    "modules2": [],
}


def compare_module_contents(module1, module2):
    """Compare two module objects and return True if they have differences in content."""
    # Compare classes
    classes1_names = {cls["name"] for cls in module1["classes"]}
    classes2_names = {cls["name"] for cls in module2["classes"]}

    if len(classes1_names) != len(classes2_names):
        return True

    for class_name in classes1_names:
        if class_name not in classes2_names:
            return True

        class1 = next(cls for cls in module1["classes"] if cls["name"] == class_name)
        class2 = next(cls for cls in module2["classes"] if cls["name"] == class_name)

        if compare_class_contents(class1, class2):
            return True

    # Compare functions
    funcs1_names = {func["name"] for func in module1["functions"]}
    funcs2_names = {func["name"] for func in module2["functions"]}

    if len(funcs1_names) != len(funcs2_names):
        return True

    for func_name in funcs1_names:
        if func_name not in funcs2_names:
            return True

    # Compare constants
    consts1_names = {const["name"] for const in module1["constants"]}
    consts2_names = {const["name"] for const in module2["constants"]}

    if len(consts1_names) != len(consts2_names):
        return True

    for const_name in consts1_names:
        if const_name not in consts2_names:
            return True

    return False


def compare_class_contents(class1, class2):
    """Compare two class objects and return True if they have differences in methods or attributes."""
    methods1 = {method["name"] for method in class1["methods"]}
    methods2 = {method["name"] for method in class2["methods"]}

    attrs1 = {attr["name"] for attr in class1["attributes"]}
    attrs2 = {attr["name"] for attr in class2["attributes"]}

    # Check if method or attribute sets differ
    if len(methods1) != len(methods2) or len(attrs1) != len(attrs2):
        return True

    for method in methods1:
        if method not in methods2:
            return True

    for attr in attrs1:
        if attr not in attrs2:
            return True

    return False


def filter_module_to_show_differences(module, other_module):
    """Filter a module to show only differences compared to another module."""
    import copy

    filtered = copy.deepcopy(module)

    other_classes_map = {cls["name"]: cls for cls in other_module["classes"]}
    other_funcs_set = {func["name"] for func in other_module["functions"]}
    other_consts_set = {const["name"] for const in other_module["constants"]}

    # Filter classes: keep only those that don't exist in other or have different content
    filtered_classes = []
    for cls in filtered["classes"]:
        other_class = other_classes_map.get(cls["name"])
        if not other_class:
            # Class only in this module, keep as is
            filtered_classes.append(cls)
        else:
            # Class in both, filter to show only differences
            filtered_class = filter_class_to_show_differences(cls, other_class)
            if filtered_class["methods"] or filtered_class["attributes"]:
                filtered_classes.append(filtered_class)

    filtered["classes"] = filtered_classes

    # Filter functions: keep only those not in other module
    filtered["functions"] = [func for func in filtered["functions"] if func["name"] not in other_funcs_set]

    # Filter constants: keep only those not in other module
    filtered["constants"] = [const for const in filtered["constants"] if const["name"] not in other_consts_set]

    return filtered


def filter_class_to_show_differences(class1, class2):
    """Filter a class to show only differences compared to another class."""
    import copy

    filtered = copy.deepcopy(class1)

    methods2_names = {method["name"] for method in class2["methods"]}
    attrs2_names = {attr["name"] for attr in class2["attributes"]}

    # Keep only methods that are different (not in class2)
    filtered["methods"] = [method for method in filtered["methods"] if method["name"] not in methods2_names]

    # Keep only attributes that are different
    filtered["attributes"] = [attr for attr in filtered["attributes"] if attr["name"] not in attrs2_names]

    return filtered


def calculate_comparison_stats(modules1, modules2):
    """Calculate statistics for differences at all three levels."""
    module_names1 = {module["name"] for module in modules1}
    module_names2 = {module["name"] for module in modules2}

    common_names = module_names1 & module_names2
    unique_names1 = module_names1 - module_names2
    unique_names2 = module_names2 - module_names1

    # Level 1: Module differences
    level1 = {
        "total1": len(modules1),
        "total2": len(modules2),
        "unique1": len(unique_names1),
        "unique2": len(unique_names2),
        "common": len(common_names),
    }

    # Level 2: Direct children differences (classes, functions, constants)
    level2 = {
        "classes1_unique": 0,
        "classes2_unique": 0,
        "functions1_unique": 0,
        "functions2_unique": 0,
        "constants1_unique": 0,
        "constants2_unique": 0,
        "classes_different": 0,
        "functions_different": 0,
        "constants_different": 0,
    }

    # Level 3: Class members differences (methods, attributes)
    level3 = {
        "methods1_unique": 0,
        "methods2_unique": 0,
        "attributes1_unique": 0,
        "attributes2_unique": 0,
        "methods_different": 0,
        "attributes_different": 0,
    }

    # For unique modules, count their content
    for module_name in unique_names1:
        mod = next(m for m in modules1 if m["name"] == module_name)
        level2["classes1_unique"] += len(mod["classes"])
        level2["functions1_unique"] += len(mod["functions"])
        level2["constants1_unique"] += len(mod["constants"])

        for cls in mod["classes"]:
            level3["methods1_unique"] += len(cls["methods"])
            level3["attributes1_unique"] += len(cls["attributes"])

    for module_name in unique_names2:
        mod = next(m for m in modules2 if m["name"] == module_name)
        level2["classes2_unique"] += len(mod["classes"])
        level2["functions2_unique"] += len(mod["functions"])
        level2["constants2_unique"] += len(mod["constants"])

        for cls in mod["classes"]:
            level3["methods2_unique"] += len(cls["methods"])
            level3["attributes2_unique"] += len(cls["attributes"])

    # For common modules, compare their content
    for module_name in common_names:
        mod1 = next(m for m in modules1 if m["name"] == module_name)
        mod2 = next(m for m in modules2 if m["name"] == module_name)

        # Compare classes
        classes1_names = {cls["name"] for cls in mod1["classes"]}
        classes2_names = {cls["name"] for cls in mod2["classes"]}

        for class_name in classes1_names:
            if class_name not in classes2_names:
                level2["classes1_unique"] += 1
                cls = next(c for c in mod1["classes"] if c["name"] == class_name)
                level3["methods1_unique"] += len(cls["methods"])
                level3["attributes1_unique"] += len(cls["attributes"])

        for class_name in classes2_names:
            if class_name not in classes1_names:
                level2["classes2_unique"] += 1
                cls = next(c for c in mod2["classes"] if c["name"] == class_name)
                level3["methods2_unique"] += len(cls["methods"])
                level3["attributes2_unique"] += len(cls["attributes"])

        # For classes in both, compare members
        for class_name in classes1_names:
            if class_name in classes2_names:
                cls1 = next(c for c in mod1["classes"] if c["name"] == class_name)
                cls2 = next(c for c in mod2["classes"] if c["name"] == class_name)

                if compare_class_contents(cls1, cls2):
                    level3["methods_different"] += 1

                    methods1_names = {method["name"] for method in cls1["methods"]}
                    methods2_names = {method["name"] for method in cls2["methods"]}

                    for method_name in methods1_names:
                        if method_name not in methods2_names:
                            level3["methods1_unique"] += 1

                    for method_name in methods2_names:
                        if method_name not in methods1_names:
                            level3["methods2_unique"] += 1

                    attrs1_names = {attr["name"] for attr in cls1["attributes"]}
                    attrs2_names = {attr["name"] for attr in cls2["attributes"]}

                    for attr_name in attrs1_names:
                        if attr_name not in attrs2_names:
                            level3["attributes1_unique"] += 1

                    for attr_name in attrs2_names:
                        if attr_name not in attrs1_names:
                            level3["attributes2_unique"] += 1

        # Compare functions
        funcs1_names = {func["name"] for func in mod1["functions"]}
        funcs2_names = {func["name"] for func in mod2["functions"]}

        for func_name in funcs1_names:
            if func_name not in funcs2_names:
                level2["functions1_unique"] += 1

        for func_name in funcs2_names:
            if func_name not in funcs1_names:
                level2["functions2_unique"] += 1

        # Compare constants
        consts1_names = {const["name"] for const in mod1["constants"]}
        consts2_names = {const["name"] for const in mod2["constants"]}

        for const_name in consts1_names:
            if const_name not in consts2_names:
                level2["constants1_unique"] += 1

        for const_name in consts2_names:
            if const_name not in consts1_names:
                level2["constants2_unique"] += 1

    return {"level1": level1, "level2": level2, "level3": level3}


async def compare_boards():
    """Compare two selected boards."""
    # Get board selections
    board1_version = document.getElementById("board1-version").value
    board1_name = document.getElementById("board1").value
    board2_version = document.getElementById("board2-version").value
    board2_name = document.getElementById("board2").value

    # Validate selections
    if not board1_version or not board1_name or not board2_version or not board2_name:
        show_message("compare-results", "Board Comparison", "Please select both version and board for both boards to compare.")
        return

    if not app_state["db"]:
        show_message("compare-results", "Board Comparison", "Database not available for comparison.")
        return

    # Show loading with progress
    show_loading("compare-results", "Preparing comparison...", "Initializing...")

    try:
        # Small delay to show initial message
        await asyncio.sleep(0.5)

        # Find board info
        board1_info = board_utils.find_board_in_list(app_state["boards"], board1_version, board1_name)
        board2_info = board_utils.find_board_in_list(app_state["boards"], board2_version, board2_name)

        if not board1_info or not board2_info:
            show_error("compare-results", "Board Comparison Error", "One or more selected boards could not be found.")
            return

        # Convert to comparison format
        board1 = {"version": board1_version, "port": board1_info[0], "board": board1_info[1]}
        board2 = {"version": board2_version, "port": board2_info[0], "board": board2_info[1]}

        # Update progress for board 1
        show_loading("compare-results", f"Fetching modules for {board1_name}...", "Step 1 of 3")

        print(f"Fetching modules for board 1: {board1}")
        modules1 = get_board_modules(board1)

        # Small delay to show progress
        await asyncio.sleep(0.3)

        # Update progress for board 2
        show_loading("compare-results", f"Fetching modules for {board2_name}...", "Step 2 of 3")

        print(f"Fetching modules for board 2: {board2}")
        modules2 = get_board_modules(board2)

        # Small delay to show progress
        await asyncio.sleep(0.2)

        # Update progress for comparison
        show_loading("compare-results", "Analyzing differences...", "Step 3 of 3")

        # Small delay to show final step
        await asyncio.sleep(0.2)

        print(f"Board 1 has {len(modules1)} modules, Board 2 has {len(modules2)} modules")

        # Store comparison data globally
        comparison_data["board1"] = board1
        comparison_data["board2"] = board2
        comparison_data["modules1"] = modules1
        comparison_data["modules2"] = modules2

        # Update the comparison display
        update_comparison()

    except Exception as e:
        print(f"Error during comparison: {e}")
        show_error("compare-results", "⚠️ Comparison Error", str(e), show_retry=True)


def render_module_tree_dom(modules, options):
    """
    Render module tree using DOM templates instead of HTML strings.

    Args:
        modules: List of module objects
        options: Dict with module_prefix, get_badge_class, get_module_badge, show_details
    """
    show_details = options.get("show_details", True)

    # Create container element
    container = document.createElement("div")
    container.className = "module-tree"

    for module in modules:
        module_element = create_module_item(module, options)
        if module_element and show_details:
            # Add children to module
            children_container = module_element.querySelector("[data-module-children]")
            if children_container:
                # Add classes
                for cls in module.get("classes", []):
                    class_element = create_class_item(cls, module["name"], options.get("module_prefix", "tree"))
                    if class_element:
                        # Add methods and attributes to class
                        class_children = class_element.querySelector("[data-class-children]") 
                        if class_children:
                            # Add methods
                            for method in cls.get("methods", []):
                                method_element = create_method_item(method)
                                if method_element:
                                    class_children.appendChild(method_element)
                            
                            # Add attributes  
                            for attr in cls.get("attributes", []):
                                attr_element = create_attribute_item(attr)
                                if attr_element:
                                    class_children.appendChild(attr_element)
                        
                        children_container.appendChild(class_element)
                
                # Add functions
                for func in module.get("functions", []):
                    func_element = create_function_item(func)
                    if func_element:
                        children_container.appendChild(func_element)
                
                # Add constants
                for const in module.get("constants", []):
                    const_element = create_constant_item(const)
                    if const_element:
                        children_container.appendChild(const_element)
        
        if module_element:
            container.appendChild(module_element)

    return container


def create_method_item(method):
    """Create a method item using template."""
    # Format method signature
    signature = method["name"]
    
    # Build parameter list
    params = ""
    if method.get("parameters"):
        param_strs = []
        for param in method["parameters"]:
            param_str = param["name"]
            
            # Add type hint if available
            if param.get("type_hint") and param["type_hint"] not in ["None", ""]:
                param_str += f": {param['type_hint']}"
            
            # Add default value if available
            if param.get("default_value") and param["default_value"] != "None":
                param_str += f" = {param['default_value']}"
            elif param.get("is_optional"):
                param_str += " = None"
            
            # Handle variadic parameters
            if param.get("is_variadic"):
                param_str = ("**" if param["name"] == "kwargs" else "*") + param_str
            
            param_strs.append(param_str)
        
        params = ", ".join(param_strs)
    
    signature += f"({params})"
    
    # Add return type if available
    if method.get("return_type") and method["return_type"] not in ["None", "", "Any"]:
        signature += f" -> {method['return_type']}"
    
    # Format decorators
    decorators_list = method.get("decorators_list", [])
    if not decorators_list:
        # Fallback to building from boolean flags
        if method.get("is_property"):
            decorators_list.append("property")
        if method.get("is_classmethod"):
            decorators_list.append("classmethod")
        if method.get("is_staticmethod"):
            decorators_list.append("staticmethod")
    
    decorator_strs = [f"@{d}" for d in decorators_list]
    async_marker = "async " if method.get("is_async") else ""
    
    icon_class = "fas fa-ellipsis" if method.get("is_property") else "fas fa-bolt"
    
    decorator_span = f'{" ".join(decorator_strs)} ' if decorator_strs else ""
    
    # Get template and populate
    method_element = get_template("function-item-template")
    if method_element:
        populate_template(method_element, {
            "function-icon": icon_class,
            "decorators": decorator_span,
            "signature": f"{async_marker}{signature}"
        })
    
    return method_element


def create_attribute_item(attr):
    """Create an attribute item using template."""
    type_hint = f": {attr['type_hint']}" if attr.get("type_hint") else ""
    value = f" = {attr['value']}" if attr.get("value") else ""
    
    # Get template and populate
    attr_element = get_template("constant-item-template")
    if attr_element:
        populate_template(attr_element, {
            "constant-signature": f"{attr['name']}{type_hint}{value}"
        })
        
        # Update icon for attributes (use circle-dot instead of circle)
        icon_elem = attr_element.querySelector(".fa-icon")
        if icon_elem:
            icon_elem.className = "fas fa-circle-dot fa-icon"
    
    return attr_element


def render_module_tree_html(modules, options):
    """
    Legacy function that returns HTML string for backward compatibility.
    Consider migrating to render_module_tree_dom for better performance.
    """
    dom_tree = render_module_tree_dom(modules, options)
    return dom_tree.innerHTML if dom_tree else ""


def update_comparison():
    """Update comparison display with current comparison data."""
    if not comparison_data["board1"] or not comparison_data["board2"]:
        return

    print("Updating comparison display...")

    board1 = comparison_data["board1"]
    board2 = comparison_data["board2"]
    modules1 = comparison_data["modules1"]
    modules2 = comparison_data["modules2"]

    # Check if hide common is enabled
    hide_common_checkbox = document.getElementById("hide-common")
    hide_common = hide_common_checkbox.checked if hide_common_checkbox else False

    # Get module names for comparison
    module_names1 = {module["name"] for module in modules1}
    module_names2 = {module["name"] for module in modules2}

    common_names = module_names1 & module_names2
    unique_names1 = module_names1 - module_names2
    unique_names2 = module_names2 - module_names1

    print(f"Common: {len(common_names)}, Unique to 1: {len(unique_names1)}, Unique to 2: {len(unique_names2)}")

    # Calculate comprehensive statistics
    stats = calculate_comparison_stats(modules1, modules2)
    level1, level2, level3 = stats["level1"], stats["level2"], stats["level3"]

    # Get board names for display
    board1_name = format_board_name(board1["port"], board1["board"])
    board2_name = format_board_name(board2["port"], board2["board"])

    # Update stats display
    stats_element = document.getElementById("compare-stats")
    if stats_element:
        stats_element.style.display = "block"

        # Use template for statistics
        stats_template = get_template("stats-template")
        if stats_template:
            stats_template.style.display = "block"
            populate_template(
                stats_template,
                {
                    "board1-name": board1_name,
                    "board2-name": board2_name,
                    "board1-name-footer": board1_name,
                    "board2-name-footer": board2_name,
                    "level1-unique1": level1["unique1"],
                    "level1-common": level1["common"],
                    "level1-unique2": level1["unique2"],
                    "level2-classes1-unique": level2["classes1_unique"],
                    "level2-classes-different": level2["classes_different"],
                    "level2-classes2-unique": level2["classes2_unique"],
                    "level2-functions1-unique": level2["functions1_unique"],
                    "level2-functions2-unique": level2["functions2_unique"],
                    "level2-constants1-unique": level2["constants1_unique"],
                    "level2-constants2-unique": level2["constants2_unique"],
                    "level3-methods1-unique": level3["methods1_unique"],
                    "level3-methods-different": level3["methods_different"],
                    "level3-methods2-unique": level3["methods2_unique"],
                    "level3-attributes1-unique": level3["attributes1_unique"],
                    "level3-attributes2-unique": level3["attributes2_unique"],
                },
            )
            stats_element.innerHTML = ""
            stats_element.appendChild(stats_template)

    # Determine modules to show for each board
    if hide_common:
        # Show only unique modules and common modules with differences
        board1_modules_to_show = []
        board2_modules_to_show = []

        # Add unique modules
        unique_modules1 = [m for m in modules1 if m["name"] in unique_names1]
        unique_modules2 = [m for m in modules2 if m["name"] in unique_names2]

        board1_modules_to_show.extend(unique_modules1)
        board2_modules_to_show.extend(unique_modules2)

        # TODO: Add common modules with differences (filtered)
        # For now, we'll show unique modules only
    else:
        # Show all modules sorted
        board1_modules_to_show = sorted(modules1, key=lambda m: m["name"])
        board2_modules_to_show = sorted(modules2, key=lambda m: m["name"])

    # Use comparison grid template
    comparison_grid = get_template("comparison-grid-template")
    if comparison_grid:
        comparison_grid.style.display = "block"

        # Generate module trees using DOM-based rendering
        board1_tree_dom = render_module_tree_dom(
            board1_modules_to_show,
            {
                "module_prefix": "board1",
                "get_badge_class": lambda module: "unique-to-board1" if module["name"] in unique_names1 else "",
                "get_module_badge": lambda module: " [UNIQUE]" if module["name"] in unique_names1 else "",
                "show_details": True,
            },
        )

        board2_tree_dom = render_module_tree_dom(
            board2_modules_to_show,
            {
                "module_prefix": "board2",
                "get_badge_class": lambda module: "unique-to-board2" if module["name"] in unique_names2 else "",
                "get_module_badge": lambda module: " [UNIQUE]" if module["name"] in unique_names2 else "",
                "show_details": True,
            },
        )

        # Populate board headers
        populate_template(
            comparison_grid,
            {"board1-header": f"{board1_name} ({board1['version']})", "board2-header": f"{board2_name} ({board2['version']})"},
        )

        # Set board modules content using DOM elements
        board1_container = comparison_grid.querySelector("[data-board1-modules]")
        board2_container = comparison_grid.querySelector("[data-board2-modules]")

        if board1_container:
            board1_container.innerHTML = ""  # Clear existing content
            if len(board1_modules_to_show) > 0:
                board1_container.appendChild(board1_tree_dom)
            else:
                # Use template for "No differences" message
                no_diff_elem = get_template("message-template")
                if no_diff_elem:
                    populate_template(no_diff_elem, {
                        "data-show-detail-view": "false",
                        "data-show-simple": "true", 
                        "data-simple-text": "No differences"
                    })
                    board1_container.appendChild(no_diff_elem)

        if board2_container:
            board2_container.innerHTML = ""  # Clear existing content
            if len(board2_modules_to_show) > 0:
                board2_container.appendChild(board2_tree_dom)
            else:
                # Use template for "No differences" message
                no_diff_elem = get_template("message-template")
                if no_diff_elem:
                    populate_template(no_diff_elem, {
                        "data-show-detail-view": "false",
                        "data-show-simple": "true", 
                        "data-simple-text": "No differences"
                    })
                    board2_container.appendChild(no_diff_elem)

        # Handle common modules section
        common_section = comparison_grid.querySelector("[data-common-section]")
        if not hide_common and len(common_names) > 0:
            common_modules = [m for m in modules1 if m["name"] in common_names]
            common_tree_dom = render_module_tree_dom(
                common_modules,
                {
                    "module_prefix": "common",
                    "get_badge_class": lambda module: "",
                    "get_module_badge": lambda module: "",
                    "show_details": True,
                },
            )

            populate_template(comparison_grid, {"common-header": f"Common Modules ({len(common_names)})"})

            common_container = comparison_grid.querySelector("[data-common-modules]")
            if common_container and common_tree_dom:
                common_container.innerHTML = ""  # Clear existing content
                common_container.appendChild(common_tree_dom)

            if common_section:
                common_section.style.display = "block"
        else:
            if common_section:
                common_section.style.display = "none"

        # Update the comparison results display
        results = document.getElementById("compare-results")
        results.innerHTML = ""
        results.appendChild(comparison_grid)

    print("Comparison display updated")


async def search_apis():
    """Search for APIs across boards."""
    search_input = document.getElementById("search-input")
    search_term = search_input.value.strip()

    if not search_term:
        show_message("search-results", "Search Results", "Enter a search term to find modules, classes, methods, functions, or constants.")
        return

    if not app_state["db"]:
        show_error("search-results", "Search Error", "Database not loaded. Please wait for the application to initialize.")
        return

    # Show loading
    show_loading("search-results", f'Searching for "{search_term}"...', "Scanning database...")

    try:
        # Allow UI update
        await asyncio.sleep(0.1)

        search_results = await perform_search(search_term)
        display_search_results(search_results, search_term)

    except Exception as e:
        show_error("search-results", "Search Error", f"Error performing search: {str(e)}")


async def perform_search(search_term):
    """Perform comprehensive search across all database entities."""
    if not app_state["db"]:
        print("Database not available for search")
        return []

    # Use LIKE with wildcards for flexible matching
    search_pattern = f"%{search_term}%"
    results = []

    print(f"Starting search for: '{search_term}' with pattern: '{search_pattern}'")

    # First check if we have any data at all
    try:
        count_stmt = app_state["db"].prepare("SELECT COUNT(*) as count FROM unique_modules")
        count_stmt.step()
        module_count = count_stmt.getAsObject()["count"]
        count_stmt.free()
        print(f"Total modules in database: {module_count}")

        # Show some sample module names for debugging
        sample_stmt = app_state["db"].prepare("SELECT name FROM unique_modules LIMIT 10")
        sample_names = []
        while sample_stmt.step():
            name = sample_stmt.getAsObject()["name"]
            sample_names.append(name)
            # Print each name individually to see exact content
            print(f"Raw module name: '{name}' (len: {len(name)}, chars: {[ord(c) for c in name[:20]]})")
        sample_stmt.free()
        print(f"Sample module names: {sample_names}")

        # Test exact match for first module
        if sample_names:
            first_module = sample_names[0]
            print(f"Testing with first module: '{first_module}' (type: {type(first_module)}, len: {len(first_module)})")

            # Test different query approaches
            test_stmt = app_state["db"].prepare("SELECT COUNT(*) as count FROM unique_modules WHERE name = ?")
            test_stmt.bind([first_module])
            test_stmt.step()
            exact_count = test_stmt.getAsObject()["count"]
            test_stmt.free()
            print(f"Exact match count for '{first_module}': {exact_count}")

            # Try a simple SELECT to see what we get
            debug_stmt = app_state["db"].prepare("SELECT name FROM unique_modules WHERE name = ? LIMIT 1")
            debug_stmt.bind([first_module])
            if debug_stmt.step():
                found_name = debug_stmt.getAsObject()["name"]
                print(f"Found exact name: '{found_name}' (type: {type(found_name)})")
                print(f"Comparison: '{first_module}' == '{found_name}': {first_module == found_name}")
            else:
                print("No exact match found in debug query")
            debug_stmt.free()

            # Test LIKE query for search term
            test_like_stmt = app_state["db"].prepare("SELECT COUNT(*) as count FROM unique_modules WHERE name LIKE ?")
            test_like_stmt.bind([search_pattern])
            test_like_stmt.step()
            like_search_count = test_like_stmt.getAsObject()["count"]
            test_like_stmt.free()
            print(f"LIKE match count for search pattern '{search_pattern}': {like_search_count}")
    except Exception as e:
        print(f"Error counting modules: {e}")

    try:
        # Search modules - try a simpler approach first
        print("Searching modules...")

        # First try without any LIKE pattern - just get all modules and filter in Python
        all_modules_stmt = app_state["db"].prepare("""
            SELECT DISTINCT 
                um.name as entity_name,
                'module' as entity_type,
                b.version, b.port, b.board,
                um.id as module_id,
                NULL as class_id,
                NULL as parent_name
            FROM unique_modules um
            JOIN board_module_support bms ON um.id = bms.module_id
            JOIN boards b ON bms.board_id = b.id  
            ORDER BY b.version DESC, b.port, b.board, um.name
        """)

        all_modules = []
        while all_modules_stmt.step():
            result_obj = all_modules_stmt.getAsObject()
            # Convert to regular Python dict to avoid JS proxy issues
            result = {
                "entity_name": result_obj["entity_name"],
                "entity_type": result_obj["entity_type"],
                "version": result_obj["version"],
                "port": result_obj["port"],
                "board": result_obj["board"],
                "module_id": result_obj["module_id"],
                "class_id": result_obj["class_id"],
                "parent_name": result_obj["parent_name"],
            }
            all_modules.append(result)
        all_modules_stmt.free()

        print(f"Retrieved {len(all_modules)} total module entries")

        # Filter in Python for case-insensitive search
        search_term_lower = search_term.lower()
        module_matches = []
        for module in all_modules:
            if search_term_lower in module["entity_name"].lower():
                module_matches.append(module)
                # Debug: Print first few matches
                if len(module_matches) <= 3:
                    print(
                        f"Match {len(module_matches)}: {module['entity_name']} (ID: {module['module_id']}, port: {module['port']}, board: {module['board']})"
                    )

        print(f"Found {len(module_matches)} modules matching '{search_term}' after Python filtering")
        results.extend(module_matches)

        # Search classes
        stmt = app_state["db"].prepare("""
            SELECT DISTINCT
                uc.name as entity_name,
                'class' as entity_type,
                b.version, b.port, b.board,
                um.id as module_id,
                uc.id as class_id,
                um.name as parent_name
            FROM unique_classes uc
            JOIN unique_modules um ON uc.module_id = um.id
            JOIN board_class_support bcs ON uc.id = bcs.class_id
            JOIN boards b ON bcs.board_id = b.id
            WHERE uc.name LIKE ? COLLATE NOCASE
            ORDER BY b.version DESC, b.port, b.board, um.name, uc.name
        """)

        stmt.bind([search_pattern])
        while stmt.step():
            results.append(dict(stmt.getAsObject()))
        stmt.free()

        # Search methods
        stmt = app_state["db"].prepare("""
            SELECT DISTINCT
                umet.name as entity_name,
                'method' as entity_type,
                b.version, b.port, b.board,
                um.id as module_id,
                uc.id as class_id,
                uc.name as parent_name
            FROM unique_methods umet
            JOIN unique_classes uc ON umet.class_id = uc.id
            JOIN unique_modules um ON uc.module_id = um.id
            JOIN board_method_support bmets ON umet.id = bmets.method_id
            JOIN boards b ON bmets.board_id = b.id
            WHERE umet.name LIKE ? COLLATE NOCASE
            ORDER BY b.version DESC, b.port, b.board, um.name, uc.name, umet.name
        """)

        stmt.bind([search_pattern])
        while stmt.step():
            results.append(dict(stmt.getAsObject()))
        stmt.free()

        # Search module constants
        stmt = app_state["db"].prepare("""
            SELECT DISTINCT
                umc.name as entity_name,
                'constant' as entity_type,
                b.version, b.port, b.board,
                um.id as module_id,
                NULL as class_id,
                um.name as parent_name
            FROM unique_module_constants umc
            JOIN unique_modules um ON umc.module_id = um.id
            JOIN board_module_constant_support bmcs ON umc.id = bmcs.constant_id
            JOIN boards b ON bmcs.board_id = b.id
            WHERE umc.name LIKE ? COLLATE NOCASE
            ORDER BY b.version DESC, b.port, b.board, um.name, umc.name
        """)

        stmt.bind([search_pattern])
        while stmt.step():
            results.append(dict(stmt.getAsObject()))
        stmt.free()

        # Search class attributes
        stmt = app_state["db"].prepare("""
            SELECT DISTINCT
                uca.name as entity_name,
                'attribute' as entity_type,
                b.version, b.port, b.board,
                um.id as module_id,
                uc.id as class_id,
                uc.name as parent_name
            FROM unique_class_attributes uca
            JOIN unique_classes uc ON uca.class_id = uc.id
            JOIN unique_modules um ON uc.module_id = um.id
            JOIN board_class_attribute_support bcas ON uca.id = bcas.attribute_id
            JOIN boards b ON bcas.board_id = b.id
            WHERE uca.name LIKE ? COLLATE NOCASE
            ORDER BY b.version DESC, b.port, b.board, um.name, uc.name, uca.name
        """)

        stmt.bind([search_pattern])
        while stmt.step():
            results.append(dict(stmt.getAsObject()))
        stmt.free()

        # Search parameters
        stmt = app_state["db"].prepare("""
            SELECT DISTINCT
                up.name as entity_name,
                'parameter' as entity_type,
                b.version, b.port, b.board,
                um.id as module_id,
                uc.id as class_id,
                umet.name as parent_name
            FROM unique_parameters up
            JOIN unique_methods umet ON up.method_id = umet.id
            JOIN unique_classes uc ON umet.class_id = uc.id
            JOIN unique_modules um ON uc.module_id = um.id
            JOIN board_method_support bmets ON umet.id = bmets.method_id
            JOIN boards b ON bmets.board_id = b.id
            WHERE up.name LIKE ? COLLATE NOCASE
            ORDER BY b.version DESC, b.port, b.board, um.name, uc.name, umet.name, up.name
        """)

        stmt.bind([search_pattern])
        while stmt.step():
            results.append(dict(stmt.getAsObject()))
        stmt.free()

    except Exception as e:
        print(f"Search error: {e}")
        return []

    return results


def display_search_results(results, search_term):
    """Display search results using templates."""
    results_div = document.getElementById("search-results")

    if not results:
        # Use no results template
        no_results_element = get_template("message-template")
        if no_results_element:
            no_results_element.style.display = "block"
            
            # Set content directly to avoid HTML encoding issues
            header_element = no_results_element.querySelector("[data-message-header]")
            content_element = no_results_element.querySelector("[data-message-content]")
            subtitle_element = no_results_element.querySelector("[data-message-subtitle]")
            
            if header_element:
                header_element.textContent = "Search Results"
            if content_element:
                content_element.innerHTML = f'No results found for "<strong>{search_term}</strong>"'
            if subtitle_element:
                subtitle_element.textContent = "Try a different search term or check spelling."
                
            # Show the detail view
            detail_view = no_results_element.querySelector("[data-show-detail-view]")
            if detail_view:
                detail_view.style.display = "block"
                
            results_div.innerHTML = ""
            results_div.appendChild(no_results_element)
        return

    # Group results by entity type for better organization
    grouped_results = {}
    for result in results:
        entity_type = result["entity_type"]
        if entity_type not in grouped_results:
            grouped_results[entity_type] = []
        grouped_results[entity_type].append(result)

    # Use search results template
    search_results_element = get_template("search-results-template")
    if search_results_element:
        search_results_element.style.display = "block"
        
        # Set the HTML content directly instead of using data attributes
        summary_element = search_results_element.querySelector("[data-search-summary]")
        if summary_element:
            summary_element.innerHTML = f'Found <strong>{len(results)}</strong> results for "<strong>{search_term}</strong>"'

        # Get categories container
        categories_container = search_results_element.querySelector("[data-search-categories]")
        if categories_container:
            # Sort entity types for consistent display
            entity_order = ["module", "class", "function", "method", "constant", "attribute", "parameter"]
            type_labels = {
                "module": "Modules",
                "class": "Classes", 
                "function": "Functions",
                "method": "Methods",
                "constant": "Constants",
                "attribute": "Attributes",
                "parameter": "Parameters",
            }

            for entity_type in entity_order:
                if entity_type in grouped_results:
                    type_results = grouped_results[entity_type]
                    
                    # Create category section
                    category_element = get_template("search-category-template")
                    if category_element:
                        populate_template(category_element, {
                            "category-icon": get_entity_icon(entity_type),
                            "category-title": f"{type_labels[entity_type]} ({len(type_results)})"
                        })

                        # Get results container for this category
                        category_results = category_element.querySelector("[data-category-results]")
                        if category_results:
                            for result in type_results:
                                # Create individual result item
                                result_element = create_search_result_item(result, entity_type)
                                if result_element:
                                    category_results.appendChild(result_element)

                        categories_container.appendChild(category_element)

        # Update the search results display
        results_div.innerHTML = ""
        results_div.appendChild(search_results_element)


def create_search_result_item(result, entity_type):
    """Create a search result item using template."""
    board_name = format_board_name(result["port"], result["board"])
    context_path = get_context_path(result)
    
    # Use search result template
    result_element = get_template("search-result-item-template")
    if result_element:
        # Populate template data
        populate_template(result_element, {
            "entity-name": result["entity_name"],
            "context-path": context_path,
            "board-name": board_name,
            "version": result['version']
        })
        
        # Set entity icon
        icon_elem = result_element.querySelector("[data-entity-icon]")
        if icon_elem:
            icon_elem.className = f"fas {get_entity_icon(entity_type)}"
        
        # Set click handler
        module_id = result["module_id"]
        class_id = result.get("class_id", "")
        entity_name = result["entity_name"]
        
        def click_handler(e):
            # Call openSearchResult if it exists
            if hasattr(window, "openSearchResult"):
                window.openSearchResult(module_id, class_id, entity_name, entity_type)
        
        result_element.onclick = click_handler
    
    return result_element


def get_entity_icon(entity_type):
    """Get appropriate Font Awesome icon for entity type."""
    icons = {
        "module": "fa-cube",
        "class": "fa-object-group",
        "function": "fa-code",
        "method": "fa-cog",
        "constant": "fa-hashtag",
        "attribute": "fa-tag",
        "parameter": "fa-list",
    }
    return icons.get(entity_type, "fa-question")


def get_context_path(result):
    """Get the context path for a search result."""
    module_name = result.get("parent_name", "")

    if result["entity_type"] == "module":
        return "Module"
    elif result["entity_type"] == "class":
        return f"in {module_name}"
    elif result["entity_type"] == "function":
        return f"in {module_name}"
    elif result["entity_type"] == "method":
        return f"in {module_name}.{result['parent_name']}"
    elif result["entity_type"] == "constant":
        return f"in {module_name}"
    elif result["entity_type"] == "attribute":
        return f"in {module_name}.{result['parent_name']}"
    elif result["entity_type"] == "parameter":
        parent = result.get("parent_name", "")
        if result.get("class_id"):
            return f"in {module_name}.{parent}()"
        else:
            return f"in {module_name}.{parent}()"

    return ""


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


async def load_board_details():
    """Load board details when a board is selected."""
    version_select = document.getElementById("explorer-version")
    board_select = document.getElementById("explorer-board")

    selected_version = version_select.value
    selected_board_name = board_select.value

    content = document.getElementById("explorer-content")

    if not selected_version or not selected_board_name:
        # Use template for selection prompt
        select_prompt = get_template("message-template")
        if select_prompt:
            populate_template(select_prompt, {
                "data-show-detail-view": "false",
                "data-show-loading": "true",
                "data-simple-message": "Select both version and board to explore modules and APIs"
            })
            content.innerHTML = ""
            content.appendChild(select_prompt)
        else:
            content.innerHTML = '<div class="loading"><p>Select both version and board to explore modules and APIs</p></div>'
        return

    # Show loading using template
    loading_template = get_template("loading-template")
    if loading_template:
        populate_template(loading_template, {
            "data-show-spinner": "false",
            "data-show-progress": "true",
            "data-loading-text": "Loading board details..."
        })
        content.innerHTML = ""
        content.appendChild(loading_template)
    else:
        # Fallback loading HTML
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

        # Use template-based board details
        board_details = get_template("board-details-template")
        if board_details:
            # Populate header information
            populate_template(board_details, {
                "board-title": f"{selected_board_name} ({selected_version})"
            })
            
            # Create module tree using DOM-based rendering
            options = {
                "module_prefix": "explorer",
                "get_badge_class": lambda m: "",
                "get_module_badge": lambda m: "",
                "show_details": True
            }
            
            module_tree_dom = render_module_tree_dom(modules, options)
            
            # Use board content template
            board_content_template = get_template("board-content-template")
            if board_content_template:
                # Populate template data
                populate_template(board_content_template, {
                    "modules-title": f"Modules ({len(modules)})"
                })
                
                # Add module tree to template
                modules_tree_container = board_content_template.querySelector("[data-modules-tree]")
                if modules_tree_container and module_tree_dom:
                    modules_tree_container.appendChild(module_tree_dom)
                
                # Add content to board details
                board_content = board_details.querySelector("[data-board-content]")
                if board_content:
                    board_content.appendChild(board_content_template)
            
            # Clear and update content
            content.innerHTML = ""
            content.appendChild(board_details)

    except Exception as e:
        # Use error template instead of inline HTML
        error_template = get_template("error-template")
        if error_template:
            populate_template(error_template, {
                "data-error-message": str(e),
                "data-error-details": f"{type(e).__name__}: {str(e)}",
                "data-error-icon": "true"
            })
            content.innerHTML = ""
            content.appendChild(error_template)
        else:
            # Fallback if template not found
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


# Searchable dropdown functionality (MicroPython compatible)
def make_dropdown_searchable(select_id):
    """Convert a select element to a searchable combobox for MicroPython"""
    import js

    select_element = js.document.getElementById(select_id)
    if not select_element:
        return

    # Store original options (simplified for MicroPython)
    original_options = []
    options = select_element.options
    for i in range(options.length):
        option = options[i]
        original_options.append({"value": str(option.value), "text": str(option.textContent), "selected": bool(option.selected)})

    # Create wrapper container
    wrapper = js.document.createElement("div")
    wrapper.className = "combobox-wrapper"

    # Determine if this is a version select
    is_version_select = "version" in select_id
    if is_version_select:
        wrapper.style.width = "160px"

    # Create search input
    search_input = js.document.createElement("input")
    search_input.type = "text"
    search_input.className = "combobox-input"

    # Set placeholder based on field type
    if is_version_select:
        search_input.placeholder = "Version..."
    else:
        label_text = str(select_element.previousElementSibling.textContent).lower()
        search_input.placeholder = f"Type to search {label_text}..."

    if is_version_select:
        search_input.style.width = "160px"

    # Create dropdown arrow
    arrow = js.document.createElement("div")
    arrow.innerHTML = "▼"
    arrow.className = "combobox-arrow"

    # Create dropdown list
    dropdown = js.document.createElement("div")
    dropdown.className = "combobox-dropdown"

    # Replace select with wrapper
    select_element.parentNode.insertBefore(wrapper, select_element)
    wrapper.appendChild(search_input)
    wrapper.appendChild(arrow)
    wrapper.appendChild(dropdown)
    select_element.style.display = "none"

    # State variables (using global dict to avoid closure issues)
    state = {"is_open": False, "selected_value": str(select_element.value), "filtered_options": original_options[:]}

    def update_display_value():
        state["selected_value"] = str(select_element.value)
        selected_option = None
        for opt in original_options:
            if opt["value"] == state["selected_value"]:
                selected_option = opt
                break

        if selected_option and selected_option["value"] != "":
            search_input.value = selected_option["text"]
            search_input.style.color = "#000"
        else:
            search_input.value = ""
            search_input.style.color = "#666"

    def populate_dropdown(options=None):
        if options is None:
            options = state["filtered_options"]

        dropdown.innerHTML = ""
        current_value = str(select_element.value)

        if len(options) == 0:
            no_results = js.document.createElement("div")
            no_results.textContent = "No matches found"
            no_results.style.cssText = "padding: 8px; color: #666; font-style: italic;"
            dropdown.appendChild(no_results)
            return

        for option in options:
            if option["value"] == "":
                continue  # Skip default option

            item = js.document.createElement("div")
            item.textContent = option["text"]
            item.setAttribute("data-value", option["value"])

            if option["value"] == current_value:
                item.classList.add("selected")

            # Store option value on element for click handler
            item._option_value = option["value"]
            dropdown.appendChild(item)

    def open_dropdown():
        if state["is_open"]:
            return
        state["is_open"] = True
        dropdown.style.display = "block"
        populate_dropdown()
        search_input.style.borderRadius = "4px 4px 0 0"

    def close_dropdown():
        if not state["is_open"]:
            return
        state["is_open"] = False
        dropdown.style.display = "none"
        search_input.style.borderRadius = "4px"
        update_display_value()

    def filter_options(search_term):
        if not search_term.strip():
            state["filtered_options"] = original_options[:]
        else:
            state["filtered_options"] = []
            search_lower = search_term.lower()
            for option in original_options:
                if option["value"] != "" and search_lower in option["text"].lower():
                    state["filtered_options"].append(option)
        populate_dropdown()

    # Set up event handlers using JavaScript (MicroPython approach)
    # Replace hyphens with underscores for valid JavaScript function names
    js_safe_id = select_id.replace("-", "_")

    js.eval(f"""
    (function() {{
        const searchInput = document.getElementById('{select_id}').parentNode.querySelector('.combobox-input');
        const dropdown = searchInput.parentNode.querySelector('.combobox-dropdown');
        const wrapper = searchInput.parentNode;
        const select = document.getElementById('{select_id}');
        
        searchInput.addEventListener('focus', function() {{
            window.micropython_dropdown_{js_safe_id}_open();
        }});
        
        searchInput.addEventListener('input', function(e) {{
            window.micropython_dropdown_{js_safe_id}_filter(e.target.value);
        }});
        
        searchInput.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape') {{
                window.micropython_dropdown_{js_safe_id}_close();
            }} else if (e.key === 'Enter') {{
                e.preventDefault();
                window.micropython_dropdown_{js_safe_id}_enter();
            }}
        }});
        
        dropdown.addEventListener('click', function(e) {{
            if (e.target._option_value) {{
                window.micropython_dropdown_{js_safe_id}_select(e.target._option_value);
            }}
        }});
        
        document.addEventListener('click', function(e) {{
            if (!wrapper.contains(e.target)) {{
                window.micropython_dropdown_{js_safe_id}_close();
            }}
        }});
    }})();
    """)

    # Expose Python functions to JavaScript
    def js_open():
        open_dropdown()

    def js_close():
        close_dropdown()

    def js_filter(term):
        if not state["is_open"]:
            open_dropdown()
        filter_options(str(term))

    def js_enter():
        visible_options = [opt for opt in state["filtered_options"] if opt["value"] != ""]
        if len(visible_options) == 1:
            js_select(visible_options[0]["value"])

    def js_select(value):
        state["selected_value"] = str(value)
        select_element.value = state["selected_value"]
        # Trigger change event
        change_event = js.document.createEvent("Event")
        change_event.initEvent("change", True, True)
        select_element.dispatchEvent(change_event)
        update_display_value()
        close_dropdown()

    # Register functions with JavaScript window object
    js.window[f"micropython_dropdown_{js_safe_id}_open"] = js_open
    js.window[f"micropython_dropdown_{js_safe_id}_close"] = js_close
    js.window[f"micropython_dropdown_{js_safe_id}_filter"] = js_filter
    js.window[f"micropython_dropdown_{js_safe_id}_enter"] = js_enter
    js.window[f"micropython_dropdown_{js_safe_id}_select"] = js_select

    # Initialize display
    update_display_value()

    return wrapper


def initialize_searchable_dropdowns():
    """Initialize searchable dropdowns for comparison selects"""
    dropdown_ids = ["board1-version", "board1", "board2-version", "board2"]
    for select_id in dropdown_ids:
        make_dropdown_searchable(select_id)


def update_board_options(version_id, board_id):
    """Update board options based on version selection"""
    # This will be called when version changes
    pass


def update_version_options(version_id, board_id):
    """Update version options based on board selection"""
    # This will be called when board changes
    pass


def update_comparison_url():
    """Update URL with current comparison parameters (MicroPython compatible)"""

    try:
        board1_version = str(js.document.getElementById("board1-version").value)
        board1 = str(js.document.getElementById("board1").value)
        board2_version = str(js.document.getElementById("board2-version").value)
        board2 = str(js.document.getElementById("board2").value)
        hide_common = bool(js.document.getElementById("hide-common").checked)

        # Build URL parameters
        params = ["view=compare"]

        if board1:
            params.append(f"board1={board1}")
        if board1_version:
            params.append(f"version1={board1_version}")
        if board2:
            params.append(f"board2={board2}")
        if board2_version:
            params.append(f"version2={board2_version}")
        if hide_common:
            params.append("diff=true")

        # Update URL without page reload using JavaScript
        params_str = "&".join(params)
        js.eval(f"""
        (function() {{
            const newUrl = window.location.pathname + '?{params_str}';
            window.history.replaceState({{}}, '', newUrl);
        }})();
        """)

    except Exception as e:
        print(f"Error updating comparison URL: {e}")


def share_comparison():
    """Share current comparison by copying URL to clipboard (MicroPython compatible)"""

    try:
        current_url = str(js.window.location.href)

        # Try modern clipboard API first, fallback to older method
        js.eval(f"""
        (function() {{
            const url = '{current_url}';
            if (navigator.clipboard && navigator.clipboard.writeText) {{
                navigator.clipboard.writeText(url).then(function() {{
                    window.micropython_share_success();
                }}).catch(function() {{
                    window.micropython_share_fallback(url);
                }});
            }} else {{
                window.micropython_share_fallback(url);
            }}
        }})();
        """)

    except Exception as e:
        print(f"Error sharing comparison: {e}")
        update_status("Failed to copy link to clipboard", "error")


def share_success():
    """Called when clipboard copy succeeds"""
    import js

    try:
        share_btn = js.document.querySelector(".share-btn")
        original_text = str(share_btn.innerHTML)
        share_btn.innerHTML = '<span class="share-icon">✓</span> Copied!'

        # Restore text after 2 seconds
        js.setTimeout(lambda: setattr(share_btn, "innerHTML", original_text), 2000)
    except Exception as e:
        print(f"Error updating share button: {e}")


def share_fallback(url):
    """Fallback for older browsers"""
    import js

    try:
        # Create temporary textarea for copying
        js.eval(f"""
        (function() {{
            const textarea = document.createElement('textarea');
            textarea.value = '{url}';
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand('copy');
            document.body.removeChild(textarea);
            window.micropython_share_success();
        }})();
        """)
    except Exception as e:
        print(f"Error with fallback copy: {e}")
        update_status("Failed to copy link to clipboard", "error")


# Toggle functions for expandable tree functionality
def toggle_module(module_id, event):
    """Toggle module expansion."""
    event.stopPropagation()
    element = document.getElementById(module_id)
    if element:
        if element.classList.contains("hidden"):
            element.classList.remove("hidden")
        else:
            element.classList.add("hidden")


def toggle_class(class_id, event):
    """Toggle class expansion."""
    event.stopPropagation()
    element = document.getElementById(class_id)
    if element:
        if element.classList.contains("hidden"):
            element.classList.remove("hidden")
        else:
            element.classList.add("hidden")


async def open_search_result(module_id, class_id, entity_name, entity_type):
    """Open a module viewer with the search result highlighted."""
    print(f"Opening search result: {entity_name} ({entity_type}) in module {module_id}")
    print(f"Debug search result data: module_id={module_id} (type: {type(module_id)})")

    # Switch to explorer tab first
    switch_page("explorer")

    # Get board info for this module
    if not app_state["db"]:
        print("Database not available")
        return

    try:
        # Get board information for this module using the normalized schema
        # First get the module name from unique_modules
        print(f"Looking for module with ID: {module_id} (type: {type(module_id)})")

        # Ensure module_id is an integer
        module_id_int = int(module_id)
        print(f"Converted to int: {module_id_int}")

        module_stmt = app_state["db"].prepare("SELECT name FROM unique_modules WHERE id = ?")
        module_stmt.bind(ffi.to_js([module_id_int]))

        if not module_stmt.step():
            print("Module not found")
            # Debug: Let's see what IDs actually exist
            debug_stmt = app_state["db"].prepare("SELECT id, name FROM unique_modules LIMIT 10")
            print("Sample module IDs in database:")
            while debug_stmt.step():
                row = debug_stmt.getAsObject()
                print(f"  ID: {row['id']}, Name: {row['name']}")
            debug_stmt.free()
            module_stmt.free()
            return

        module_name = module_stmt.getAsObject()["name"]
        module_stmt.free()
        print(f"Found module: {module_name}")
        print(f"Found module: {module_name}")

        # Now get board information through the junction table
        stmt = app_state["db"].prepare("""
            SELECT DISTINCT b.version, b.port, b.board
            FROM unique_modules um
            JOIN board_module_support bms ON um.id = bms.module_id
            JOIN boards b ON bms.board_id = b.id
            WHERE um.id = ?
            LIMIT 1
        """)
        stmt.bind(ffi.to_js([module_id_int]))

        if not stmt.step():
            print("Board not found for module")
            stmt.free()
            return

        board_info = stmt.getAsObject()
        stmt.free()

        # Set the explorer dropdowns to match this board
        version_select = document.getElementById("explorer-version")
        board_select = document.getElementById("explorer-board")

        # Set version
        version_select.value = board_info["version"]

        # Set board (need to format the board name)
        board_name = format_board_name(board_info["port"], board_info["board"])
        board_select.value = board_name

        # Load the board details which will show all modules
        await load_board_details()

        # After loading, try to highlight the specific element
        await asyncio.sleep(0.5)  # Give time for content to load
        await highlight_search_target(module_id, class_id, entity_name, entity_type)

    except Exception as e:
        print(f"Error opening search result: {e}")


async def highlight_search_target(module_id, class_id, entity_name, entity_type):
    """Highlight the specific search target in the loaded content."""
    module_name = ""
    try:
        # Get module name first using normalized schema
        module_id_int = int(module_id) if module_id else None
        if module_id_int:
            stmt = app_state["db"].prepare("SELECT name FROM unique_modules WHERE id = ?")
            stmt.bind(ffi.to_js([module_id_int]))
            if not stmt.step():
                stmt.free()
                return
            module_name = stmt.getAsObject()["name"]
            stmt.free()

        # Find and expand the target module
        module_element_id = f"module-{module_name}"
        module_element = document.getElementById(module_element_id)

        if module_element:
            # Expand the module if it's collapsed
            if "hidden" in module_element.classList:
                module_element.classList.remove("hidden")

            # If targeting a class or its members, expand the class too
            if class_id and (entity_type in ["class", "method", "attribute"]):
                stmt = app_state["db"].prepare("SELECT name FROM classes WHERE id = ?")
                stmt.bind([class_id])
                if stmt.step():
                    class_name = stmt.getAsObject()["name"]
                    class_element_id = f"class-{module_name}-{class_name}"
                    class_element = document.getElementById(class_element_id)
                    if class_element and "hidden" in class_element.classList:
                        class_element.classList.remove("hidden")
                stmt.free()

            # Scroll to the module
            module_element.scrollIntoView({"behavior": "smooth", "block": "center"})

            # Add temporary highlight effect
            module_element.style.backgroundColor = "#fff3cd"
            module_element.style.border = "2px solid #ffc107"

            # Remove highlight after 3 seconds
            def remove_highlight():
                module_element.style.backgroundColor = ""
                module_element.style.border = ""

            # Use JavaScript setTimeout for the delay
            js.window.setTimeout(remove_highlight, 3000)

        print(f"Highlighted {entity_name} in module {module_name}")

    except Exception as e:
        print(f"Error highlighting search target: {e}")


# Register functions with JavaScript
js.window["micropython_share_success"] = share_success
js.window["micropython_share_fallback"] = share_fallback
js.window["toggleModule"] = toggle_module
js.window["toggleClass"] = toggle_class
js.window["openSearchResult"] = open_search_result


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

        # Initialize searchable dropdowns after populating selects
        initialize_searchable_dropdowns()

        # Check URL parameters and auto-switch to comparison mode if needed
        url = js.eval("new URL(window.location.href)")

        # Get individual parameters using URLSearchParams.get() method
        search_params = url.searchParams
        view = search_params.get("view")

        if view == "compare":
            # Switch to comparison mode
            switch_page("compare")

        update_status("Loaded database. Application ready!", "success")
    else:
        # Database is required
        update_status("Failed to load database. Cannot continue.", "error")


# Start the application


asyncio.create_task(main())
