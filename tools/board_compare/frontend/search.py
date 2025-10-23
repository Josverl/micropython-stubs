# search.py - Search APIs functionality
# Extracted from main.py as part of Sprint 3 refactoring

import asyncio
import json

# Import modules
import database
import ui
from pyscript import document, ffi, window


async def search_apis():
    """Search for APIs across boards."""
    search_input = document.getElementById("search-input")
    search_term = search_input.value.strip()

    if not search_term:
        ui.show_message("search-results", "Search Results", "Enter a search term to find modules, classes, methods, functions, or constants.")
        return

    if not database.app_state["db"]:
        ui.show_error("search-results", "Search Error", "Database not loaded. Please wait for the application to initialize.")
        return

    # Show loading
    ui.show_loading("search-results", f'Searching for "{search_term}"...', "Scanning database...")

    try:
        # Allow UI update
        await asyncio.sleep(0.1)

        search_results = await perform_search(search_term)
        display_search_results(search_results, search_term)

    except Exception as e:
        ui.show_error("search-results", "Search Error", f"Error performing search: {str(e)}")


async def perform_search(search_term):
    """Perform comprehensive search across all database entities."""
    if not database.app_state["db"]:
        print("Database not available for search")
        return []

    # Use LIKE with wildcards for flexible matching
    search_pattern = f"%{search_term}%"
    results = []

    print(f"Starting search for: '{search_term}' with pattern: '{search_pattern}'")

    # First check if we have any data at all
    try:
        count_stmt = database.app_state["db"].prepare("SELECT COUNT(*) as count FROM unique_modules")
        count_stmt.step()
        module_count = count_stmt.getAsObject()["count"]
        count_stmt.free()
        print(f"Total modules in database: {module_count}")

        # Show some sample module names for debugging
        sample_stmt = database.app_state["db"].prepare("SELECT name FROM unique_modules LIMIT 10")
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
            test_stmt = database.app_state["db"].prepare("SELECT COUNT(*) as count FROM unique_modules WHERE name = ?")
            test_stmt.bind(ffi.to_js([first_module]))
            test_stmt.step()
            exact_count = test_stmt.getAsObject()["count"]
            test_stmt.free()
            print(f"Exact match count for '{first_module}': {exact_count}")

            # Try a simple SELECT to see what we get
            debug_stmt = database.app_state["db"].prepare("SELECT name FROM unique_modules WHERE name = ? LIMIT 1")
            debug_stmt.bind(ffi.to_js([first_module]))
            if debug_stmt.step():
                found_name = debug_stmt.getAsObject()["name"]
                print(f"Found exact name: '{found_name}' (type: {type(found_name)})")
                print(f"Comparison: '{first_module}' == '{found_name}': {first_module == found_name}")
            else:
                print("No exact match found in debug query")
            debug_stmt.free()

            # Test LIKE query for search term
            test_like_stmt = database.app_state["db"].prepare("SELECT COUNT(*) as count FROM unique_modules WHERE name LIKE ?")
            test_like_stmt.bind(ffi.to_js([search_pattern]))
            test_like_stmt.step()
            like_search_count = test_like_stmt.getAsObject()["count"]
            test_like_stmt.free()
            print(f"LIKE match count for search pattern '{search_pattern}': {like_search_count}")
    except Exception as e:
        print(f"Error counting modules: {e}")

    try:
        # Use unified v_board_entities view - replaces 6 separate queries
        print(f"Searching all entities using v_board_entities view for: '{search_term}'")
        
        stmt = database.app_state["db"].prepare("""
            SELECT DISTINCT
                entity_type,
                entity_name,
                version,
                port,
                board,
                module_id,
                class_id,
                parent_name
            FROM v_board_entities
            WHERE entity_name LIKE ? COLLATE NOCASE
            ORDER BY version DESC, port, board, module_id, entity_type, entity_name
        """)
        
        stmt.bind(ffi.to_js([search_pattern]))
        
        # Count results by type for debugging
        entity_counts = {}
        
        while stmt.step():
            result_obj = stmt.getAsObject()
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
            results.append(result)
            
            # Track counts by entity type
            entity_type = result["entity_type"]
            entity_counts[entity_type] = entity_counts.get(entity_type, 0) + 1
        
        stmt.free()
        
        # Log results by entity type
        print(f"Search completed. Found {len(results)} total results:")
        for entity_type, count in sorted(entity_counts.items()):
            print(f"  {entity_type}: {count}")
            
        # Show sample results
        if results:
            print("Sample results (first 3):")
            for i, result in enumerate(results[:3]):
                print(f"  {i+1}. {result['entity_type']}: {result['entity_name']} (module_id: {result['module_id']})")

    except Exception as e:
        print(f"Search error: {e}")
        import traceback
        traceback.print_exc()
        return []

    print(f"Search completed successfully. Total results: {len(results)}")
    return results


def enhance_results_with_children(results):
    """Enhance search results by adding children of found modules and classes."""
    print("enhance_results_with_children: Starting...")
    
    if not database.app_state["db"]:
        print("enhance_results_with_children: No database available")
        return results
    
    enhanced_results = list(results)  # Start with original results
    found_modules = set()
    found_classes = set()
    
    print(f"enhance_results_with_children: Processing {len(results)} original results")
    
    # Identify found modules and classes
    for result in results:
        if result["entity_type"] == "module":
            found_modules.add(result["module_id"])
        elif result["entity_type"] == "class" and result.get("class_id"):
            found_classes.add(result["class_id"])
    
    print(f"enhance_results_with_children: Found {len(found_modules)} modules, {len(found_classes)} classes")
    
    # For now, just return the original results to test if this function is being called
    print(f"enhance_results_with_children: Returning {len(enhanced_results)} results")
    return enhanced_results


def group_results_hierarchically(results):
    """Group search results hierarchically showing parent-child relationships.
    
    When a class is found, include its methods and attributes.
    When a module is found, include its classes and constants.
    Hide peer entities (siblings at the same level).
    """
    # For now, just return results as-is without complex hierarchical grouping
    # This avoids the issue where classes get marked as children and show tree indicators
    # TODO: Implement proper hierarchical expansion later
    return results


def convert_search_results_to_tree_format(results):
    """Convert search results into the module tree format used by existing tree system."""
    print(f"Converting {len(results)} search results to tree format")
    
    modules = {}
    
    # Filter out __init__ modules and other irrelevant results
    filtered_results = []
    for result in results:
        module_name = result.get("parent_name") if result["entity_type"] != "module" else result["entity_name"]
        # Skip __init__ modules as they're typically empty structural modules
        if module_name and module_name.strip() and module_name != "__init__":
            filtered_results.append(result)
    
    # Deduplicate search results - same method/attribute in same class should only appear once
    seen_items = set()
    deduplicated_results = []
    for result in filtered_results:
        # Create unique key based on entity type, name, and class context
        key = (
            result["entity_type"],
            result["entity_name"], 
            result.get("module_id"),
            result.get("class_id", "")  # Use empty string for module-level items
        )
        if key not in seen_items:
            seen_items.add(key)
            deduplicated_results.append(result)
    
    print(f"After deduplication: {len(deduplicated_results)} results (removed {len(filtered_results) - len(deduplicated_results)} duplicates)")
    results = deduplicated_results
    
    # First pass: collect all module names by module_id and identify found classes/methods
    module_names = {}
    module_contexts = {}  # Store board/version info for modules
    found_classes = {}  # class_id -> {methods: set(), attributes: set()}
    board_contexts = {}
    
    for result in results:
        entity_type = result["entity_type"]
        module_id = result.get("module_id")
        class_id = result.get("class_id")
        entity_name = result["entity_name"]
        
        if entity_type == "module":
            module_names[module_id] = result["entity_name"]
        elif entity_type != "module" and result.get("parent_name"):
            # For non-module entities, parent_name is the module name
            module_names[module_id] = result["parent_name"]
        
        # Store board context for modules
        if module_id and module_id not in module_contexts:
            module_contexts[module_id] = {
                "version": result["version"],
                "port": result["port"], 
                "board": result["board"]
            }
        
        if entity_type == "class" and class_id:
            if class_id not in found_classes:
                found_classes[class_id] = {"methods": set(), "attributes": set()}
            # Store board context for fetching basic class info
            board_contexts[class_id] = {
                "version": result["version"],
                "port": result["port"], 
                "board": result["board"],
                "module_id": module_id
            }
        elif entity_type == "method" and class_id:
            if class_id not in found_classes:
                found_classes[class_id] = {"methods": set(), "attributes": set()}
            found_classes[class_id]["methods"].add(entity_name)
            # Store board context
            board_contexts[class_id] = {
                "version": result["version"],
                "port": result["port"], 
                "board": result["board"],
                "module_id": module_id
            }
        elif entity_type == "attribute" and class_id:
            if class_id not in found_classes:
                found_classes[class_id] = {"methods": set(), "attributes": set()}
            found_classes[class_id]["attributes"].add(entity_name)
            # Store board context
            board_contexts[class_id] = {
                "version": result["version"],
                "port": result["port"], 
                "board": result["board"],
                "module_id": module_id
            }
    
    # Second pass: build module tree with only search-relevant content
    for result in results:
        entity_type = result["entity_type"]
        module_id = result.get("module_id")
        class_id = result.get("class_id")
        entity_name = result["entity_name"]
        
        # Get module info  
        if module_id:
            if module_id not in modules:
                # Create module entry if it doesn't exist
                module_name = module_names.get(module_id, "unknown")
                module_context = module_contexts.get(module_id, {})
                modules[module_id] = {
                    "name": module_name,
                    "id": module_id,
                    "classes": {},
                    "constants": [],
                    "functions": [],  # Keep for compatibility even though we don't use it
                    "version": module_context.get("version", ""),
                    "port": module_context.get("port", ""),
                    "board": module_context.get("board", "")
                }
            
            module = modules[module_id]
            
            # For ANY result that has a class_id, ensure the class exists first
            if class_id and class_id not in module["classes"]:
                # Get basic class info and create empty containers for methods/attributes
                try:
                    basic_class = database.get_basic_class_info_for_search(class_id, board_contexts[class_id])
                except KeyError as e:
                    # Class ID not found in board_contexts - this can happen with cross-board search results
                    print(f"Warning: Class ID {class_id} not found in board contexts (key error: {e})")
                    basic_class = None
                except Exception as e:
                    print(f"Error fetching class info for class_id={class_id}: {type(e).__name__}: {e}")
                    basic_class = None
                    
                if basic_class:
                    basic_class["methods"] = []
                    basic_class["attributes"] = []
                    module["classes"][class_id] = basic_class
                else:
                    # Fallback to basic class info if fetch fails
                    module["classes"][class_id] = {
                        "name": "UnknownClass",
                        "id": class_id,
                        "methods": [],
                        "attributes": [],
                        "base_classes": []
                    }
            
            # Now add the specific search result to the appropriate container
            if entity_type == "method" and class_id:
                # Add method to its class
                method_item = {
                    "name": entity_name,
                    "signature": f"{entity_name}()"  # Simple signature for search results
                }
                module["classes"][class_id]["methods"].append(method_item)
                
            elif entity_type == "attribute" and class_id:
                # Add attribute to its class
                attr_item = {
                    "name": entity_name
                }
                module["classes"][class_id]["attributes"].append(attr_item)
                
            elif entity_type == "class" and class_id:
                # Class was directly found in search - populate with COMPLETE class content
                if class_id in module["classes"]:
                    complete_class = database.get_complete_class_for_search(class_id, board_contexts[class_id])
                    if complete_class:
                        # Replace the basic class with the complete one
                        module["classes"][class_id] = complete_class
                    else:
                        print(f"Warning: Failed to get complete class content for {entity_name} (class_id={class_id})")
                else:
                    print(f"Warning: Class {entity_name} (id={class_id}) not found in module classes - unexpected state")
            
            elif entity_type == "constant" and not class_id:
                # Add module-level constant
                module["constants"].append({
                    "name": entity_name,
                    "value": "?",  # We don't have the value in search results
                    "type": "?"
                })
    
    # Convert modules dict to list
    tree_modules = []
    
    # Manually iterate to avoid potential JsProxy issues in PyScript
    try:
        # Get all keys as a list first
        all_keys = []
        for k in modules:
            all_keys.append(k)
        
        # Iterate using the keys list
        for module_id in all_keys:
            module = modules[module_id]
            
            # Convert classes dict to list, filtering out placeholder UnknownClass entries
            # UnknownClass placeholders are created for missing class IDs but have no real content
            classes_list = []
            classes_dict = module["classes"]
            for class_id in classes_dict:
                cls = classes_dict[class_id]
                # Skip UnknownClass placeholders - they're just fallbacks with no content
                if cls.get("name") == "UnknownClass":
                    continue
                classes_list.append(cls)
            
            module["classes"] = classes_list
            
            # Skip empty modules - no classes, methods, attributes, or constants
            if (not classes_list and 
                not module.get("methods") and 
                not module.get("attributes") and 
                not module.get("constants")):
                continue
                
            tree_modules.append(module)
    except Exception as e:
        print(f"Error converting modules dict to tree list: {type(e).__name__}: {e}")
        raise
    
    print(f"Created {len(tree_modules)} modules for tree display")
    return tree_modules


def display_search_results(results, search_term):
    """Display search results using the same DRY tree structure as module explorer."""
    results_div = document.getElementById("search-results")

    if not results:
        ui.show_message("search-results", "Search Results", f'No results found for "<strong>{search_term}</strong>"')
        update_search_url(search_term)
        return

    # Convert search results to tree format (modules with their classes/constants as children)
    tree_modules = convert_search_results_to_tree_format(results)
    
    # Use the existing tree rendering system
    options = {
        "module_prefix": "search",
        "show_details": True,
        "get_badge_class": lambda m: "",
        "get_module_badge": lambda m: "",
    }
    
    # Render using existing tree system
    tree_dom = ui.render_module_tree_dom(tree_modules, options)
    
    # Create search results header
    search_header = document.createElement("div")
    search_header.className = "search-results-header"
    search_header.style.marginBottom = "20px"
    search_header.style.padding = "15px"
    search_header.style.backgroundColor = "#f8f9fa"
    search_header.style.borderRadius = "8px"
    search_header.style.border = "1px solid #dee2e6"
    
    # Create title
    title = document.createElement("h2")
    title.style.margin = "0 0 10px 0"
    title.style.color = "#333"
    title.innerHTML = f'Search Results for "<strong>{search_term}</strong>"'
    
    # Create summary 
    summary = document.createElement("p")
    summary.style.margin = "0"
    summary.style.color = "#666"
    summary.innerHTML = f'Found <strong>{len(results)}</strong> items across <strong>{len(tree_modules)}</strong> modules - expand modules to see details'
    
    search_header.appendChild(title)
    search_header.appendChild(summary)
    
    # Update the search results display
    results_div.innerHTML = ""
    results_div.appendChild(search_header)
    results_div.appendChild(tree_dom)

    # Update URL with search results
    update_search_url(search_term)


def create_search_result_item(result, entity_type):
    """Create a search result item using template with hierarchical indentation."""
    board_name = database.format_board_name(result["port"], result["board"])
    context_path = get_context_path(result)

    # Use search result template
    result_element = ui.get_template("search-result-item-template")
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
        ui.populate_template(
            result_element,
            {"entity-name": entity_name, "context-path": context_path, "board-name": board_name, "version": result["version"]},
        )

        # Set entity icon
        icon_elem = result_element.querySelector("[data-entity-icon]")
        if icon_elem:
            icon_elem.className = f"fas {get_entity_icon(entity_type)}"

        # Set up expansion capability and click handler
        module_id = result["module_id"]
        class_id = result.get("class_id", "")
        entity_name_clean = result["entity_name"]  # Use original name for click handler
        
        # Check if this item can have children and set up expansion
        can_expand = setup_search_result_expansion(result_element, result, entity_type, module_id, class_id)
        
        # Set click handler - if item can expand, handle expansion; otherwise navigate
        def click_handler(e):
            if can_expand:
                toggle_search_result_expansion(result_element, result, entity_type, module_id, class_id, e)
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


def get_entity_icon(entity_type):
    """Get appropriate Font Awesome icon for entity type."""
    icons = {
        "module": "fa-cube",
        "class": "fa-object-group", 
        "function": "fa-bolt",
        "method": "fa-bolt",
        "constant": "fa-circle",
        "attribute": "fa-tag",
        "parameter": "fa-list",
    }
    return icons.get(entity_type, "fa-question")


def setup_search_result_expansion(result_element, result, entity_type, module_id, class_id):
    """Set up expansion capability for search result items. Returns True if item can expand."""
    # Only modules and classes can potentially expand
    if entity_type not in ["module", "class"]:
        return False
    
    # Check if this item actually has children
    has_children = check_search_result_has_children(entity_type, module_id, class_id)
    
    if has_children:
        # Show expansion icon
        expansion_icon = result_element.querySelector("[data-expansion-icon]")
        if expansion_icon:
            expansion_icon.style.display = "inline"
        
        # Add expandable class
        result_element.classList.add("expandable")
        
        # Store data for expansion
        result_element.setAttribute("data-entity-type", entity_type)
        result_element.setAttribute("data-module-id", str(module_id))
        if class_id:
            result_element.setAttribute("data-class-id", str(class_id))
    
    return has_children


def check_search_result_has_children(entity_type, module_id, class_id):
    """Check if a search result item has children using v_entity_hierarchy view.
    
    Uses the v_entity_hierarchy view for unified parent-child queries.
    Replaces multiple UNION queries with single view query.
    """
    if not database.app_state["db"]:
        return False
    
    try:
        # Determine parent_id and parent_type based on entity_type
        if entity_type == "module":
            parent_id = int(module_id)
            parent_type = "module"
        elif entity_type == "class":
            parent_id = int(class_id)
            parent_type = "class"
        else:
            return False
        
        # Single query using v_entity_hierarchy view
        stmt = database.app_state["db"].prepare("""
            SELECT COUNT(*) as count 
            FROM v_entity_hierarchy 
            WHERE parent_id = ? AND parent_type = ?
            LIMIT 1
        """)
        stmt.bind(ffi.to_js([parent_id, parent_type]))
            
        if stmt.step():
            count = stmt.getAsObject()["count"]
            stmt.free()
            return count > 0
        
        stmt.free()
        return False
        
    except Exception as e:
        print(f"Error checking children for {entity_type}: {e}")
        return False


def toggle_search_result_expansion(result_element, result, entity_type, module_id, class_id, event):
    """Toggle expansion of a search result item."""
    event.stopPropagation()
    
    children_container = result_element.querySelector("[data-search-result-children]")
    expansion_icon = result_element.querySelector("[data-expansion-icon]")
    
    if not children_container:
        return
    
    # Toggle expansion state
    is_expanded = not children_container.classList.contains("hidden")
    
    if is_expanded:
        # Collapse
        children_container.classList.add("hidden")
        if expansion_icon:
            expansion_icon.style.transform = "rotate(0deg)"
    else:
        # Expand - load children if not already loaded
        if children_container.children.length == 0:
            load_search_result_children(children_container, entity_type, module_id, class_id, result)
        
        children_container.classList.remove("hidden")
        if expansion_icon:
            expansion_icon.style.transform = "rotate(90deg)"


def load_search_result_children(container, entity_type, module_id, class_id, parent_result):
    """Load and display children of a search result item, reusing existing database queries."""
    if not database.app_state["db"]:
        return
    
    try:
        children = []
        
        if entity_type == "module":
            # Get classes for this module
            classes = get_search_result_classes(module_id, parent_result)
            children.extend(classes)
            
            # Get constants for this module
            constants = get_search_result_constants(module_id, parent_result)
            children.extend(constants)
            
        elif entity_type == "class":
            # Get methods for this class
            methods = get_search_result_methods(class_id, parent_result)
            children.extend(methods)
            
            # Get attributes for this class
            attributes = get_search_result_attributes(class_id, parent_result)
            children.extend(attributes)
        
        # Display children
        for child in children:
            child_element = create_search_result_item(child, child["entity_type"])
            container.appendChild(child_element)
            
    except Exception as e:
        print(f"Error loading children for {entity_type}: {e}")


# Helper functions for search result children - using v_entity_hierarchy view
def get_search_result_children_from_hierarchy(parent_id, parent_type, parent_result, entity_type_filter=None):
    """Get children for a parent entity using v_entity_hierarchy view.
    
    Unified function that replaces individual get_search_result_* functions.
    Uses v_entity_hierarchy view for consistent parent-child queries.
    
    Args:
        parent_id: ID of the parent entity
        parent_type: Type of parent ('module' or 'class')
        parent_result: Parent result dict to copy context from
        entity_type_filter: Optional filter for specific entity type
        
    Returns:
        List of child result dicts with appropriate type-specific ID fields
    """
    children = []
    
    # Query v_entity_hierarchy view for all children
    sql = """
        SELECT entity_id, entity_type, entity_name 
        FROM v_entity_hierarchy 
        WHERE parent_id = ? AND parent_type = ?
    """
    if entity_type_filter:
        sql += " AND entity_type = ?"
        
    stmt = database.app_state["db"].prepare(sql)
    
    if entity_type_filter:
        stmt.bind(ffi.to_js([int(parent_id), parent_type, entity_type_filter]))
    else:
        stmt.bind(ffi.to_js([int(parent_id), parent_type]))
    
    while stmt.step():
        child_data = stmt.getAsObject()
        child_result = dict(parent_result)  # Copy parent data
        
        # Set entity type and name
        child_result["entity_type"] = child_data["entity_type"]
        child_result["entity_name"] = child_data["entity_name"]
        
        # Set type-specific ID field for backward compatibility
        entity_type = child_data["entity_type"]
        entity_id = child_data["entity_id"]
        
        if entity_type == "class":
            child_result["class_id"] = entity_id
        elif entity_type == "constant":
            child_result["constant_id"] = entity_id
        elif entity_type == "method":
            child_result["method_id"] = entity_id
        elif entity_type == "attribute":
            child_result["attribute_id"] = entity_id
            
        children.append(child_result)
    
    stmt.free()
    return children


def get_search_result_classes(module_id, parent_result):
    """Get classes for a module in search result format.
    
    Wrapper for backward compatibility - uses v_entity_hierarchy view.
    """
    return get_search_result_children_from_hierarchy(
        int(module_id), "module", parent_result, "class"
    )


def get_search_result_constants(module_id, parent_result):
    """Get constants for a module in search result format.
    
    Wrapper for backward compatibility - uses v_entity_hierarchy view.
    """
    return get_search_result_children_from_hierarchy(
        int(module_id), "module", parent_result, "constant"
    )


def get_search_result_methods(class_id, parent_result):
    """Get methods for a class in search result format.
    
    Wrapper for backward compatibility - uses v_entity_hierarchy view.
    """
    return get_search_result_children_from_hierarchy(
        int(class_id), "class", parent_result, "method"
    )


def get_search_result_attributes(class_id, parent_result):
    """Get attributes for a class in search result format.
    
    Wrapper for backward compatibility - uses v_entity_hierarchy view.
    """
    return get_search_result_children_from_hierarchy(
        int(class_id), "class", parent_result, "attribute"
    )


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


def get_method_parameters(method_id):
    """Get parameters for a method/function."""
    if not database.app_state["db"]:
        return []

    try:
        stmt = database.app_state["db"].prepare("""
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


def update_search_url(query=""):
    """Update the URL to reflect the current search state."""
    # Get current URL
    url = window.location.href.split('?')[0]

    # Build query parameters
    params = []
    params.append("view=search")

    if query:
        params.append(f"query={window.encodeURIComponent(query)}")

    if params:
        new_url = f"{url}?{'&'.join(params)}"
        window.history.replaceState(ffi.to_js({}), ffi.to_js(""), ffi.to_js(new_url))


async def populate_search_from_url(search_params):
    """Populate the search page from URL parameters."""
    try:
        query = search_params.get("query")

        if query:
            search_input = document.getElementById("search-input")
            if search_input:
                # Decode the query parameter
                search_input.value = window.decodeURIComponent(query)
                
                # Perform the search
                await search_apis()

    except Exception as e:
        print(f"Error populating search from URL: {e}")


def share_search(event=None):
    """Share the current search view."""
    print("=== Share Search Called ===")
    
    search_input = document.getElementById("search-input")
    query = search_input.value.strip() if search_input else ""
    
    print(f"Search query: '{query}'")

    if not query:
        print("No query entered, showing error")
        ui.show_error("Please enter a search term to share")
        return

    # Build share URL
    base_url = window.location.href.split('?')[0]
    params = ["view=search"]

    params.append(f"query={window.encodeURIComponent(query)}")

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


async def open_search_result(module_id, class_id, entity_name, entity_type):
    """Navigate to search result in the explorer."""
    # Switch to explorer page
    from main import switch_page
    switch_page("explorer")

    # Find the board that has this module
    if not database.app_state["db"]:
        return

    try:
        # Get board info for this module
        stmt = database.app_state["db"].prepare("""
            SELECT b.version, b.port, b.board
            FROM boards b
            JOIN board_module_support bms ON b.id = bms.board_id
            WHERE bms.module_id = ?
            ORDER BY b.version DESC
            LIMIT 1
        """)
        stmt.bind(ffi.to_js([int(module_id)]))

        if stmt.step():
            board_info = stmt.getAsObject()
            board_name = database.format_board_name(board_info["port"], board_info["board"])

            # Set the dropdowns
            version_select = document.getElementById("explorer-version")
            if version_select:
                version_select.value = board_info["version"]

            board_select = document.getElementById("explorer-board")
            if board_select:
                board_select.value = board_name

            # Load board details
            from explorer import load_board_details
            await load_board_details()

            # TODO: Expand to specific item (module, class, method) if needed
            # This would require additional DOM traversal and expansion logic

        stmt.free()

    except Exception as e:
        print(f"Error opening search result: {e}")


def setup_search_event_handlers():
    """Set up event handlers specific to the search page."""
    # Search button - HTML has mpy-click="search_apis" which calls main.search_apis()
    # Previous Python override removed: search_btn.onclick = lambda e: asyncio.create_task(search_apis())
    
    # Search input (Enter key) - direct event handler (no mpy-click equivalent for keypress)
    search_input = document.getElementById("search-input")
    if search_input:
        search_input.onkeypress = lambda e: asyncio.create_task(search_apis()) if e.key == "Enter" else None

    # Share button - HTML has mpy-click="share_search" which calls main.share_search()
    # Previous Python override removed: share_search_btn.onclick = lambda e: share_search()

    # Max results dropdown (for URL updates)
    max_results_select = document.getElementById("max-results")
    if max_results_select:
        max_results_select.onchange = lambda e: update_search_url(search_input.value if search_input else "")