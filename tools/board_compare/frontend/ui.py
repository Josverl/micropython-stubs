"""
UI and Template Management Module

This module contains all UI-related functions including:
- Template utilities (get_template, populate_template)
- Display functions (show_loading, show_error, show_message, update_status)
- Item creation functions (create_*_item)
- Tree rendering functions (render_module_tree_dom, render_module_tree_html)
- Search result functions
"""

import database
from pyscript import document, ffi, window


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
                    target.setAttribute("mpy-click", value)
            elif key.endswith("-class") and value:
                target.className = value
            elif key.endswith("-target") and value:
                # Set data attribute for element ID reference (used by toggle functions)
                target.setAttribute(f"data-{key}", value)
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


def create_module_item(module, options):
    """Create a module item using template."""
    # Import format_board_name from database module to avoid circular imports
    import database
    
    module_prefix = options.get("module_prefix", "tree")
    get_badge_class = options.get("get_badge_class", lambda m: "")
    get_module_badge = options.get("get_module_badge", lambda m: "")

    classes = module.get("classes", [])
    functions = module.get("functions", [])
    constants = module.get("constants", [])

    # has_children = len(classes) > 0 or len(functions) > 0 or len(constants) > 0
    is_deprecated = module["name"].startswith("u") and len(module["name"]) != "uctypes"
    # FIXME: Why does in not work ?
    # is_deprecated =str(module['name']) in database.U_MODULES
    # if is_deprecated:
    #     print(f"{module['name']=}")
    #     window.console.log(ffi.to_js(module["name"]))
    #     window.console.log(ffi.to_js(module))

    badge_class = get_badge_class(module)
    module_badge = get_module_badge(module)
    # Use module ID to ensure uniqueness when same module names exist across different boards
    module_id = module.get('id', 'unknown')
    module_tree_id = f"{module_prefix}-module-{module['name']}-{module_id}"

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

    # Format board and version information if available
    board_version_label = ""
    if module.get("version") and module.get("port") and module.get("board"):
        board_name = database.format_board_name(module["port"], module["board"])
        board_version_label = f"[{board_name} {module['version']}]"

    module_header_class = "module-header"
    if badge_class:
        module_header_class += " unique"
    if is_deprecated:
        module_header_class += " deprecated"

    # Get template and populate
    module_element = get_template("module-item-template")
    if module_element:
        populate_template(
            module_element,
            {
                "module-header-class": module_header_class,
                "module-click": "toggle_tree_node",
                "module-target": module_tree_id,  # Element ID to toggle
                "module-data": module["name"],
                "module-name": module["name"],
                "module-badge-style": "inline" if module_badge else "hide",
                "module-details": module_summary,
                "module-board-version": board_version_label,
                "module-id": module_tree_id,
            },
        )

        # Show/hide badge
        badge_elem = module_element.querySelector("[data-module-badge]")
        if badge_elem:
            badge_elem.style.display = "inline" if module_badge else "none"

    return module_element


def create_class_item(cls, module_name, module_prefix, module_id=None):
    """Create a class item using template."""
    # Use module_id to ensure uniqueness when same module names exist across different boards
    if module_id:
        class_id = f"{module_prefix}-class-{module_name}-{cls['name']}-{module_id}"
    else:
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

    base_classes_span = f" {base_classes_str}" if base_classes_str else ""

    # Get template and populate
    class_element = get_template("class-item-template")
    if class_element:
        populate_template(
            class_element,
            {
                "class-click": "toggle_tree_node",
                "class-target": class_id,  # Element ID to toggle
                "class-signature": f"class {cls['name']}",
                "base-classes": base_classes_span,
                "class-summary": class_summary,
                "class-id": class_id,
            },
        )

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

    function_decorator_span = f"{' '.join(decorator_strs)} " if decorator_strs else ""

    # Get template and populate
    function_element = get_template("function-item-template")
    if function_element:
        icon_type = "property" if func.get("is_property") else "function"
        populate_template(
            function_element,
            {
                "function-icon": database.get_icon_class(icon_type),
                "decorators": function_decorator_span,
                "signature": f"{async_marker}{signature}",
            },
        )

    return function_element


def create_constant_item(const):
    """Create a constant item using template."""
    const_value = f" = {const['value']}" if const.get("value") else ""

    # Get template and populate
    constant_element = get_template("constant-item-template")
    if constant_element:
        populate_template(constant_element, {"constant-signature": f"{const['name']}{const_value}"})

    return constant_element


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

    icon_type = "property" if method.get("is_property") else "method"

    decorator_span = f"{' '.join(decorator_strs)} " if decorator_strs else ""

    # Get template and populate
    method_element = get_template("function-item-template")
    if method_element:
        populate_template(
            method_element,
            {
                "function-icon": database.get_icon_class(icon_type),
                "decorators": decorator_span,
                "signature": f"{async_marker}{signature}",
            },
        )

    return method_element


def create_attribute_item(attr):
    """Create an attribute item using template."""
    type_hint = f": {attr['type_hint']}" if attr.get("type_hint") else ""
    value = f" = {attr['value']}" if attr.get("value") else ""

    # Get template and populate
    attr_element = get_template("constant-item-template")
    if attr_element:
        populate_template(attr_element, {"constant-signature": f"{attr['name']}{type_hint}{value}"})

        # Update icon for attributes (use circle-dot instead of circle)
        icon_elem = attr_element.querySelector(".fa-icon")
        if icon_elem:
            icon_elem.className = f"{database.get_icon_class('variable')} fa-icon"

    return attr_element


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
                    class_element = create_class_item(cls, module["name"], options.get("module_prefix", "tree"), module.get("id"))
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


def render_module_tree_html(modules, options):
    """
    Legacy function that returns HTML string for backward compatibility.
    Consider migrating to render_module_tree_dom for better performance.
    """
    dom_tree = render_module_tree_dom(modules, options)
    return dom_tree.innerHTML if dom_tree else ""


def create_search_result_item(result, entity_type, format_board_name_fn, get_context_path_fn, get_entity_icon_fn, setup_search_result_expansion_fn, toggle_search_result_expansion_fn):
    """Create a search result item using template with hierarchical indentation."""
    # Accept functions as parameters to avoid circular imports
    
    board_name = format_board_name_fn(result["port"], result["board"])
    context_path = get_context_path_fn(result)

    # Use search result template
    result_element = get_template("search-result-item-template")
    if result_element:
        # Apply hierarchical styling
        if result.get("is_grandchild"):
            result_element.style.marginLeft = "40px"
            result_element.style.borderLeft = "2px solid #e9ecef"
            result_element.style.paddingLeft = "10px"
            result_element.classList.add("hierarchy-grandchild")
        elif result.get("is_child"):
            result_element.style.marginLeft = "20px"
            result_element.style.borderLeft = "2px solid #dee2e6"
            result_element.style.paddingLeft = "10px"
            result_element.classList.add("hierarchy-child")
        else:
            result_element.classList.add("hierarchy-parent")

        # Add hierarchy indicator icon
        entity_name = result["entity_name"]
        
        # Only add tree indicators for entities that are truly leaf nodes
        # Classes and modules should remain expandable, so don't add └─ 
        if result.get("is_grandchild"):
            # Grandchildren (methods, attributes, parameters) are leaf nodes
            entity_name = f"└─ {entity_name}"
        elif result.get("is_child") and result["entity_type"] in ["method", "attribute", "parameter", "constant"]:
            # Direct children that are leaf nodes
            entity_name = f"└─ {entity_name}"
        
        # Populate template data
        populate_template(
            result_element,
            {"entity-name": entity_name, "context-path": context_path, "board-name": board_name, "version": result["version"]},
        )

        # Set entity icon
        icon_elem = result_element.querySelector("[data-entity-icon]")
        if icon_elem:
            icon_elem.className = f"fas {get_entity_icon_fn(entity_type)}"

        # Set up expansion capability and click handler
        module_id = result["module_id"]
        class_id = result.get("class_id", "")
        entity_name_clean = result["entity_name"]  # Use original name for click handler
        
        # Check if this item can have children and set up expansion
        can_expand = setup_search_result_expansion_fn(result_element, result, entity_type, module_id, class_id)
        
        # Set click handler - if item can expand, handle expansion; otherwise navigate
        def click_handler(e):
            if can_expand:
                toggle_search_result_expansion_fn(result_element, result, entity_type, module_id, class_id, e)
            else:
                # Call openSearchResult for leaf items or navigation
                if hasattr(window, "openSearchResult"):
                    window.openSearchResult(module_id, class_id, entity_name_clean, entity_type)

        header = result_element.querySelector("[data-search-result-header]")
        if header:
            header.onclick = click_handler
        else:
            result_element.onclick = click_handler

    return result_element