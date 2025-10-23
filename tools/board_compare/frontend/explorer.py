# explorer.py - Board Explorer functionality
# Extracted from main.py as part of Sprint 3 refactoring

import asyncio

# Import modules
import database
import ui
from pyscript import document, ffi, window


async def load_board_details():
    """Load board details when a board is selected."""
    version_input = document.getElementById("explorer-version")
    board_input = document.getElementById("explorer-board")

    selected_version = version_input.value if version_input else ""
    selected_board_name = board_input.value if board_input else ""

    content = document.getElementById("explorer-content")

    if not selected_version or not selected_board_name:
        # Show selection prompt using message template
        ui.show_message("explorer-content", "", "Select both version and board to explore modules and APIs")
        return

    # Show loading using template
    ui.show_loading("explorer-content", "Loading board details...", "Fetching modules...")

    if not database.app_state["db"]:
        # Database is required - use error template
        ui.show_error(
            "explorer-content",
            f"{selected_board_name} ({selected_version})",
            "Database not loaded. Please refresh the page to retry loading the database.",
        )
        return

    try:
        # Find the actual port/board from the board list
        board_info = None
        for board in database.app_state["boards"]:
            board_name = database.format_board_name(board.get("port", ""), board.get("board", ""))
            if board_name == selected_board_name and (not selected_version or board.get("version", "") == selected_version):
                board_info = board
                break

        if not board_info:
            ui.show_error("explorer-content", "Board Not Found", f"Could not find board: {selected_board_name} ({selected_version})")
            return

        # Store current board
        database.app_state["current_board"] = board_info

        # Load modules for this board
        modules = database.get_board_modules(board_info)

        if not modules:
            ui.show_error("explorer-content", f"{selected_board_name} ({selected_version})", "No modules found for this board")
            return

        # Create board details display
        board_display_name = database.format_board_name(board_info.get("port", ""), board_info.get("board", ""))
        version_info = f" ({board_info['version']})" if board_info.get("version") else ""

        # Create module tree using DOM-based rendering
        options = {"module_prefix": "explorer", "get_badge_class": lambda m: "", "get_module_badge": lambda m: "", "show_details": True}

        module_tree_dom = ui.render_module_tree_dom(modules, options)

        # Create board details using templates
        board_details_element = ui.get_template("board-details-template")
        board_content_element = ui.get_template("board-content-template")

        if board_details_element and board_content_element:
            # Populate board details template
            ui.populate_template(board_details_element, {"board-title": f"{board_display_name}{version_info}"})

            # Populate board content template
            ui.populate_template(board_content_element, {"modules-title": f"Modules ({len(modules)})"})

            # Get the board content container and modules tree container
            board_content_container = board_details_element.querySelector("[data-board-content]")
            modules_tree_container = board_content_element.querySelector("[data-modules-tree]")

            if board_content_container and modules_tree_container:
                # Add the module tree DOM to the modules container
                if module_tree_dom:
                    modules_tree_container.appendChild(module_tree_dom)

                # Add the board content to the board details
                board_content_container.appendChild(board_content_element)

                # Replace the explorer content with the new template-based structure
                content.innerHTML = ""
                content.appendChild(board_details_element)

        # Update URL to reflect current state
        update_explorer_url()

    except Exception as e:
        ui.show_error("explorer-content", "⚠️ Error Loading Board", f"{str(e)}")
        print(f"Error loading board details: {e}")


def update_explorer_url():
    """Update the URL to reflect the current explorer state."""
    version_input = document.getElementById("explorer-version")
    board_input = document.getElementById("explorer-board")

    version = version_input.value if version_input else ""
    board = board_input.value if board_input else ""

    # Get current URL
    url = window.location.href.split("?")[0]

    # Build query parameters
    params = []
    params.append("view=explorer")

    if version:
        params.append(f"version={window.encodeURIComponent(version)}")
    if board:
        params.append(f"board={window.encodeURIComponent(board)}")

    if params:
        new_url = f"{url}?{'&'.join(params)}"
        window.history.replaceState(ffi.to_js({}), ffi.to_js(""), ffi.to_js(new_url))


async def populate_explorer_from_url(search_params):
    """Populate the explorer page from URL parameters."""
    try:
        version = search_params.get("version")
        board = search_params.get("board")

        if version:
            version_input = document.getElementById("explorer-version")
            if version_input:
                version_input.value = version

        if board:
            board_input = document.getElementById("explorer-board")
            if board_input:
                board_input.value = board

        # Trigger board details load if both are set
        if version and board:
            await load_board_details()

    except Exception as e:
        print(f"Error populating explorer from URL: {e}")


def share_explorer(event=None):
    """Share the current explorer view."""
    print("=== Share Explorer Called ===")

    version_input = document.getElementById("explorer-version")
    board_input = document.getElementById("explorer-board")

    version = version_input.value if version_input else ""
    board = board_input.value if board_input else ""

    print(f"Version: '{version}', Board: '{board}'")

    if not board:
        print("No board selected, showing error")
        ui.show_error("Please select a board to share")
        return

    # Build share URL
    base_url = window.location.href.split("?")[0]
    params = ["view=explorer"]

    if version:
        params.append(f"version={window.encodeURIComponent(version)}")
    if board:
        params.append(f"board={window.encodeURIComponent(board)}")

    share_url = f"{base_url}?{'&'.join(params)}"
    print(f"Share URL: {share_url}")

    # Copy to clipboard
    try:
        print("Attempting to copy to clipboard...")
        window.navigator.clipboard.writeText(share_url)
        print("Clipboard write successful, updating status...")

        # Update status directly by manipulating DOM elements
        status_text = document.getElementById("status-text")
        status_elem = document.getElementById("status")
        if status_text and status_elem:
            status_text.innerText = "Share URL copied to clipboard!"
            status_elem.classList.remove("error")
            status_elem.classList.add("success")

        print("Status updated successfully")
    except Exception as e:
        print(f"Error copying to clipboard: {e}")

        # Update status directly by manipulating DOM elements
        status_text = document.getElementById("status-text")
        status_elem = document.getElementById("status")
        if status_text and status_elem:
            status_text.innerText = "Failed to copy URL to clipboard"
            status_elem.classList.remove("success")
            status_elem.classList.add("error")


def setup_explorer_event_handlers():
    """Set up event handlers specific to the explorer page."""
    print("Setting up explorer event handlers...")

    # Version input change handler
    version_input = document.getElementById("explorer-version")
    if version_input:
        print(f"Found version input: {version_input}")

        def version_handler(e):
            asyncio.create_task(load_board_details())
            update_explorer_url()

        version_input.oninput = version_handler
        version_input.onchange = version_handler
    else:
        print("Version input not found!")

    # Board input change handler
    board_input = document.getElementById("explorer-board")
    if board_input:
        print(f"Found board input: {board_input}")

        def board_handler(e):
            asyncio.create_task(load_board_details())
            update_explorer_url()

        board_input.oninput = board_handler
        board_input.onchange = board_handler
    else:
        print("Board input not found!")

    # Share button - HTML has mpy-click="share_explorer" which calls main.share_explorer()
    # Previous Python override removed: share_explorer_btn.onclick = lambda e: share_explorer()

