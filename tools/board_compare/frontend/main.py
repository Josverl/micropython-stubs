# main.py - Application coordination and initialization
# Refactored in Sprint 3 to coordinate page modules

import asyncio
import js

# Import all modules
import database
import ui
import explorer
import compare
import search

from pyscript import document


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
    if not database.app_state["boards"]:
        return

    # Get unique versions
    versions = list(set(board.get("version", "") for board in database.app_state["boards"]))
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
    board_names = list(set(database.format_board_name(board.get("port", ""), board.get("board", "")) for board in database.app_state["boards"]))
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


def initialize_searchable_dropdowns():
    """Initialize searchable dropdowns using JavaScript."""
    js.eval("""
    // Initialize searchable dropdowns for board selection
    function initializeSearchableDropdown(selectId) {
        const select = document.getElementById(selectId);
        if (!select) return;
        
        // Create wrapper
        const wrapper = document.createElement('div');
        wrapper.className = 'dropdown-wrapper';
        wrapper.style.position = 'relative';
        wrapper.style.display = 'inline-block';
        wrapper.style.width = '100%';
        
        // Create search input
        const input = document.createElement('input');
        input.type = 'text';
        input.className = 'form-control dropdown-search';
        input.placeholder = select.options[0]?.text || 'Select...';
        input.style.width = '100%';
        
        // Create dropdown
        const dropdown = document.createElement('div');
        dropdown.className = 'dropdown-options';
        dropdown.style.position = 'absolute';
        dropdown.style.top = '100%';
        dropdown.style.left = '0';
        dropdown.style.right = '0';
        dropdown.style.backgroundColor = 'white';
        dropdown.style.border = '1px solid #ced4da';
        dropdown.style.borderTop = 'none';
        dropdown.style.maxHeight = '200px';
        dropdown.style.overflowY = 'auto';
        dropdown.style.zIndex = '1000';
        dropdown.style.display = 'none';
        
        // Populate dropdown options
        function populateDropdown(filter = '') {
            dropdown.innerHTML = '';
            for (let i = 0; i < select.options.length; i++) {
                const option = select.options[i];
                if (filter === '' || option.text.toLowerCase().includes(filter.toLowerCase())) {
                    const div = document.createElement('div');
                    div.className = 'dropdown-option';
                    div.textContent = option.text;
                    div.style.padding = '8px 12px';
                    div.style.cursor = 'pointer';
                    div.style.borderBottom = '1px solid #eee';
                    
                    div.addEventListener('click', () => {
                        select.value = option.value;
                        input.value = option.text;
                        dropdown.style.display = 'none';
                        
                        // Trigger change event
                        const changeEvent = new Event('change', { bubbles: true });
                        select.dispatchEvent(changeEvent);
                    });
                    
                    div.addEventListener('mouseenter', () => {
                        div.style.backgroundColor = '#f8f9fa';
                    });
                    
                    div.addEventListener('mouseleave', () => {
                        div.style.backgroundColor = 'white';
                    });
                    
                    dropdown.appendChild(div);
                }
            }
        }
        
        // Event listeners
        input.addEventListener('input', (e) => {
            populateDropdown(e.target.value);
            dropdown.style.display = 'block';
        });
        
        input.addEventListener('focus', () => {
            populateDropdown(input.value);
            dropdown.style.display = 'block';
        });
        
        document.addEventListener('click', (e) => {
            if (!wrapper.contains(e.target)) {
                dropdown.style.display = 'none';
            }
        });
        
        // Replace select with wrapper
        select.parentNode.insertBefore(wrapper, select);
        select.style.display = 'none';
        
        wrapper.appendChild(input);
        wrapper.appendChild(dropdown);
        wrapper.appendChild(select);
        
        populateDropdown();
    }
    
    // Initialize all board selects
    initializeSearchableDropdown('explorer-board');
    initializeSearchableDropdown('board1');
    initializeSearchableDropdown('board2');
    """)


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

    # Set up page-specific event handlers
    explorer.setup_explorer_event_handlers()
    compare.setup_compare_event_handlers()
    search.setup_search_event_handlers()


async def main():
    """Main entry point for the application."""
    update_status("Loading board utilities...", "info")

    # Set up event handlers
    setup_event_handlers()

    # Load database
    db_loaded = await database.load_database()

    if db_loaded:
        # Load board list from database
        await database.load_board_list_from_db()
        populate_board_selects()

        # Initialize searchable dropdowns after populating selects
        initialize_searchable_dropdowns()

        # Check URL parameters and auto-switch to appropriate mode
        url = js.eval("new URL(window.location.href)")

        # Get individual parameters using URLSearchParams.get() method
        search_params = url.searchParams
        view = search_params.get("view")

        # Handle different views and populate their parameters
        if view == "compare":
            # Switch to comparison mode and populate parameters
            switch_page("compare")
            await compare.populate_comparison_from_url(search_params)
        elif view == "explorer":
            # Switch to explorer mode and populate parameters
            switch_page("explorer")
            await explorer.populate_explorer_from_url(search_params)
        elif view == "search":
            # Switch to search mode and populate parameters
            switch_page("search")
            await search.populate_search_from_url(search_params)

        update_status("Loaded database. Application ready!", "success")
    else:
        # Database is required
        update_status("Failed to load database. Cannot continue.", "error")


# Start the application
asyncio.create_task(main())