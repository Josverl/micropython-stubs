"""
PyScript application for MicroPython board comparison.
"""

import json
from pyscript import document, window, fetch
from pyodide.ffi import create_proxy


# Global data storage
data = {
    "boards": [],
    "board1": None,
    "board2": None
}


async def load_data():
    """Load board comparison data from JSON file."""
    try:
        response = await fetch("board_comparison.json")
        json_data = await response.json()
        data["boards"] = json_data.get("boards", [])
        populate_board_selects()
    except Exception as e:
        show_error(f"Error loading data: {e}")


def populate_board_selects():
    """Populate the board selection dropdowns."""
    board1_select = document.getElementById("board1")
    board2_select = document.getElementById("board2")
    
    # Clear existing options (except first)
    board1_select.innerHTML = '<option value="">Select a board...</option>'
    board2_select.innerHTML = '<option value="">Select a board...</option>'
    
    # Add board options
    for idx, board in enumerate(data["boards"]):
        board_name = f"{board['port']}-{board['board']} (v{board['version']})"
        
        option1 = document.createElement("option")
        option1.value = str(idx)
        option1.textContent = board_name
        board1_select.appendChild(option1)
        
        option2 = document.createElement("option")
        option2.value = str(idx)
        option2.textContent = board_name
        board2_select.appendChild(option2)


def compare_boards(event):
    """Compare the selected boards."""
    board1_idx = document.getElementById("board1").value
    board2_idx = document.getElementById("board2").value
    
    if not board1_idx or not board2_idx:
        show_error("Please select both boards to compare")
        return
    
    data["board1"] = data["boards"][int(board1_idx)]
    data["board2"] = data["boards"][int(board2_idx)]
    
    display_comparison()


def display_comparison():
    """Display the comparison results."""
    board1 = data["board1"]
    board2 = data["board2"]
    
    # Get module sets (now just module names)
    modules1 = set(board1.get("modules", []))
    modules2 = set(board2.get("modules", []))
    
    common = modules1 & modules2
    unique1 = modules1 - modules2
    unique2 = modules2 - modules1
    
    # Update stats
    document.getElementById("stats").style.display = "block"
    document.getElementById("common-modules").textContent = str(len(common))
    document.getElementById("board1-unique").textContent = str(len(unique1))
    document.getElementById("board2-unique").textContent = str(len(unique2))
    
    # Build comparison HTML
    html = f"""
    <div class="comparison-grid">
        <div class="board-section">
            <div class="board-header">
                {board1['port']}-{board1['board']} (v{board1['version']})
            </div>
            <div class="module-list">
                <h3>Modules ({len(modules1)})</h3>
    """
    
    # Board 1 modules
    for name in sorted(modules1):
        if name in unique1:
            css_class = "module-item unique-to-board1"
            badge = " [UNIQUE]"
        else:
            css_class = "module-item"
            badge = ""
        
        html += f"""
                <div class="{css_class}">
                    <div class="module-name">{name}{badge}</div>
                </div>
        """
    
    html += """
            </div>
        </div>
        <div class="board-section">
            <div class="board-header">
    """
    html += f"{board2['port']}-{board2['board']} (v{board2['version']})"
    html += """
            </div>
            <div class="module-list">
                <h3>Modules ("""
    html += str(len(modules2))
    html += """)</h3>
    """
    
    # Board 2 modules
    for name in sorted(modules2):
        if name in unique2:
            css_class = "module-item unique-to-board2"
            badge = " [UNIQUE]"
        else:
            css_class = "module-item"
            badge = ""
        
        html += f"""
                <div class="{css_class}">
                    <div class="module-name">{name}{badge}</div>
                </div>
        """
    
    html += """
            </div>
        </div>
    </div>
    """
    
    # Add summary for common modules
    if common:
        html += f"""
        <div class="detail-view">
            <div class="detail-header">Common Modules Summary</div>
            <p style="color: #666; margin-bottom: 15px;">
                Both boards share {len(common)} common modules. The database contains detailed 
                API information for comparison (classes, methods, parameters).
            </p>
            <div style="columns: 3; column-gap: 20px;">
        """
        
        for name in sorted(common):
            html += f"<div style='break-inside: avoid; padding: 5px;'>📦 {name}</div>"
        
        html += """
            </div>
        </div>
        """
    
    document.getElementById("results").innerHTML = html


def show_error(message):
    """Display an error message."""
    results = document.getElementById("results")
    results.innerHTML = f"""
    <div style="background: #f8d7da; color: #721c24; padding: 20px; border-radius: 8px; border-left: 4px solid #dc3545;">
        <strong>Error:</strong> {message}
    </div>
    """


# Initialize when page loads
async def main():
    """Main entry point."""
    # Show loading state
    results = document.getElementById("results")
    results.innerHTML = """
    <div class="loading">
        <div class="spinner"></div>
        <p>Loading board data...</p>
    </div>
    """
    
    await load_data()
    
    # Clear loading state
    results.innerHTML = """
    <div style="text-align: center; padding: 40px; color: #666;">
        <p>👆 Select two boards above and click "Compare Boards" to see the differences</p>
    </div>
    """


# Start the application
import asyncio
asyncio.ensure_future(main())
