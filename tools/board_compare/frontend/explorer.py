# explorer.py - Board Explorer functionality
# Extracted from main.py as part of Sprint 3 refactoring

import asyncio
import json

# Import modules
import database
import ui
from pyscript import document, window


async def load_board_details():
    """Load the details for the selected board."""
    version_select = document.getElementById("explorer-version")
    board_select = document.getElementById("explorer-board")
    
    selected_version = version_select.value if version_select else ""
    selected_board = board_select.value if board_select else ""
    
    if not selected_board:
        return
    
    ui.show_loading("Loading board details...")
    
    try:
        # Find the board in the database
        matching_boards = []
        for board in database.app_state["boards"]:
            board_name = database.format_board_name(board.get("port", ""), board.get("board", ""))
            if board_name == selected_board:
                if not selected_version or board.get("version", "") == selected_version:
                    matching_boards.append(board)
        
        if not matching_boards:
            ui.show_error("Board not found in database")
            return
        
        # Use the first matching board (or most recent if multiple)
        board = matching_boards[0] if len(matching_boards) == 1 else max(matching_boards, key=lambda b: b.get("version", ""))
        
        # Store current board
        database.app_state["current_board"] = board
        
        # Get board display name for use throughout function
        board_display_name = database.format_board_name(board.get("port", ""), board.get("board", ""))
        
        # Update board info display
        info_elem = document.getElementById("board-info")
        if info_elem:
            version_info = f" (v{board['version']})" if board.get("version") else ""
            info_elem.innerHTML = f"<h3>{board_display_name}{version_info}</h3>"
        
        # Load modules for this board
        modules = database.get_board_modules(board["id"])
        
        if not modules:
            ui.show_error("No modules found for this board")
            return
        
        # Update modules count
        modules_heading = document.getElementById("modules-heading")
        if modules_heading:
            modules_heading.innerHTML = f'<span class="icon">📁</span> Modules ({len(modules)})'
        
        # Render the module tree using UI function
        render_options = {
            'expand_deprecated': True,
            'show_only_differences': False
        }
        
        modules_container = document.getElementById("modules")
        if modules_container:
            # Use the ui function to render the tree into the container
            tree_html = ui.render_module_tree_dom(modules, render_options)
            modules_container.innerHTML = tree_html
        
        ui.show_message(f"Loaded {len(modules)} modules for {board_display_name}")
        
        # Update URL to reflect current state
        update_explorer_url()
        
    except Exception as e:
        ui.show_error(f"Error loading board details: {str(e)}")
        print(f"Error in load_board_details: {e}")


def update_explorer_url():
    """Update the URL to reflect the current explorer state."""
    version_select = document.getElementById("explorer-version")
    board_select = document.getElementById("explorer-board")
    
    version = version_select.value if version_select else ""
    board = board_select.value if board_select else ""
    
    # Get current URL
    url = window.location.href.split('?')[0]
    
    # Build query parameters
    params = []
    params.append("view=explorer")
    
    if version:
        params.append(f"version={window.encodeURIComponent(version)}")
    if board:
        params.append(f"board={window.encodeURIComponent(board)}")
    
    if params:
        new_url = f"{url}?{'&'.join(params)}"
        window.history.replaceState({}, "", new_url)


async def populate_explorer_from_url(search_params):
    """Populate the explorer page from URL parameters."""
    if "view" in search_params and search_params["view"][0] == "explorer":
        version = search_params.get("version", [""])[0]
        board = search_params.get("board", [""])[0]
        
        # Set the version dropdown
        version_select = document.getElementById("explorer-version")
        if version_select and version:
            version_select.value = version
        
        # Set the board dropdown  
        board_select = document.getElementById("explorer-board")
        if board_select and board:
            board_select.value = board
            
        # Load the board details if we have a board selected
        if board:
            await load_board_details()


def share_explorer():
    """Share the current explorer view."""
    version_select = document.getElementById("explorer-version")
    board_select = document.getElementById("explorer-board")
    
    version = version_select.value if version_select else ""
    board = board_select.value if board_select else ""
    
    if not board:
        ui.show_error("Please select a board to share")
        return
    
    # Build share URL
    base_url = window.location.href.split('?')[0]
    params = ["view=explorer"]
    
    if version:
        params.append(f"version={window.encodeURIComponent(version)}")
    if board:
        params.append(f"board={window.encodeURIComponent(board)}")
    
    share_url = f"{base_url}?{'&'.join(params)}"
    
    # Copy to clipboard
    window.navigator.clipboard.writeText(share_url).then(
        lambda: ui.show_message("Share URL copied to clipboard!"),
        lambda: ui.show_error("Failed to copy URL to clipboard")
    )


def setup_explorer_event_handlers():
    """Set up event handlers specific to the explorer page."""
    # Version dropdown change handler
    version_select = document.getElementById("explorer-version")
    if version_select:
        version_select.onchange = lambda e: asyncio.create_task(load_board_details())
    
    # Board dropdown change handler  
    board_select = document.getElementById("explorer-board")
    if board_select:
        board_select.onchange = lambda e: asyncio.create_task(load_board_details())
    
    # Share button
    share_explorer_btn = document.getElementById("share-explorer")
    if share_explorer_btn:
        share_explorer_btn.onclick = lambda e: share_explorer()