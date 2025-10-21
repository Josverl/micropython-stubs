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
        # Search modules - try a simpler approach first
        print("Searching modules...")

        # First try without any LIKE pattern - just get all modules and filter in Python
        all_modules_stmt = database.app_state["db"].prepare("""
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
        print(f"Added {len(module_matches)} module results. Total results so far: {len(results)}")

        # Search classes
        print(f"Starting class search for pattern: {search_pattern}")
        stmt = database.app_state["db"].prepare("""
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

        stmt.bind(ffi.to_js([search_pattern]))
        class_count = 0
        while stmt.step():
            class_count += 1
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
            # Debug: Print first few matches
            if class_count <= 3:
                print(f"Class match {class_count}: {result['entity_name']} in {result['parent_name']} (ID: {result['class_id']})")
        stmt.free()
        print(f"Found {class_count} classes matching '{search_term}'")

        # Search methods
        print(f"Starting method search for pattern: {search_pattern}")
        stmt = database.app_state["db"].prepare("""
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

        stmt.bind(ffi.to_js([search_pattern]))
        method_count = 0
        while stmt.step():
            method_count += 1
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
        stmt.free()
        print(f"Found {method_count} methods matching '{search_term}'")

        # Search module constants
        stmt = database.app_state["db"].prepare("""
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

        stmt.bind(ffi.to_js([search_pattern]))
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
        stmt.free()

        # Search class attributes
        stmt = database.app_state["db"].prepare("""
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

        stmt.bind(ffi.to_js([search_pattern]))
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
        stmt.free()

        # Search parameters
        stmt = database.app_state["db"].prepare("""
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

        stmt.bind(ffi.to_js([search_pattern]))
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
        stmt.free()

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
    print(f"DEBUG: Converting {len(results)} search results to tree format")
    
    # Debug: Log sample results to understand data structure
    for i, result in enumerate(results[:5]):  # Log first 5 results
        print(f"DEBUG: Result {i}: {result['entity_type']} '{result['entity_name']}' in module {result.get('parent_name', 'N/A')} (module_id: {result.get('module_id')}, class_id: {result.get('class_id')})")
    
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
        else:
            print(f"DEBUG: Filtering duplicate {result['entity_type']} '{result['entity_name']}' in class {result.get('class_id')}")
    
    print(f"DEBUG: After deduplication: {len(deduplicated_results)} results (removed {len(filtered_results) - len(deduplicated_results)} duplicates)")
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
                basic_class = database.get_basic_class_info_for_search(class_id, board_contexts[class_id])
                if basic_class:
                    basic_class["methods"] = []
                    basic_class["attributes"] = []
                    module["classes"][class_id] = basic_class
                    print(f"DEBUG: Created class {basic_class['name']} (id: {class_id}) in module {module['name']}")
                else:
                    # Fallback to basic class info if fetch fails
                    module["classes"][class_id] = {
                        "name": "UnknownClass",
                        "id": class_id,
                        "methods": [],
                        "attributes": [],
                        "base_classes": []
                    }
                    print(f"DEBUG: Created fallback class (id: {class_id}) in module {module['name']}")
            
            # Now add the specific search result to the appropriate container
            if entity_type == "method" and class_id:
                # Add method to its class
                method_item = {
                    "name": entity_name,
                    "signature": f"{entity_name}()"  # Simple signature for search results
                }
                module["classes"][class_id]["methods"].append(method_item)
                print(f"DEBUG: Added method {entity_name} to class {class_id} in module {module['name']}")
                
            elif entity_type == "attribute" and class_id:
                # Add attribute to its class
                attr_item = {
                    "name": entity_name
                }
                module["classes"][class_id]["attributes"].append(attr_item)
                print(f"DEBUG: Added attribute {entity_name} to class {class_id} in module {module['name']}")
                
            elif entity_type == "class" and class_id:
                # Class was directly found in search - populate with COMPLETE class content
                if class_id in module["classes"]:
                    print(f"DEBUG: Class {entity_name} was directly found in search - populating with complete content")
                    complete_class = database.get_complete_class_for_search(class_id, board_contexts[class_id])
                    if complete_class:
                        # Replace the basic class with the complete one
                        module["classes"][class_id] = complete_class
                        print(f"DEBUG: Populated class {entity_name} with {len(complete_class.get('methods', []))} methods and {len(complete_class.get('attributes', []))} attributes")
                    else:
                        print(f"DEBUG: Failed to get complete class content for {entity_name}")
                else:
                    print(f"DEBUG: Class {entity_name} not found in module classes - this shouldn't happen")
            
            elif entity_type == "constant" and not class_id:
                # Add module-level constant
                module["constants"].append({
                    "name": entity_name,
                    "value": "?",  # We don't have the value in search results
                    "type": "?"
                })
                print(f"DEBUG: Added constant {entity_name} to module {module['name']}")
    
    # Convert to list format expected by tree renderer
    tree_modules = []
    for module in modules.values():
        # Convert classes dict to list
        module["classes"] = list(module["classes"].values())
        tree_modules.append(module)
    
    print(f"DEBUG: Created {len(tree_modules)} modules for tree display")
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
    """Check if a search result item has children using existing database queries."""
    if not database.app_state["db"]:
        return False
    
    try:
        if entity_type == "module":
            # Check if module has classes or functions
            stmt = database.app_state["db"].prepare("""
                SELECT COUNT(*) as count FROM (
                    SELECT 1 FROM unique_classes WHERE module_id = ? 
                    UNION ALL 
                    SELECT 1 FROM unique_module_constants WHERE module_id = ?
                ) LIMIT 1
            """)
            stmt.bind(ffi.to_js([int(module_id), int(module_id)]))
            
        elif entity_type == "class":
            # Check if class has methods or attributes  
            stmt = database.app_state["db"].prepare("""
                SELECT COUNT(*) as count FROM (
                    SELECT 1 FROM unique_methods WHERE class_id = ?
                    UNION ALL
                    SELECT 1 FROM unique_class_attributes WHERE class_id = ?
                ) LIMIT 1
            """)
            stmt.bind(ffi.to_js([int(class_id), int(class_id)]))
        else:
            return False
            
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


# Helper functions for search result children (DRY - reuse database patterns)
def get_search_result_classes(module_id, parent_result):
    """Get classes for a module in search result format."""
    classes = []
    stmt = database.app_state["db"].prepare("SELECT id, name FROM unique_classes WHERE module_id = ?")
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
    stmt = database.app_state["db"].prepare("SELECT id, name FROM unique_module_constants WHERE module_id = ?")
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
    stmt = database.app_state["db"].prepare("SELECT id, name FROM unique_methods WHERE class_id = ?")
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
    stmt = database.app_state["db"].prepare("SELECT id, name FROM unique_class_attributes WHERE class_id = ?")
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
        window.history.replaceState({}, "", new_url)


async def populate_search_from_url(search_params):
    """Populate the search page from URL parameters."""
    if "view" in search_params and search_params["view"][0] == "search":
        query = search_params.get("query", [""])[0]

        # Set the search input
        search_input = document.getElementById("search-input")
        if search_input and query:
            search_input.value = query
            
            # Perform the search
            await search_apis()


def share_search():
    """Share the current search view."""
    search_input = document.getElementById("search-input")
    query = search_input.value.strip() if search_input else ""

    if not query:
        ui.show_error("Please enter a search term to share")
        return

    # Build share URL
    base_url = window.location.href.split('?')[0]
    params = ["view=search"]

    params.append(f"query={window.encodeURIComponent(query)}")

    share_url = f"{base_url}?{'&'.join(params)}"

    # Copy to clipboard
    window.navigator.clipboard.writeText(share_url).then(
        lambda: ui.show_message("Share URL copied to clipboard!"),
        lambda: ui.show_error("Failed to copy URL to clipboard")
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
    # Search button
    search_btn = document.getElementById("search-btn")
    if search_btn:
        search_btn.onclick = lambda e: asyncio.create_task(search_apis())

    # Search input (Enter key)
    search_input = document.getElementById("search-input")
    if search_input:
        search_input.onkeypress = lambda e: asyncio.create_task(search_apis()) if e.key == "Enter" else None

    # Share button
    share_search_btn = document.getElementById("share-search")
    if share_search_btn:
        share_search_btn.onclick = lambda e: share_search()

    # Max results dropdown (for URL updates)
    max_results_select = document.getElementById("max-results")
    if max_results_select:
        max_results_select.onchange = lambda e: update_search_url(search_input.value if search_input else "")