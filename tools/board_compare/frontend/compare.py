# compare.py - Board Comparison functionality
# Extracted from main.py as part of Sprint 3 refactoring

import asyncio
import copy
import json

# Import modules
import database
import ui
from pyscript import document, ffi, window

# Global comparison data (moved from main.py)
comparison_data = {
    "board1": None,
    "board2": None,
    "modules1": None,
    "modules2": None,
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
    print("compare_boards() function called!")
    # Get board selections
    board1_version = document.getElementById("board1-version").value
    board1_name = document.getElementById("board1").value
    board2_version = document.getElementById("board2-version").value
    board2_name = document.getElementById("board2").value

    # Validate selections
    if not board1_version or not board1_name or not board2_version or not board2_name:
        ui.show_message("compare-results", "Board Comparison", "Please select both version and board for both boards to compare.")
        return

    if not database.app_state["db"]:
        ui.show_message("compare-results", "Board Comparison", "Database not available for comparison.")
        return

    # Show loading with progress
    ui.show_loading("compare-results", "Preparing comparison...", "Initializing...")

    try:
        # Small delay to show initial message
        await asyncio.sleep(0.2)
        print(f"Comparing boards: {board1_name} ({board1_version}) vs {board2_name} ({board2_version})")
        # Find board info
        board1_info = database.find_board_in_list(database.app_state["boards"], board1_version, board1_name)
        board2_info = database.find_board_in_list(database.app_state["boards"], board2_version, board2_name)

        if not board1_info or not board2_info:
            if not board1_info:
                msg = f"Board 1: '{board1_name}' version '{board1_version}' not found."
            else:
                msg = f"Board 2: '{board2_name}' version '{board2_version}' not found."
            print(msg)
            ui.show_error("compare-results", "Board Comparison Error", msg)
            return

        # Convert to comparison format
        board1 = {"version": board1_version, "port": board1_info[0], "board": board1_info[1]}
        board2 = {"version": board2_version, "port": board2_info[0], "board": board2_info[1]}
        # Update progress for board 1
        ui.show_loading("compare-results", f"Fetching modules for {board1_name}...", "Step 1 of 3")

        print(f"Fetching modules for board 1: {board1}")
        modules1 = database.get_board_modules(board1)

        # Small delay to show progress
        await asyncio.sleep(0.3)

        # Update progress for board 2
        ui.show_loading("compare-results", f"Fetching modules for {board2_name}...", "Step 2 of 3")

        print(f"Fetching modules for board 2: {board2}")
        modules2 = database.get_board_modules(board2)

        # Small delay to show progress
        await asyncio.sleep(0.2)

        # Update progress for comparison
        ui.show_loading("compare-results", "Analyzing differences...", "Step 3 of 3")

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
        ui.show_error("compare-results", "⚠️ Comparison Error", str(e), show_retry=True)


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
        module_element = ui.create_module_item(module, options)
        if module_element and show_details:
            # Add children to module
            children_container = module_element.querySelector("[data-module-children]")
            if children_container:
                # Add classes
                for cls in module.get("classes", []):
                    class_element = ui.create_class_item(cls, module["name"], options.get("module_prefix", "tree"), module.get("id"))
                    if class_element:
                        # Add methods and attributes to class
                        class_children = class_element.querySelector("[data-class-children]")
                        if class_children:
                            # Add methods
                            for method in cls.get("methods", []):
                                method_element = ui.create_method_item(method)
                                if method_element:
                                    class_children.appendChild(method_element)

                            # Add attributes
                            for attr in cls.get("attributes", []):
                                attr_element = ui.create_attribute_item(attr)
                                if attr_element:
                                    class_children.appendChild(attr_element)

                        children_container.appendChild(class_element)

                # Add functions
                for func in module.get("functions", []):
                    func_element = ui.create_function_item(func)
                    if func_element:
                        children_container.appendChild(func_element)

                # Add constants
                for const in module.get("constants", []):
                    const_element = ui.create_constant_item(const)
                    if const_element:
                        children_container.appendChild(const_element)

        if module_element:
            container.appendChild(module_element)

    return container


def render_module_tree_html(modules, options):
    """
    Legacy function that returns HTML string for backward compatibility.
    Consider migrating to render_module_tree_dom for better performance.
    """
    dom_tree = ui.render_module_tree_dom(modules, options)
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
    board1_name = database.format_board_name(board1["port"], board1["board"])
    board2_name = database.format_board_name(board2["port"], board2["board"])

    # Update stats display
    stats_element = document.getElementById("compare-stats")
    if stats_element:
        stats_element.style.display = "block"

        # Use template for statistics
        stats_template = ui.get_template("stats-template")
        if stats_template:
            stats_template.style.display = "block"
            ui.populate_template(
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
    comparison_grid = ui.get_template("comparison-grid-template")
    if comparison_grid:
        comparison_grid.style.display = "block"

        # Generate module trees using DOM-based rendering
        board1_tree_dom = ui.render_module_tree_dom(
            board1_modules_to_show,
            {
                "module_prefix": "board1",
                "get_badge_class": lambda module: "unique-to-board1" if module["name"] in unique_names1 else "",
                "get_module_badge": lambda module: " [UNIQUE]" if module["name"] in unique_names1 else "",
                "show_details": True,
            },
        )

        board2_tree_dom = ui.render_module_tree_dom(
            board2_modules_to_show,
            {
                "module_prefix": "board2",
                "get_badge_class": lambda module: "unique-to-board2" if module["name"] in unique_names2 else "",
                "get_module_badge": lambda module: " [UNIQUE]" if module["name"] in unique_names2 else "",
                "show_details": True,
            },
        )

        # Populate board headers
        ui.populate_template(
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
                no_diff_elem = ui.get_template("message-template")
                if no_diff_elem:
                    ui.populate_template(
                        no_diff_elem, {"data-show-detail-view": "false", "data-show-simple": "true", "data-simple-text": "No differences"}
                    )
                    board1_container.appendChild(no_diff_elem)

        if board2_container:
            board2_container.innerHTML = ""  # Clear existing content
            if len(board2_modules_to_show) > 0:
                board2_container.appendChild(board2_tree_dom)
            else:
                # Use template for "No differences" message
                no_diff_elem = ui.get_template("message-template")
                if no_diff_elem:
                    ui.populate_template(
                        no_diff_elem, {"data-show-detail-view": "false", "data-show-simple": "true", "data-simple-text": "No differences"}
                    )
                    board2_container.appendChild(no_diff_elem)

        # Handle common modules section
        common_section = comparison_grid.querySelector("[data-common-section]")
        if not hide_common and len(common_names) > 0:
            common_modules = [m for m in modules1 if m["name"] in common_names]
            common_tree_dom = ui.render_module_tree_dom(
                common_modules,
                {
                    "module_prefix": "common",
                    "get_badge_class": lambda module: "",
                    "get_module_badge": lambda module: "",
                    "show_details": True,
                },
            )

            ui.populate_template(comparison_grid, {"common-header": f"Common Modules ({len(common_names)})"})

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


def update_comparison_url():
    """Update the URL to reflect the current comparison state."""
    board1_version = document.getElementById("board1-version").value
    board1_name = document.getElementById("board1").value
    board2_version = document.getElementById("board2-version").value
    board2_name = document.getElementById("board2").value
    hide_common = document.getElementById("hide-common").checked

    # Get current URL
    url = window.location.href.split('?')[0]

    # Build query parameters
    params = []
    params.append("view=compare")

    if board1_version:
        params.append(f"board1_version={window.encodeURIComponent(board1_version)}")
    if board1_name:
        params.append(f"board1={window.encodeURIComponent(board1_name)}")
    if board2_version:
        params.append(f"board2_version={window.encodeURIComponent(board2_version)}")
    if board2_name:
        params.append(f"board2={window.encodeURIComponent(board2_name)}")
    if hide_common:
        params.append("hide_common=true")

    if params:
        new_url = f"{url}?{'&'.join(params)}"
        window.history.replaceState(ffi.to_js({}), ffi.to_js(""), ffi.to_js(new_url))


async def populate_comparison_from_url(search_params):
    """Populate the comparison page from URL parameters."""
    try:
        board1_version = search_params.get("board1_version")
        board1 = search_params.get("board1")
        board2_version = search_params.get("board2_version")
        board2 = search_params.get("board2")
        hide_common = search_params.get("hide_common") == "true"

        # Set the inputs
        board1_version_input = document.getElementById("board1-version")
        if board1_version_input and board1_version:
            board1_version_input.value = board1_version

        board1_input = document.getElementById("board1")
        if board1_input and board1:
            board1_input.value = board1

        board2_version_input = document.getElementById("board2-version")
        if board2_version_input and board2_version:
            board2_version_input.value = board2_version

        board2_input = document.getElementById("board2")
        if board2_input and board2:
            board2_input.value = board2

        hide_common_checkbox = document.getElementById("hide-common")
        if hide_common_checkbox:
            hide_common_checkbox.checked = hide_common

        # Trigger comparison if all selections are made
        if board1_version and board1 and board2_version and board2:
            await compare_boards()

    except Exception as e:
        print(f"Error populating comparison from URL: {e}")


def share_comparison(event=None):
    """Share the current comparison view."""
    print("=== Share Comparison Called ===")
    
    board1_version = document.getElementById("board1-version").value
    board1_name = document.getElementById("board1").value
    board2_version = document.getElementById("board2-version").value
    board2_name = document.getElementById("board2").value
    hide_common = document.getElementById("hide-common").checked

    print(f"Board 1: Version '{board1_version}', Name '{board1_name}'")
    print(f"Board 2: Version '{board2_version}', Name '{board2_name}'")
    print(f"Hide common: {hide_common}")

    if not all([board1_version, board1_name, board2_version, board2_name]):
        print("Missing selections, showing error")
        ui.show_error("Please select all comparison options to share")
        return

    # Build share URL
    base_url = window.location.href.split('?')[0]
    params = ["view=compare"]

    params.append(f"board1_version={window.encodeURIComponent(board1_version)}")
    params.append(f"board1={window.encodeURIComponent(board1_name)}")
    params.append(f"board2_version={window.encodeURIComponent(board2_version)}")
    params.append(f"board2={window.encodeURIComponent(board2_name)}")

    if hide_common:
        params.append("hide_common=true")

    share_url = f"{base_url}?{'&'.join(params)}"
    print(f"Share URL: {share_url}")
    
    print("Attempting to copy to clipboard...")

    # Copy to clipboard using ffi.to_js to avoid PyProxy issues
    from pyscript import ffi
    
    def success_callback():
        print("Clipboard write successful, updating status...")
        # Update status directly via DOM
        status_element = document.getElementById("status")
        if status_element:
            status_element.innerHTML = "<strong>Status:</strong> Share URL copied to clipboard!"
            print("Status updated successfully")
        else:
            print("Status element not found")
    
    def error_callback():
        print("Clipboard write failed")
        # Update status directly via DOM  
        status_element = document.getElementById("status")
        if status_element:
            status_element.innerHTML = "<strong>Status:</strong> Failed to copy URL to clipboard"
    
    window.navigator.clipboard.writeText(ffi.to_js(share_url)).then(
        ffi.create_proxy(success_callback),
        ffi.create_proxy(error_callback)
    )


def setup_compare_event_handlers():
    """Set up event handlers specific to the comparison page."""
    print("Setting up compare event handlers...")
    
    # Compare button - HTML has mpy-click="compare_boards" which calls main.compare_boards()
    # Previous Python override removed - compare_btn.onclick was set to async handler

    # Hide common checkbox
    hide_common_checkbox = document.getElementById("hide-common")
    if hide_common_checkbox:
        hide_common_checkbox.onchange = lambda e: update_comparison()

    # Share button - HTML has mpy-click="share_comparison" which calls main.share_comparison()
    # Previous Python override removed - share_compare_btn.onclick was set to lambda

    # Board selection change handlers (for URL updates)
    for input_id in ["board1-version", "board1", "board2-version", "board2"]:
        input_elem = document.getElementById(input_id)
        if input_elem:
            input_elem.onchange = lambda e: update_comparison_url()
            input_elem.oninput = lambda e: update_comparison_url()