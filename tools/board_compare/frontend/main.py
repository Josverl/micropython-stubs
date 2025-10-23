# main.py - Application coordination and initialization
# Refactored in Sprint 3 to coordinate page modules

import asyncio

import compare

# Import all modules
import database
import explorer
import js
import search
import ui

# Import share functions directly to make them available in global scope for mpy-click
from compare import share_comparison
from explorer import share_explorer
from pyscript import document
from search import share_search

__version__ = "0.5.0"


def go_explorer(event=None):
    """Wrapper for mpy-click navigation to explorer page."""
    switch_page("explorer")

def go_compare(event=None):
    """Wrapper for mpy-click navigation to compare page."""
    switch_page("compare")

def go_search(event=None):
    """Wrapper for mpy-click navigation to search page."""
    switch_page("search")

def retry_comparison(event=None):
    """Wrapper for mpy-click retry button in error template."""
    asyncio.create_task(compare.compare_boards())

def search_apis(event=None):
    """Wrapper for mpy-click search button - handles async search_apis() from search module."""
    asyncio.create_task(search.search_apis())

def compare_boards(event=None):
    """Wrapper for mpy-click compare button - handles async compare_boards() from compare module."""
    asyncio.create_task(compare.compare_boards())

def toggle_tree_node(event):
    """Toggle visibility of a tree node's children (modules, classes)."""
    if event:
        event.stopPropagation()
        # Get element ID from data attribute
        target = event.target
        # Find the element with data-module-target or data-class-target
        # Note: dataset is a JS proxy, use attribute access not .get()
        element_id = getattr(target.dataset, 'moduleTarget', None) or getattr(target.dataset, 'classTarget', None)
        if element_id:
            elem = document.getElementById(element_id)
            if elem:
                elem.classList.toggle("hidden")

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
    """Populate all board selection datalists."""
    if not database.app_state["boards"]:
        return

    # Get unique versions
    versions = list(set(board.get("version", "") for board in database.app_state["boards"]))
    versions.sort(reverse=True)

    # Populate version datalists
    for list_id in ["explorer-version-list", "board1-version-list", "board2-version-list"]:
        datalist = document.getElementById(list_id)
        datalist.innerHTML = '<option value="">All versions</option>'

        for version in versions:
            option = document.createElement("option")
            option.value = version
            datalist.appendChild(option)

    # Get unique board names (formatted)
    board_names = list(set(database.format_board_name(board.get("port", ""), board.get("board", "")) for board in database.app_state["boards"]))
    board_names.sort()

    # Populate board datalists
    for list_id in ["explorer-board-list", "board1-list", "board2-list"]:
        datalist = document.getElementById(list_id)
        datalist.innerHTML = '<option value="">Select a board...</option>'

        for board_name in board_names:
            option = document.createElement("option")
            option.value = board_name
            datalist.appendChild(option)


def initialize_input_change_handlers():
    """Set up change handlers for input elements - handled by individual modules."""
    # URL update handlers are now set up by the individual page modules
    # in their respective setup_*_event_handlers() functions
    pass


def setup_event_handlers():
    """Set up event listeners for the UI."""
    # Navigation handled by mpy-click attributes (go_explorer/go_compare/go_search)

    # Set up page-specific event handlers
    print("Setting up page-specific event handlers...")
    explorer.setup_explorer_event_handlers()
    compare.setup_compare_event_handlers()
    search.setup_search_event_handlers()
    print("Event handlers setup complete")


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

        # Initialize input change handlers for URL updates
        initialize_input_change_handlers()

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