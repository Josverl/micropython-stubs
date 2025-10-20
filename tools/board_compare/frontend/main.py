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

    # Search button
    search_btn = document.getElementById("search-btn")
    if search_btn:
        search_btn.onclick = lambda e: search_apis()

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
        board1_version.onchange = make_comparison_change_handler('board1-version', 'board1')
    
    board1 = document.getElementById("board1")
    if board1:
        board1.onchange = make_board_change_handler_comparison('board1-version', 'board1')
    
    board2_version = document.getElementById("board2-version")
    if board2_version:
        board2_version.onchange = make_comparison_change_handler('board2-version', 'board2')
    
    board2 = document.getElementById("board2")
    if board2:
        board2.onchange = make_board_change_handler_comparison('board2-version', 'board2')
    
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
        "common": len(common_names)
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
        "constants_different": 0
    }
    
    # Level 3: Class members differences (methods, attributes)
    level3 = {
        "methods1_unique": 0,
        "methods2_unique": 0,
        "attributes1_unique": 0,
        "attributes2_unique": 0,
        "methods_different": 0,
        "attributes_different": 0
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
    
    results = document.getElementById("compare-results")
    
    # Validate selections
    if not board1_version or not board1_name or not board2_version or not board2_name:
        results.innerHTML = """
        <div class="detail-view">
            <div class="detail-header">Board Comparison</div>
            <p style="color: #666;">Please select both version and board for both boards to compare.</p>
        </div>
        """
        return
    
    if not app_state["db"]:
        results.innerHTML = """
        <div class="detail-view">
            <div class="detail-header">Board Comparison</div>
            <p style="color: #dc3545;">Database not available for comparison.</p>
        </div>
        """
        return
    
    # Show loading with progress
    results.innerHTML = """
    <div class="loading">
        <div class="spinner"></div>
        <p>Preparing comparison...</p>
        <div class="progress-step">Initializing...</div>
    </div>
    """
    
    try:
        # Small delay to show initial message
        await asyncio.sleep(0.5)
        
        # Find board info
        board1_info = board_utils.find_board_in_list(app_state["boards"], board1_version, board1_name)
        board2_info = board_utils.find_board_in_list(app_state["boards"], board2_version, board2_name)
        
        if not board1_info or not board2_info:
            results.innerHTML = """
            <div class="detail-view">
                <div class="detail-header">Board Comparison Error</div>
                <p style="color: #dc3545;">One or more selected boards could not be found.</p>
            </div>
            """
            return
        
        # Convert to comparison format
        board1 = {
            "version": board1_version,
            "port": board1_info[0],
            "board": board1_info[1]
        }
        board2 = {
            "version": board2_version,
            "port": board2_info[0], 
            "board": board2_info[1]
        }
        
        # Update progress for board 1
        results.innerHTML = f"""
        <div class="loading">
            <div class="spinner"></div>
            <p>Fetching modules for <strong>{board1_name}</strong>...</p>
            <div class="progress-step">Step 1 of 3</div>
        </div>
        """
        
        print(f"Fetching modules for board 1: {board1}")
        modules1 = get_board_modules(board1)
        
        # Small delay to show progress
        await asyncio.sleep(0.3)
        
        # Update progress for board 2
        results.innerHTML = f"""
        <div class="loading">
            <div class="spinner"></div>
            <p>Fetching modules for <strong>{board2_name}</strong>...</p>
            <div class="progress-step">Step 2 of 3</div>
        </div>
        """
        
        print(f"Fetching modules for board 2: {board2}")
        modules2 = get_board_modules(board2)
        
        # Small delay to show progress
        await asyncio.sleep(0.3)
        
        # Update progress for comparison
        results.innerHTML = """
        <div class="loading">
            <div class="spinner"></div>
            <p>Analyzing differences...</p>
            <div class="progress-step">Step 3 of 3</div>
        </div>
        """
        
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
        results.innerHTML = f"""
        <div class="detail-view">
            <h3 style="color: #dc3545;">⚠️ Comparison Error</h3>
            <p style="color: #666; margin: 15px 0;">{str(e)}</p>
            <button onclick="pyscript.run_code('await compare_boards()')" 
                    style="margin-top: 15px; padding: 10px 20px; background: #667eea; 
                           color: white; border: none; border-radius: 6px; cursor: pointer; 
                           font-weight: 600;">
                🔄 Try Again
            </button>
        </div>
        """


def render_module_tree_html(modules, options):
    """
    Render HTML for module tree with expandable functionality.
    
    Args:
        modules: List of module objects
        options: Dict with module_prefix, get_badge_class, get_module_badge, show_details
    """
    module_prefix = options.get("module_prefix", "tree")
    get_badge_class = options.get("get_badge_class", lambda m: "")
    get_module_badge = options.get("get_module_badge", lambda m: "")
    show_details = options.get("show_details", True)
    
    html = ""
    
    for module in modules:
        classes = module.get("classes", [])
        functions = module.get("functions", [])  
        constants = module.get("constants", [])
        
        has_children = len(classes) > 0 or len(functions) > 0 or len(constants) > 0
        
        is_deprecated = (module["name"].startswith("u") and 
                        len(module["name"]) > 1 and 
                        not has_children)
        
        deprecation_style = "color: #88474eff; font-style: italic;" if is_deprecated else "color: #6c757d;"
        summary_bg = "#ffe6e6" if is_deprecated else "#e9ecef"
        
        badge_class = get_badge_class(module)
        module_badge = get_module_badge(module)
        module_tree_id = f"{module_prefix}-module-{module['name']}"
        badge_class_str = f" {badge_class}" if badge_class else ""
        
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
        
        html += f"""
            <div class="tree-item">
                <div class="tree-node{badge_class_str}" onclick="toggleModule('{module_tree_id}', event)" data-module="{module['name']}">
                    <span class="tree-icon"><i class="fas fa-cube fa-icon"></i></span>
                    <strong style="color: #2c3e50; font-size: 1.1em;">{module['name']}{module_badge}</strong>
                    <span style="{deprecation_style} font-size: 0.9em; margin-left: auto; background: {summary_bg}; padding: 4px 8px; border-radius: 12px;">
                        {module_summary}
                    </span>
                </div>
                <div id="{module_tree_id}" class="tree-children hidden">
        """
        
        if show_details:
            # Add classes
            for cls in classes:
                has_methods_to_show = (len(cls.get("methods", [])) > 0 or 
                                     len(cls.get("attributes", [])) > 0)
                class_id = f"{module_prefix}-class-{module['name']}-{cls['name']}"
                
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
                
                base_classes_span = f'<span style="color: #888; font-size: 0.9em; font-weight: normal;"> {base_classes_str}</span>' if base_classes_str else ''
                
                html += f"""
                    <div class="tree-item">
                        <div class="tree-node" onclick="toggleClass('{class_id}', event)">
                            <span class="tree-icon"><i class="fas fa-object-group fa-icon"></i></span>
                            <span style="color: #495057; font-weight: 600;">class {cls['name']}</span>
                            {base_classes_span}
                            <span style="color: #6c757d; font-size: 0.85em; margin-left: auto; background: #f8f9fa; padding: 2px 6px; border-radius: 8px;">
                                {class_summary}
                            </span>
                        </div>
                """
                
                if has_methods_to_show:
                    html += f'<div id="{class_id}" class="tree-children hidden">'
                    
                    # Add methods
                    for method in cls.get("methods", []):
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
                        if (method.get("return_type") and 
                            method["return_type"] not in ["None", "", "Any"]):
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
                        
                        decorator_span = f'<span style="color: #888; font-size: 0.85em;">{" ".join(decorator_strs)} </span>' if decorator_strs else ''
                        
                        html += f"""
                        <div class="tree-item"><div class="tree-node">
                            <span class="tree-icon"><i class="{icon_class} fa-icon"></i></span>
                            <span style="color: #495057;">
                                {decorator_span}
                                <code style="background: #f8f9fa; padding: 2px 4px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 0.9em;">
                                    {async_marker}{signature}
                                </code>
                            </span>
                        </div></div>
                        """
                    
                    # Add attributes
                    for attr in cls.get("attributes", []):
                        type_hint = f": {attr['type_hint']}" if attr.get("type_hint") else ""
                        value = f" = {attr['value']}" if attr.get("value") else ""
                        
                        html += f"""
                        <div class="tree-item"><div class="tree-node">
                            <span class="tree-icon"><i class="fas fa-circle-dot fa-icon"></i></span>
                            <span style="color: #495057;">
                                <code style="background: #f8f9fa; padding: 2px 4px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 0.9em;">
                                    {attr['name']}{type_hint}{value}
                                </code>
                            </span>
                        </div></div>
                        """
                    
                    html += "</div>"
                html += "</div>"
            
            # Add functions
            for func in functions:
                # Format function signature (reuse method logic)
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
                
                if (func.get("return_type") and 
                    func["return_type"] not in ["None", "", "Any"]):
                    signature += f" -> {func['return_type']}"
                
                decorators_list = func.get("decorators_list", [])
                decorator_strs = [f"@{d}" for d in decorators_list]
                async_marker = "async " if func.get("is_async") else ""
                
                function_decorator_span = f'<span style="color: #888; font-size: 0.85em;">{" ".join(decorator_strs)} </span>' if decorator_strs else ''
                
                html += f"""
                <div class="tree-item"><div class="tree-node">
                    <span class="tree-icon"><i class="fas fa-bolt fa-icon"></i></span>
                    <span style="color: #495057;">
                        {function_decorator_span}
                        <code style="background: #f8f9fa; padding: 2px 4px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 0.9em;">
                            {async_marker}{signature}
                        </code>
                    </span>
                </div></div>
                """
            
            # Add constants
            for const in constants:
                const_value = f' = {const["value"]}' if const.get("value") else ''
                
                html += f"""
                <div class="tree-item"><div class="tree-node">
                    <span class="tree-icon"><i class="fas fa-circle fa-icon"></i></span>
                    <span style="color: #495057;">
                        <code style="background: #f8f9fa; padding: 2px 4px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 0.9em;">
                            {const['name']}{const_value}
                        </code>
                    </span>
                </div></div>
                """
        
        html += """
                </div>
            </div>
        """
    
    return html


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
        stats_element.innerHTML = f"""
        <div style="padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <h3 style="margin: 0 0 15px 0; color: #2c3e50; font-size: 1.1em;">Comparison Summary (All Levels)</h3>
            <table style="width: 100%; border-collapse: collapse; font-size: 0.9em;">
                <thead>
                    <tr style="background: #f0f0f0; border-bottom: 2px solid #667eea;">
                        <th style="padding: 10px; text-align: left; font-weight: 600;">Comparison Level</th>
                        <th style="padding: 10px; text-align: center; font-weight: 600;">{board1_name}</th>
                        <th style="padding: 10px; text-align: center; font-weight: 600;">Common</th>
                        <th style="padding: 10px; text-align: center; font-weight: 600;">{board2_name}</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 2px solid #e0e0e0; background: #f9f9f9;">
                        <td style="padding: 10px; font-weight: 600; color: #667eea;">Level 1: Modules</td>
                        <td style="padding: 10px; text-align: center; color: #FF8C00;"><strong>{level1["unique1"]}</strong> unique</td>
                        <td style="padding: 10px; text-align: center;"><strong>{level1["common"]}</strong></td>
                        <td style="padding: 10px; text-align: center; color: #008B8B;"><strong>{level1["unique2"]}</strong> unique</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e0e0e0; background: #f9f9f9;">
                        <td style="padding: 10px; font-weight: 600; color: #667eea;">Level 2: Classes</td>
                        <td style="padding: 10px; text-align: center; color: #FF8C00;"><strong>{level2["classes1_unique"]}</strong></td>
                        <td style="padding: 10px; text-align: center;"><strong>{level2["classes_different"]}</strong> differ</td>
                        <td style="padding: 10px; text-align: center; color: #008B8B;"><strong>{level2["classes2_unique"]}</strong></td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e0e0e0; color: #666; font-size: 0.85em;">
                        <td style="padding: 8px 10px;">Level 2: Functions</td>
                        <td style="padding: 8px 10px; text-align: center; color: #FF8C00;"><strong>{level2["functions1_unique"]}</strong></td>
                        <td style="padding: 8px 10px; text-align: center;">—</td>
                        <td style="padding: 8px 10px; text-align: center; color: #008B8B;"><strong>{level2["functions2_unique"]}</strong></td>
                    </tr>
                    <tr style="border-bottom: 2px solid #e0e0e0; color: #666; font-size: 0.85em;">
                        <td style="padding: 8px 10px;">Level 2: Constants</td>
                        <td style="padding: 8px 10px; text-align: center; color: #FF8C00;"><strong>{level2["constants1_unique"]}</strong></td>
                        <td style="padding: 8px 10px; text-align: center;">—</td>
                        <td style="padding: 8px 10px; text-align: center; color: #008B8B;"><strong>{level2["constants2_unique"]}</strong></td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e0e0e0; background: #f9f9f9;">
                        <td style="padding: 10px; font-weight: 600; color: #667eea;">Level 3: Methods</td>
                        <td style="padding: 10px; text-align: center; color: #FF8C00;"><strong>{level3["methods1_unique"]}</strong></td>
                        <td style="padding: 10px; text-align: center;"><strong>{level3["methods_different"]}</strong> differ</td>
                        <td style="padding: 10px; text-align: center; color: #008B8B;"><strong>{level3["methods2_unique"]}</strong></td>
                    </tr>
                    <tr style="border-bottom: 2px solid #e0e0e0; color: #666; font-size: 0.85em;">
                        <td style="padding: 8px 10px;">Level 3: Attributes</td>
                        <td style="padding: 8px 10px; text-align: center; color: #FF8C00;"><strong>{level3["attributes1_unique"]}</strong></td>
                        <td style="padding: 8px 10px; text-align: center;">—</td>
                        <td style="padding: 8px 10px; text-align: center; color: #008B8B;"><strong>{level3["attributes2_unique"]}</strong></td>
                    </tr>
                </tbody>
            </table>
            <div style="margin-top: 10px; font-size: 0.8em; color: #666;">
                <strong style="color: #FF8C00;">Dark Orange:</strong> {board1_name} | <strong>Center:</strong> Common | <strong style="color: #008B8B;">Dark Cyan:</strong> {board2_name}
            </div>
        </div>
        """
    
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
    
    # Build comparison results HTML with side-by-side layout
    html = f"""
    <div class="comparison-grid">
        <div class="board-section">
            <div class="board-header">{board1_name} ({board1["version"]})</div>
            <div class="module-tree">
    """
    
    # Render Board 1 modules
    board1_tree = render_module_tree_html(board1_modules_to_show, {
        "module_prefix": "board1",
        "get_badge_class": lambda module: "unique-to-board1" if module["name"] in unique_names1 else "",
        "get_module_badge": lambda module: " [UNIQUE]" if module["name"] in unique_names1 else "",
        "show_details": True
    })
    
    if board1_tree:
        html += board1_tree
    elif hide_common and len(board1_modules_to_show) == 0:
        html += '<p style="color: #666; padding: 20px;">No differences</p>'
    
    html += f"""
            </div>
        </div>
        <div class="board-section">
            <div class="board-header">{board2_name} ({board2["version"]})</div>
            <div class="module-tree">
    """
    
    # Render Board 2 modules
    board2_tree = render_module_tree_html(board2_modules_to_show, {
        "module_prefix": "board2",
        "get_badge_class": lambda module: "unique-to-board2" if module["name"] in unique_names2 else "",
        "get_module_badge": lambda module: " [UNIQUE]" if module["name"] in unique_names2 else "",
        "show_details": True
    })
    
    if board2_tree:
        html += board2_tree
    elif hide_common and len(board2_modules_to_show) == 0:
        html += '<p style="color: #666; padding: 20px;">No differences</p>'
    
    html += """
            </div>
        </div>
    </div>
    """
    
    # Show common modules section only if not in "show differences" mode
    if not hide_common and len(common_names) > 0:
        html += f"""
        <div class="detail-view">
            <div class="detail-header">Common Modules ({len(common_names)})</div>
            <div class="module-tree">
        """
        
        # Get common modules data
        common_modules = [m for m in modules1 if m["name"] in common_names]
        
        common_tree = render_module_tree_html(common_modules, {
            "module_prefix": "common",
            "get_badge_class": lambda module: "",
            "get_module_badge": lambda module: "",
            "show_details": True
        })
        
        html += common_tree
        
        html += """
            </div>
        </div>
        """
    
    # Update the comparison results display
    results = document.getElementById("compare-results")
    results.innerHTML = html
    
    print("Comparison display updated")


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
            attributes.append({
                "name": row["name"],
                "type_hint": row["type_hint"],
                "value": row["value"]
            })
        
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
                    "attributes": attributes
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
            
            modules.append({
                "id": module_id,
                "name": row["name"],
                "docstring": row["docstring"],
                "classes": classes,
                "functions": functions,
                "constants": constants,
            })
        
        stmt.free()
        return modules
        
    except Exception as e:
        print(f"Error getting board modules: {e}")
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
        original_options.append({
            'value': str(option.value),
            'text': str(option.textContent),
            'selected': bool(option.selected)
        })
    
    # Create wrapper container
    wrapper = js.document.createElement('div')
    wrapper.className = 'combobox-wrapper'
    
    # Determine if this is a version select
    is_version_select = 'version' in select_id
    if is_version_select:
        wrapper.style.width = '160px'
    
    # Create search input
    search_input = js.document.createElement('input')
    search_input.type = 'text'
    search_input.className = 'combobox-input'
    
    # Set placeholder based on field type
    if is_version_select:
        search_input.placeholder = 'Version...'
    else:
        label_text = str(select_element.previousElementSibling.textContent).lower()
        search_input.placeholder = f'Type to search {label_text}...'
    
    if is_version_select:
        search_input.style.width = '160px'
    
    # Create dropdown arrow
    arrow = js.document.createElement('div')
    arrow.innerHTML = '▼'
    arrow.className = 'combobox-arrow'
    
    # Create dropdown list
    dropdown = js.document.createElement('div')
    dropdown.className = 'combobox-dropdown'
    
    # Replace select with wrapper
    select_element.parentNode.insertBefore(wrapper, select_element)
    wrapper.appendChild(search_input)
    wrapper.appendChild(arrow)
    wrapper.appendChild(dropdown)
    select_element.style.display = 'none'
    
    # State variables (using global dict to avoid closure issues)
    state = {
        'is_open': False,
        'selected_value': str(select_element.value),
        'filtered_options': original_options[:]
    }
    
    def update_display_value():
        state['selected_value'] = str(select_element.value)
        selected_option = None
        for opt in original_options:
            if opt['value'] == state['selected_value']:
                selected_option = opt
                break
        
        if selected_option and selected_option['value'] != '':
            search_input.value = selected_option['text']
            search_input.style.color = '#000'
        else:
            search_input.value = ''
            search_input.style.color = '#666'
    
    def populate_dropdown(options=None):
        if options is None:
            options = state['filtered_options']
        
        dropdown.innerHTML = ''
        current_value = str(select_element.value)
        
        if len(options) == 0:
            no_results = js.document.createElement('div')
            no_results.textContent = 'No matches found'
            no_results.style.cssText = 'padding: 8px; color: #666; font-style: italic;'
            dropdown.appendChild(no_results)
            return
        
        for option in options:
            if option['value'] == '':
                continue  # Skip default option
            
            item = js.document.createElement('div')
            item.textContent = option['text']
            item.setAttribute('data-value', option['value'])
            
            if option['value'] == current_value:
                item.classList.add('selected')
            
            # Store option value on element for click handler
            item._option_value = option['value']
            dropdown.appendChild(item)
    
    def open_dropdown():
        if state['is_open']:
            return
        state['is_open'] = True
        dropdown.style.display = 'block'
        populate_dropdown()
        search_input.style.borderRadius = '4px 4px 0 0'
    
    def close_dropdown():
        if not state['is_open']:
            return
        state['is_open'] = False
        dropdown.style.display = 'none'
        search_input.style.borderRadius = '4px'
        update_display_value()
    
    def filter_options(search_term):
        if not search_term.strip():
            state['filtered_options'] = original_options[:]
        else:
            state['filtered_options'] = []
            search_lower = search_term.lower()
            for option in original_options:
                if option['value'] != '' and search_lower in option['text'].lower():
                    state['filtered_options'].append(option)
        populate_dropdown()
    
    # Set up event handlers using JavaScript (MicroPython approach)
    # Replace hyphens with underscores for valid JavaScript function names
    js_safe_id = select_id.replace('-', '_')
    
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
        if not state['is_open']:
            open_dropdown()
        filter_options(str(term))
    
    def js_enter():
        visible_options = [opt for opt in state['filtered_options'] if opt['value'] != '']
        if len(visible_options) == 1:
            js_select(visible_options[0]['value'])
    
    def js_select(value):
        state['selected_value'] = str(value)
        select_element.value = state['selected_value']
        # Trigger change event
        change_event = js.document.createEvent('Event')
        change_event.initEvent('change', True, True)
        select_element.dispatchEvent(change_event)
        update_display_value()
        close_dropdown()
    
    # Register functions with JavaScript window object
    js.window[f'micropython_dropdown_{js_safe_id}_open'] = js_open
    js.window[f'micropython_dropdown_{js_safe_id}_close'] = js_close
    js.window[f'micropython_dropdown_{js_safe_id}_filter'] = js_filter
    js.window[f'micropython_dropdown_{js_safe_id}_enter'] = js_enter
    js.window[f'micropython_dropdown_{js_safe_id}_select'] = js_select
    
    # Initialize display
    update_display_value()
    
    return wrapper


def initialize_searchable_dropdowns():
    """Initialize searchable dropdowns for comparison selects"""
    dropdown_ids = ['board1-version', 'board1', 'board2-version', 'board2']
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
        board1_version = str(js.document.getElementById('board1-version').value)
        board1 = str(js.document.getElementById('board1').value)
        board2_version = str(js.document.getElementById('board2-version').value)
        board2 = str(js.document.getElementById('board2').value)
        hide_common = bool(js.document.getElementById('hide-common').checked)
        
        # Build URL parameters
        params = ['view=compare']
        
        if board1:
            params.append(f'board1={board1}')
        if board1_version:
            params.append(f'version1={board1_version}')
        if board2:
            params.append(f'board2={board2}')
        if board2_version:
            params.append(f'version2={board2_version}')
        if hide_common:
            params.append('diff=true')
        
        # Update URL without page reload using JavaScript
        params_str = '&'.join(params)
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
        share_btn = js.document.querySelector('.share-btn')
        original_text = str(share_btn.innerHTML)
        share_btn.innerHTML = '<span class="share-icon">✓</span> Copied!'
        
        # Restore text after 2 seconds
        js.setTimeout(lambda: setattr(share_btn, 'innerHTML', original_text), 2000)
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


# Register share functions with JavaScript
js.window['micropython_share_success'] = share_success
js.window['micropython_share_fallback'] = share_fallback
js.window['toggleModule'] = toggle_module
js.window['toggleClass'] = toggle_class


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
        url_params = js.eval("""
            (() => {
                const url = new URL(window.location.href);
                const params = {};
                for (const [key, value] of url.searchParams) {
                    params[key] = value;
                }
                return params;
            })()
        """)
        
        if url_params and url_params.view == "compare":
            # Switch to comparison mode
            switch_page("compare")
            
            # Set the board selections if provided
            if url_params.board1 and url_params.version1:
                js.eval(f"document.getElementById('board1-version').value = '{url_params.version1}'")
                js.eval(f"document.getElementById('board1').value = '{url_params.board1}'")
            if url_params.board2 and url_params.version2:
                js.eval(f"document.getElementById('board2-version').value = '{url_params.version2}'")
                js.eval(f"document.getElementById('board2').value = '{url_params.board2}'")
            
            # Trigger comparison if both boards are selected
            if url_params.board1 and url_params.version1 and url_params.board2 and url_params.version2:
                # Use the async compare_boards function instead
                await compare_boards()
        
        update_status("Loaded database. Application ready!", "success")
    else:
        # Database is required
        update_status("Failed to load database. Cannot continue.", "error")


# Start the application


asyncio.create_task(main())
